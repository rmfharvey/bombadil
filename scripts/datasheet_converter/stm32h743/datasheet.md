## **STM32H742xI/G STM32H743xI/G**

##### 32-bit Arm [®] Cortex [®] -M7 480MHz MCUs, up to 2MB flash, up to 1MB RAM, 46 com. and analog interfaces

**Datasheet**                             - **production data**


###### **Features**

**Includes ST state-of-the-art patented**
**technology**


**Core**


- 32-bit Arm [®] Cortex [®] -M7 core with doubleprecision FPU and L1 cache: 16 Kbytes of data
and 16 Kbytes of instruction cache; frequency
up to 480 MHz, MPU, 1027 DMIPS/
2.14 DMIPS/MHz (Dhrystone 2.1), and DSP
instructions


**Memories**


- Up to 2 Mbytes of flash memory with readwhile-write support


- Up to 1 Mbyte of RAM: 192 Kbytes of TCM
RAM (inc. 64 Kbytes of ITCM RAM +
128 Kbytes of DTCM RAM for time critical
routines), Up to 864 Kbytes of user SRAM, and
4 Kbytes of SRAM in Backup domain


- Dual mode Quad-SPI memory interface
running up to 133 MHz


- Flexible external memory controller with up to
32-bit data bus: SRAM, PSRAM,
SDRAM/LPSDR SDRAM, NOR/NAND flash
memory clocked up to 100 MHz in
Synchronous mode


- CRC calculation unit


**Security**


- ROP, PC-ROP, active tamper


**General-purpose input/outputs**


- Up to 168 I/O ports with interrupt capability


**Reset and power management**


- 3 separate power domains which can be
independently clock-gated or switched off:

–
D1: high-performance capabilities









–
D2: communication peripherals and timers

–
D3: reset/clock control/power management


- 1.62 to 3.6 V application supply and I/Os


- POR, PDR, PVD and BOR


- Dedicated USB power embedding a 3.3 V
internal regulator to supply the internal PHYs


- Embedded regulator (LDO) with configurable
scalable output to supply the digital circuitry


- Voltage scaling in Run and Stop mode (6
configurable ranges)


- Backup regulator (~0.9 V)


- Voltage reference for analog peripheral/V REF+

- Low-power modes: Sleep, Stop, Standby and
V BAT supporting battery charging


**Low-power consumption**


- V BAT battery operating mode with charging
capability


- CPU and domain power state monitoring pins


- 2.95 µA in Standby mode (Backup SRAM OFF,
RTC/LSE ON)


**Clock management**


- Internal oscillators: 64 MHz HSI, 48 MHz
HSI48, 4 MHz CSI, 32 kHz LSI


- External oscillators: 4-48 MHz HSE,
32.768 kHz LSE



March 2023 DS12110 Rev 10 1/357



This is information on a product in full production.



_[www.st.com](http://www.st.com)_


- 3× PLLs (1 for the system clock, 2 for kernel
clocks) with Fractional mode


**Interconnect matrix**


- 3 bus matrices (1 AXI and 2 AHB)


- Bridges (5× AHB2-APB, 2× AXI2-AHB)


**4 DMA controllers to unload the CPU**


- 1× high-speed master direct memory access
controller (MDMA) with linked list support


- 2× dual-port DMAs with FIFO


- 1× basic DMA with request router capabilities


**Up to 35 communication peripherals**


- 4× I2Cs FM+ interfaces (SMBus/PMBus)


- 4× USARTs/4x UARTs (ISO7816 interface,
LIN, IrDA, up to 12.5 Mbit/s) and 1x LPUART


- 6× SPIs, 3 with muxed duplex I2S audio class
accuracy via internal audio PLL or external
clock, 1x I2S in LP domain (up to 150 MHz)


- 4x SAIs (serial audio interface)


- SPDIFRX interface


- SWPMI single-wire protocol master I/F


- MDIO Slave interface


- 2× SD/SDIO/MMC interfaces (up to 125 MHz)


- 2× CAN controllers: 2 with CAN FD, 1 with
time-triggered CAN (TT-CAN)


- 2× USB OTG interfaces (1FS, 1HS/FS) crystalless solution with LPM and BCD


- Ethernet MAC interface with DMA controller


- HDMI-CEC


- 8- to 14-bit camera interface (up to 80 MHz)


**11 analog peripherals**


- 3× ADCs with 16-bit max. resolution (up to 36
channels, up to 3.6 MSPS)


- 1× temperature sensor


- 2× 12-bit D/A converters (1 MHz)


- 2× ultra-low-power comparators


- 2× operational amplifiers (7.3 MHz bandwidth)


- 1× digital filters for sigma delta modulator
(DFSDM) with 8 channels/4 filters


**Graphics**


- LCD-TFT controller up to XGA resolution



**STM32H742xI/G STM32H743xI/G**


- Chrom-ART graphical hardware Accelerator
(DMA2D) to reduce CPU load


- Hardware JPEG Codec


**Up to 22 timers and watchdogs**


- 1× high-resolution timer (2.1 ns max
resolution)


- 2× 32-bit timers with up to 4 IC/OC/PWM or
pulse counter and quadrature (incremental)
encoder input (up to 240 MHz)


- 2× 16-bit advanced motor control timers (up to
240 MHz)


- 10× 16-bit general-purpose timers (up to
240 MHz)


- 5× 16-bit low-power timers (up to 240 MHz)


- 2× watchdogs (independent and window)


- 1× SysTick timer


- RTC with sub-second accuracy and hardware
calendar


**Debug mode**


- SWD & JTAG interfaces


- 4-Kbyte embedded trace buffer


**True random number generators (3**
**oscillators each)**


**96-bit unique ID**


**All packages are ECOPACK2 compliant**

**Table 1. Device summary**






|Reference|Part number|
|---|---|
|STM32H742xI/G|STM32H742VI, STM32H742ZI,<br>STM32H742II, STM32H742BI,<br>STM32H742XI, STM32H742AI,<br>STM32H742VG, STM32H742ZG,<br>STM32H742IG, STM32H742BG,<br>STM32H742XG, STM32H742AG|
|STM32H743xI/G|STM32H743VI, STM32H743ZI,<br>STM32H743II, STM32H743BI,<br>STM32H743XI, STM32H743AI,<br>STM32H743VG, STM32H743ZG,<br>STM32H743IG, STM32H743BG,<br>STM32H743XG, STM32H743AG|



2/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Contents**

### **Contents**


**1** **Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16**


**2** **Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17**


**3** **Functional overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25**


3.1 Arm [®] Cortex [®] -M7 with FPU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.2 Memory protection unit (MPU) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.3 Memories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.3.1 Embedded flash memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.3.2 Embedded SRAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.4 Boot modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27


3.5 Power supply management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27


3.5.1 Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27


3.5.2 Power supply supervisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29


3.5.3 Voltage regulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29


3.6 Low-power strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30


3.7 Reset and clock controller (RCC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


3.7.1 Clock management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


3.7.2 System reset sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


3.8 General-purpose input/outputs (GPIOs) . . . . . . . . . . . . . . . . . . . . . . . . . . 32


3.9 Bus-interconnect matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32


3.10 DMA controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34


3.11 Chrom-ART Accelerator (DMA2D) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34


3.12 Nested vectored interrupt controller (NVIC) . . . . . . . . . . . . . . . . . . . . . . . 35


3.13 Extended interrupt and event controller (EXTI) . . . . . . . . . . . . . . . . . . . . 35


3.14 Cyclic redundancy check calculation unit (CRC) . . . . . . . . . . . . . . . . . . . 35


3.15 Flexible memory controller (FMC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


3.16 Quad-SPI memory interface (QUADSPI) . . . . . . . . . . . . . . . . . . . . . . . . . 36


3.17 Analog-to-digital converters (ADCs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


3.18 Temperature sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


3.19 V BAT operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


3.20 Digital-to-analog converters (DAC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38


DS12110 Rev 10 3/357



7


**Contents** **STM32H742xI/G STM32H743xI/G**


3.21 Ultra-low-power comparators (COMP) . . . . . . . . . . . . . . . . . . . . . . . . . . . 38


3.22 Operational amplifiers (OPAMP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38


3.23 Digital filter for sigma-delta modulators (DFSDM) . . . . . . . . . . . . . . . . . . 39


3.24 Digital camera interface (DCMI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40


3.25 LCD-TFT controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40


3.26 JPEG Codec (JPEG) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.27 True random number generator (RNG) . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.28 Timers and watchdogs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


3.28.1 High-resolution timer (HRTIM1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43


3.28.2 Advanced-control timers (TIM1, TIM8) . . . . . . . . . . . . . . . . . . . . . . . . . 44


3.28.3 General-purpose timers (TIMx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44


3.28.4 Basic timers TIM6 and TIM7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


3.28.5 Low-power timers (LPTIM1, LPTIM2, LPTIM3, LPTIM4, LPTIM5) . . . . 45


3.28.6 Independent watchdog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


3.28.7 Window watchdog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


3.28.8 SysTick timer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


3.29 Real-time clock (RTC), backup SRAM and backup registers . . . . . . . . . . 46

3.30 Inter-integrated circuit interface (I [2] C) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47


3.31 Universal synchronous/asynchronous receiver transmitter (USART) . . . 47


3.32 Low-power universal asynchronous receiver transmitter (LPUART) . . . . 48


3.33 Serial peripheral interfaces (SPI)/integrated interchip
sound interfaces (I2S) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49


3.34 Serial audio interfaces (SAI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49


3.35 SPDIFRX Receiver Interface (SPDIFRX) . . . . . . . . . . . . . . . . . . . . . . . . . 50


3.36 Single wire protocol master interface (SWPMI) . . . . . . . . . . . . . . . . . . . . 50


3.37 Management Data Input/Output (MDIO) slaves . . . . . . . . . . . . . . . . . . . . 51


3.38 SD/SDIO/MMC card host interfaces (SDMMC) . . . . . . . . . . . . . . . . . . . . 51


3.39 Controller area network (FDCAN1, FDCAN2) . . . . . . . . . . . . . . . . . . . . . 51


3.40 Universal serial bus on-the-go high-speed (OTG_HS) . . . . . . . . . . . . . . . 52


3.41 Ethernet MAC interface with dedicated DMA controller (ETH) . . . . . . . . . 52


3.42 High-definition multimedia interface (HDMI)

            - consumer electronics control (CEC) . . . . . . . . . . . . . . . . . . . . . . . . . . . 53


3.43 Debug infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53


**4** **Memory mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54**


4/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Contents**


**5** **Pin descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55**


**6** **Electrical characteristics (rev Y) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102**


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


6.3.2 VCAP external capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107


6.3.3 Operating conditions at power-up / power-down . . . . . . . . . . . . . . . . . 107


6.3.4 Embedded reset and power control block characteristics . . . . . . . . . . 108


6.3.5 Embedded reference voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109


6.3.6 Supply current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110


6.3.7 Wakeup time from low-power modes . . . . . . . . . . . . . . . . . . . . . . . . . . 123


6.3.8 External clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 124


6.3.9 Internal clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 128


6.3.10 PLL characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130


6.3.11 Memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132


6.3.12 EMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134


6.3.13 Absolute maximum ratings (electrical sensitivity) . . . . . . . . . . . . . . . . 136


6.3.14 I/O current injection characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 136


6.3.15 I/O port characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137


6.3.16 NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145


6.3.17 FMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146


6.3.18 Quad-SPI interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 166


6.3.19 Delay block (DLYB) characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 168


6.3.20 16-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168


6.3.21 DAC electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173


6.3.22 Voltage reference buffer characteristics . . . . . . . . . . . . . . . . . . . . . . . 176


6.3.23 Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 177


6.3.24 Temperature and V BAT monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178


DS12110 Rev 10 5/357



7


**Contents** **STM32H742xI/G STM32H743xI/G**


6.3.25 Voltage booster for analog switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179


6.3.26 Comparator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180


6.3.27 Operational amplifier characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 181


6.3.28 Digital filter for Sigma-Delta Modulators (DFSDM) characteristics . . . 184


6.3.29 Camera interface (DCMI) timing specifications . . . . . . . . . . . . . . . . . . 187


6.3.30 LCD-TFT controller (LTDC) characteristics . . . . . . . . . . . . . . . . . . . . . 188


6.3.31 Timer characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190


6.3.32 Communications interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191


6.3.33 JTAG/SWD interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 205


**7** **Electrical characteristics (rev V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208**


7.1 Parameter conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208


7.1.1 Minimum and maximum values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208


7.1.2 Typical values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208


7.1.3 Typical curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208


7.1.4 Loading capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208


7.1.5 Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208


7.1.6 Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209


7.1.7 Current consumption measurement . . . . . . . . . . . . . . . . . . . . . . . . . . 210


7.2 Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210


7.3 Operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212


7.3.1 General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212


7.3.2 VCAP external capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214


7.3.3 Operating conditions at power-up / power-down . . . . . . . . . . . . . . . . . 214


7.3.4 Embedded reset and power control block characteristics . . . . . . . . . . 215


7.3.5 Embedded reference voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216


7.3.6 Supply current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217


7.3.7 Wakeup time from low-power modes . . . . . . . . . . . . . . . . . . . . . . . . . . 229


7.3.8 External clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 230


7.3.9 Internal clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 234


7.3.10 PLL characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237


7.3.11 Memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239


7.3.12 EMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240


7.3.13 Absolute maximum ratings (electrical sensitivity) . . . . . . . . . . . . . . . . 242


7.3.14 I/O current injection characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 243


7.3.15 I/O port characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244


7.3.16 NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251


6/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Contents**


7.3.17 FMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251


7.3.18 Quad-SPI interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 273


7.3.19 Delay block (DLYB) characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 276


7.3.20 16-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276


7.3.21 DAC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285


7.3.22 Voltage reference buffer characteristics . . . . . . . . . . . . . . . . . . . . . . . 289


7.3.23 Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 290


7.3.24 Temperature and V BAT monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291


7.3.25 Voltage booster for analog switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291


7.3.26 Comparator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292


7.3.27 Operational amplifier characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 293


7.3.28 Digital filter for Sigma-Delta Modulators (DFSDM) characteristics . . . 295


7.3.29 Camera interface (DCMI) timing specifications . . . . . . . . . . . . . . . . . . 298


7.3.30 LCD-TFT controller (LTDC) characteristics . . . . . . . . . . . . . . . . . . . . . 299


7.3.31 Timer characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301


7.3.32 Communication interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301


**8** **Package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321**


8.1 Device marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321


8.2 LQFP100 package information (1L) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321


8.3 TFBGA100 package information (A08Q) . . . . . . . . . . . . . . . . . . . . . . . . 325


8.4 LQFP144 package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328


8.5 UFBGA169 package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331


8.6 LQFP176 package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334


8.7 LQFP208 package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338


8.8 UFBGA(176+25) package information . . . . . . . . . . . . . . . . . . . . . . . . . . 341


8.9 TFBGA240+25 package information . . . . . . . . . . . . . . . . . . . . . . . . . . . 343


8.10 Thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345


8.10.1 Reference documents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347


**9** **Ordering information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348**


**10** **Important security notice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349**


**11** **Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 350**


DS12110 Rev 10 7/357



7


**List of tables** **STM32H742xI/G STM32H743xI/G**

### **List of tables**


Table 1. Device summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Table 2. STM32H742xI/G and STM32H743xI/G features and peripheral counts. . . . . . . . . . . . . . . 19
Table 3. System vs domain low-power mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
Table 4. DFSDM implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
Table 5. Timer feature comparison. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Table 6. USART features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Table 7. Flash memory and SRAM memory mapping for STM32H742xI/G. . . . . . . . . . . . . . . . . . . 54
Table 8. Legend/abbreviations used in the pinout table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Table 9. Pin/ball definition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

Table 10. Port A alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

Table 11. Port B alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

Table 12. Port C alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

Table 13. Port D alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92

Table 14. Port E alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94

Table 15. Port F alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

Table 16. Port G alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

Table 17. Port H alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98

Table 18. Port I alternate functions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99

Table 19. Port J alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

Table 20. Port K alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

Table 21. Voltage characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Table 22. Current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

Table 23. Thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
Table 24. General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Table 25. VCAP operating conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
Table 26. Operating conditions at power-up / power-down (regulator ON) . . . . . . . . . . . . . . . . . . . 107
Table 27. Reset and power control block characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
Table 28. Embedded reference voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Table 29. Internal reference voltage calibration values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Table 30. Typical and maximum current consumption in Run mode, code with data processing
running from ITCM, regulator ON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
Table 31. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory, cache ON, regulator ON. . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Table 32. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory, cache OFF, regulator ON. . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Table 33. Typical consumption in Run mode and corresponding performance
versus code position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Table 34. Typical current consumption batch acquisition mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Table 35. Typical and maximum current consumption in Sleep mode, regulator ON. . . . . . . . . . . . 113
Table 36. Typical and maximum current consumption in Stop mode, regulator ON. . . . . . . . . . . . . 114
Table 37. Typical and maximum current consumption in Standby mode . . . . . . . . . . . . . . . . . . . . . 114
Table 38. Typical and maximum current consumption in VBAT mode . . . . . . . . . . . . . . . . . . . . . . . 115
Table 39. Peripheral current consumption in Run mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
Table 40. Peripheral current consumption in Stop, Standby and VBAT mode . . . . . . . . . . . . . . . . . 122
Table 41. Low-power mode wakeup timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
Table 42. High-speed external user clock characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
Table 43. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Table 44. 4-48 MHz HSE oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126


8/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **List of tables**


Table 45. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Table 46. HSI48 oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128

Table 47. HSI oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

Table 48. CSI oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

Table 49. LSI oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
Table 50. PLL characteristics (wide VCO frequency range). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
Table 51. PLL characteristics (medium VCO frequency range) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
Table 52. Flash memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Table 53. Flash memory programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
Table 54. Flash memory endurance and data retention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
Table 55. EMS characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

Table 56. EMI characteristics for fHSE = 8 MHz and fCPU = 400 MHz . . . . . . . . . . . . . . . . . . . . . . 135
Table 57. ESD absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
Table 58. Electrical sensitivities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
Table 59. I/O current injection susceptibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Table 60. I/O static characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Table 61. Output voltage characteristics for all I/Os except PC13, PC14, PC15 and PI8 . . . . . . . . 140
Table 62. Output voltage characteristics for PC13, PC14, PC15 and PI8 . . . . . . . . . . . . . . . . . . . . 141
Table 63. Output timing characteristics (HSLV OFF) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
Table 64. Output timing characteristics (HSLV ON) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
Table 65. NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
Table 66. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings . . . . . . . . . . . . . . . . . 148
Table 67. Asynchronous non-multiplexed SRAM/PSRAM/NOR read - NWAIT timings . . . . . . . . . . 148
Table 68. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings . . . . . . . . . . . . . . . . . 149
Table 69. Asynchronous non-multiplexed SRAM/PSRAM/NOR write - NWAIT timings. . . . . . . . . . 150
Table 70. Asynchronous multiplexed PSRAM/NOR read timings. . . . . . . . . . . . . . . . . . . . . . . . . . . 151
Table 71. Asynchronous multiplexed PSRAM/NOR read-NWAIT timings . . . . . . . . . . . . . . . . . . . . 151
Table 72. Asynchronous multiplexed PSRAM/NOR write timings . . . . . . . . . . . . . . . . . . . . . . . . . . 152
Table 73. Asynchronous multiplexed PSRAM/NOR write-NWAIT timings . . . . . . . . . . . . . . . . . . . . 153
Table 74. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
Table 75. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
Table 76. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 158
Table 77. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
Table 78. Switching characteristics for NAND flash read cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Table 79. Switching characteristics for NAND flash write cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Table 80. SDRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
Table 81. LPSDR SDRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Table 82. SDRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
Table 83. LPSDR SDRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
Table 84. QUADSPI characteristics in SDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166

Table 85. QUADSPI characteristics in DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
Table 86. Dynamics characteristics: Delay Block characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
Table 87. ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
Table 88. ADC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
Table 89. DAC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
Table 90. DAC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
Table 91. VREFBUF characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

Table 92. Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
Table 93. Temperature sensor calibration values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Table 94. V BAT monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Table 95. V BAT charging characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Table 96. Temperature monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178


DS12110 Rev 10 9/357



12


**List of tables** **STM32H742xI/G STM32H743xI/G**


Table 97. Voltage booster for analog switch characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Table 98. COMP characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180

Table 99. OPAMP characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
Table 100. DFSDM measured timing - 1.62-3.6 V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
Table 101. DCMI characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

Table 102. LTDC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188

Table 103. TIMx characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Table 104. Minimum i2c_ker_ck frequency in all I2C modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
Table 105. I2C analog filter characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
Table 106. SPI dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
Table 107. I [2] S dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
Table 108. SAI characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
Table 109. MDIO Slave timing parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
Table 110. Dynamic characteristics: SD / MMC characteristics, VDD = 2.7 to 3.6 V . . . . . . . . . . . . . 199
Table 111. Dynamic characteristics: eMMC characteristics, VDD = 1.71 to 1.9 V . . . . . . . . . . . . . . . 200
Table 112. USB OTG_FS electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
Table 113. Dynamic characteristics: USB ULPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
Table 114. Dynamics characteristics: Ethernet MAC signals for SMI. . . . . . . . . . . . . . . . . . . . . . . . . 203
Table 115. Dynamics characteristics: Ethernet MAC signals for RMII . . . . . . . . . . . . . . . . . . . . . . . . 204
Table 116. Dynamics characteristics: Ethernet MAC signals for MII . . . . . . . . . . . . . . . . . . . . . . . . . 205
Table 117. Dynamics JTAG characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
Table 118. Dynamics SWD characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
Table 119. Voltage characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
Table 120. Current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211

Table 121. Thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
Table 122. General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
Table 123. Supply voltage and maximum frequency configuration . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Table 124. VCAP operating conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
Table 125. Operating conditions at power-up / power-down (regulator ON) . . . . . . . . . . . . . . . . . . . 214
Table 126. Reset and power control block characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
Table 127. Embedded reference voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
Table 128. Internal reference voltage calibration values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
Table 129. Typical and maximum current consumption in Run mode, code with data processing
running from ITCM, LDO regulator ON. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
Table 130. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory, cache ON,
LDO regulator ON. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
Table 131. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory, cache OFF,
LDO regulator ON. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
Table 132. Typical and maximum current consumption batch acquisition mode,
LDO regulator ON. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
Table 133. Typical and maximum current consumption in Stop, LDO regulator ON . . . . . . . . . . . . . 220
Table 134. Typical and maximum current consumption in Sleep mode, LDO regulator. . . . . . . . . . . 221
Table 135. Typical and maximum current consumption in Standby . . . . . . . . . . . . . . . . . . . . . . . . . . 221
Table 136. Typical and maximum current consumption in VBAT mode . . . . . . . . . . . . . . . . . . . . . . . 222
Table 137. Peripheral current consumption in Run mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
Table 138. Low-power mode wakeup timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
Table 139. High-speed external user clock characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
Table 140. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
Table 141. 4-48 MHz HSE oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232

Table 142. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233


10/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **List of tables**


Table 143. HSI48 oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234

Table 144. HSI oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235

Table 145. CSI oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235

Table 146. LSI oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
Table 147. PLL characteristics (wide VCO frequency range). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
Table 148. PLL characteristics (medium VCO frequency range) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
Table 149. Flash memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
Table 150. Flash memory programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
Table 151. Flash memory endurance and data retention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
Table 152. EMS characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240

Table 153. EMI characteristics for fHSE = 8 MHz and fCPU = 400 MHz . . . . . . . . . . . . . . . . . . . . . . 241
Table 154. ESD absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
Table 155. Electrical sensitivities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
Table 156. I/O current injection susceptibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
Table 157. I/O static characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
Table 158. Output voltage characteristics for all I/Os except PC13, PC14, PC15 and PI8 . . . . . . . . 246
Table 159. Output voltage characteristics for PC13, PC14, PC15 and PI8 . . . . . . . . . . . . . . . . . . . . 247
Table 160. Output timing characteristics (HSLV OFF) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
Table 161. Output timing characteristics (HSLV ON) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
Table 162. NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
Table 163. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings . . . . . . . . . . . . . . . . . 253
Table 164. Asynchronous non-multiplexed SRAM/PSRAM/NOR read-NWAIT timings . . . . . . . . . . . 253
Table 165. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings . . . . . . . . . . . . . . . . . 255
Table 166. Asynchronous non-multiplexed SRAM/PSRAM/NOR write-NWAIT timings. . . . . . . . . . . 255
Table 167. Asynchronous multiplexed PSRAM/NOR read timings. . . . . . . . . . . . . . . . . . . . . . . . . . . 257
Table 168. Asynchronous multiplexed PSRAM/NOR read-NWAIT timings . . . . . . . . . . . . . . . . . . . . 257
Table 169. Asynchronous multiplexed PSRAM/NOR write timings . . . . . . . . . . . . . . . . . . . . . . . . . . 258
Table 170. Asynchronous multiplexed PSRAM/NOR write-NWAIT timings . . . . . . . . . . . . . . . . . . . . 258
Table 171. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
Table 172. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
Table 173. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 264
Table 174. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
Table 175. Switching characteristics for NAND flash read cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
Table 176. Switching characteristics for NAND flash write cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
Table 177. SDRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
Table 178. LPSDR SDRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
Table 179. SDRAM Write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
Table 180. LPSDR SDRAM Write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
Table 181. QUADSPI characteristics in SDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274

Table 182. QUADSPI characteristics in DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
Table 183. Delay Block characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
Table 184. ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276

Table 185. Minimum sampling time vs RAIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
Table 186. ADC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
Table 187. DAC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
Table 188. DAC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
Table 189. VREFBUF characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289

Table 190. Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
Table 191. Temperature sensor calibration values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
Table 192. V BAT monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
Table 193. V BAT charging characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
Table 194. Temperature monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291


DS12110 Rev 10 11/357



12


**List of tables** **STM32H742xI/G STM32H743xI/G**


Table 195. Voltage booster for analog switch characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
Table 196. COMP characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292

Table 197. Operational amplifier characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
Table 198. DFSDM measured timing - 1.62-3.6 V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296
Table 199. DCMI characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298

Table 200. LTDC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299

Table 201. TIMx characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
Table 202. Minimum i2c_ker_ck frequency in all I2C modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
Table 203. I2C analog filter characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
Table 204. USART characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
Table 205. SPI dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305
Table 206. I [2] S dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
Table 207. SAI characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
Table 208. MDIO Slave timing parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
Table 209. Dynamics characteristics: SD / MMC characteristics, VDD = 2.7 to 3.6 V . . . . . . . . . . . . 312
Table 210. Dynamics characteristics: eMMC characteristics VDD = 1.71V to 1.9V. . . . . . . . . . . . . . 313
Table 211. USB OTG_FS electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
Table 212. Dynamics characteristics: USB ULPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
Table 213. Dynamics characteristics: Ethernet MAC signals for SMI . . . . . . . . . . . . . . . . . . . . . . . . 316
Table 214. Dynamics characteristics: Ethernet MAC signals for RMII . . . . . . . . . . . . . . . . . . . . . . . . 317
Table 215. Dynamics characteristics: Ethernet MAC signals for MII . . . . . . . . . . . . . . . . . . . . . . . . . 318
Table 216. Dynamics JTAG characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
Table 217. Dynamics SWD characteristics: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
Table 218. LQFP100 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322

Table 219. TFBGA100 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
Table 220. TFBGA100 - Example of PCB design rules (0.8 mm pitch BGA) . . . . . . . . . . . . . . . . . . . 327
Table 221. LQFP144 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329

Table 222. UFBGA169 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332
Table 223. UFBGA169 - Example of PCB design rules (0.5 mm pitch BGA). . . . . . . . . . . . . . . . . . . 333
Table 224. LQFP176 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335

Table 225. LQFP208 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
Table 226. UFBGA(176+25) - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
Table 227. UFBGA(176+25) - Example of PCB design rules (0.65 mm pitch BGA) . . . . . . . . . . . . . 342
Table 228. TFBGA240+25 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344
Table 229. TFBGA240+25 - Example of PCB design rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
Table 230. Thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346

Table 231. Document revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 350


12/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **List of figures**

### **List of figures**


Figure 1. STM32H742xI/G block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
Figure 2. STM32H743xI/G block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Figure 3. Power-up/power-down sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
Figure 4. STM32H743xI/G bus matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
Figure 5. LQFP100 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
Figure 6. TFBGA100 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
Figure 7. LQFP144 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
Figure 8. UFBGA169 ballout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
Figure 9. LQFP176 pinout  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
Figure 10. UFBGA176+25 ballout  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
Figure 11. LQFP208 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Figure 12. TFBGA240+25 ballout  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
Figure 13. Pin loading conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Figure 14. Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Figure 15. Power supply scheme. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
Figure 16. Current consumption measurement scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Figure 17. External capacitor C EXT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
Figure 18. High-speed external clock source AC timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
Figure 19. Low-speed external clock source AC timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Figure 20. Typical application with an 8 MHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Figure 21. Typical application with a 32.768 kHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
Figure 22. VIL/VIH for all I/Os except BOOT0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
Figure 23. Recommended NRST pin protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
Figure 24. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms . . . . . . . . . . . . . . 147
Figure 25. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms . . . . . . . . . . . . . . 149
Figure 26. Asynchronous multiplexed PSRAM/NOR read waveforms. . . . . . . . . . . . . . . . . . . . . . . . 150
Figure 27. Asynchronous multiplexed PSRAM/NOR write waveforms . . . . . . . . . . . . . . . . . . . . . . . 152
Figure 28. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
Figure 29. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
Figure 30. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 158
Figure 31. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
Figure 32. NAND controller waveforms for read access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
Figure 33. NAND controller waveforms for write access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
Figure 34. NAND controller waveforms for common memory read access . . . . . . . . . . . . . . . . . . . . 161
Figure 35. NAND controller waveforms for common memory write access. . . . . . . . . . . . . . . . . . . . 162
Figure 36. SDRAM read access waveforms (CL = 1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
Figure 37. SDRAM write access waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Figure 38. Quad-SPI timing diagram - SDR mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
Figure 39. Quad-SPI timing diagram - DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
Figure 40. ADC accuracy characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
Figure 41. Typical connection diagram when using the ADC with FT/TT pins featuring
analog switch function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
Figure 42. Power supply and reference decoupling (V REF+ not connected to V DDA ). . . . . . . . . . . . . 172
Figure 43. Power supply and reference decoupling (V REF+ connected to V DDA ). . . . . . . . . . . . . . . . 172
Figure 44. 12-bit buffered /non-buffered DAC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
Figure 45. Channel transceiver timing diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
Figure 46. DCMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
Figure 47. LCD-TFT horizontal timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189


DS12110 Rev 10 13/357



15


**List of figures** **STM32H742xI/G STM32H743xI/G**


Figure 48. LCD-TFT vertical timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
Figure 49. SPI timing diagram - slave mode and CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
Figure 50. SPI timing diagram - slave mode and CPHA = 1 [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
Figure 51. SPI timing diagram - master mode [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
Figure 52. I [2] S slave timing diagram (Philips protocol) [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
Figure 53. I [2] S master timing diagram (Philips protocol) [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
Figure 54. SAI master timing waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
Figure 55. SAI slave timing waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
Figure 56. MDIO Slave timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
Figure 57. SDIO high-speed mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Figure 58. SD default mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Figure 59. DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Figure 60. ULPI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
Figure 61. Ethernet SMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
Figure 62. Ethernet RMII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
Figure 63. Ethernet MII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
Figure 64. JTAG timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Figure 65. SWD timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Figure 66. Pin loading conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
Figure 67. Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
Figure 68. Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
Figure 69. Current consumption measurement scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
Figure 70. External capacitor C EXT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
Figure 71. High-speed external clock source AC timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
Figure 72. Low-speed external clock source AC timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
Figure 73. Typical application with an 8 MHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
Figure 74. Typical application with a 32.768 kHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
Figure 75. VIL/VIH for all I/Os except BOOT0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
Figure 76. Recommended NRST pin protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
Figure 77. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms . . . . . . . . . . . . . . 252
Figure 78. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms . . . . . . . . . . . . . . 254
Figure 79. Asynchronous multiplexed PSRAM/NOR read waveforms. . . . . . . . . . . . . . . . . . . . . . . . 256
Figure 80. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
Figure 81. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
Figure 82. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 263
Figure 83. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
Figure 84. NAND controller waveforms for read access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
Figure 85. NAND controller waveforms for write access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
Figure 86. NAND controller waveforms for common memory read access . . . . . . . . . . . . . . . . . . . . 268
Figure 87. NAND controller waveforms for common memory write access. . . . . . . . . . . . . . . . . . . . 269
Figure 88. SDRAM read access waveforms (CL = 1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
Figure 89. SDRAM write access waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
Figure 90. QUADSPI timing diagram - SDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
Figure 91. Quad-SPI timing diagram - DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
Figure 92. ADC accuracy characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
Figure 93. Typical connection diagram when using the ADC with FT/TT pins
featuring analog switch function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
Figure 94. Power supply and reference decoupling (V REF+ not connected to V DDA ). . . . . . . . . . . . . 284
Figure 95. Power supply and reference decoupling (V REF+ connected to V DDA ). . . . . . . . . . . . . . . . 284
Figure 96. 12-bit buffered /non-buffered DAC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
Figure 97. Channel transceiver timing diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
Figure 98. DCMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298


14/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **List of figures**


Figure 99. LCD-TFT horizontal timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
Figure 100. LCD-TFT vertical timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
Figure 101. USART timing diagram in Master mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
Figure 102. USART timing diagram in Slave mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
Figure 103. SPI timing diagram - slave mode and CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
Figure 104. SPI timing diagram - slave mode and CPHA = 1 [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
Figure 105. SPI timing diagram - master mode [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307
Figure 106. I [2] S slave timing diagram (Philips protocol) [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
Figure 107. I [2] S master timing diagram (Philips protocol) [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
Figure 108. SAI master timing waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
Figure 109. SAI slave timing waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
Figure 110. MDIO Slave timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
Figure 111. SDIO high-speed mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
Figure 112. SD default mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
Figure 113. DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
Figure 114. ULPI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
Figure 115. Ethernet SMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
Figure 116. Ethernet RMII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
Figure 117. Ethernet MII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
Figure 118. JTAG timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
Figure 119. SWD timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320
Figure 120. LQFP100 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
Figure 121. LQFP100 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324
Figure 122. TFBGA100 - Outline [(13)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
Figure 123. TFBGA100 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
Figure 124. LQFP144 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
Figure 125. LQFP144 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
Figure 126. UFBGA169 - Outline. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332
Figure 127. UFBGA169 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 333
Figure 128. LQFP176 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334
Figure 129. LQFP176 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
Figure 130. LQFP208 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
Figure 131. LQFP208 - footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340
Figure 132. UFBGA(176+25) - Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
Figure 133. UFBGA(176+25) - Footprint example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342
Figure 134. TFBGA240+25 - Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
Figure 135. TFBGA240+25 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345


DS12110 Rev 10 15/357



15


**Introduction** **STM32H742xI/G STM32H743xI/G**

#### **1 Introduction**


This document provides information on STM32H742xI/G STM32H743xI/G microcontrollers,
such as description, functional overview, pin assignment and definition, electrical
characteristics, packaging, and ordering information.


This document should be read in conjunction with the STM32H742xI/G STM32H743xI/G
reference manual (RM0433), available from the STMicroelectronics website _www.st.com_ .


For information on the device errata with respect to the datasheet and reference manual,
refer to the STM32H742xI/G STM32H743xI/G errata sheet (ES0392), available on the
STMicroelectronics website _www.st.com_ .


For information on the Arm [®(a)] Cortex [®] -M7 core, please refer to the Cortex [®] -M7 Technical
Reference Manual, available from the http://www.arm.com website.


a. Arm is a registered trademark of Arm Limited (or its subsidiaries) in the US and/or elsewhere.


16/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Description**

#### **2 Description**


STM32H742xI/G and STM32H743xI/G devices are based on the high-performance Arm [®]
Cortex [®] -M7 32-bit RISC core operating at up to 480 MHz. The Cortex [®] -M7 core features a
floating point unit (FPU) which supports Arm [®] double-precision (IEEE 754 compliant) and
single-precision data-processing instructions and data types. STM32H742xI/G and
STM32H743xI/G devices support a full set of DSP instructions and a memory protection unit
(MPU) to enhance application security.


STM32H742xI/G and STM32H743xI/G devices incorporate high-speed embedded
memories with a dual-bank flash memory of up to 2 Mbytes, up to 1 Mbyte of RAM
(including 192 Kbytes of TCM RAM, up to 864 Kbytes of user SRAM and 4 Kbytes of
backup SRAM), as well as an extensive range of enhanced I/Os and peripherals connected
to APB buses, AHB buses, 2x32-bit multi-AHB bus matrix and a multi layer AXI interconnect
supporting internal and external memory access.


All the devices offer three ADCs, two DACs, two ultra-low power comparators, a low-power
RTC, a high-resolution timer, 12 general-purpose 16-bit timers, two PWM timers for motor
control, five low-power timers, a true random number generator (RNG). The devices support
four digital filters for external sigma-delta modulators (DFSDM). They also feature standard
and advanced communication interfaces.


      - Standard peripherals

– Four I [2] Cs


–
Four USARTs, four UARTs and one LPUART


–
Six SPIs, three I2Ss in Half-duplex mode. To achieve audio class accuracy, the
I2S peripherals can be clocked by a dedicated internal audio PLL or by an external
clock to allow synchronization.


– Four SAI serial audio interfaces


– One SPDIFRX interface


–
One SWPMI (Single Wire Protocol Master Interface)


–
Management Data Input/Output (MDIO) slaves


– Two SDMMC interfaces


–
A USB OTG full-speed and a USB OTG high-speed interface with full-speed
capability (with the ULPI)


–
One FDCAN plus one TT-FDCAN interface


– An Ethernet interface


– Chrom-ART Accelerator


– HDMI-CEC


      - Advanced peripherals including


–
A flexible memory control (FMC) interface


–
A Quad-SPI flash memory interface


– A camera interface for CMOS sensors


–
An LCD-TFT display controller (only available on STM32H743xI/G)


–
A JPEG hardware compressor/decompressor (only available on STM32H743xI/G)


Refer to _Table 2: STM32H742xI/G and STM32H743xI/G features and peripheral counts_ for
the list of peripherals available on each part number.


DS12110 Rev 10 17/357



54


**Description** **STM32H742xI/G STM32H743xI/G**


STM32H742xI/G and STM32H743xI/G devices operate in the –40 to +85 °C temperature
range from a 1.62 to 3.6 V power supply. The supply voltage can drop down to 1.62 V by
using an external power supervisor (see _Section 3.5.2: Power supply supervisor)_ and
connecting the PDR_ON pin to V SS . Otherwise the supply voltage must stay above 1.71 V
with the embedded power voltage detector enabled.


Dedicated supply inputs for USB (OTG_FS and OTG_HS) are available on all packages
except LQFP100 to allow a greater power supply choice.


A comprehensive set of power-saving modes allows the design of low-power applications.


STM32H742xI/G and STM32H743xI/G devices are offered in 8 packages ranging from 100
pins to 240 pins/balls. The set of included peripherals changes with the device chosen.


These features make STM32H742xI/G and STM32H743xI/G microcontrollers suitable for a
wide range of applications:


      - Motor drive and application control


      - Medical equipment


      - Industrial applications: PLC, inverters, circuit breakers


      - Printers, and scanners


      - Alarm systems, video intercom, and HVAC


      - Home audio appliances


      - Mobile applications, Internet of Things


      - Wearable devices: smart watches.


_Figure 1_ and _Figure 2_ shows the device block diagrams.


18/357 DS12110 Rev 10


**Table 2. STM32H742xI/G and STM32H743xI/G features and peripheral counts**








|Peripherals|Col2|STM32H 742VG|STM32H742ZG|STM32H742AG|STM32H742IG|STM32H742BG|STM32H742XG|STM32H743VG|STM32H743ZG|STM32H743AG|STM32H743IG|STM32H743BG|STM32H743XG|STM32H 742VI|STM32H742ZI|STM32H742AI|STM32H742II|STM32H742BI|STM32H742XI|STM32H743VI|STM32H743ZI|STM32H743AI|STM32H743II|STM32H743BI|STM32H743XI|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Flash memory in Kbytes|Flash memory in Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 512 Kbytes|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|2 x 1 Mbyte|
|SRAM in<br>Kbytes|SRAM<br>mapped onto<br>AXI bus|384|384|384|384|384|384|512|512|512|512|512|512|384|384|384|384|384|384|512|512|512|512|512|512|
|SRAM in<br>Kbytes|SRAM1<br>(D2 domain)|32|32|32|32|32|32|128|128|128|128|128|128|32|32|32|32|32|32|128|128|128|128|128|128|
|SRAM in<br>Kbytes|SRAM2<br>(D2 domain)|16|16|16|16|16|16|128|128|128|128|128|128|16|16|16|16|16|16|128|128|128|128|128|128|
|SRAM in<br>Kbytes|SRAM3<br>(D2 domain)|-|-|-|-|-|-|32|32|32|32|32|32|-|-|-|-|-|-|32|32|32|32|32|32|
|SRAM in<br>Kbytes|SRAM4<br>(D3 domain)|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|
|TCM RAM<br>in Kbytes|ITCM RAM<br>(instruction)|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|
|TCM RAM<br>in Kbytes|DTCM RAM<br>(data)|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|128|
|Backup SRAM (Kbytes)|Backup SRAM (Kbytes)|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|
|FMC|FMC|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|GPIOs|GPIOs|82|114|131|140|168|168|82|114|131|140|168|168|82|114|131|140|168|168|82|114|131|140|168|168|
|Quad-SPI interface|Quad-SPI interface|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Ethernet|Ethernet|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|


**Table 2. STM32H742xI/G and STM32H743xI/G features and peripheral counts (continued)**
















|Peripherals|Col2|STM32H 742VG|STM32H742ZG|STM32H742AG|STM32H742IG|STM32H742BG|STM32H742XG|STM32H743VG|STM32H743ZG|STM32H743AG|STM32H743IG|STM32H743BG|STM32H743XG|STM32H 742VI|STM32H742ZI|STM32H742AI|STM32H742II|STM32H742BI|STM32H742XI|STM32H743VI|STM32H743ZI|STM32H743AI|STM32H743II|STM32H743BI|STM32H743XI|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Timers|High-<br>resolution|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|
|Timers|General-<br>purpose|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|10|
|Timers|Advanced-<br>control (PWM)|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|
|Timers|Basic|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|
|Timers|Low-power|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|5|
|Tamper pins<br>Wakeup pins|Tamper pins<br>Wakeup pins|4<br>2|4<br>2|5<br>2|6<br>3|6<br>3|6<br>3|4<br>2|4<br>2|5<br>2|6<br>3|6<br>3|6<br>3|4<br>2|4<br>2|5<br>2|6<br>3|6<br>3|6<br>3|4<br>2|4<br>2|5<br>2|6<br>3|6<br>3|6<br>3|
|Random number generator|Random number generator|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Communi-<br>cation<br>interfaces|SPI / I2S|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|6/3(1)|
|Communi-<br>cation<br>interfaces|I2C|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|
|Communi-<br>cation<br>interfaces|USART/<br>UART/<br>LPUART|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|4/4<br>/1|
|Communi-<br>cation<br>interfaces|SAI|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|4|
|Communi-<br>cation<br>interfaces|SPDIFRX|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|4 inputs|
|Communi-<br>cation<br>interfaces|SWPMI|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Communi-<br>cation<br>interfaces|MDIO|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Communi-<br>cation<br>interfaces|SDMMC|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|
|Communi-<br>cation<br>interfaces|FDCAN/TT-<br>FDCAN|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|1/1|
|Communi-<br>cation<br>interfaces|USB OTG_FS|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Communi-<br>cation<br>interfaces|USB<br>OTG_HS|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|


**Table 2. STM32H742xI/G and STM32H743xI/G features and peripheral counts (continued)**














































|Peripherals|STM32H 742VG|STM32H742ZG|STM32H742AG|STM32H742IG|STM32H742BG|STM32H742XG|STM32H743VG|STM32H743ZG|STM32H743AG|STM32H743IG|STM32H743BG|STM32H743XG|STM32H 742VI|STM32H742ZI|STM32H742AI|STM32H742II|STM32H742BI|STM32H742XI|STM32H743VI|STM32H743ZI|STM32H743AI|STM32H743II|STM32H743BI|STM32H743XI|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Ethernet and camera<br>interface|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|LCD-TFT|-|-|-|-|-|-|Yes|Yes|Yes|Yes|Yes|Yes|-|-|-|-|-|-|Yes|Yes|Yes|Yes|Yes|Yes|
|JPEG Codec|-|-|-|-|-|-|Yes|Yes|Yes|Yes|Yes|Yes|-|-|-|-|-|-|Yes|Yes|Yes|Yes|Yes|Yes|
|Chrom-ART Accelerator<br>(DMA2D)|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|16-bit ADCs<br>Number of Direct channels<br>Number of Fast channels<br>Number of Slow channels|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|
|16-bit ADCs<br>Number of Direct channels<br>Number of Fast channels<br>Number of Slow channels|2<br>3<br>11|2<br>9<br>17|2<br>9<br>21|2<br>9<br>21|2<br>9<br>21|4<br>9<br>23|2<br>3<br>11|2<br>9<br>17|2<br>9<br>21|2<br>9<br>21|2<br>9<br>21|4<br>9<br>23|2<br>3<br>11|2<br>9<br>17|2<br>9<br>21|2<br>9<br>21|2<br>9<br>21|4<br>9<br>23|2<br>3<br>11|2<br>9<br>17|2<br>9<br>21|2<br>9<br>21|2<br>9<br>21|4<br>9<br>23|
|12-bit DAC<br>Number of channels|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|Yes<br>2|
|Comparators|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|
|Operational amplifiers|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|
|DFSDM|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|Maximum CPU frequency|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|480MHz(2)(3)/400 MHz|
|Operating voltage|1.71<br>to<br>3.6<br>V(4)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.71<br>to<br>3.6<br>V(4)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.71<br>to<br>3.6<br>V(4)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.71<br>to<br>3.6<br>V(4)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|1.62 to 3.6 V(5)|
|Operating temperatures|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|Ambient temperatures: –40 up to +85 °C(6)|
|Operating temperatures|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|Junction temperature: –40 to + 125 °C|
|Package|LQFP100<br>TFBGA100|LQFP144|UFBGA169|LQFP176<br>UFBGA176+25|LQFP208|TFBGA240+25|LQFP100<br>TFBGA100|LQFP144|UFBGA169|LQFP176<br>UFBGA176+25|LQFP208|TFBGA240+25|LQFP100<br>TFBGA100|LQFP144|UFBGA169|LQFP176<br>UFBGA176+25|LQFP208|TFBGA240+25|LQFP100<br>TFBGA100|LQFP144|UFBGA169|LQFP176<br>UFBGA176+25|LQFP208|TFBGA240+25|


1. The SPI1, SPI2 and SPI3 interfaces give the flexibility to work in an exclusive way in either the SPI mode or the I2S audio mode.


2. The maximum CPU frequency of 480 MHz can be obtained on devices revision V.


3. The product junction temperature must be kept within the –40 to +105 °C temperature range.


4. Since the LQFP100 package does not feature the PDR_ON pin (tied internally to V DD ), the minimum V DD value for this package is 1.71 V.


5. V DD /V DDA can drop down to 1.62 V by using an external power supervisor (see _Section 3.5.2: Power supply supervisor)_ and connecting PDR_ON pin to V SS . Otherwise the supply voltage must stay
above 1.71 V with the embedded power voltage detector enabled.


6. The product junction temperature must be kept within the –40 to +125 °C temperature range.


**STM32H742xI/G STM32H743xI/G** **Description**


**Figure 1. STM32H742xI/G block diagram**


















|Col1|AHB1|(240MHz)|Col4|
|---|---|---|---|
|DMA1|DMA2<br>E|THER<br>MAC<br>SDM|MC2<br>OTG_HS<br>PHY|


















































|I-TCM<br>64KB|D-TCM<br>64KB|Col3|
|---|---|---|
||||
|**AXIM**<br>Arm CPU<br>Cortex-M7<br>480 MHz<br>AHB<br>JTAG/SW<br>ETM|**AXIM**<br>Arm CPU<br>Cortex-M7<br>480 MHz<br>AHB<br>JTAG/SW<br>ETM|**AXIM**<br>Arm CPU<br>Cortex-M7<br>480 MHz<br>AHB<br>JTAG/SW<br>ETM|
|MDMA<br>AHB<br>I-Cache<br>16KB<br>D-Cache<br>16KB<br>16 Streams<br>FIFO|MDMA<br>AHB<br>I-Cache<br>16KB<br>D-Cache<br>16KB<br>16 Streams<br>FIFO|MDMA<br>AHB<br>I-Cache<br>16KB<br>D-Cache<br>16KB<br>16 Streams<br>FIFO|







































































DS12110 Rev 10 23/357



54


**Description** **STM32H742xI/G STM32H743xI/G**


**Figure 2. STM32H743xI/G block diagram**


















|Col1|AHB1|(240MHz)|Col4|Col5|
|---|---|---|---|---|
|DMA1|DMA2<br>E|THER<br>MAC<br>SDM|MC2<br>OTG_HS<br>PHY|MC2<br>OTG_HS<br>PHY|




















































|I-TCM<br>64KB|D-TCM<br>64KB|Col3|
|---|---|---|
||||
|**AXIM**<br>Arm  CPU<br>Cortex-M7<br>480 MHz<br>AHBP<br>AHB<br>JTAG/SW<br>ETM<br>I-Cache<br>16KB<br>D-Cache<br>16KB|**AXIM**<br>Arm  CPU<br>Cortex-M7<br>480 MHz<br>AHBP<br>AHB<br>JTAG/SW<br>ETM<br>I-Cache<br>16KB<br>D-Cache<br>16KB|**AXIM**<br>Arm  CPU<br>Cortex-M7<br>480 MHz<br>AHBP<br>AHB<br>JTAG/SW<br>ETM<br>I-Cache<br>16KB<br>D-Cache<br>16KB|















































































24/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**

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


      - Harvard architecture with L1 caches (16 Kbytes of I-cache and 16 Kbytes of D-cache)


      - 64-bit AXI interface


      - 64-bit ITCM interface


      - 2x32-bit DTCM interfaces


The following memory interfaces are supported:


      - Separate Instruction and Data buses (Harvard Architecture) to optimize CPU latency


      - Tightly Coupled Memory (TCM) interface designed for fast and deterministic SRAM

accesses


      - AXI Bus interface to optimize Burst transfers


      - Dedicated low-latency AHB-Lite peripheral bus (AHBP) to connect to peripherals.


The processor supports a set of DSP instructions which allow efficient signal processing and
complex algorithm execution.


It also supports single and double precision FPU (floating point unit) speeds up software
development by using metalanguage development tools, while avoiding saturation.


_Figure 1_ and _Figure 2_ shows the general block diagram of the STM32H742xI/G and
STM32H743xI/G family.


_Note:_ _Cortex_ [®] _-M7 with FPU core is binary compatible with the Cortex_ [®] _-M4 core._

###### **3.2 Memory protection unit (MPU)**


The memory protection unit (MPU) manages the CPU access rights and the attributes of the
system resources. It has to be programmed and enabled before use. Its main purposes are
to prevent an untrusted user program to accidentally corrupt data used by the OS and/or by
a privileged task, but also to protect data processes or read-protect memory regions.

The MPU defines access rules for privileged accesses and user program accesses. It
allows defining up to 16 protected regions that can in turn be divided into up to 8
independent subregions, where region address, size, and attributes can be configured. The
protection area ranges from 32 bytes to 4 Gbytes of addressable memory.
When an unauthorized access is performed, a memory management exception is
generated.


DS12110 Rev 10 25/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.3 Memories**


**3.3.1** **Embedded flash memory**


The STM32H742xI/G and STM32H743xI/G devices embed up to 2 Mbytes of flash memory
that can be used for storing programs and data.


The flash memory is organized as 266-bit flash words memory that can be used for storing
both code and data constants. Each word consists of:


      - One flash word (8 words, 32 bytes or 256 bits)


      - 10 ECC bits.


The flash memory is divided into two independent banks. Each bank is organized as follows:


**•** A user flash memory block of 512 Kbytes (STM32H7xxxG) or 1-Mbyte (STM32H7xxxI)
containing eight user sectors of 128 Kbytes (4 K flash memory words)


**•** 128 Kbytes of System flash memory from which the device can boot


      - 2 Kbytes (64 flash words) of user option bytes for user configuration


**3.3.2** **Embedded SRAM**


All devices feature:


      - 384 (STM32H742xI/G) or 512 Kbytes (STM32H743xI/G) of AXI-SRAM mapped onto
AXI bus on D1 domain.


      - SRAM1 mapped on D2 domain: 32 (STM32H742xI/G) or 128 Kbytes
(STM32H743xI/G)


      - SRAM2 mapped on D2 domain: 16 (STM32H742xI/G) or 128 Kbytes
(STM32H743xI/G)128 Kbytes


      - SRAM3 mapped on D2 domain: 32 Kbytes (STM32H743xI/G only)


      - SRAM4 mapped on D3 domain: 64 Kbytes


      - 4 Kbytes of backup SRAM


The content of this area is protected against possible unwanted write accesses,
and is retained in Standby or V BAT mode.


      - RAM mapped to TCM interface (ITCM and DTCM):


Both ITCM and DTCM RAMs are 0 wait state memories. either They can be accessed
either from the CPU or the MDMA (even in Sleep mode) through a specific AHB slave
of the CPU(AHBP):


–
64 Kbytes of ITCM-RAM (instruction RAM)


This RAM is connected to ITCM 64-bit interface designed for execution of critical
real-times routines by the CPU.


–
128 Kbytes of DTCM-RAM (2x 64-Kbyte DTCM-RAMs on 2x32-bit DTCM ports)


The DTCM-RAM could be used for critical real-time data, such as interrupt service
routines or stack/heap memory. Both DTCM-RAMs can be used in parallel (for
load/store operations) thanks to the Cortex [®] -M7 dual issue capability.


The MDMA can be used to load code or data in ITCM or DTCM RAMs.


26/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


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

###### **3.4 Boot modes**


At startup, the boot memory space is selected by the BOOT pin and BOOT_ADDx option
bytes, allowing to program any boot memory address from 0x0000 0000 to 0x3FFF FFFF
which includes:


      - All flash address space


      - All RAM address space: ITCM, DTCM RAMs and SRAMs


      - The System memory bootloader


The boot loader is located in non-user System memory. It is used to reprogram the flash
memory through a serial interface (USART, I2C, SPI, USB-DFU). Refer to _STM32_
_microcontroller System memory Boot mode_ application note (AN2606) for details.

###### **3.5 Power supply management**


**3.5.1** **Power supply scheme**


STM32H742xI/G STM32H743xI/G power supply voltages are the following:


      - V DD = 1.62 to 3.6 V: external power supply for I/Os, provided externally through V DD
pins.


      - V DDLDO = 1.62 to 3.6 V: supply voltage for the internal regulator supplying V CORE

      - V DDA = 1.62 to 3.6 V: external analog power supplies for ADC, DAC, COMP and
OPAMP.


      - V DD33USB and V DD50USB :


V DD50USB can be supplied through the USB cable to generate the V DD33USB via the
USB internal regulator. This allows supporting a V DD supply different from 3.3 V.


The USB regulator can be bypassed to supply directly V DD33USB with
V DD33USB ≈ 3.3 V (see electrical characteristics).


      - V BAT = 1.2 to 3.6 V: power supply for the V SW domain when V DD is not present.


      - V CAP : V CORE supply voltage, which values depend on voltage scaling (1.0 V, 1.1 V,
1.2 V or 1.35 V). They are configured through VOS bits in PWR_D3CR register and


DS12110 Rev 10 27/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**


ODEN bit in the SYSCFG_PWRCR register. The V CORE domain is split into the
following power domains that can be independently switch off.

– D1 domain containing some peripherals and the Cortex [®] -M7 core.


–
D2 domain containing a large part of the peripherals.


–
D3 domain containing some peripherals and the system control.


During power-up and power-down phases, the following power sequence requirements
must be respected (see _Figure 3_ ):


      - When V DD is below 1 V, other power supplies (V DDA, V DD33USB, V DD50USB ) must
remain below V DD + 300 mV.


      - When V DD is above 1 V, all power supplies are independent.


During the power-down phase, V DD can temporarily become lower than other supplies only
if the energy provided to the microcontroller remains below 1 mJ. This allows external
decoupling capacitors to be discharged with different time constants during the power-down
transient phase.


**Figure 3. Power-up/power-down sequence**











1. V DDx refers to any power supply among V DDA, V DD33USB, V DD50USB .


28/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


**3.5.2** **Power supply supervisor**


The devices have an integrated power-on reset (POR)/ power-down reset (PDR) circuitry
coupled with a Brownout reset (BOR) circuitry:


      - Power-on reset (POR)


The POR supervisor monitors V DD power supply and compares it to a fixed threshold.
The devices remain in Reset mode when V DD is below this threshold,


      - Power-down reset (PDR)


The PDR supervisor monitors V DD power supply. A reset is generated when V DD drops
below a fixed threshold.


The PDR supervisor can be enabled/disabled through PDR_ON pin.


      - Brownout reset (BOR)


The BOR supervisor monitors V DD power supply. Three BOR thresholds (from 2.1 to
2.7 V) can be configured through option bytes. A reset is generated when V DD drops
below this threshold.


**3.5.3** **Voltage regulator**


The same voltage regulator supplies the 3 power domains (D1, D2 and D3). D1 and D2 can
be independently switched off.


Voltage regulator output can be adjusted according to application needs through 6 power
supply levels:


      - Run mode (VOS0 to VOS3)


–
Scale 0: boosted performance (available only with LDO regulator)


–
Scale 1: high performance


–
Scale 2: medium performance and consumption


–
Scale 3: optimized performance and low-power consumption


      - Stop mode (SVOS3 to SVOS5)


–
Scale 3: peripheral with wakeup from Stop mode capabilities (UART, SPI, I2C,
LPTIM) are operational


–
Scale 4 and 5 where the peripheral with wakeup from Stop mode is disabled


The peripheral functionality is disabled but wakeup from Stop mode is possible
through GPIO or asynchronous interrupt .


DS12110 Rev 10 29/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.6 Low-power strategy**


There are several ways to reduce power consumption on STM32H742xI/G and

STM32H743xI/G:

      - Decrease the dynamic power consumption by slowing down the system clocks even in
Run mode and by individually clock gating the peripherals that are not used.


      - Save power consumption when the CPU is idle, by selecting among the available lowpower mode according to the user application needs. This allows achieving the best
compromise between short startup time, low-power consumption, as well as available
wakeup sources.


The devices feature several low-power modes:


      - CSleep (CPU clock stopped)


      - CStop (CPU sub-system clock stopped)


      - DStop (Domain bus matrix clock stopped)


      - Stop (System clock stopped)


      - DStandby (Domain powered down)


      - Standby (System powered down)


CSleep and CStop low-power modes are entered by the MCU when executing the WFI
(Wait for Interrupt) or WFE (Wait for Event) instructions, or when the SLEEPONEXIT bit of
the Cortex [®] -Mx core is set after returning from an interrupt service routine.


A domain can enter low-power mode (DStop or DStandby) when the processor, its
subsystem and the peripherals allocated in the domain enter low-power mode.


If part of the domain is not in low-power mode, the domain remains in the current mode.


Finally the system can enter Stop or Standby when all EXTI wakeup sources are cleared
and the power domains are in DStop or DStandby mode.


**Table 3. System vs domain low-power mode**

|System power mode|D1 domain power<br>mode|D2 domain power<br>mode|D3 domain power<br>mode|
|---|---|---|---|
|Run|DRun/DStop/DStandby|DRun/DStop/DStandby|DRun|
|Stop|DStop/DStandby|DStop/DStandby|DStop|
|Standby|DStandby|DStandby|DStandby|



30/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**

###### **3.7 Reset and clock controller (RCC)**


The clock and reset controller is located in D3 domain. The RCC manages the generation of
all the clocks, as well as the clock gating and the control of the system and peripheral
resets. It provides a high flexibility in the choice of clock sources and allows to apply clock
ratios to improve the power consumption. In addition, on some communication peripherals
that are capable to work with two different clock domains (either a bus interface clock or a
kernel peripheral clock), the system frequency can be changed without modifying the
baudrate.


**3.7.1** **Clock management**


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


**3.7.2** **System reset sources**


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


DS12110 Rev 10 31/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.8 General-purpose input/outputs (GPIOs)**


Each of the GPIO pins can be configured by software as output (push-pull or open-drain,
with or without pull-up or pull-down), as input (floating, with or without pull-up or pull-down)
or as peripheral alternate function. Most of the GPIO pins are shared with digital or analog
alternate functions. All GPIOs are high-current-capable and have speed selection to better
manage internal noise, power consumption and electromagnetic emission.


After reset, all GPIOs (except debug pins) are in Analog mode to reduce power
consumption (refer to GPIOs register reset values in the device reference manual).


The I/O configuration can be locked if needed by following a specific sequence in order to
avoid spurious writing to the I/Os registers.

###### **3.9 Bus-interconnect matrix**


The devices feature an AXI bus matrix, two AHB bus matrices and bus bridges that allow
interconnecting bus masters with bus slaves (see _Figure 4_ ).


_Figure 4_ shows STM32H743xI/G bus matrix. All peripherals may not be available for
STM32H742xI/G (refer to _Table 2: STM32H742xI/G and STM32H743xI/G features and_
_peripheral counts_ ).


32/357 DS12110 Rev 10


**Figure 4. STM32H743xI/G bus matrix**




|Col1|APB3|Col3|
|---|---|---|
||APB3||
||AHB3|AHB3|
||||




|Col1|Col2|Col3|DMMC1|MDMA|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||


|Col1|Col2|Col3|Col4|DMA2|Col6|Col7|Ethernet<br>MAC|Col9|SDMMC2|Col11|USBHS1|Col13|USBHS2|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||DMA1_PERIPH|DMA2_MEM|DMA2_PERIPH||||||||||||
||||||||||||||||||
|||||||||||||||||SRAM1 128<br>Kbyte|
||||||||||||||||||
|||||||||||||||||SRAM2 128<br>Kbyte|
||||||||||||||||||
|||||||||||||||||SRAM3<br>32 Kbyte<br>AHB1<br>AHB2|
||||||||||||||||||
||||||||||||||||(2)|(2)|
||||||||||||||||||


|AHBS<br>CPU<br>ITCM<br>Cortex-M7 64 Kbyte<br>I$ D$ DTCM<br>16KB 16KB 128 Kbyte<br>AXIM AHBP<br>SDMMC1 MDMA DMA2D LTDC<br>D1-to-D2 A<br>APB3<br>AHB3<br>Flash A<br>Up to 1 Mbyte<br>Flash B<br>Up to 1 Mbyte<br>AXI SRAM<br>512 Kbyte<br>QSPI<br>FMC<br>64-bit AXI bus matrix<br>D1 domain|Col2|Col3|DMA1 DMA2 Et Mhe Ar Cnet SDMMC2 USBHS1 USBHS2<br>DMA1_PERIPH DMA2_PERIPH<br>DMA1_MEM DMA2_MEM<br>SRAM1 128<br>Kbyte<br>SRAM2 128<br>Kbyte<br>SRAM3<br>32 Kbyte<br>AHB1<br>AHB2<br>APB1<br>APB2<br>(1)<br>(2)<br>32-bit AHB bus matrix<br>D2 domain|
|---|---|---|---|
|AXIM<br>SDMMC1<br>MDMA<br>DMA2D<br>LTDC<br>Cortex-M7<br>I$<br>16KB<br>D$<br>16KB<br>AHBP<br>APB3<br>64-bit AXI bus matrix<br>**D1 domain**<br>DTCM<br>128 Kbyte<br>ITCM<br>64 Kbyte<br>Flash A<br>Up to 1 Mbyte<br>Flash B<br>Up to 1 Mbyte<br>AXI SRAM<br>512 Kbyte<br>QSPI<br>FMC<br>AHBS<br>**CPU**<br>D1-to-D2 A<br>AHB3|AXIM<br>SDMMC1<br>MDMA<br>DMA2D<br>LTDC<br>Cortex-M7<br>I$<br>16KB<br>D$<br>16KB<br>AHBP<br>APB3<br>64-bit AXI bus matrix<br>**D1 domain**<br>DTCM<br>128 Kbyte<br>ITCM<br>64 Kbyte<br>Flash A<br>Up to 1 Mbyte<br>Flash B<br>Up to 1 Mbyte<br>AXI SRAM<br>512 Kbyte<br>QSPI<br>FMC<br>AHBS<br>**CPU**<br>D1-to-D2 A<br>AHB3|HB|HB|
|AXIM<br>SDMMC1<br>MDMA<br>DMA2D<br>LTDC<br>Cortex-M7<br>I$<br>16KB<br>D$<br>16KB<br>AHBP<br>APB3<br>64-bit AXI bus matrix<br>**D1 domain**<br>DTCM<br>128 Kbyte<br>ITCM<br>64 Kbyte<br>Flash A<br>Up to 1 Mbyte<br>Flash B<br>Up to 1 Mbyte<br>AXI SRAM<br>512 Kbyte<br>QSPI<br>FMC<br>AHBS<br>**CPU**<br>D1-to-D2 A<br>AHB3||||




























|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||




**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.10 DMA controllers**


The devices feature four DMA instances to unload CPU activity:


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


The DMA request router could be considered as an extension of the DMA controller. It
routes the DMA peripheral requests to the DMA controller itself. This allowing managing the
DMA requests with a high flexibility, maximizing the number of DMA requests that run
concurrently, as well as generating DMA requests from peripheral output trigger or DMA
event.

###### **3.11 Chrom-ART Accelerator (DMA2D)**


The Chrom-Art Accelerator (DMA2D) is a graphical accelerator which offers advanced bit
blitting, row data copy and pixel format conversion. It supports the following functions:


      - Rectangle filling with a fixed color


      - Rectangle copy


      - Rectangle copy with pixel format conversion


      - Rectangle composition with blending and pixel format conversion


Various image format coding are supported, from indirect 4bpp color mode up to 32bpp
direct color. It embeds dedicated memory to store color lookup tables. The DMA2D also
supports block based YCbCr to handle JPEG decoder output.


An interrupt can be generated when an operation is complete or at a programmed
watermark.


All the operations are fully automatized and are running independently from the CPU or the
DMAs.


34/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**

###### **3.12 Nested vectored interrupt controller (NVIC)**


The devices embed a nested vectored interrupt controller which is able to manage 16
priority levels, and handle up to 150 maskable interrupt channels plus the 16 interrupt lines
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

###### **3.13 Extended interrupt and event controller (EXTI)**


The EXTI controller performs interrupt and event management. In addition, it can wake up
the processor, power domains and/or D3 domain from Stop mode.


The EXTI handles up to 89 independent event/interrupt lines split as 28 configurable events
and 61 direct events .


Configurable events have dedicated pending flags, active edge selection, and software
trigger capable.


Direct events provide interrupts or events from peripherals having a status flag.

###### **3.14 Cyclic redundancy check calculation unit (CRC)**


The CRC (cyclic redundancy check) calculation unit is used to get a CRC code using a
programmable polynomial.


Among other applications, CRC-based techniques are used to verify data transmission or
storage integrity. In the scope of the EN/IEC 60335-1 standard, they offer a means of
verifying the flash memory integrity. The CRC calculation unit helps compute a signature of
the software during runtime, to be compared with a reference signature generated at linktime and stored at a given memory location.


DS12110 Rev 10 35/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.15 Flexible memory controller (FMC)**


The FMC controller main features are the following:

      - Interface with static-memory mapped devices including:


–
Static random access memory (SRAM)


–
NOR flash memory/OneNAND flash memory


–
PSRAM (4 memory banks)


–
NAND flash memory with ECC hardware to check up to 8 Kbytes of data


      - Interface with synchronous DRAM (SDRAM/Mobile LPSDR SDRAM) memories


      - 8-,16-,32-bit data bus width


      - Independent Chip Select control for each memory bank


      - Independent configuration for each memory bank


      - Write FIFO


      - Read FIFO for SDRAM controller


      - The maximum FMC_CLK/FMC_SDCLK frequency for synchronous accesses is the
FMC kernel clock divided by 2.

###### **3.16 Quad-SPI memory interface (QUADSPI)**


All devices embed a Quad-SPI memory interface, which is a specialized communication
interface targeting Single, Dual or Quad-SPI flash memories. It supports both single and
double datarate operations.


It can operate in any of the following modes:


      - Direct mode through registers


      - External flash status register polling mode


      - Memory mapped mode.


Up to 256 Mbytes of external flash memory can be mapped, and 8-, 16- and 32-bit data
accesses are supported as well as code execution.


The opcode and the frame format are fully programmable.

###### **3.17 Analog-to-digital converters (ADCs)**


The STM32H742xI/G and STM32H743xI/G devices embed three analog-to-digital
converters, which resolution can be configured to 16, 14, 12, 10 or 8 bits.


Each ADC shares up to 20 external channels, performing conversions in the Single-shot or
Scan mode. In Scan mode, automatic conversion is performed on a selected group of
analog inputs.


Additional logic functions embedded in the ADC interface allow:


      - Simultaneous sample and hold


      - Interleaved sample and hold


The ADC can be served by the DMA controller, thus allowing to automatically transfer ADC
converted values to a destination location without any software action.


36/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


In addition, an analog watchdog feature can accurately monitor the converted voltage of
one, some or all selected channels. An interrupt is generated when the converted voltage is
outside the programmed thresholds.


To synchronize A/D conversion and timers, the ADCs could be triggered by any of TIM1,
TIM2, TIM3, TIM4, TIM6, TIM8, TIM15, HRTIM1 and LPTIM1 timer.

###### **3.18 Temperature sensor**


STM32H742xI/G and STM32H743xI/G devices embed a temperature sensor that generates
a voltage (V TS ) that varies linearly with the temperature. This temperature sensor is
internally connected to ADC3_IN18. The conversion range is between 1.7 V and 3.6 V. It

−
can measure the device junction temperature ranging from 40 up to +125 °C.


The temperature sensor have a good linearity, but it has to be calibrated to obtain a good
overall accuracy of the temperature measurement. As the temperature sensor offset varies
from chip to chip due to process variation, the uncalibrated internal temperature sensor is
suitable for applications that detect temperature changes only. To improve the accuracy of
the temperature sensor measurement, each device is individually factory-calibrated by ST.
The temperature sensor factory calibration data are stored by ST in the System memory
area, which is accessible in Read-only mode.

###### **3.19 V BAT operation**


The V BAT power domain contains the RTC, the backup registers and the backup SRAM.


To optimize battery duration, this power domain is supplied by V DD when available or by the
voltage applied on VBAT pin (when V DD supply is not present). V BAT power is switched
when the PDR detects that V DD dropped below the PDR level.


The voltage on the VBAT pin could be provided by an external battery, a supercapacitor or
directly by V DD, in which case, the V BAT mode is not functional.


V BAT operation is activated when V DD is not present.


The V BAT pin supplies the RTC, the backup registers and the backup SRAM.


_Note:_ _When the microcontroller is supplied from V_ _BAT_ _, external interrupts and RTC alarm/events_
_do not exit it from V_ _BAT_ _operation._


_When PDR_ON pin is connected to V_ _SS_ _(Internal Reset OFF), the V_ _BAT_ _functionality is no_
_more available and V_ _BAT_ _pin should be connected to V_ _DD_ _._


DS12110 Rev 10 37/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.20 Digital-to-analog converters (DAC)**


The two 12-bit buffered DAC channels can be used to convert two digital signals into two
analog voltage signal outputs.


This dual digital Interface supports the following features:


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

###### **3.21 Ultra-low-power comparators (COMP)**


STM32H742xI/G and STM32H743xI/G devices embed two rail-to-rail comparators (COMP1
and COMP2). They feature programmable reference voltage (internal or external),
hysteresis and speed (low speed for low-power) as well as selectable output polarity.


The reference voltage can be one of the following:


      - An external I/O


      - A DAC output channel


      - An internal reference voltage or submultiple (1/4, 1/2, 3/4).


All comparators can wake up from Stop mode, generate interrupts and breaks for the timers,
and be combined into a window comparator.

###### **3.22 Operational amplifiers (OPAMP)**


STM32H742xI/G and STM32H743xI/G devices embed two rail-to-rail operational amplifiers
(OPAMP1 and OPAMP2) with external or internal follower routing and PGA capability.


The operational amplifier main features are:


      - PGA with a non-inverting gain ranging of 2, 4, 8 or 16 or inverting gain ranging of -1, -3,
-7 or -15


      - One positive input connected to DAC


      - Output connected to internal ADC


      - Low input bias current down to 1 nA


      - Low input offset voltage down to 1.5 mV


      - Gain bandwidth up to 7.3 MHz


38/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


The devices embeds two operational amplifiers (OPAMP1 and OPAMP2) with two inputs
and one output each. These three I/Os can be connected to the external pins, thus enabling
any type of external interconnections. The operational amplifiers can be configured
internally as a follower, as an amplifier with a non-inverting gain ranging from 2 to 16 or with
inverting gain ranging from -1 to -15.

###### **3.23 Digital filter for sigma-delta modulators (DFSDM)**


The devices embed one DFSDM with 4 digital filters modules and 8 external input serial
channels (transceivers) or alternately 8 internal parallel inputs support.


The DFSDM peripheral is dedicated to interface the external Σ∆ modulators to
microcontroller and then to perform digital filtering of the received data streams (which
represent analog value on Σ∆ modulators inputs). DFSDM can also interface PDM (Pulse
Density Modulation) microphones and perform PDM to PCM conversion and filtering in
hardware. DFSDM features optional parallel data stream inputs from internal ADC
peripherals or microcontroller memory (through DMA/CPU transfers into DFSDM).


DFSDM transceivers support several serial interface formats (to support various Σ∆
modulators). DFSDM digital filter modules perform digital processing according user
selected filter parameters with up to 24-bit final ADC resolution.


The DFSDM peripheral supports:


      - 8 multiplexed input digital serial channels:


–
configurable SPI interface to connect various SD modulator(s)


–
configurable Manchester coded 1 wire interface support


–
PDM (Pulse Density Modulation) microphone input support


–
maximum input clock frequency up to 20 MHz (10 MHz for Manchester coding)


–
clock output for SD modulator(s): 0..20 MHz


      - alternative inputs from 8 internal digital parallel channels (up to 16 bit input resolution):


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


DS12110 Rev 10 39/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**


      - short circuit detector to detect saturated analog input values (bottom and top range):


–
up to 8-bit counter to detect 1..256 consecutive 0’s or 1’s on serial data stream


–
monitoring continuously each input serial channel


      - break signal generation on analog watchdog event or on short circuit detector event


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


**Table 4. DFSDM implementation**

|DFSDM features|DFSDM1|
|---|---|
|Number of filters|4|
|Number of input<br>transceivers/channels|8|
|Internal ADC parallel input|X|
|Number of external triggers|16|
|Regular channel information in<br>identification register|X|


###### **3.24 Digital camera interface (DCMI)**


The devices embed a camera interface that can connect with camera modules and CMOS
sensors through an 8-bit to 14-bit parallel interface, to receive video data. The camera
interface can achieve a data transfer rate up to 140 Mbyte/s using a 80 MHz pixel clock. It
features:


      - Programmable polarity for the input pixel clock and synchronization signals


      - Parallel data communication can be 8-, 10-, 12- or 14-bit


      - Supports 8-, 10-, 12- and 14-bit progressive video monochrome or raw bayer format,
YCbCr 4:2:2 progressive video, RGB 565 progressive video or compressed data (like
JPEG)


      - Supports Continuous mode or Snapshot (a single frame) mode


      - Capability to automatically crop the image

###### **3.25 LCD-TFT controller**


The LCD-TFT display controller (only available on STM32H743xI/G) provides a 24-bit
parallel digital RGB (Red, Green, Blue) and delivers all signals to interface directly to a


40/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


broad range of LCD and TFT panels up to XGA (1024x768) resolution with the following
features:


      - 2 display layers with dedicated FIFO (64x64-bit)


      - Color Look-Up table (CLUT) up to 256 colors (256x24-bit) per layer


      - Up to 8 input color formats selectable per layer


      - Flexible blending between two layers using alpha value (per pixel or constant)


      - Flexible programmable parameters for each layer


      - Color keying (transparency color)


      - Up to 4 programmable interrupt events


      - AXI master interface with burst of 16 words

###### **3.26 JPEG Codec (JPEG)**


The JPEG Codec (only available on STM32H743xI/G) can encode and decode a JPEG
stream as defined in the _**ISO/IEC 10918-1**_ specification. It provides an fast and simple
hardware compressor and decompressor of JPEG images with full management of JPEG
headers.


The JPEG codec main features are as follows:


      - 8-bit/channel pixel depths


      - Single clock per pixel encoding and decoding


      - Support for JPEG header generation and parsing


      - Up to four programmable quantization tables


      - Fully programmable Huffman tables (two AC and two DC)


      - Fully programmable minimum coded unit (MCU)


      - Encode/decode support (non simultaneous)


      - Single clock Huffman coding and decoding


      - Two-channel interface: Pixel/Compress In, Pixel/Compressed Out


      - Support for single greyscale component


      - Ability to enable/disable header processing


      - Fully synchronous design


      - Configuration for High-speed decode mode

###### **3.27 True random number generator (RNG)**


The RNG is a true random number generator that provides full entropy outputs to the
application as 32-bit samples. It is composed of a live entropy source (analog) and an
internal conditioning component.

###### **3.28 Timers and watchdogs**


The devices include one high-resolution timer, two advanced-control timers, ten generalpurpose timers, two basic timers, five low-power timers, two watchdogs and a SysTick timer.


All timer counters can be frozen in Debug mode.


DS12110 Rev 10 41/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**


_Table 5_ compares the features of the advanced-control, general-purpose and basic timers.


**Table 5. Timer feature comparison**




















|Timer<br>type|Timer|Counter<br>resolution|Counter<br>type|Prescaler<br>factor|DMA<br>request<br>generation|Capture/<br>compare<br>channels|Comple-<br>mentary<br>output|Max<br>interface<br>clock<br>(MHz)|Max<br>timer<br>clock<br>(MHz)<br>(1)|
|---|---|---|---|---|---|---|---|---|---|
|High-<br>resolution<br>timer|HRTIM1|16-bit|Up|/1 /2 /4<br>(x2 x4 x8<br>x16 x32,<br>with DLL)|Yes|10|Yes|480|480|
|Advanced<br>-control|TIM1,<br>TIM8|16-bit|Up,<br>Down,<br>Up/down|Any<br>integer<br>between 1<br>and<br>65536|Yes|4|Yes|120|240|
|General<br>purpose|TIM2,<br>TIM5|32-bit|Up,<br>Down,<br>Up/down|Any<br>integer<br>between 1<br>and<br>65536|Yes|4|No|120|240|
|General<br>purpose|TIM3,<br>TIM4|16-bit|Up,<br>Down,<br>Up/down|Any<br>integer<br>between 1<br>and<br>65536|Yes|4|No|120|240|
|General<br>purpose|TIM12|16-bit|Up|Any<br>integer<br>between 1<br>and<br>65536|No|2|No|120|240|
|General<br>purpose|TIM13,<br>TIM14|16-bit|Up|Any<br>integer<br>between 1<br>and<br>65536|No|1|No|120|240|
|General<br>purpose|TIM15|16-bit|Up|Any<br>integer<br>between 1<br>and<br>65536|Yes|2|1|120|240|
|General<br>purpose|TIM16,<br>TIM17|16-bit|Up|Any<br>integer<br>between 1<br>and<br>65536|Yes|1|1|120|240|



42/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


**Table 5. Timer feature comparison (continued)**


























|Timer<br>type|Timer|Counter<br>resolution|Counter<br>type|Prescaler<br>factor|DMA<br>request<br>generation|Capture/<br>compare<br>channels|Comple-<br>mentary<br>output|Max<br>interface<br>clock<br>(MHz)|Max<br>timer<br>clock<br>(MHz)<br>(1)|
|---|---|---|---|---|---|---|---|---|---|
|Basic|TIM6,<br>TIM7|16-bit|Up|Any<br>integer<br>between 1<br>and<br>65536|Yes|0|No|120|240|
|Low-<br>power<br>timer|LPTIM1,<br>LPTIM2,<br>LPTIM3,<br>LPTIM4,<br>LPTIM5|16-bit|Up|1, 2, 4, 8,<br>16, 32, 64,<br>128|No|0|No|120|240|



1. The maximum timer clock is up to 480 MHz depending on TIMPRE bit in the RCC_CFGR register and D2PRE1/2 bits in
RCC_D2CFGR register.


**3.28.1** **High-resolution timer (HRTIM1)**


The high-resolution timer (HRTIM1) allows generating digital signals with high-accuracy
timings, such as PWM or phase-shifted pulses.


It consists of 6 timers, 1 master and 5 slaves, totaling 10 high-resolution outputs, which can
be coupled by pairs for deadtime insertion. It also features 5 fault inputs for protection
purposes and 10 inputs to handle external events such as current limitation, zero voltage or
zero current switching.


The HRTIM1 timer is made of a digital kernel clocked at 480 MHz The high-resolution is
available on the 10 outputs in all operating modes: variable duty cycle, variable frequency,
and constant ON time.


The slave timers can be combined to control multiswitch complex converters or operate
independently to manage multiple independent converters.


The waveforms are defined by a combination of user-defined timings and external events
such as analog or digital feedbacks signals.


HRTIM1 timer includes options for blanking and filtering out spurious events or faults. It also
offers specific modes and features to offload the CPU: DMA requests, Burst mode
controller, Push-pull and Resonant mode.


It supports many topologies including LLC, Full bridge phase shifted, buck or boost
converters, either in voltage or current mode, as well as lighting application (fluorescent or
LED). It can also be used as a general purpose timer, for instance to achieve high-resolution
PWM-emulated DAC.


DS12110 Rev 10 43/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**


**3.28.2** **Advanced-control timers (TIM1, TIM8)**


The advanced-control timers (TIM1, TIM8) can be seen as three-phase PWM generators
multiplexed on 6 channels. They have complementary PWM outputs with programmable
inserted dead times. They can also be considered as complete general-purpose timers.
Their 4 independent channels can be used for:


      - Input capture


      - Output compare


      - PWM generation (Edge- or Center-aligned modes)


      - One-pulse mode output


If configured as standard 16-bit timers, they have the same features as the general-purpose
TIMx timers. If configured as 16-bit PWM generators, they have full modulation capability (0100%).


The advanced-control timer can work together with the TIMx timers via the Timer Link
feature for synchronization or event chaining.


TIM1 and TIM8 support independent DMA request generation.


**3.28.3** **General-purpose timers (TIMx)**


There are ten synchronizable general-purpose timers embedded in the STM32H742xI/G
and STM32H743xI/G devices (see _Table 5_ for differences).


      - **TIM2, TIM3, TIM4, TIM5**


The devices include 4 full-featured general-purpose timers: TIM2, TIM3, TIM4 and
TIM5. TIM2 and TIM5 are based on a 32-bit auto-reload up/downcounter and a 16-bit
prescaler while TIM3 and TIM4 are based on a 16-bit auto-reload up/downcounter and
a 16-bit prescaler. All timers feature 4 independent channels for input capture/output
compare, PWM or One-pulse mode output. This gives up to 16 input capture/output
compare/PWMs on the largest packages.


TIM2, TIM3, TIM4 and TIM5 general-purpose timers can work together, or with the
other general-purpose timers and the advanced-control timers TIM1 and TIM8 via the
Timer Link feature for synchronization or event chaining.


Any of these general-purpose timers can be used to generate PWM outputs.


TIM2, TIM3, TIM4, TIM5 all have independent DMA request generation. They are
capable of handling quadrature (incremental) encoder signals and the digital outputs
from 1 to 4 hall-effect sensors.


      - **TIM12, TIM13, TIM14, TIM15, TIM16, TIM17**


These timers are based on a 16-bit auto-reload upcounter and a 16-bit prescaler.
TIM13, TIM14, TIM16 and TIM17 feature one independent channel, whereas TIM12
and TIM15 have two independent channels for input capture/output compare, PWM or
One-pulse mode output. They can be synchronized with the TIM2, TIM3, TIM4, TIM5
full-featured general-purpose timers or used as simple timebases.


44/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


**3.28.4** **Basic timers TIM6 and TIM7**


These timers are mainly used for DAC trigger and waveform generation. They can also be
used as a generic 16-bit time base.


TIM6 and TIM7 support independent DMA request generation.


**3.28.5** **Low-power timers (LPTIM1, LPTIM2, LPTIM3, LPTIM4, LPTIM5)**


The low-power timers have an independent clock and is running also in Stop mode if it is
clocked by LSE, LSI or an external clock. It is able to wakeup the devices from Stop mode.


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


**3.28.6** **Independent watchdog**


The independent watchdog is based on a 12-bit downcounter and 8-bit prescaler. It is
clocked from an independent 32 kHz internal RC and as it operates independently from the
main clock, it can operate in Stop and Standby modes. It can be used either as a watchdog
to reset the device when a problem occurs, or as a free-running timer for application timeout
management. It is hardware- or software-configurable through the option bytes.


**3.28.7** **Window watchdog**


The window watchdog is based on a 7-bit downcounter that can be set as free-running. It
can be used as a watchdog to reset the device when a problem occurs. It is clocked from
the main clock. It has an early warning interrupt capability and the counter can be frozen in
Debug mode.


**3.28.8** **SysTick timer**


This timer is dedicated to real-time operating systems, but could also be used as a standard
downcounter. It features:


      - A 24-bit downcounter


      - Autoreload capability


      - Maskable system interrupt generation when the counter reaches 0


      - Programmable clock source.


DS12110 Rev 10 45/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.29 Real-time clock (RTC), backup SRAM and backup registers**


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


      - 17-bit auto-reload wakeup timer (WUT) for periodic events with programmable
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


All RTC events (Alarm, Wakeup Timer, Timestamp or Tamper) can generate an interrupt and
wakeup the device from the low-power modes.


46/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**

###### **3.30 Inter-integrated circuit interface (I2C)**


STM32H742xI/G and STM32H743xI/G devices embed four I [2] C interfaces.


The I [2] C bus interface handles communications between the microcontroller and the serial
I [2] C bus. It controls all I [2] C bus-specific sequencing, protocol, arbitration and timing.


The I2C peripheral supports:


      - I [2] C-bus specification and user manual rev. 5 compatibility:


–
Slave and Master modes, multimaster capability


–
Standard-mode (Sm), with a bitrate up to 100 kbit/s


–
Fast-mode (Fm), with a bitrate up to 400 kbit/s


–
Fast-mode Plus (Fm+), with a bitrate up to 1 Mbit/s and 20 mA output drive I/Os


–
7-bit and 10-bit addressing mode, multiple 7-bit slave addresses


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

      - Power System Management Protocol (PMBus [TM] ) specification rev 1.1 compatibility


      - Independent clock: a choice of independent clock sources allowing the I2C
communication speed to be independent from the PCLK reprogramming.


      - Wakeup from Stop mode on address match


      - Programmable analog and digital noise filters


      - 1-byte buffer with DMA capability

###### **3.31 Universal synchronous/asynchronous receiver transmitter** **(USART)**


STM32H742xI/G and STM32H743xI/G devices have four embedded universal synchronous
receiver transmitters (USART1, USART2, USART3 and USART6) and four universal
asynchronous receiver transmitters (UART4, UART5, UART7 and UART8). Refer to _Table 6_
for a summary of USARTx and UARTx features.


These interfaces provide asynchronous communication, IrDA SIR ENDEC support,
multiprocessor communication mode, single-wire Half-duplex communication mode and
have LIN Master/Slave capability. They provide hardware management of the CTS and RTS
signals, and RS485 Driver Enable. They are able to communicate at speeds of up to
12.5 Mbit/s.


USART1, USART2, USART3 and USART6 also provide Smartcard mode (ISO 7816
compliant) and SPI-like communication capability.


The USARTs embed a Transmit FIFO (TXFIFO) and a Receive FIFO (RXFIFO). FIFO mode
is enabled by software and is disabled by default.


DS12110 Rev 10 47/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**


All USART have a clock domain independent from the CPU clock, allowing the USARTx to
wake up the MCU from Stop mode.The wakeup from Stop mode is programmable and can
be done on:


      - Start bit detection


      - Any received data frame


      - A specific programmed data frame


      - Specific TXFIFO/RXFIFO status when FIFO mode is enabled.


All USART interfaces can be served by the DMA controller.


**Table 6. USART features**







|USART modes/features(1)|USART1/2/3/6|UART4/5/7/8|
|---|---|---|
|Hardware flow control for modem|X|X|
|Continuous communication using DMA|X|X|
|Multiprocessor communication|X|X|
|Synchronous mode (Master/Slave)|X|-|
|Smartcard mode|X|-|
|Single-wire Half-duplex communication|X|X|
|IrDA SIR ENDEC block|X|X|
|LIN mode|X|X|
|Dual clock domain and wakeup from low power mode|X|X|
|Receiver timeout interrupt|X|X|
|Modbus communication|X|X|
|Auto baud rate detection|X|X|
|Driver Enable|X|X|
|USART data length|7, 8 and 9 bits|7, 8 and 9 bits|
|Tx/Rx FIFO|X|X|
|Tx/Rx FIFO size|16|16|


1. X = supported.

###### **3.32 Low-power universal asynchronous receiver transmitter** **(LPUART)**


The device embeds one Low-Power UART (LPUART1). The LPUART supports
asynchronous serial communication with minimum power consumption. It supports half
duplex single wire communication and modem operations (CTS/RTS). It allows
multiprocessor communication.


The LPUARTs embed a Transmit FIFO (TXFIFO) and a Receive FIFO (RXFIFO). FIFO
mode is enabled by software and is disabled by default.


48/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


The LPUART has a clock domain independent from the CPU clock, and can wakeup the
system from Stop mode. The wakeup from Stop mode are programmable and can be done

on:


      - Start bit detection


      - Any received data frame


      - A specific programmed data frame


      - Specific TXFIFO/RXFIFO status when FIFO mode is enabled.


Only a 32.768 kHz clock (LSE) is needed to allow LPUART communication up to
9600 baud. Therefore, even in Stop mode, the LPUART can wait for an incoming frame
while having an extremely low energy consumption. Higher speed clock can be used to
reach higher baudrates.


LPUART interface can be served by the DMA controller.

###### **3.33 Serial peripheral interfaces (SPI)/integrated interchip** **sound interfaces (I2S)**


The devices feature up to six SPIs (SPI2S1, SPI2S2, SPI2S3, SPI4, SPI5 and SPI6) that
allow communicating up to 150 Mbits/s in Master and Slave modes, in Half-duplex, Fullduplex and Simplex modes. The 3-bit prescaler gives 8 master mode frequencies and the
frame is configurable from 4 to 16 bits. All SPI interfaces support NSS pulse mode, TI mode,
Hardware CRC calculation and 8x 8-bit embedded Rx and Tx FIFOs with DMA capability.


Three standard I [2] S interfaces (multiplexed with SPI1, SPI2 and SPI3) are available. They
can be operated in Master or Slave mode, in Simplex or Full-duplex communication mode,
and can be configured to operate with a 16-/32-bit resolution as an input or output channel.
Audio sampling frequencies from 8 kHz up to 192 kHz are supported. When either or both of
the I [2] S interfaces is/are configured in Master mode, the master clock can be output to the
external DAC/CODEC at 256 times the sampling frequency. All I [2] S interfaces support 16x 8bit embedded Rx and Tx FIFOs with DMA capability.

###### **3.34 Serial audio interfaces (SAI)**


The devices embed 4 SAIs (SAI1, SAI2, SAI3 and SAI4) that allow designing many stereo
or mono audio protocols such as I2S, LSB or MSB-justified, PCM/DSP, TDM or AC’97. An
SPDIF output is available when the audio block is configured as a transmitter. To bring this
level of flexibility and reconfigurability, the SAI contains two independent audio sub-blocks.
Each block has it own clock generator and I/O line controller.
Audio sampling frequencies up to 192 kHz are supported.
In addition, up to 6 microphones can be supported thanks to an embedded PDM interface.
The SAI can work in master or slave configuration. The audio sub-blocks can be either
receiver or transmitter and can work synchronously or asynchronously (with respect to the
other one). The SAI can be connected with other SAIs to work synchronously.


DS12110 Rev 10 49/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.35 SPDIFRX Receiver Interface (SPDIFRX)**


The SPDIFRX peripheral is designed to receive an S/PDIF flow compliant with IEC-60958
and IEC-61937. These standards support simple stereo streams up to high sample rate,
and compressed multi-channel surround sound, such as those defined by Dolby or DTS (up
to 5.1).


The main SPDIFRX features are the following:


      - Up to 4 inputs available


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
valid signal will be available, the SPDIFRX will re-sample the incoming signal, decode the
Manchester stream, recognize frames, sub-frames and blocks elements. It delivers to the
CPU decoded data, and associated status flags.


The SPDIFRX also offers a signal named spdif_frame_sync, which toggles at the S/PDIF
sub-frame rate that will be used to compute the exact sample rate for clock drift algorithms.

###### **3.36 Single wire protocol master interface (SWPMI)**


The Single wire protocol master interface (SWPMI) is the master interface corresponding to
the Contactless Frontend (CLF) defined in the ETSI TS 102 613 technical specification. The
main features are:


      - Full-duplex communication mode


      - automatic SWP bus state management (active, suspend, resume)


      - configurable bitrate up to 2 Mbit/s


      - automatic SOF, EOF and CRC handling


SWPMI can be served by the DMA controller.


50/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**

###### **3.37 Management Data Input/Output (MDIO) slaves**


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

###### **3.38 SD/SDIO/MMC card host interfaces (SDMMC)**


Two SDMMC host interfaces are available. They support _MultiMediaCard System_
_Specification Version 4.51_ in three different databus modes: 1 bit (default), 4 bits and 8 bits.


Both interfaces support the _SD memory card specifications version 4.1._ and the _SDIO card_
_specification version 4.0._ in two different databus modes: 1 bit (default) and 4 bits.


Each SDMMC host interface supports only one SD/SDIO/MMC card at any one time and a
stack of MMC Version 4.51 or previous.


The SDMMC host interface embeds a dedicated DMA controller allowing high-speed
transfers between the interface and the SRAM.

###### **3.39 Controller area network (FDCAN1, FDCAN2)**


The controller area network (CAN) subsystem consists of two CAN modules, a shared
message RAM memory and a clock calibration unit.


Both CAN modules (FDCAN1 and FDCAN2) are compliant with ISO 11898-1 (CAN protocol
specification version 2.0 part A, B) and CAN FD protocol specification version 1.0.


FDCAN1 supports time triggered CAN (TT-FDCAN) specified in ISO 11898-4, including
event synchronized time-triggered communication, global system time, and clock drift
compensation. The FDCAN1 contains additional registers, specific to the time triggered
feature. The CAN FD option can be used together with event-triggered and time-triggered
CAN communication.


A 10-Kbyte message RAM memory implements filters, receive FIFOs, receive buffers,
transmit event FIFOs, transmit buffers (and triggers for TT-FDCAN). This message RAM is
shared between the two FDCAN1 and FDCAN2 modules.


The common clock calibration unit is optional. It can be used to generate a calibrated clock
for both FDCAN1 and FDCAN2 from the HSI internal RC oscillator and the PLL, by
evaluating CAN messages received by the FDCAN1.


DS12110 Rev 10 51/357



54


**Functional overview** **STM32H742xI/G STM32H743xI/G**

###### **3.40 Universal serial bus on-the-go high-speed (OTG_HS)**


The devices embed two USB OTG high-speed (up to 480 Mbit/s) device/host/OTG
peripheral. OTG-HS1 supports both full-speed and high-speed operations, while OTG-HS2
supports only full-speed operations. They both integrate the transceivers for full-speed
operation (12 Mbit/s) and are able to operate from the internal HSI48 oscillator. OTG-HS1
features a UTMI low-pin interface (ULPI) for high-speed operation (480 Mbit/s). When using
the USB OTG-HS1 in HS mode, an external PHY device connected to the ULPI is required.


The USB OTG HS peripherals are compliant with the USB 2.0 specification and with the
OTG 2.0 specification. They have software-configurable endpoint setting and supports
suspend/resume. The USB OTG controllers require a dedicated 48 MHz clock that is
generated by a PLL connected to the HSE oscillator.


The main features are:


      - Combined Rx and Tx FIFO size of 4 Kbytes with dynamic FIFO sizing


      - Supports the session request protocol (SRP) and host negotiation protocol (HNP)


      - 9 bidirectional endpoints (including EP0)


      - 16 host channels with periodic OUT support


      - Software configurable to OTG1.3 and OTG2.0 modes of operation


      - USB 2.0 LPM (Link Power Management) support


      - Battery Charging Specification Revision 1.2 support


      - Internal FS OTG PHY support


      - External HS or HS OTG operation supporting ULPI in SDR mode (OTG_HS1 only)


The OTG PHY is connected to the microcontroller ULPI port through 12 signals. It can
be clocked using the 60 MHz output.


      - Internal USB DMA


      - HNP/SNP/IP inside (no need for any external resistor)


      - For OTG/Host modes, a power switch is needed in case bus-powered devices are
connected

###### **3.41 Ethernet MAC interface with dedicated DMA controller (ETH)**


The devices provide an IEEE-802.3-2002-compliant media access controller (MAC) for
ethernet LAN communications through an industry-standard medium-independent interface
(MII) or a reduced medium-independent interface (RMII). The microcontroller requires an
external physical interface device (PHY) to connect to the physical LAN bus (twisted-pair,
fiber, etc.). The PHY is connected to the device MII port using 17 signals for MII or 9 signals
for RMII, and can be clocked using the 25 MHz (MII) from the microcontroller.


52/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Functional overview**


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

###### **3.42 High-definition multimedia interface (HDMI)** **- consumer electronics control (CEC)**


The devices embed a HDMI-CEC controller that provides hardware support for the
Consumer Electronics Control (CEC) protocol (Supplement 1 to the HDMI standard).


This protocol provides high-level control functions between all audiovisual products in an
environment. It is specified to operate at low speeds with minimum processing and memory
overhead. It has a clock domain independent from the CPU clock, allowing the HDMI-CEC
controller to wakeup the MCU from Stop mode on data reception.

###### **3.43 Debug infrastructure**


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


The debug can be controlled via a JTAG/Serial-wire debug access port, using industry
standard debugging tools.


The trace port performs data capture for logging and analysis.


DS12110 Rev 10 53/357



54


**Memory mapping** **STM32H742xI/G STM32H743xI/G**

#### **4 Memory mapping**


Refer to _Table 7_ for details on STM32H742xI/G flash and SRAM block memory mapping
and to the product line reference manual for information on the boundary addresses for all
STM32H742xI/G peripherals.


Details on STM32H743xGxI/G flash and SRAM block memory mapping and boundary
addresses for all STM32H743xI/G peripherals are given in the product line reference
manual.


**Table 7. Flash memory and SRAM memory mapping for STM32H742xI/G**

|Col1|Memory|Size in Kbytes|Start address|
|---|---|---|---|
|**RAM area**|Backup SRAM|4|0x3880 0000|
|**RAM area**|SRAM4|64|0x3800 0000|
|**RAM area**|SRAM2|16|0x3002 0000|
|**RAM area**|SRAM1|32|0x3000 0000|
|**RAM area**|AXI-SRAM|384|0x2400 0000|
|**RAM area**|DTCM|128|0x2000 0000|
|**Code area**|System memory 2|-|0x1FF4 0000|
|**Code area**|System memory|-|0x1FF0 0000|
|**Code area**|Flash memory|2048|0x0800 0000|
|**Code area**|ITCM|64|0x0000 0000|



54/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**

#### **5 Pin descriptions**



**Figure 5. LQFP100 pinout**







1. The above figure shows the package top view.



DS12110 Rev 10 55/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Figure 6. TFBGA100 pinout**


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




















|PC14-<br>OSC32_IN|PC13|PE2|PB9|PB7|PB4|PB3|PA15|PA14|PA13|
|---|---|---|---|---|---|---|---|---|---|
|**PC15-**<br>**OSC32_OUT**|**VBAT**|**PE3**|**PB8**|**PB6**|**PD5**|**PD2**|**PC11**|**PC10**|**PA12**|
|**PH0-OSC_IN**|**VSS**|**PE4**|**PE1**|**PB5**|**PD6**|**PD3**|**PC12**|**PA9**|**PA11**|
|**PH1-**<br>**OSC_OUT**|**VDD**|**PE5**|**PE0**|**BOOT0**|**PD7**|**PD4**|**PD0**|**PA8**|**PA10**|
|**NRST**|**PC2_C**|**PE6**|**VSS**|**VSS**|**VSS**|**VCAP**|**PD1**|**PC9**|**PC7**|
|**PC0**|**PC1**|**PC3_C**|**VDDLDO**|**VDD**|**VDD33USB**|**PDR_ON**|**VCAP**|**PC8**|**PC6**|
|**VSSA**|**PA0**|**PA4**|**PC4**|**PB2**|**PE10**|**PE14**|**PD15**|**PD11**|**PB15**|
|**VDDA**|**PA1**|**PA5**|**PC5**|**PE7**|**PE11**|**PE15**|**PD14**|**PD10**|**PB14**|
|**VSS**|**PA2**|**PA6**|**PB0**|**PE8**|**PE12**|**PB10**|**PB13**|**PD9**|**PD13**|
|**VDD**|**PA3**|**PA7**|**PB1**|**PE9**|**PE13**|**PB11**|**PB12**|**PD8**|**PD12**|



MSv46177V2



1. The above figure shows the package top view.


56/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Figure 7. LQFP144 pinout**





1. The above figure shows the package top view.



DS12110 Rev 10 57/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Figure 8. UFBGA169 ballout**


1 2 3 4 5 6 7 8 9 10 11 12 13



A


B


C


D


E


F


G


H


J


K


L


M


N



|PE4|PE2|VDD|PI6|PB6|PI2|VDD|PG10|PD5|VDD|PC12|PC10|PI0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PC15-<br>OSC32_<br>OUT|PE3|VSS|VDDLDO|PB8|PB4|PI3|PG11|PD6|VSS|PC11|PA14|PI1|
|PC14-<br>OSC32_<br>IN|PE6|PE5|PDR_ON|PB9|PB5|PG14|PG9|PD4|PD1|PA15|VSS|VDD|
|VDD|VSS|PC13|PE1|PE0|PB7|PG13|PD7|PD3|PD0|PA13|VDDLDO|VCAP|
|PI11|PI7|VBAT|PF1|PF3|BOOT0|PG15|PG12|PD2|PA10|PA9|PA8|PA12|
|PI13|PI12|PF0|PF2|PF5|PF7|PB3|PG4|PC6|PC7|PC9|PC8|PA11|
|VDD|VSS|PF4|PF6|PF9|NRST|PF13|PE7|PG6|PG7|PG8|VDD50_<br>USB|VDD33_<br>USB|
|PH0-<br>OSC_<br>IN|PH1-<br>OSC_<br>OUT|PF10|PF8|PJ1|PA4|PF14|PE8|PG2|PG3|PG5|VSS|VDD|
|PC0|PC1|VSSA|PJ0|PA0|PA7|PF15|PE9|PE14|PD11|PD13|PD15|PD14|
|PC3_C|PC2_C|PH4|PA1|PA6|PC4|PG0|PE13|PH10|PH12|PD9|PD10|PD12|
|VDDA|VREF+|PH5|PA5|PB1|PB2|PG1|PE12|PB10|PH11|PB13|VSS|VDD|
|VDD|VSS|PH3|VSS|PB0|PF11|VSS|PE10|PB11|VDDLDO|VSS|PD8|PB15|
|PA2|PH2|PA3|VDD|PC5|PF12|VDD|PE11|PE15|VCAP|VDD|PB12|PB14|


MSv45339V4

















1. The above figure shows the package top view.


58/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Figure 9. LQFP176 pinout**





1. The above figure shows the package top view.



DS12110 Rev 10 59/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**

|Col1|Figure 10. UFBGA176+25 ballout|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|MSv41912V3<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>A<br>PE3<br>PE2<br>PE1<br>PE0<br>PB8<br>PB5<br>PG14<br>PG13<br>PB4<br>PB3<br>PD7<br>PC12<br>PA15<br>PA14<br>PA13<br>B<br>PE4<br>PE5<br>PE6<br>PB9<br>PB7<br>PB6<br>PG15<br>PG12<br>PG11<br>PG10<br>PD6<br>PD0<br>PC11<br>PC10<br>PA12<br>C<br>VBAT<br>PI7<br>PI6<br>PI5<br>VDD<br>PDR_ON<br>VDD<br>VDD<br>VDD<br>PG9<br>PD5<br>PD1<br>PI3<br>PI2<br>PA11<br>D<br>PC13<br>PI8<br>PI9<br>PI4<br>VSS<br>BOOT0<br>VSS<br>VSS<br>VSS<br>PD4<br>PD3<br>PD2<br>PH15<br>PI1<br>PA10<br>E<br>PC14-<br>OSC32_<br>IN<br>PF0<br>PI10<br>PI11<br>PH13<br>PH14<br>PI0<br>PA9<br>F<br>PC15-<br>OSC32_<br>OUT<br>VSS<br>VDD<br>PH2<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VCAP<br>PC9<br>PA8<br>G<br>PH0-<br>OSC_IN<br>VSS<br>VDD<br>PH3<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>PC8<br>PC7<br>H<br>PH1-<br>OSC_<br>OUT<br>PF2<br>PF1<br>PH4<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>33USB<br>PG8<br>PC6<br>J<br>NRST<br>PF3<br>PF4<br>PH5<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>VDD<br>VDD<br>PG7<br>PG6<br>K<br>PF7<br>PF6<br>PF5<br>VDD<br>VSS<br>VSS<br>VSS<br>VSS<br>VSS<br>PH12<br>PG5<br>PG4<br>PG3<br>L<br>PF10<br>PF9<br>PF8<br>PH11<br>PH10<br>PD15<br>PG2<br>M<br>VSSA<br>PC0<br>PC1<br>PC2_C<br>PC3_C<br>PB2<br>PG1<br>VSS<br>VSS<br>VCAP<br>PH6<br>PH8<br>PH9<br>PD14<br>PD13<br>N<br>VREF-<br>PA1<br>PA0<br>PA4<br>PC4<br>PF13<br>PG0<br>VDD<br>VDD<br>VDD<br>PE13<br>PH7<br>PD12<br>PD11<br>PD10<br>P<br>VREF+<br>PA2<br>PA6<br>PA5<br>PC5<br>PF12<br>PF15<br>PE8<br>PE9<br>PE11<br>PE14<br>PB12<br>PB13<br>PD9<br>PD8<br>R<br>VDDA<br>PA3<br>PA7<br>PB1<br>PB0<br>PF11<br>PF14<br>PE7<br>PE10<br>PE12<br>PE15<br>PB10<br>PB11<br>PB14<br>PB15<br>VSS|
|||1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|
||A|PE3|PE2|PE1|PE0|PB8|PB5|PG14|PG13|PB4|PB3|PD7|PC12|PA15|PA14|PA13|
||B|PE4|PE5|PE6|PB9|PB7|PB6|PG15|PG12|PG11|PG10|PD6|PD0|PC11|PC10|PA12|
||C|VBAT|PI7|PI6|PI5|VDD|PDR_ON|VDD|VDD|VDD|PG9|PD5|PD1|PI3|PI2|PA11|
||D|PC13|PI8|PI9|PI4|VSS|BOOT0|VSS|VSS|VSS|PD4|PD3|PD2|PH15|PI1|PA10|
||E|PC14-<br>OSC32_<br>IN|PF0|PI10|PI11||||||||PH13|PH14|PI0|PA9|
||F|PC15-<br>OSC32_<br>OUT|VSS|VDD|PH2||VSS|VSS|VSS|VSS|VSS||VSS|VCAP|PC9|PA8|
||G|PH0-<br>OSC_IN|VSS|VDD|PH3||VSS|VSS|VSS|VSS|VSS||VSS|VDD|PC8|PC7|
||H|PH1-<br>OSC_<br>OUT|PF2|PF1|PH4||VSS|VSS|VSS|VSS|VSS||VSS|VDD<br>33USB|PG8|PC6|
||J|NRST|PF3|PF4|PH5||VSS|VSS|VSS|VSS|VSS||VDD|VDD|PG7|PG6|
||K|PF7|PF6|PF5|VDD||VSS|VSS|VSS|VSS|VSS||PH12|PG5|PG4|PG3|
||L|PF10|PF9|PF8|VSS||||||||PH11|PH10|PD15|PG2|
||M|VSSA|PC0|PC1|PC2_C|PC3_C|PB2|PG1|VSS|VSS|VCAP|PH6|PH8|PH9|PD14|PD13|
||N|VREF-|PA1|PA0|PA4|PC4|PF13|PG0|VDD|VDD|VDD|PE13|PH7|PD12|PD11|PD10|
||P|VREF+|PA2|PA6|PA5|PC5|PF12|PF15|PE8|PE9|PE11|PE14|PB12|PB13|PD9|PD8|
||R|VDDA|PA3|PA7|PB1|PB0|PF11|PF14|PE7|PE10|PE12|PE15|PB10|PB11|PB14|PB15|
||||||||||||||||||



1. The above figure shows the package top view.


60/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Figure 11. LQFP208 pinout**







1. The above figure shows the package top view.



DS12110 Rev 10 61/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Figure 12. TFBGA240+25 ballout**












|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VSS|PI6|PI5|PI4|PB5|VDD<br>LDO|VCAP|PK5|PG10|PG9|PD5|PD4|PC10|PA15|PI1|PI0|VSS|
|VBAT|VSS|PI7|PE1|PB6|VSS|PB4|PK4|PG11|PJ15|PD6|PD3|PC11|PA14|PI2|PH15|PH14|
|PC15-<br>OSC32_<br>OUT|PC14-<br>OSC32_<br>IN|PE2<br>|PE0|PB7|PB3|PK6|PK3|PG12|VSS|PD7|PC12|VSS|PI3|PA13|VSS|VDD<br>LDO|
|PE5|PE4<br>|PE3|PB9|PB8|PG15|PK7|PG14|PG13|PJ14|PJ12|PD2|PD0|PA10|PA9|PH13|VCAP|
|NC(2)|PI9|PC13|PI8|PE6|VDD|PDR_<br>ON|BOO<br>T0|VDD|PJ13|VDD|PD1|PC8|PC9|PA8|PA12|PA11|
|VSS(3)|VSS(4)|PI10|PI11|VDD||||||||PC7|PC6|PG8|PG7|VDD33<br>USB|
|PF2|VSS(4)|PF1|PF0|VDD||VSS|VSS|VSS|VSS|VSS||VDD|PG5|PG6|VSS|VDD50<br>USB|
|PI12|PI13|PI14|PF3|VDD||VSS|VSS|VSS|VSS|VSS||VDD|PG4|PG3|PG2|PK2|
|PH1-<br>OSC_<br>~~OUT~~|PH0-<br>OSC_IN|VSS|PF5|PF4||VSS|VSS|VSS|VSS|VSS||VDD|PK0|PK1|VSS|VSS|
|NRST<br>|PF6|PF7|PF8|VDD||VSS|VSS|VSS|VSS|VSS||VDD|PJ11|VSS|NC|NC|
|VDDA|PC0|PF10|PF9|VDD||VSS|VSS|VSS|VSS|VSS||VDD|PJ10|VSS|NC|NC|
|VREF+|PC1|PC2|PC3|VDD||||||||VDD|PJ9|VSS|NC|NC|
|VREF-|PH2|PA2|PA1|PA0|PJ0|VDD|VDD|PE10|VDD|VDD|VDD|PJ8|PJ7|PJ6|VSS|NC|
|VSSA|PH3|PH4|PH5|PI15|PJ1|PF13|PF14|PE9|PE11|PB10|PB11|PH10|PH11|PD15|PD14|VDD|
|PC2_C|PC3_C|PA6|VSS|PA7|PB2|PF12|VSS|PF15|PE12|PE15|PJ5|PH9|PH12|PD11|PD12|PD13|
|PA0_C|PA1_C|PA5|PC4|PB1|PJ2|PF11|PG0|PE8|PE13|PH6|VSS|PH8|PB12|PB15|PD10|PD9|
|VSS|PA3|PA4|PC5|PB0|PJ3|PJ4|PG1|PE7|PE14|VCAP|VDD<br>LDO|PH7|PB13|PB14|PD8|VSS|



1. The above figure shows the package top view.


2. This ball should remain floating.


3. This ball should not remain floating. It can be connected to VSS or VDD. It is reserved for future use.


4. This ball should be connected to VSS.


62/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 8. Legend/abbreviations used in the pinout table**







|Name|Col2|Abbreviation|Definition|
|---|---|---|---|
|Pin name|Pin name|Unless otherwise specified in brackets below the pin name, the pin function during<br>and after reset is the same as the actual pin name|Unless otherwise specified in brackets below the pin name, the pin function during<br>and after reset is the same as the actual pin name|
|Pin type|Pin type|S|Supply pin|
|Pin type|Pin type|I|Input only pin|
|Pin type|Pin type|I/O|Input / output pin|
|Pin type|Pin type|ANA|Analog-only Input|
|I/O structure|I/O structure|FT|5 V tolerant I/O|
|I/O structure|I/O structure|TT|3.3 V tolerant I/O|
|I/O structure|I/O structure|B|Dedicated BOOT0 pin|
|I/O structure|I/O structure|RST|Bidirectional reset pin with embedded weak pull-up resistor|
|I/O structure|I/O structure|**Option for TT and FT I/Os**|**Option for TT and FT I/Os**|
|I/O structure|I/O structure|_f|I2C FM+ option|
|I/O structure|I/O structure|_a|analog option (supplied by VDDA)|
|I/O structure|I/O structure|_u|USB option (supplied by VDD33USB)|
|I/O structure|I/O structure|_h|High-speed low-voltage I/O|
|Notes|Notes|Unless otherwise specified by a note, all I/Os are set as floating inputs during and<br>after reset.|Unless otherwise specified by a note, all I/Os are set as floating inputs during and<br>after reset.|
|Pin functions|Alternate<br>functions|Functions selected through GPIOx_AFR registers|Functions selected through GPIOx_AFR registers|
|Pin functions|Additional<br>functions|Functions directly selected/enabled through peripheral registers|Functions directly selected/enabled through peripheral registers|


_Table 9_ and _Table 10_ to _Table 20_ show STM32H743xI/G pin/ball definition and alternate
functions, respectively. Refer to _Table 2_ for the features and peripherals available on
STM32H742xI/G devices.


DS12110 Rev 10 63/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition**



















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|1|A3|1|A2|A2|1|1|C3|PE2|I/O|FT_h|-|TRACECLK, SAI1_CK1,<br>SPI4_SCK,<br>SAI1_MCLK_A,<br>SAI4_MCLK_A,<br>QUADSPI_BK1_IO2,<br>SAI4_CK1,<br>ETH_MII_TXD3,<br>FMC_A23, EVENTOUT|-|
|2|B3|2|B2|A1|2|2|D3|PE3|I/O|FT_h|-|TRACED0, TIM15_BKIN,<br>SAI1_SD_B, SAI4_SD_B,<br>FMC_A19, EVENTOUT|-|
|3|C3|3|A1|B1|3|3|D2|PE4|I/O|FT_h|-|TRACED1, SAI1_D2,<br>DFSDM1_DATIN3,<br>TIM15_CH1N,<br>SPI4_NSS, SAI1_FS_A,<br>SAI4_FS_A, SAI4_D2,<br>FMC_A20, DCMI_D4,<br>LCD_B0, EVENTOUT|-|
|4|D3|4|C3|B2|4|4|D1|PE5|I/O|FT_h|-|TRACED2, SAI1_CK2,<br>DFSDM1_CKIN3,<br>TIM15_CH1, SPI4_MISO,<br>SAI1_SCK_A,<br>SAI4_SCK_A, SAI4_CK2,<br>FMC_A21, DCMI_D6,<br>LCD_G0, EVENTOUT|-|
|5|E3|5|C2|B3|5|5|E5|PE6|I/O|FT_h|-|TRACED3, TIM1_BKIN2,<br>SAI1_D1, TIM15_CH2,<br>SPI4_MOSI, SAI1_SD_A,<br>SAI4_SD_A, SAI4_D1,<br>SAI2_MCLK_B,<br>TIM1_BKIN2_COMP12,<br>FMC_A22, DCMI_D7,<br>LCD_G1, EVENTOUT|-|
|-|-|-|M4|H10|-|-|A1|VSS|S|-|-|-|-|
|-|-|-|A3|-|-|-|-|VDD|S|-|-|-|-|
|6|B2|6|E3|C1|6|6|B1|VBAT|S|-|-|-|-|
|-|-|-|-|J6|-|-|B2|VSS|S|-|-|-|-|
|-|-|-|-|D2|7|7|E4|PI8|I/O|FT|-|EVENTOUT|RTC_TAMP2/<br>WKUP3|
|7|A2|7|D3|D1|8|8|E3|PC13|I/O|FT|-|EVENTOUT|RTC_TAMP1/<br>RTC_TS/<br>WKUP4|
|-|-|-|-|J7|-|-|B6|VSS|S|-|-|-|-|


64/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|8|A1|8|C1|E1|9|9|C2|PC14-<br>OSC32_<br>IN<br>(OSC32_<br>IN)(1)|I/O|FT|-|EVENTOUT|OSC32_IN|
|9|B1|9|B1|F1|10|10|C1|PC15-<br>OSC32_<br>OUT<br>(OSC32_<br>OUT)(1)|I/O|FT|-|EVENTOUT|OSC32_<br>OUT|
|-|-|-|-|D3|11|11|E2|PI9|I/O|FT_h|-|UART4_RX,<br>FDCAN1_RX, FMC_D30,<br>LCD_VSYNC,<br>EVENTOUT|-|
|-|-|-|-|E3|12|12|F3|PI10|I/O|FT_h|-|ETH_MII_RX_ER,<br>FMC_D31, LCD_HSYNC,<br>EVENTOUT|-|
|-|-|-|E1|E4|13|13|F4|PI11|I/O|FT|-|LCD_G6,<br>OTG_HS_ULPI_DIR,<br>EVENTOUT|WKUP5|
|-|C2|-|D2|F2|14|14|A17|VSS|S|-|-|-|-|
|-|D2|-|D1|F3|15|15|E6|VDD|S|-|-|-|-|
|-|-|-|-|-|-|-|E1(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|F1(3)|VSS|S|-|-|-|-|
|-|-|-|-|-|-|-|G2(4)|VSS|S|-|-|-|-|
|-|-|10|F3|E2|16|16|G4|PF0|I/O|FT_f|-|I2C2_SDA, FMC_A0,<br>EVENTOUT|-|
|-|-|11|E4|H3|17|17|G3|PF1|I/O|FT_f|-|I2C2_SCL, FMC_A1,<br>EVENTOUT|-|
|-|-|12|F4|H2|18|18|G1|PF2|I/O|FT|-|I2C2_SMBA, FMC_A2,<br>EVENTOUT|-|
|-|-|-|F2|-|-|19|H1|PI12|I/O|FT|-|LCD_HSYNC,<br>EVENTOUT|-|
|-|-|-|F1|-|-|20|H2|PI13|I/O|FT|-|LCD_VSYNC,<br>EVENTOUT|-|
|-|-|-|-|-|-|21|H3|PI14|I/O|FT_h|-|LCD_CLK, EVENTOUT|-|
|-|-|13|E5|J2|19|22|H4|PF3|I/O|FT_<br>ha|-|FMC_A3, EVENTOUT|ADC3_INP5|
|-|-|14|G3|J3|20|23|J5|PF4|I/O|FT_<br>ha|-|FMC_A4, EVENTOUT|ADC3_INN5,<br>ADC3_INP9|


DS12110 Rev 10 65/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|15|F5|K3|21|24|J4|PF5|I/O|FT_<br>ha|-|FMC_A5, EVENTOUT|ADC3_INP4|
|10|-|16|B10|G2|22|25|C10|VSS|S|-|-|-|-|
|11|-|17|G1|G3|23|26|E9|VDD|S|-|-|-|-|
|-|-|18|G4|K2|24|27|K2|PF6|I/O|FT_<br>ha|-|TIM16_CH1, SPI5_NSS,<br>SAI1_SD_B, UART7_RX,<br>SAI4_SD_B,<br>QUADSPI_BK1_IO3,<br>EVENTOUT|ADC3_INN4,<br>ADC3_INP8|
|-|-|19|F6|K1|25|28|K3|PF7|I/O|FT_<br>ha|-|TIM17_CH1, SPI5_SCK,<br>SAI1_MCLK_B,<br>UART7_TX,<br>SAI4_MCLK_B,<br>QUADSPI_BK1_IO2,<br>EVENTOUT|ADC3_INP3|
|-|-|20|H4|L3|26|29|K4|PF8|I/O|FT_<br>ha|-|TIM16_CH1N,<br>SPI5_MISO,<br>SAI1_SCK_B,<br>UART7_RTS/UART7_DE<br>, SAI4_SCK_B,<br>TIM13_CH1,<br>QUADSPI_BK1_IO0,<br>EVENTOUT|ADC3_INN3,<br>ADC3_INP7|
|-|-|21|G5|L2|27|30|L4|PF9|I/O|FT_<br>ha|-|TIM17_CH1N,<br>SPI5_MOSI, SAI1_FS_B,<br>UART7_CTS,<br>SAI4_FS_B, TIM14_CH1,<br>QUADSPI_BK1_IO1,<br>EVENTOUT|ADC3_INP2|
|-|-|22|H3|L1|28|31|L3|PF10|I/O|FT_<br>ha|-|TIM16_BKIN, SAI1_D3,<br>QUADSPI_CLK,<br>SAI4_D3, DCMI_D11,<br>LCD_DE, EVENTOUT|ADC3_INN2,<br>ADC3_INP6|
|12|C1|23|H1|G1|29|32|J2|PH0-<br>OSC_IN<br>(PH0)|I/O|FT|-|EVENTOUT|OSC_IN|
|13|D1|24|H2|H1|30|33|J1|PH1-<br>OSC_OUT<br>(PH1)|I/O|FT|-|EVENTOUT|OSC_OUT|
|14|E1|25|G6|J1|31|34|K1|NRST|I/O|RST|-|-|-|


66/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**





















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|15|F1|26|J1|M2|32|35|L2|PC0|I/O|FT_a|-|DFSDM1_CKIN0,<br>DFSDM1_DATIN4,<br>SAI2_FS_B,<br>OTG_HS_ULPI_STP,<br>FMC_SDNWE, LCD_R5,<br>EVENTOUT|ADC123_<br>INP10|
|16|F2|27|J2|M3|33|36|M2|PC1|I/O|FT_<br>ha|-|TRACED0, SAI1_D1,<br>DFSDM1_DATIN0,<br>DFSDM1_CKIN4,<br>SPI2_MOSI/I2S2_SDO,<br>SAI1_SD_A, SAI4_SD_A,<br>SDMMC2_CK, SAI4_D1,<br>ETH_MDC,<br>MDIOS_MDC,<br>EVENTOUT|ADC123_<br>INN10,<br>ADC123_<br>INP11,<br>RTC_TAMP3/<br>WKUP6|
|-|-|-|-|-|-|-|M3(5)|PC2|I/O|FT_a|-|CDSLEEP,<br>DFSDM1_CKIN1,<br>SPI2_MISO/I2S2_SDI,<br>DFSDM1_CKOUT,<br>OTG_HS_ULPI_DIR,<br>ETH_MII_TXD2,<br>FMC_SDNE0,<br>EVENTOUT|ADC123_<br>INN11,<br>ADC123_<br>INP12|
|17<br>(6)|E2(6)|28(6)|K2(6)|M4(6)|34(6)|37(6)|R1(5)|PC2_C|ANA|TT_a|-|-|ADC3_INN1,<br>ADC3_INP0|
|-|-|-|-|-|-|-|M4(5)|PC3|I/O|FT_a|-|CSLEEP,<br>DFSDM1_DATIN1,<br>SPI2_MOSI/I2S2_SDO,<br>OTG_HS_ULPI_NXT,<br>ETH_MII_TX_CLK,<br>FMC_SDCKE0,<br>EVENTOUT|ADC12_INN12,<br>ADC12_INP13|
|18<br>(6)|F3(6)|29(6)|K1(6)|M5(6)|35(6)|38(6)|R2(5)|PC3_C|ANA|TT_a|-|-|ADC3_INP1|
|-|F5|30|-|G3|36|39|E11|VDD|S|-|-|-|-|
|-|E6|-|B3|J10|-|-|C13|VSS|S|-|-|-|-|
|19|G1|31|J3|M1|37|40|P1|VSSA|S|-|-|-|-|
|-|-|-|-|N1|-|-|N1|VREF-|S|-|-|-|-|
|20|-(7)|32|L2|P1|38|41|M1|VREF+|S|-|-|-|-|
|21|H1|33|L1|R1|39|42|L1|VDDA|S|-|-|-|-|


DS12110 Rev 10 67/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**

































|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|22|G2|34|J5|N3|40|43|N5(5)|PA0|I/O|FT_a|-|TIM2_CH1/TIM2_ETR,<br>TIM5_CH1, TIM8_ETR,<br>TIM15_BKIN,<br>USART2_CTS/USART2_<br>NSS, UART4_TX,<br>SDMMC2_CMD,<br>SAI2_SD_B,<br>ETH_MII_CRS,<br>EVENTOUT|ADC1_INP16,<br>WKUP1|
|-|-|-|-|-|-|-|T1(5)|PA0_C|ANA|TT_a|-|-|ADC12_INN1,<br>ADC12_INP0|
|23|H2|35|K4|N2|41|44|N4(5)|PA1|I/O|FT_<br>ha|-|TIM2_CH2, TIM5_CH2,<br>LPTIM3_OUT,<br>TIM15_CH1N,<br>USART2_RTS/USART2_<br>DE, UART4_RX,<br>QUADSPI_BK1_IO3,<br>SAI2_MCLK_B,<br>ETH_MII_RX_CLK/ETH_<br>RMII_REF_CLK,<br>LCD_R2, EVENTOUT|ADC1_INN16,<br>ADC1_INP17|
|-|-|-|-|-|-|-|T2(5)|PA1_C|ANA|TT_a|-|-|ADC12_INP1|
|24|J2|36|N1|P2|42|45|N3|PA2|I/O|FT_a|-|TIM2_CH3, TIM5_CH3,<br>LPTIM4_OUT,<br>TIM15_CH1,<br>USART2_TX,<br>SAI2_SCK_B,<br>ETH_MDIO,<br>MDIOS_MDIO, LCD_R1,<br>EVENTOUT|ADC12_INP14,<br>WKUP2|
|-|-|-|N2|F4|43|46|N2|PH2|I/O|FT_<br>ha|-|LPTIM1_IN2,<br>QUADSPI_BK2_IO0,<br>SAI2_SCK_B,<br>ETH_MII_CRS,<br>FMC_SDCKE0, LCD_R0,<br>EVENTOUT|ADC3_INP13|
|-|K1|-|M1|-|-|-|F5|VDD|S|-|-|-|-|
|-|J1|-|M7|J8|-|-|C16|VSS|S|-|-|-|-|
|-|-|-|M3|G4|44|47|P2|PH3|I/O|FT_<br>ha|-|QUADSPI_BK2_IO1,<br>SAI2_MCLK_B,<br>ETH_MII_COL,<br>FMC_SDNE0, LCD_R1,<br>EVENTOUT|ADC3_INN13,<br>ADC3_INP14|
|-|-|-|K3|H4|45|48|P3|PH4|I/O|FT_fa|-|I2C2_SCL, LCD_G5,<br>OTG_HS_ULPI_NXT,<br>LCD_G4, EVENTOUT|ADC3_INN14,<br>ADC3_INP15|
|-|-|-|L3|J4|46|49|P4|PH5|I/O|FT_fa|-|I2C2_SDA, SPI5_NSS,<br>FMC_SDNWE,<br>EVENTOUT|ADC3_INN15,<br>ADC3_INP16|


68/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**


















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|25|K2|37|N3|R2|47|50|U2|PA3|I/O|FT_<br>ha|-|TIM2_CH4, TIM5_CH4,<br>LPTIM5_OUT,<br>TIM15_CH2,<br>USART2_RX, LCD_B2,<br>OTG_HS_ULPI_D0,<br>ETH_MII_COL, LCD_B5,<br>EVENTOUT|ADC12_INP15|
|26|-|38|G2|K6|-|51|F2(4)|VSS|S|-|-|-|-|
|-|-|-|-|L4|48|-|-|VSS|S|-|-|-|-|
|27|-|39|-|K4|49|52|G5|VDD|S|-|-|-|-|
|28|G3|40|H6|N4|50|53|U3|PA4|I/O|TT_a|-|D1PWREN, TIM5_ETR,<br>SPI1_NSS/I2S1_WS,<br>SPI3_NSS/I2S3_WS,<br>USART2_CK, SPI6_NSS,<br>OTG_HS_SOF,<br>DCMI_HSYNC,<br>LCD_VSYNC,<br>EVENTOUT|ADC12_INP18,<br>DAC1_OUT1|
|29|H3|41|L4|P4|51|54|T3|PA5|I/O|TT_<br>ha|-|D2PWREN,<br>TIM2_CH1/TIM2_ETR,<br>TIM8_CH1N,<br>SPI1_SCK/I2S1_CK,<br>SPI6_SCK,<br>OTG_HS_ULPI_CK,<br>LCD_R4, EVENTOUT|ADC12_INN18,<br>ADC12_INP19,<br>DAC1_OUT2|
|30|J3|42|K5|P3|52|55|R3|PA6|I/O|FT_a|-|TIM1_BKIN, TIM3_CH1,<br>TIM8_BKIN,<br>SPI1_MISO/I2S1_SDI,<br>SPI6_MISO, TIM13_CH1,<br>TIM8_BKIN_COMP12,<br>MDIOS_MDC,<br>TIM1_BKIN_COMP12,<br>DCMI_PIXCLK, LCD_G2,<br>EVENTOUT|ADC12_INP3|
|31|K3|43|J6|R3|53|56|R5|PA7|I/O|TT_a|-|TIM1_CH1N, TIM3_CH2,<br>TIM8_CH1N,<br>SPI1_MOSI/I2S1_SDO,<br>SPI6_MOSI, TIM14_CH1,<br>ETH_MII_RX_DV/ETH_R<br>MII_CRS_DV,<br>FMC_SDNWE,<br>EVENTOUT|ADC12_INN3,<br>ADC12_INP7,<br>OPAMP1_VINM|



DS12110 Rev 10 69/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**



















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|32|G4|44|K6|N5|54|57|T4|PC4|I/O|TT_a|-|DFSDM1_CKIN2,<br>I2S1_MCK,<br>SPDIFRX1_IN3,<br>ETH_MII_RXD0/ETH_R<br>MII_RXD0, FMC_SDNE0,<br>EVENTOUT|ADC12_INP4,<br>OPAMP1_<br>VOUT,<br>COMP1_INM|
|33|H4|45|N5|P5|55|58|U4|PC5|I/O|TT_a|-|SAI1_D3,<br>DFSDM1_DATIN2,<br>SPDIFRX1_IN4,<br>SAI4_D3,<br>ETH_MII_RXD1/ETH_R<br>MII_RXD1,<br>FMC_SDCKE0,<br>COMP1_OUT,<br>EVENTOUT|ADC12_INN4,<br>ADC12_INP8,<br>OPAMP1_<br>VINM|
|-|-|-|N4|-|-|59|G13|VDD|S|-|-|-|-|
|-|-|-|H12|J9|-|60|R4|VSS|S|-|-|-|-|
|34|J4|46|M5|R5|56|61|U5|PB0|I/O|FT_a|-|TIM1_CH2N, TIM3_CH3,<br>TIM8_CH2N,<br>DFSDM1_CKOUT,<br>UART4_CTS, LCD_R3,<br>OTG_HS_ULPI_D1,<br>ETH_MII_RXD2,<br>LCD_G1, EVENTOUT|ADC12_INN5,<br>ADC12_INP9,<br>OPAMP1_VINP,<br>COMP1_INP|
|35|K4|47|L5|R4|57|62|T5|PB1|I/O|TT_a|-|TIM1_CH3N, TIM3_CH4,<br>TIM8_CH3N,<br>DFSDM1_DATIN1,<br>LCD_R6,<br>OTG_HS_ULPI_D2,<br>ETH_MII_RXD3,<br>LCD_G0, EVENTOUT|ADC12_INP5,<br>COMP1_INM|
|36|G5|48|L6|M6|58|63|R6|PB2|I/O|FT_<br>ha|-|RTC_OUT, SAI1_D1,<br>DFSDM1_CKIN1,<br>SAI1_SD_A,<br>SPI3_MOSI/I2S3_SDO,<br>SAI4_SD_A,<br>QUADSPI_CLK,<br>SAI4_D1, EVENTOUT|COMP1_INP|
|-|-|-|-|-|-|64|P5|PI15|I/O|FT|-|LCD_G2, LCD_R0,<br>EVENTOUT|-|
|-|-|-|J4|-|-|65|N6|PJ0|I/O|FT|-|LCD_R7, LCD_R1,<br>EVENTOUT|-|
|-|-|-|H5|-|-|66|P6|PJ1|I/O|FT|-|LCD_R2, EVENTOUT|-|
|-|-|-|-|-|-|67|T6|PJ2|I/O|FT|-|LCD_R3, EVENTOUT|-|


70/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**




















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|-|-|-|-|68|U6|PJ3|I/O|FT|-|LCD_R4, EVENTOUT|-|
|-|-|-|-|-|-|69|U7|PJ4|I/O|FT|-|LCD_R5, EVENTOUT|-|
|-|-|49|M6|R6|59|70|T7|PF11|I/O|FT_a|-|SPI5_MOSI, SAI2_SD_B,<br>FMC_SDNRAS,<br>DCMI_D12, EVENTOUT|ADC1_INP2|
|-|-|50|N6|P6|60|71|R7|PF12|I/O|FT_<br>ha|-|FMC_A6, EVENTOUT|ADC1_INN2,<br>ADC1_INP6|
|-|-|51|M11|M8|61|72|J3|VSS|S|-|-|-|-|
|-|-|52|-|N8|62|73|H5|VDD|S|-|-|-|-|
|-|-|53|G7|N6|63|74|P7|PF13|I/O|FT_<br>ha|-|DFSDM1_DATIN6,<br>I2C4_SMBA, FMC_A7,<br>EVENTOUT|ADC2_INP2|
|-|-|54|H7|R7|64|75|P8|PF14|I/O|FT_<br>fha|-|DFSDM1_CKIN6,<br>I2C4_SCL, FMC_A8,<br>EVENTOUT|ADC2_INN2,<br>ADC2_INP6|
|-|-|55|J7|P7|65|76|R9|PF15|I/O|FT_fh|-|I2C4_SDA, FMC_A9,<br>EVENTOUT|-|
|-|-|56|K7|N7|66|77|T8|PG0|I/O|FT_h|-|FMC_A10, EVENTOUT|-|
|-|-|-|M2|F6|-|-|J16|VSS|S|-|-|-|-|
|-|-|-|A10|-|-|-|H13|VDD|S|-|-|-|-|
|-|-|57|L7|M7|67|78|U8|PG1|I/O|TT_h|-|FMC_A11, EVENTOUT|OPAMP2_<br>VINM|
|37|H5|58|G8|R8|68|79|U9|PE7|I/O|TT_<br>ha|-|TIM1_ETR,<br>DFSDM1_DATIN2,<br>UART7_RX,<br>QUADSPI_BK2_IO0,<br>FMC_D4/FMC_DA4,<br>EVENTOUT|OPAMP2_<br>VOUT,<br>COMP2_INM|
|38|J5|59|H8|P8|69|80|T9|PE8|I/O|TT_<br>ha|-|TIM1_CH1N,<br>DFSDM1_CKIN2,<br>UART7_TX,<br>QUADSPI_BK2_IO1,<br>FMC_D5/FMC_DA5,<br>COMP2_OUT,<br>EVENTOUT|OPAMP2_<br>VINM|
|39|K5|60|J8|P9|70|81|P9|PE9|I/O|TT_<br>ha|-|TIM1_CH1,<br>DFSDM1_CKOUT,<br>UART7_RTS/UART7_DE<br>, QUADSPI_BK2_IO2,<br>FMC_D6/FMC_DA6,<br>EVENTOUT|OPAMP2_VINP,<br>COMP2_INP|



DS12110 Rev 10 71/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**

















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|61|C12|M9|71|82|J17|VSS|S|-|-|-|-|
|-|-|62|C13|N9|72|83|J13|VDD|S|-|-|-|-|
|40|G6|63|M8|R9|73|84|N9|PE10|I/O|FT_<br>ha|-|TIM1_CH2N,<br>DFSDM1_DATIN4,<br>UART7_CTS,<br>QUADSPI_BK2_IO3,<br>FMC_D7/FMC_DA7,<br>EVENTOUT|COMP2_INM|
|41|H6|64|N8|P10|74|85|P10|PE11|I/O|FT_<br>ha|-|TIM1_CH2,<br>DFSDM1_CKIN4,<br>SPI4_NSS, SAI2_SD_B,<br>FMC_D8/FMC_DA8,<br>LCD_G3, EVENTOUT|COMP2_INP|
|42|J6|65|L8|R10|75|86|R10|PE12|I/O|FT_h|-|TIM1_CH3N,<br>DFSDM1_DATIN5,<br>SPI4_SCK,<br>SAI2_SCK_B,<br>FMC_D9/FMC_DA9,<br>COMP1_OUT, LCD_B4,<br>EVENTOUT|-|
|43|K6|66|K8|N11|76|87|T10|PE13|I/O|FT_h|-|TIM1_CH3,<br>DFSDM1_CKIN5,<br>SPI4_MISO, SAI2_FS_B,<br>FMC_D10/FMC_DA10,<br>COMP2_OUT, LCD_DE,<br>EVENTOUT|-|
|-|-|-|L12|F7|-|-|T12|VSS|S|-|-|-|-|
|-|-|-|H13|-|-|-|K13|VDD|S|-|-|-|-|
|44|G7|67|J9|P11|77|88|U10|PE14|I/O|FT_h|-|TIM1_CH4, SPI4_MOSI,<br>SAI2_MCLK_B,<br>FMC_D11/FMC_DA11,<br>LCD_CLK, EVENTOUT|-|
|45|H7|68|N9|R11|78|89|R11|PE15|I/O|FT_h|-|TIM1_BKIN,<br>FMC_D12/FMC_DA12,<br>TIM1_BKIN_COMP12/<br>COMP_TIM1_BKIN,<br>LCD_R7, EVENTOUT|-|


72/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**



















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|46|J7|69|L9|R12|79|90|P11|PB10|I/O|FT_f|-|TIM2_CH3,<br>HRTIM_SCOUT,<br>LPTIM2_IN1, I2C2_SCL,<br>SPI2_SCK/I2S2_CK,<br>DFSDM1_DATIN7,<br>USART3_TX,<br>QUADSPI_BK1_NCS,<br>OTG_HS_ULPI_D3,<br>ETH_MII_RX_ER,<br>LCD_G4, EVENTOUT|-|
|47|K7|70|M9|R13|80|91|P12|PB11|I/O|FT_f|-|TIM2_CH4,<br>HRTIM_SCIN,<br>LPTIM2_ETR,<br>I2C2_SDA,<br>DFSDM1_CKIN7,<br>USART3_RX,<br>OTG_HS_ULPI_D4,<br>ETH_MII_TX_EN/ETH_R<br>MII_TX_EN, LCD_G5,<br>EVENTOUT|-|
|48|F8|71|N10|M10|81|92|U11|VCAP|S|-|-|-|-|
|49|E4|-|-|K7|-|93|-|VSS|S|-|-|-|-|
|-|-|-|M10|-|-|-|U12|VDDLDO<br>(8)|S|-|-|-|-|
|50|-|72|M1|N10|82|94|L13|VDD|S|-|-|-|-|
|-|-|-|-|-|-|95|R12|PJ5|I/O|FT|-|LCD_R6, EVENTOUT|-|
|-|-|-|-|M11|83|96|T11|PH6|I/O|FT|-|TIM12_CH1,<br>I2C2_SMBA, SPI5_SCK,<br>ETH_MII_RXD2,<br>FMC_SDNE1, DCMI_D8,<br>EVENTOUT|-|
|-|-|-|-|N12|84|97|U13|PH7|I/O|FT_fa|-|I2C3_SCL, SPI5_MISO,<br>ETH_MII_RXD3,<br>FMC_SDCKE1,<br>DCMI_D9, EVENTOUT|-|
|-|-|-|-|M12|85|98|T13|PH8|I/O|FT_fh<br>a|-|TIM5_ETR, I2C3_SDA,<br>FMC_D16,<br>DCMI_HSYNC, LCD_R2,<br>EVENTOUT|-|
|-|-|-|-|F8|-|-|-|VSS|S|-|-|-|-|
|-|-|-|L13|-|-|-|M13|VDD|S|-|-|-|-|


DS12110 Rev 10 73/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**













|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|-|-|M13|86|99|R13|PH9|I/O|FT_h|-|TIM12_CH2,<br>I2C3_SMBA, FMC_D17,<br>DCMI_D0, LCD_R3,<br>EVENTOUT|-|
|-|-|-|K9|L13|87|100|P13|PH10|I/O|FT_h|-|TIM5_CH1, I2C4_SMBA,<br>FMC_D18, DCMI_D1,<br>LCD_R4, EVENTOUT|-|
|-|-|-|L10|L12|88|101|P14|PH11|I/O|FT_fh|-|TIM5_CH2, I2C4_SCL,<br>FMC_D19, DCMI_D2,<br>LCD_R5, EVENTOUT|-|
|-|-|-|K10|K12|89|102|R14|PH12|I/O|FT_fh|-|TIM5_CH3, I2C4_SDA,<br>FMC_D20, DCMI_D3,<br>LCD_R6, EVENTOUT|-|
|-|-|-|-|H12|90|-|N16|VSS|S|-|-|-|-|
|-|-|-|N11|J12|91|103|P17|VDD|S|-|-|-|-|
|51|K8|73|N12|P12|92|104|T14|PB12(9)|I/O|FT_u|-|TIM1_BKIN, I2C2_SMBA,<br>SPI2_NSS/I2S2_WS,<br>DFSDM1_DATIN1,<br>USART3_CK,<br>FDCAN2_RX,<br>OTG_HS_ULPI_D5,<br>ETH_MII_TXD0/ETH_RM<br>II_TXD0, OTG_HS_ID,<br>TIM1_BKIN_COMP12,<br>UART5_RX, EVENTOUT|-|
|52|J8|74|L11|P13|93|105|U14|PB13(9)|I/O|FT_u|-|TIM1_CH1N,<br>LPTIM2_OUT,<br>SPI2_SCK/I2S2_CK,<br>DFSDM1_CKIN1,<br>USART3_CTS/USART3_<br>NSS, FDCAN2_TX,<br>OTG_HS_ULPI_D6,<br>ETH_MII_TXD1/ETH_RM<br>II_TXD1, UART5_TX,<br>EVENTOUT|OTG_HS_<br>VBUS|


74/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**











|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|53|H10|75|N13|R14|94|106|U15|PB14|I/O|FT_u|-|TIM1_CH2N,<br>TIM12_CH1,<br>TIM8_CH2N,<br>USART1_TX,<br>SPI2_MISO/I2S2_SDI,<br>DFSDM1_DATIN2,<br>USART3_RTS/<br>USART3_DE,<br>UART4_RTS/UART4_DE<br>, SDMMC2_D0,<br>OTG_HS_DM,<br>EVENTOUT|-|
|54|G10|76|M13|R15|95|107|T15|PB15|I/O|FT_u|-|RTC_REFIN,<br>TIM1_CH3N,<br>TIM12_CH2,<br>TIM8_CH3N,<br>USART1_RX,<br>SPI2_MOSI/I2S2_SDO,<br>DFSDM1_CKIN2,<br>UART4_CTS,<br>SDMMC2_D1,<br>OTG_HS_DP,<br>EVENTOUT|-|
|55|K9|77|M12|P15|96|108|U16|PD8|I/O|FT_h|-|DFSDM1_CKIN3,<br>SAI3_SCK_B,<br>USART3_TX,<br>SPDIFRX1_IN2,<br>FMC_D13/FMC_DA13,<br>EVENTOUT|-|
|56|J9|78|K11|P14|97|109|T17|PD9|I/O|FT_h|-|DFSDM1_DATIN3,<br>SAI3_SD_B,<br>USART3_RX,<br>FMC_D14/FMC_DA14,<br>EVENTOUT|-|
|57|H9|79|K12|N15|98|110|T16|PD10|I/O|FT_h|-|DFSDM1_CKOUT,<br>SAI3_FS_B,<br>USART3_CK,<br>FMC_D15/FMC_DA15,<br>LCD_B3, EVENTOUT|-|
|-|-|-|N7|-|-|-|N12|VDD|S|-|-|-|-|
|-|-|-|-|F9|-|-|U17|VSS|S|-|-|-|-|


DS12110 Rev 10 75/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**



















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|58|G9|80|J10|N14|99|111|R15|PD11|I/O|FT_h|-|LPTIM2_IN2,<br>I2C4_SMBA,<br>USART3_CTS/USART3_<br>NSS,<br>QUADSPI_BK1_IO0,<br>SAI2_SD_A, FMC_A16,<br>EVENTOUT|-|
|59|K10|81|K13|N13|100|112|R16|PD12|I/O|FT_fh|-|LPTIM1_IN1, TIM4_CH1,<br>LPTIM2_IN1, I2C4_SCL,<br>USART3_RTS/USART3_<br>DE, QUADSPI_BK1_IO1,<br>SAI2_FS_A, FMC_A17,<br>EVENTOUT|-|
|60|J10|82|J11|M15|101|113|R17|PD13|I/O|FT_fh|-|LPTIM1_OUT,<br>TIM4_CH2, I2C4_SDA,<br>QUADSPI_BK1_IO3,<br>SAI2_SCK_A, FMC_A18,<br>EVENTOUT|-|
|-|-|83|-|K8|102|114|-|VSS|S|-|-|-|-|
|-|-|84|-|J13|103|115|N11|VDD|S|-|-|-|-|
|61|H8|85|J13|M14|104|116|P16|PD14|I/O|FT_h|-|TIM4_CH3,<br>SAI3_MCLK_B,<br>UART8_CTS,<br>FMC_D0/FMC_DA0,<br>EVENTOUT|-|
|62|G8|86|J12|L14|105|117|P15|PD15|I/O|FT_h|-|TIM4_CH4,<br>SAI3_MCLK_A,<br>UART8_RTS/UART8_DE<br>, FMC_D1/FMC_DA1,<br>EVENTOUT|-|
|-|-|-|-|-|-|118|N15|PJ6|I/O|FT|-|TIM8_CH2, LCD_R7,<br>EVENTOUT|-|
|-|-|-|-|-|-|119|N14|PJ7|I/O|FT|-|TRGIN, TIM8_CH2N,<br>LCD_G0, EVENTOUT|-|
|-|-|-|-|-|-|-|N10|VDD|S|-|-|-|-|
|-|-|-|-|F10|-|-|R8|VSS|S|-|-|-|-|
|-|-|-|-|-|-|120|N13|PJ8|I/O|FT|-|TIM1_CH3N, TIM8_CH1,<br>UART8_TX, LCD_G1,<br>EVENTOUT|-|
|-|-|-|-|-|-|121|M14|PJ9|I/O|FT|-|TIM1_CH3, TIM8_CH1N,<br>UART8_RX, LCD_G2,<br>EVENTOUT|-|


76/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|-|-|-|-|122|L14|PJ10|I/O|FT|-|TIM1_CH2N, TIM8_CH2,<br>SPI5_MOSI, LCD_G3,<br>EVENTOUT|-|
|-|-|-|-|-|-|123|K14|PJ11|I/O|FT|-|TIM1_CH2, TIM8_CH2N,<br>SPI5_MISO, LCD_G4,<br>EVENTOUT|-|
|-|-|-|-|-|-|124|N8|VDD|S||-||-|
|-|-|-|-|G6|-|125|U1|VSS|S|-|-|-|-|
|-|-|-|-|-|-|-|N17<br>(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|M16<br>(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|M17<br>(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|K15|VSS|S|-|-|-|-|
|-|-|-|-|-|-|-|L16(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|L17(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|K16<br>(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|K17<br>(2)|NC|-|-|-|-|-|
|-|-|-|-|-|-|-|L15|VSS|S|-|-|-|-|
|-|-|-|-|-|-|126|J14|PK0|I/O|FT|-|TIM1_CH1N, TIM8_CH3,<br>SPI5_SCK, LCD_G5,<br>EVENTOUT|-|
|-|-|-|-|-|-|127|J15|PK1|I/O|FT|-|TIM1_CH1, TIM8_CH3N,<br>SPI5_NSS, LCD_G6,<br>EVENTOUT|-|
|-|-|-|-|-|-|128|H17|PK2|I/O|FT|-|TIM1_BKIN, TIM8_BKIN,<br>TIM8_BKIN_COMP12,<br>TIM1_BKIN_COMP12,<br>LCD_G7, EVENTOUT|-|
|-|-|87|H9|L15|106|129|H16|PG2|I/O|FT_h|-|TIM8_BKIN,<br>TIM8_BKIN_COMP12,<br>FMC_A12, EVENTOUT|-|
|-|-|88|H10|K15|107|130|H15|PG3|I/O|FT_h|-|TIM8_BKIN2,<br>TIM8_BKIN2_COMP12,<br>FMC_A13, EVENTOUT|-|
|-|-|-|-|G7|-|-|-|VSS|S|-|-|-|-|


DS12110 Rev 10 77/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**

























|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|-|-|-|-|-|N7|VDD|S|-|-|-|-|
|-|-|89|F8|K14|108|131|H14|PG4|I/O|FT_h|-|TIM1_BKIN2,<br>TIM1_BKIN2_COMP12,<br>FMC_A14/FMC_BA0,<br>EVENTOUT|-|
|-|-|90|H11|K13|109|132|G14|PG5|I/O|FT_h|-|TIM1_ETR,<br>FMC_A15/FMC_BA1,<br>EVENTOUT|-|
|-|-|91|G9|J15|110|133|G15|PG6|I/O|FT_h|-|TIM17_BKIN,<br>HRTIM_CHE1,<br>QUADSPI_BK1_NCS,<br>FMC_NE3, DCMI_D12,<br>LCD_R7, EVENTOUT|-|
|-|-|92|G10|J14|111|134|F16|PG7|I/O|FT_h|-|HRTIM_CHE2,<br>SAI1_MCLK_A,<br>USART6_CK, FMC_INT,<br>DCMI_D13, LCD_CLK,<br>EVENTOUT|-|
|-|-|93|G11|H14|112|135|F15|PG8|I/O|FT_h|-|TIM8_ETR, SPI6_NSS,<br>USART6_RTS/USART6_<br>DE, SPDIFRX1_IN3,<br>ETH_PPS_OUT,<br>FMC_SDCLK, LCD_G7,<br>EVENTOUT|-|
|-|-|94|-|G12|113|136|G16|VSS|S|-|-|-|-|
|-|-|-|G12|-|-|-|G17|VDD50<br>USB(10)|S|-|-|-|-|
|-|F6|95|G13|H13|114|137|F17|VDD33<br>USB|S|-|-|-|-|
|-|-|-|-|-|-|-|M5|VDD|S|-|-|-|-|
|63|F10|96|F9|H15|115|138|F14|PC6|I/O|FT_h|-|HRTIM_CHA1,<br>TIM3_CH1, TIM8_CH1,<br>DFSDM1_CKIN3,<br>I2S2_MCK, USART6_TX,<br>SDMMC1_D0DIR,<br>FMC_NWAIT,<br>SDMMC2_D6,<br>SDMMC1_D6, DCMI_D0,<br>LCD_HSYNC,<br>EVENTOUT|SWPMI_IO|


78/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**


















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|64|E10|97|F10|G15|116|139|F13|PC7|I/O|FT_h|-|TRGIO, HRTIM_CHA2,<br>TIM3_CH2, TIM8_CH2,<br>DFSDM1_DATIN3,<br>I2S3_MCK,<br>USART6_RX,<br>SDMMC1_D123DIR,<br>FMC_NE1,<br>SDMMC2_D7,<br>SWPMI_TX,<br>SDMMC1_D7, DCMI_D1,<br>LCD_G6, EVENTOUT|-|
|65|F9|98|F12|G14|117|140|E13|PC8|I/O|FT_h|-|TRACED1,<br>HRTIM_CHB1,<br>TIM3_CH3, TIM8_CH3,<br>USART6_CK,<br>UART5_RTS/UART5_DE<br>, FMC_NE2/FMC_NCE,<br>SWPMI_RX,<br>SDMMC1_D0, DCMI_D2,<br>EVENTOUT|-|
|66|E9|99|F11|F14|118|141|E14|PC9|I/O|FT_fh|-|MCO2, TIM3_CH4,<br>TIM8_CH4, I2C3_SDA,<br>I2S_CKIN, UART5_CTS,<br>QUADSPI_BK1_IO0,<br>LCD_G3,<br>SWPMI_SUSPEND,<br>SDMMC1_D1, DCMI_D3,<br>LCD_B2, EVENTOUT|-|
|-|-|-|-|G8|-|-|-|VSS|S|-|-|-|-|
|-|-|-|-|-|-|-|L5|VDD|S|-|-|-|-|
|67|D9|100|E12|F15|119|142|E15|PA8|I/O|FT_<br>fha|-|MCO1, TIM1_CH1,<br>HRTIM_CHB2,<br>TIM8_BKIN2, I2C3_SCL,<br>USART1_CK,<br>OTG_FS_SOF,<br>UART7_RX,<br>TIM8_BKIN2_COMP12,<br>LCD_B3, LCD_R6,<br>EVENTOUT|-|
|68|C9|101|E11|E15|120|143|D15|PA9|I/O|FT_u|-|TIM1_CH2,<br>HRTIM_CHC1,<br>LPUART1_TX,<br>I2C3_SMBA,<br>SPI2_SCK/I2S2_CK,<br>USART1_TX, DCMI_D0,<br>LCD_R5, EVENTOUT|OTG_FS_VBUS|



DS12110 Rev 10 79/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**













|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|69|D10|102|E10|D15|121|144|D14|PA10|I/O|FT_u|-|TIM1_CH3,<br>HRTIM_CHC2,<br>LPUART1_RX,<br>USART1_RX,<br>OTG_FS_ID,<br>MDIOS_MDIO, LCD_B4,<br>DCMI_D1, LCD_B1,<br>EVENTOUT|-|
|70|C10|103|F13|C15|122|145|E17|PA11|I/O|FT_u|-|TIM1_CH4,<br>HRTIM_CHD1,<br>LPUART1_CTS,<br>SPI2_NSS/I2S2_WS,<br>UART4_RX,<br>USART1_CTS/USART1_<br>NSS, FDCAN1_RX,<br>OTG_FS_DM, LCD_R4,<br>EVENTOUT|-|
|71|B10|104|E13|B15|123|146|E16|PA12|I/O|FT_u|-|TIM1_ETR,<br>HRTIM_CHD2,<br>LPUART1_RTS/<br>LPUART1_DE,<br>SPI2_SCK/I2S2_CK,<br>UART4_TX,<br>USART1_RTS/USART1_<br>DE, SAI2_FS_B,<br>FDCAN1_TX,<br>OTG_FS_DP, LCD_R5,<br>EVENTOUT|-|
|72|A10|105|D11|A15|124|147|C15|PA13<br>(JTMS/SW<br>DIO)|I/O|FT|-|JTMS-SWDIO,<br>EVENTOUT|-|
|73|E7|106|D13|F13|125|148|D17|VCAP|S|-|-|-|-|
|74|E5|107|-|F12|126|149|-|VSS|S|-|-|-|-|
|-|-|-|D12|-|-|-|C17|VDDLDO<br>(8)||-|-|-|-|
|75|-|108|-|G13|127|150|K5|VDD|S|-|-|-|-|
|-|-|-|-|E12|128|151|D16|PH13|I/O|FT_h|-|TIM8_CH1N, UART4_TX,<br>FDCAN1_TX, FMC_D21,<br>LCD_G2, EVENTOUT|-|
|-|-|-|-|E13|129|152|B17|PH14|I/O|FT_h|-|TIM8_CH2N,<br>UART4_RX,<br>FDCAN1_RX, FMC_D22,<br>DCMI_D4, LCD_G3,<br>EVENTOUT|-|


80/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**






























|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|-|-|D13|130|153|B16|PH15|I/O|FT_h|-|TIM8_CH3N, FMC_D23,<br>DCMI_D11, LCD_G4,<br>EVENTOUT|-|
|-|-|-|A13|E14|131|154|A16|PI0|I/O|FT_h|-|TIM5_CH4,<br>SPI2_NSS/I2S2_WS,<br>FMC_D24, DCMI_D13,<br>LCD_G5, EVENTOUT|-|
|-|-|-|-|G9|-|-|-|VSS|S|-|-|-|-|
|-|-|-|B13|D14|132|155|A15|PI1|I/O|FT_h|-|TIM8_BKIN2,<br>SPI2_SCK/I2S2_CK,<br>TIM8_BKIN2_COMP12,<br>FMC_D25, DCMI_D8,<br>LCD_G6, EVENTOUT|-|
|-|-|-|A6|C14|133|156|B15|PI2|I/O|FT_h|-|TIM8_CH4,<br>SPI2_MISO/I2S2_SDI,<br>FMC_D26, DCMI_D9,<br>LCD_G7, EVENTOUT|-|
|-|-|-|B7|C13|134|157|C14|PI3|I/O|FT_h|-|TIM8_ETR,<br>SPI2_MOSI/I2S2_SDO,<br>FMC_D27, DCMI_D10,<br>EVENTOUT|-|
|-|-|-|-|D9|135|-|-|VSS|S|-|-|-|-|
|-|-|-|-|C9|136|158|-|VDD|S|-|-|-|-|
|76|A9|109|B12|A14|137|159|B14|PA14<br>(JTCK/SW<br>CLK)|I/O|FT|-|JTCK-SWCLK,<br>EVENTOUT|-|
|77|A8|110|C11|A13|138|160|A14|PA15<br>(JTDI)|I/O|FT|-|JTDI,<br>TIM2_CH1/TIM2_ETR,<br>HRTIM_FLT1, CEC,<br>SPI1_NSS/I2S1_WS,<br>SPI3_NSS/I2S3_WS,<br>SPI6_NSS,<br>UART4_RTS/UART4_DE<br>, UART7_TX,<br>EVENTOUT|-|
|78|B9|111|A12|B14|139|161|A13|PC10|I/O|FT_<br>ha|-|HRTIM_EEV1,<br>DFSDM1_CKIN5,<br>SPI3_SCK/I2S3_CK,<br>USART3_TX,<br>UART4_TX,<br>QUADSPI_BK1_IO1,<br>SDMMC1_D2, DCMI_D8,<br>LCD_R2, EVENTOUT|-|



DS12110 Rev 10 81/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**



















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|79|B8|112|B11|B13|140|162|B13|PC11|I/O|FT_h|-|HRTIM_FLT2,<br>DFSDM1_DATIN5,<br>SPI3_MISO/I2S3_SDI,<br>USART3_RX,<br>UART4_RX,<br>QUADSPI_BK2_NCS,<br>SDMMC1_D3, DCMI_D4,<br>EVENTOUT|-|
|80|C8|113|A11|A12|141|163|C12|PC12|I/O|FT_h|-|TRACED3,<br>HRTIM_EEV2,<br>SPI3_MOSI/I2S3_SDO,<br>USART3_CK,<br>UART5_TX,<br>SDMMC1_CK, DCMI_D9,<br>EVENTOUT|-|
|-|-|-|-|G10|-|-|-|VSS|S|-|-|-|-|
|81|D8|114|D10|B12|142|164|D13|PD0|I/O|FT_h|-|DFSDM1_CKIN6,<br>SAI3_SCK_A,<br>UART4_RX,<br>FDCAN1_RX,<br>FMC_D2/FMC_DA2,<br>EVENTOUT|-|
|82|E8|115|C10|C12|143|165|E12|PD1|I/O|FT_h|-|DFSDM1_DATIN6,<br>SAI3_SD_A, UART4_TX,<br>FDCAN1_TX,<br>FMC_D3/FMC_DA3,<br>EVENTOUT|-|
|83|B7|116|E9|D12|144|166|D12|PD2|I/O|FT_h|-|TRACED2, TIM3_ETR,<br>UART5_RX,<br>SDMMC1_CMD,<br>DCMI_D11, EVENTOUT|-|
|84|C7|117|D9|D11|145|167|B12|PD3|I/O|FT_h|-|DFSDM1_CKOUT,<br>SPI2_SCK/I2S2_CK,<br>USART2_CTS/USART2_<br>NSS, FMC_CLK,<br>DCMI_D5, LCD_G7,<br>EVENTOUT|-|
|85|D7|118|C9|D10|146|168|A12|PD4|I/O|FT_h|-|HRTIM_FLT3,<br>SAI3_FS_A,<br>USART2_RTS/USART2_<br>DE, FMC_NOE,<br>EVENTOUT|-|
|86|B6|119|A9|C11|147|169|A11|PD5|I/O|FT_h|-|HRTIM_EEV3,<br>USART2_TX,<br>FMC_NWE, EVENTOUT|-|


82/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**






















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|120|-|D8|148|170|-|VSS|S|-|-|-|-|
|-|-|121|-|C8|149|171|-|VDD|S|-|-|-|-|
|87|C6|122|B9|B11|150|172|B11|PD6|I/O|FT_h|-|SAI1_D1,<br>DFSDM1_CKIN4,<br>DFSDM1_DATIN1,<br>SPI3_MOSI/I2S3_SDO,<br>SAI1_SD_A,<br>USART2_RX,<br>SAI4_SD_A, SAI4_D1,<br>SDMMC2_CK,<br>FMC_NWAIT,<br>DCMI_D10, LCD_B2,<br>EVENTOUT|-|
|88|D6|123|D8|A11|151|173|C11|PD7|I/O|FT_h|-|DFSDM1_DATIN4,<br>SPI1_MOSI/I2S1_SDO,<br>DFSDM1_CKIN1,<br>USART2_CK,<br>SPDIFRX1_IN1,<br>SDMMC2_CMD,<br>FMC_NE1, EVENTOUT|-|
|-|-|-|-|-|-|174|D11|PJ12|I/O|FT|-|TRGOUT, LCD_G3,<br>LCD_B0, EVENTOUT|-|
|-|-|-|-|-|-|175|E10|PJ13|I/O|FT|-|LCD_B4, LCD_B1,<br>EVENTOUT|-|
|-|-|-|-|-|-|176|D10|PJ14|I/O|FT|-|LCD_B2, EVENTOUT|-|
|-|-|-|-|-|-|177|B10|PJ15|I/O|FT|-|LCD_B3, EVENTOUT|-|
|-|-|-|-|H6|-|-|-|VSS|S|-|-|-|-|
|-|-|-|A7|-|-|-|-|VDD|S|-|-|-|-|
|-|-|124|C8|C10|152|178|A10|PG9|I/O|FT_h|-|SPI1_MISO/I2S1_SDI,<br>USART6_RX,<br>SPDIFRX1_IN4,<br>QUADSPI_BK2_IO2,<br>SAI2_FS_B,<br>FMC_NE2/FMC_NCE,<br>DCMI_VSYNC,<br>EVENTOUT|-|
|-|-|125|A8|B10|153|179|A9|PG10|I/O|FT_h|-|HRTIM_FLT5,<br>SPI1_NSS/I2S1_WS,<br>LCD_G3, SAI2_SD_B,<br>FMC_NE3, DCMI_D2,<br>LCD_B2, EVENTOUT|-|



DS12110 Rev 10 83/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**











|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|126|B8|B9|154|180|B9|PG11|I/O|FT_h|-|LPTIM1_IN2,<br>HRTIM_EEV4,<br>SPI1_SCK/I2S1_CK,<br>SPDIFRX1_IN1,<br>SDMMC2_D2,<br>ETH_MII_TX_EN/ETH_R<br>MII_TX_EN, DCMI_D3,<br>LCD_B3, EVENTOUT|-|
|-|-|127|E8|B8|155|181|C9|PG12|I/O|FT_h|-|LPTIM1_IN1,<br>HRTIM_EEV5,<br>SPI6_MISO,<br>USART6_RTS/USART6_<br>DE, SPDIFRX1_IN2,<br>LCD_B4,<br>ETH_MII_TXD1/ETH_RM<br>II_TXD1, FMC_NE4,<br>LCD_B1, EVENTOUT|-|
|-|-|128|D7|A8|156|182|D9|PG13|I/O|FT_h|-|TRACED0,<br>LPTIM1_OUT,<br>HRTIM_EEV10,<br>SPI6_SCK,<br>USART6_CTS/USART6_<br>NSS,<br>ETH_MII_TXD0/ETH_RM<br>II_TXD0, FMC_A24,<br>LCD_R0, EVENTOUT|-|
|-|-|129|C7|A7|157|183|D8|PG14|I/O|FT_h|-|TRACED1,<br>LPTIM1_ETR,<br>SPI6_MOSI,<br>USART6_TX,<br>QUADSPI_BK2_IO3,<br>ETH_MII_TXD1/ETH_RM<br>II_TXD1, FMC_A25,<br>LCD_B0, EVENTOUT|-|
|-|-|130|-|D7|158|184|-|VSS|S|-|-|-|-|
|-|-|131|-|C7|159|185|-|VDD|S|-|-|-|-|
|-|-|-|-|-|-|186|C8|PK3|I/O|FT|-|LCD_B4, EVENTOUT|-|
|-|-|-|-|-|-|187|B8|PK4|I/O|FT|-|LCD_B5, EVENTOUT|-|
|-|-|-|-|-|-|188|A8|PK5|I/O|FT|-|LCD_B6, EVENTOUT|-|
|-|-|-|-|-|-|189|C7|PK6|I/O|FT|-|LCD_B7, EVENTOUT|-|
|-|-|-|-|-|-|190|D7|PK7|I/O|FT|-|LCD_DE, EVENTOUT|-|
|-|-|-|-|H7|-|-|-|VSS|S|-|-|-|-|


84/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**






















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|-|132|E7|B7|160|191|D6|PG15|I/O|FT_h|-|USART6_CTS/USART6_<br>NSS, FMC_SDNCAS,<br>DCMI_D13, EVENTOUT|-|
|89|A7|133|F7|A10|161|192|C6|PB3(JTDO<br>/TRACES<br>WO)|I/O|FT|-|JTDO/TRACESWO,<br>TIM2_CH2,<br>HRTIM_FLT4,<br>SPI1_SCK/I2S1_CK,<br>SPI3_SCK/I2S3_CK,<br>SPI6_SCK,<br>SDMMC2_D2,<br>CRS_SYNC, UART7_RX,<br>EVENTOUT|-|
|90|A6|134|B6|A9|162|193|B7|PB4(NJTR<br>ST)|I/O|FT|-|NJTRST, TIM16_BKIN,<br>TIM3_CH1,<br>HRTIM_EEV6,<br>SPI1_MISO/I2S1_SDI,<br>SPI3_MISO/I2S3_SDI,<br>SPI2_NSS/I2S2_WS,<br>SPI6_MISO,<br>SDMMC2_D3,<br>UART7_TX, EVENTOUT|-|
|91|C5|135|C6|A6|163|194|A5|PB5|I/O|FT|-|TIM17_BKIN, TIM3_CH2,<br>HRTIM_EEV7,<br>I2C1_SMBA,<br>SPI1_MOSI/I2S1_SDO,<br>I2C4_SMBA,<br>SPI3_MOSI/I2S3_SDO,<br>SPI6_MOSI,<br>FDCAN2_RX,<br>OTG_HS_ULPI_D7,<br>ETH_PPS_OUT,<br>FMC_SDCKE1,<br>DCMI_D10, UART5_RX,<br>EVENTOUT|-|
|-|-|-|-|H8|-|-|-|VSS|S|-|-|-|-|
|92|B5|136|A5|B6|164|195|B5|PB6|I/O|FT_f|-|TIM16_CH1N,<br>TIM4_CH1,<br>HRTIM_EEV8,<br>I2C1_SCL, CEC,<br>I2C4_SCL, USART1_TX,<br>LPUART1_TX,<br>FDCAN2_TX,<br>QUADSPI_BK1_NCS,<br>DFSDM1_DATIN5,<br>FMC_SDNE1, DCMI_D5,<br>UART5_TX, EVENTOUT|-|



DS12110 Rev 10 85/357



101


**Pin descriptions** **STM32H742xI/G STM32H743xI/G**


**Table 9. Pin/ball definition (continued)**



















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|93|A5|137|D6|B5|165|196|C5|PB7|I/O|FT_fa|-|TIM17_CH1N,<br>TIM4_CH2,<br>HRTIM_EEV9,<br>I2C1_SDA, I2C4_SDA,<br>USART1_RX,<br>LPUART1_RX,<br>DFSDM1_CKIN5,<br>FMC_NL, DCMI_VSYNC,<br>EVENTOUT|PVD_IN|
|94|D5|138|E6|D6|166|197|E8|BOOT0|I|B|-|-|VPP|
|95|B4|139|B5|A5|167|198|D5|PB8|I/O|FT_fh|-|TIM16_CH1, TIM4_CH3,<br>DFSDM1_CKIN7,<br>I2C1_SCL, I2C4_SCL,<br>SDMMC1_CKIN,<br>UART4_RX,<br>FDCAN1_RX,<br>SDMMC2_D4,<br>ETH_MII_TXD3,<br>SDMMC1_D4, DCMI_D6,<br>LCD_B6, EVENTOUT|-|
|96|A4|140|C5|B4|168|199|D4|PB9|I/O|FT_fh|-|TIM17_CH1, TIM4_CH4,<br>DFSDM1_DATIN7,<br>I2C1_SDA,<br>SPI2_NSS/I2S2_WS,<br>I2C4_SDA,<br>SDMMC1_CDIR,<br>UART4_TX,<br>FDCAN1_TX,<br>SDMMC2_D5,<br>I2C4_SMBA,<br>SDMMC1_D5, DCMI_D7,<br>LCD_B7, EVENTOUT|-|
|97|D4|141|D5|A4|169|200|C4|PE0|I/O|FT_h|-|LPTIM1_ETR,<br>TIM4_ETR,<br>HRTIM_SCIN,<br>LPTIM2_ETR,<br>UART8_RX,<br>SAI2_MCLK_A,<br>FMC_NBL0, DCMI_D2,<br>EVENTOUT|-|
|98|C4|142|D4|A3|170|201|B4|PE1|I/O|FT_h|-|LPTIM1_IN2,<br>HRTIM_SCOUT,<br>UART8_TX, FMC_NBL1,<br>DCMI_D3, EVENTOUT|-|
|-|-|-|-|-|-|-|A7|VCAP|S|-|-|-|-|
|99|-|-|-|D5|-|202|-|VSS|S|-|-|-|-|


86/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Pin descriptions**


**Table 9. Pin/ball definition (continued)**















|Pin/ball name|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Pin name<br>(function<br>after<br>reset)|Pin type|I/O structure|Notes|Alternate functions|Additional<br>functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**LQFP100**|**TFBGA100**|**LQFP144**|**UFBGA169**|**UFBGA176+25**|**LQFP176**|**LQFP208**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|**TFBGA240 +25**|
|-|F7|143|C4|C6|171|203|E7|PDR_ON|I|FT|-|-|-|
|-|F4|-|B4|-|-|-|A6|VDDLDO<br>(8)|S|-|-|-|-|
|100|-|144|-|C5|172|204|-|VDD|S|-|-|-|-|
|-|-|-|-|D4|173|205|A4|PI4|I/O|FT_h|-|TIM8_BKIN,<br>SAI2_MCLK_A,<br>TIM8_BKIN_COMP12,<br>FMC_NBL2, DCMI_D5,<br>LCD_B4, EVENTOUT|-|
|-|-|-|-|C4|174|206|A3|PI5|I/O|FT_h|-|TIM8_CH1,<br>SAI2_SCK_A,<br>FMC_NBL3,<br>DCMI_VSYNC, LCD_B5,<br>EVENTOUT|-|
|-|-|-|A4|C3|175|207|A2|PI6|I/O|FT_h|-|TIM8_CH2, SAI2_SD_A,<br>FMC_D28, DCMI_D6,<br>LCD_B6, EVENTOUT|-|
|-|-|-|E2|C2|176|208|B3|PI7|I/O|FT_h|-|TIM8_CH3, SAI2_FS_A,<br>FMC_D29, DCMI_D7,<br>LCD_B7, EVENTOUT|-|
|-|-|-|-|H9|-|-|-|VSS|S|-|-|-|-|
|-|-|-|-|K9|-|-|-|VSS|S|-|-|-|-|
|-|-|-|-|K10|-|-|M15|VSS|S|-|-|-|-|


1. When this pin/ball was previously configured as an oscillator, the oscillator function is kept during and after a reset. This is
valid for all resets except for power-on reset.


2. This ball should remain floating.


3. This ball should not remain floating. It can be connected to VSS or VDD. It is reserved for future use.


4. This ball should be connected to V SS .


5. Pxy_C and Pxy pins/balls are two separate pads (analog switch open). The analog switch is configured through a SYSCFG
register. Refer to the product reference manual for a detailed description of the switch configuration bits.


6. There is a direct path between Pxy_C and Pxy pins/balls, through an analog switch. Pxy alternate functions are available on
Pxy_C when the analog switch is closed. The analog switch is configured through a SYSCFG register. Refer to the product
reference manual for a detailed description of the switch configuration bits.


7. VREF+ pin, and consequently the internal voltage reference, are not available on the TFBGA100 package. On this package,
this pin is double-bonded to VDDA which can be connected to an external reference. The internal voltage reference buffer is
not available and must be kept disabled


8. When it is not available on a package, the VDDLDO pin is internally tied to VDD.


9. When the pin is used in USB configuration (OTG_HS_ID/OTG_HS_VBUS), the I/O is supplied by V DD33USB, otherwise it is
supplied by V DD .


10. When it is not available on a package, the VDD50USB pin is internally tied to VDD33USB.


DS12110 Rev 10 87/357



101


**Table 10. Port A alternate functions**
































































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4/<br>5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1/<br>3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port A|PA0|-|TIM2_CH1/<br>TIM2_ETR|TIM5_CH1|TIM8_ETR|TIM15_BKIN|-|-|USART2_<br>CTS/<br>USART2_<br>NSS|UART4_TX|SDMMC2_<br>CMD|SAI2_SD_B|ETH_MII_<br>CRS|-|-|-|EVENT-<br>OUT|
|Port A|PA1|-|TIM2_CH2|TIM5_CH2|LPTIM3_<br>OUT|TIM15_<br>CH1N|-|-|USART2_<br>RTS/<br>USART2_<br>DE|UART4_RX|QUADSPI_<br>BK1_IO3|SAI2_MCLK<br>_B|ETH_MII_<br>RX_CLK/<br>ETH_RMII_<br>REF_CLK|-|-|LCD_R2|EVENT-<br>OUT|
|Port A|PA2|-|TIM2_CH3|TIM5_CH3|LPTIM4_<br>OUT|TIM15_CH1|-|-|USART2_<br>TX|SAI2_SCK_<br>B|-|-|ETH_MDIO|MDIOS_<br>MDIO|-|LCD_R1|EVENT-<br>OUT|
|Port A|PA3|-|TIM2_CH4|TIM5_CH4|LPTIM5_<br>OUT|TIM15_CH2|-|-|USART2_<br>RX|-|LCD_B2|OTG_HS_<br>ULPI_D0|ETH_MII_<br>COL|-|-|LCD_B5|EVENT-<br>OUT|
|Port A|PA4|D1<br>PWREN|-|TIM5_ETR|-|-|SPI1_NSS/<br>I2S1_WS|SPI3_NSS/<br>I2S3_WS|USART2_<br>CK|SPI6_NSS|-|-|-|OTG_HS_<br>SOF|DCMI_<br>HSYNC|LCD_<br>VSYNC|EVENT-<br>OUT|
|Port A|PA5|D2<br>PWREN|TIM2_CH1/<br>TIM2_ETR|-|TIM8_<br>CH1N|-|SPI1_SCK<br>/I2S1_CK|-|-|SPI6_SCK|-|OTG_HS_<br>ULPI_CK|-|-|-|LCD_R4|EVENT-<br>OUT|
|Port A|PA6|-|TIM1_BKIN|TIM3_CH1|TIM8_BKIN|-|SPI1_MISO<br>/I2S1_SDI|-|-|SPI6_MISO|TIM13_<br>CH1|TIM8_BKIN<br>_COMP12|MDIOS_<br>MDC|TIM1_BKIN<br>_COMP12|DCMI_PIX<br>CLK|LCD_G2|EVENT-<br>OUT|
|Port A|PA7|-|TIM1_CH1N|TIM3_CH2|TIM8_CH1<br>N|-|SPI1_MOSI<br>/I2S1_SDO|-|-|SPI6_MOSI|TIM14_<br>CH1|-|ETH_MII_<br>RX_DV/<br>ETH_RMII_<br>CRS_DV|FMC_SDN<br>WE|-|-|EVENT-<br>OUT|
|Port A|PA8|MCO1|TIM1_CH1|HRTIM_CH<br>B2|TIM8_BKIN<br>2|I2C3_SCL|-|-|USART1_<br>CK|-|-|OTG_FS_<br>SOF|UART7_RX|TIM8_BKIN<br>2_COMP12|LCD_B3|LCD_R6|EVENT-<br>OUT|
|Port A|PA9|-|TIM1_CH2|HRTIM_CH<br>C1|LPUART1_<br>TX|I2C3_SMBA|SPI2_SCK/<br>I2S2_CK|-|USART1_<br>TX|-|-|-|-|-|DCMI_D0|LCD_R5|EVENT-<br>OUT|
|Port A|PA10|-|TIM1_CH3|HRTIM_CH<br>C2|LPUART1_<br>RX|-|-|-|USART1_<br>RX|-|-|OTG_FS_ID|MDIOS_<br>MDIO|LCD_B4|DCMI_D1|LCD_B1|EVENT-<br>OUT|
|Port A|PA11|-|TIM1_CH4|HRTIM_CH<br>D1|LPUART1_<br>CTS|-|SPI2_NSS<br>/I2S2_WS|UART4_RX|USART1_<br>CTS/<br>USART1_<br>NSS|-|FDCAN1_<br>RX|OTG_FS_<br>DM|-|-|-|LCD_R4|EVENT-<br>OUT|
|Port A|PA12|-|TIM1_ETR|HRTIM_CH<br>D2|LPUART1_<br>RTS/<br>LPUART1_<br>DE|-|SPI2_SCK/<br>I2S2_CK|UART4_TX|USART1_<br>RTS/<br>USART1_<br>DE|SAI2_FS_B|FDCAN1_<br>TX|OTG_FS_<br>DP|-|-|-|LCD_R5|EVENT-<br>OUT|


**Table 10. Port A alternate functions (continued)**








































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4/<br>5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1/<br>3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port A|PA13|JTMS-<br>SWDIO|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|
|Port A|PA14|JTCK-<br>SWCLK|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|
|Port A|PA15|JTDI|TIM2_CH1/<br>TIM2_ETR|HRTIM_<br>FLT1|-|CEC|SPI1_NSS/<br>I2S1_WS|SPI3_NSS/<br>I2S3_WS|SPI6_NSS|UART4_<br>RTS/<br>UART4_<br>DE|-|-|UART7_TX|-|-|-|EVENT-<br>OUT|



**Table 11. Port B alternate functions**








































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/5/<br>6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/3<br>/6/UART7/S<br>DMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/<br>DCMI/LCD<br>/COMP|UART5/<br>LCD|SYS|
|Port B|PB0|-|TIM1_CH2N|TIM3_CH3|TIM8_<br>CH2N|-|-|DFSDM1_<br>CKOUT|-|UART4_<br>CTS|LCD_R3|OTG_HS_<br>ULPI_D1|ETH_MII_<br>RXD2|-|-|LCD_G1|EVENT-<br>OUT|
|Port B|PB1|-|TIM1_CH3N|TIM3_CH4|TIM8_<br>CH3N|-|-|DFSDM1_<br>DATIN1|-|-|LCD_R6|OTG_HS_<br>ULPI_D2|ETH_MII_<br>RXD3|-|-|LCD_G0|EVENT-<br>OUT|
|Port B|PB2|RTC_OUT|-|SAI1_D1|-|DFSDM1_<br>CKIN1|-|SAI1_SD_A|SPI3_<br>MOSI/I2S3_<br>SDO|SAI4_SD_<br>A|QUADSPI_<br>CLK|SAI4_D1|-|-|-|-|EVENT-<br>OUT|
|Port B|PB3|JTDO/TRA<br>CESWO|TIM2_CH2|HRTIM_<br>FLT4|-|-|SPI1_SCK/<br>I2S1_CK|SPI3_SCK/<br>I2S3_CK|-|SPI6_SCK|SDMMC2_<br>D2|CRS_SYNC|UART7_RX|-|-|-|EVENT-<br>OUT|
|Port B|PB4|NJTRST|TIM16_<br>BKIN|TIM3_CH1|HRTIM_<br>EEV6|-|SPI1_MISO/<br>I2S1_SDI|SPI3_MISO/<br>I2S3_SDI|SPI2_NSS/I<br>2S2_WS|SPI6_<br>MISO|SDMMC2_<br>D3|-|UART7_TX|-|-|-|EVENT-<br>OUT|
|Port B|PB5|-|TIM17_<br>BKIN|TIM3_CH2|HRTIM_<br>EEV7|I2C1_SMBA|SPI1_MOSI/<br>I2S1_SDO|I2C4_SMBA|SPI3_MOSI/<br>I2S3_SDO|SPI6_<br>MOSI|FDCAN2_<br>RX|OTG_HS_<br>ULPI_D7|ETH_PPS_<br>OUT|FMC_<br>SDCKE1|DCMI_<br>D10|UART5_<br>RX|EVENT-<br>OUT|
|Port B|PB6|-|TIM16_<br>CH1N|TIM4_CH1|HRTIM_<br>EEV8|I2C1_SCL|CEC|I2C4_SCL|USART1_<br>TX|LPUART1_<br>TX|FDCAN2_<br>TX|QUADSPI_<br>BK1_NCS|DFSDM1_<br>DATIN5|FMC_<br>SDNE1|DCMI_D5|UART5_<br>TX|EVENT-<br>OUT|
|Port B|PB7|-|TIM17_<br>CH1N|TIM4_CH2|HRTIM_<br>EEV9|I2C1_SDA|-|I2C4_SDA|USART1_<br>RX|LPUART1_<br>RX|-|-|DFSDM1_<br>CKIN5|FMC_NL|DCMI_<br>VSYNC|-|EVENT-<br>OUT|


**Table 11. Port B alternate functions (continued)**




























































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/5/<br>6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/3<br>/6/UART7/S<br>DMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/<br>DCMI/LCD<br>/COMP|UART5/<br>LCD|SYS|
|Port B|PB8|-|TIM16_CH1|TIM4_CH3|DFSDM1_<br>CKIN7|I2C1_SCL|-|I2C4_SCL|SDMMC1_<br>CKIN|UART4_RX|FDCAN1_<br>RX|SDMMC2_<br>D4|ETH_MII_<br>TXD3|SDMMC1_<br>D4|DCMI_D6|LCD_B6|EVENT-<br>OUT|
|Port B|PB9|-|TIM17_CH1|TIM4_CH4|DFSDM1_<br>DATIN7|I2C1_SDA|SPI2_NSS/<br>I2S2_WS|I2C4_SDA|SDMMC1_<br>CDIR|UART4_TX|FDCAN1_<br>TX|SDMMC2_<br>D5|I2C4_<br>SMBA|SDMMC1_<br>D5|DCMI_D7|LCD_B7|EVENT-<br>OUT|
|Port B|PB10|-|TIM2_CH3|HRTIM_<br>SCOUT|LPTIM2_IN<br>1|I2C2_SCL|SPI2_SCK/<br>I2S2_CK|DFSDM1_<br>DATIN7|USART3_<br>TX|-|QUADSPI_<br>BK1_NCS|OTG_HS_<br>ULPI_D3|ETH_MII_<br>RX_ER|-|-|LCD_G4|EVENT-<br>OUT|
|Port B|PB11|-|TIM2_CH4|HRTIM_<br>SCIN|LPTIM2_<br>ETR|I2C2_SDA|-|DFSDM1_<br>CKIN7|USART3_<br>RX|-|-|OTG_HS_<br>ULPI_D4|ETH_MII_<br>TX_EN/<br>ETH_RMII_<br>TX_EN|-|-|LCD_G5|EVENT-<br>OUT|
|Port B|PB12|-|TIM1_BKIN|-|-|I2C2_SMBA|SPI2_NSS/<br>I2S2_WS|DFSDM1_<br>DATIN1|USART3_<br>CK|-|FDCAN2_<br>RX|OTG_HS_<br>ULPI_D5|ETH_MII_<br>TXD0/ETH_<br>RMII_TXD0|OTG_HS_<br>ID|TIM1_<br>BKIN_<br>COMP12|UART5_<br>RX|EVENT-<br>OUT|
|Port B|PB13|-|TIM1_CH1N|-|LPTIM2_<br>OUT|-|SPI2_SCK/<br>I2S2_CK|DFSDM1_<br>CKIN1|USART3_<br>CTS/<br>USART3_<br>NSS|-|FDCAN2_<br>TX|OTG_HS_<br>ULPI_D6|ETH_MII_<br>TXD1/ETH_<br>RMII_TXD1|-|-|UART5_<br>TX|EVENT-<br>OUT|
|Port B|PB14|-|TIM1_CH2N|TIM12_<br>CH1|TIM8_<br>CH2N|USART1_TX|SPI2_MISO/<br>I2S2_SDI|DFSDM1_<br>DATIN2|USART3_<br>RTS/<br>USART3_<br>DE|UART4_<br>RTS/<br>UART4_<br>DE|SDMMC2_<br>D0|-|-|OTG_HS_<br>DM|-|-|EVENT-<br>OUT|
|Port B|PB15|RTC_<br>REFIN|TIM1_CH3N|TIM12_<br>CH2|TIM8_<br>CH3N|USART1_RX|SPI2_MOSI/<br>I2S2_SDO|DFSDM1_<br>CKIN2|-|UART4_<br>CTS|SDMMC2_<br>D1|-|-|OTG_HS_<br>DP|-|-|EVENT-<br>OUT|


**Table 12. Port C alternate functions**


















































































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port C|PC0|-|-|-|DFSDM1_<br>CKIN0|-|-|DFSDM1_<br>DATIN4|-|SAI2_FS_B|-|OTG_HS_<br>ULPI_STP|-|FMC_<br>SDNWE|-|LCD_R5|EVENT-<br>OUT|
|Port C|PC1|TRACED0|-|SAI1_D1|DFSDM1_<br>DATIN0|DFSDM1_<br>CKIN4|SPI2_<br>MOSI/I2S2<br>_SDO|SAI1_SD_A|-|SAI4_SD_<br>A|SDMMC2_<br>CK|SAI4_D1|ETH_MDC|MDIOS_<br>MDC|-|-|EVENT-<br>OUT|
|Port C|PC2|CDSLEEP|-|-|DFSDM1_<br>CKIN1|-|SPI2_<br>MISO/I2S2<br>_SDI|DFSDM1_<br>CKOUT|-|-|-|OTG_HS_<br>ULPI_DIR|ETH_MII_<br>TXD2|FMC_SDNE<br>0|-|-|EVENT-<br>OUT|
|Port C|PC3|CSLEEP|-|-|DFSDM1_<br>DATIN1|-|SPI2_<br>MOSI/I2S2<br>_SDO|-|-|-|-|OTG_HS_<br>ULPI_NXT|ETH_MII_<br>TX_CLK|FMC_SDCK<br>E0|-|-|EVENT-<br>OUT|
|Port C|PC4|-|-|-|DFSDM1_<br>CKIN2|-|I2S1_<br>MCK|-|-|-|SPDIFRX1<br>_IN3|-|ETH_MII_<br>RXD0/ETH_<br>RMII_RXD0|FMC_SDNE<br>0|-|-|EVENT-<br>OUT|
|Port C|PC5|-|-|SAI1_D3|DFSDM1_<br>DATIN2|-|-|-|-||SPDIFRX1<br>_IN4|SAI4_D3|ETH_MII_<br>RXD1/ETH_<br>RMII_RXD1|FMC_SDCK<br>E0|COMP1_<br>OUT|-|EVENT-<br>OUT|
|Port C|PC6|-|HRTIM_CH<br>A1|TIM3_CH1|TIM8_CH1|DFSDM1_<br>CKIN3|I2S2_<br>MCK|-|USART6_<br>TX|SDMMC1_<br>D0DIR|FMC_<br>NWAIT|SDMMC2_<br>D6|-|SDMMC1_<br>D6|DCMI_D0|LCD_<br>HSYNC|EVENT-<br>OUT|
|Port C|PC7|TRGIO|HRTIM_CH<br>A2|TIM3_CH2|TIM8_CH2|DFSDM1_<br>DATIN3|-|I2S3_MCK|USART6_<br>RX|SDMMC1_<br>D123DIR|FMC_NE1|SDMMC2_<br>D7|SWPMI_TX|SDMMC1_<br>D7|DCMI_D1|LCD_G6|EVENT-<br>OUT|
|Port C|PC8|TRACED1|HRTIM_CH<br>B1|TIM3_CH3|TIM8_CH3|-|-|-|USART6_<br>CK|UART5_<br>RTS/<br>UART5_<br>DE|FMC_NE2/<br>FMC_NCE|-|SWPMI_RX|SDMMC1_<br>D0|DCMI_D2|-|EVENT-<br>OUT|
|Port C|PC9|MCO2|-|TIM3_CH4|TIM8_CH4|I2C3_SDA|I2S_CKIN|-|-|UART5_<br>CTS|QUADSPI_<br>BK1_IO0|LCD_G3|SWPMI_<br>SUSPEND|SDMMC1_<br>D1|DCMI_D3|LCD_B2|EVENT-<br>OUT|
|Port C|PC10|-|-|HRTIM_<br>EEV1|DFSDM1_<br>CKIN5|-|-|SPI3_SCK/<br>I2S3_CK|USART3_<br>TX|UART4_TX|QUADSPI_<br>BK1_IO1|-|-|SDMMC1_<br>D2|DCMI_D8|LCD_R2|EVENT-<br>OUT|
|Port C|PC11|-|-|HRTIM_<br>FLT2|DFSDM1_<br>DATIN5|-|-|SPI3_MISO/<br>I2S3_SDI|USART3_<br>RX|UART4_RX|QUADSPI_<br>BK2_NCS|-|-|SDMMC1_<br>D3|DCMI_D4|-|EVENT-<br>OUT|
|Port C|PC12|TRACED3|-|HRTIM_<br>EEV2|-|-|-|SPI3_MOSI/<br>I2S3_SDO|USART3_<br>CK|UART5_TX|-|-|-|SDMMC1_<br>CK|DCMI_D9|-|EVENT-<br>OUT|
|Port C|PC13|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|


**Table 12. Port C alternate functions (continued)**

































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port C|PC14|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|
|Port C|PC15|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|


**Table 13. Port D alternate functions**
























































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port D|PD0|-|-|-|DFSDM1_<br>CKIN6|-|-|SAI3_SCK_<br>A|-|UART4_RX|FDCAN1_<br>RX|-|-|FMC_D2/<br>FMC_DA2|-|-|EVENT-<br>OUT|
|Port D|PD1|-|-|-|DFSDM1_<br>DATIN6|-|-|SAI3_SD_A|-|UART4_TX|FDCAN1_<br>TX|-|-|FMC_D3/<br>FMC_DA3|-|-|EVENT-<br>OUT|
|Port D|PD2|TRACED2|-|TIM3_ETR|-|-|-|-|-|UART5_RX|-|-|-|SDMMC1_<br>CMD|DCMI_D11|-|EVENT-<br>OUT|
|Port D|PD3|-|-|-|DFSDM1_<br>CKOUT|-|SPI2_SCK/<br>I2S2_CK|-|USART2_<br>CTS/<br>USART2_<br>NSS|-|-|-|-|FMC_CLK|DCMI_D5|LCD_G7|EVENT-<br>OUT|
|Port D|PD4|-|-|HRTIM_<br>FLT3|-|-|-|SAI3_FS_A|USART2_<br>RTS/<br>USART2_<br>DE|-|-|-|-|FMC_NOE|-|-|EVENT-<br>OUT|
|Port D|PD5|-|-|HRTIM_<br>EEV3|-|-|-|-|USART2_<br>TX|-|-|-|-|FMC_NWE|-|-|EVENT-<br>OUT|
|Port D|PD6|-|-|SAI1_D1|DFSDM1_<br>CKIN4|DFSDM1_<br>DATIN1|SPI3_<br>MOSI/I2S3<br>_SDO|SAI1_SD_A|USART2_<br>RX|SAI4_SD_<br>A|-|SAI4_D1|SDMMC2_<br>CK|FMC_<br>NWAIT|DCMI_D10|LCD_B2|EVENT-<br>OUT|
|Port D|PD7|-|-|-|DFSDM1_<br>DATIN4|-|SPI1_<br>MOSI/I2S1<br>_SDO|DFSDM1_<br>CKIN1|USART2_<br>CK|-|SPDIFRX1_<br>IN1|-|SDMMC2_<br>CMD|FMC_NE1|-|-|EVENT-<br>OUT|


**Table 13. Port D alternate functions (continued)**
























































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port D|PD8|-|-|-|DFSDM1_<br>CKIN3|-|-|SAI3_SCK_<br>B|USART3_<br>TX|-|SPDIFRX1_<br>IN2|-|-|FMC_D13/<br>FMC_DA13|-|-|EVENT-<br>OUT|
|Port D|PD9|-|-|-|DFSDM1_<br>DATIN3|-|-|SAI3_SD_B|USART3_<br>RX|-|-|-|-|FMC_D14/<br>FMC_DA14|-|-|EVENT-<br>OUT|
|Port D|PD10|-|-|-|DFSDM1_<br>CKOUT|-|-|SAI3_FS_B|USART3_<br>CK|-|-|-|-|FMC_D15/<br>FMC_DA15|-|LCD_B3|EVENT-<br>OUT|
|Port D|PD11|-|-|-|LPTIM2_<br>IN2|I2C4_SMBA|-|-|USART3_<br>CTS/<br>USART3_N<br>SS|-|QUADSPI_<br>BK1_IO0|SAI2_SD_A|-|FMC_A16|-|-|EVENT-<br>OUT|
|Port D|PD12|-|LPTIM1_IN1|TIM4_CH1|LPTIM2_<br>IN1|I2C4_SCL|-|-|USART3_<br>RTS/<br>USART3_<br>DE|-|QUADSPI_<br>BK1_IO1|SAI2_FS_A|-|FMC_A17|-|-|EVENT-<br>OUT|
|Port D|PD13|-|LPTIM1_<br>OUT|TIM4_CH2|-|I2C4_SDA|-|-||-|QUADSPI_<br>BK1_IO3|SAI2_SCK_<br>A|-|FMC_A18|-|-|EVENT-<br>OUT|
|Port D|PD14|-|-|TIM4_CH3|-|-|-|SAI3_MCLK<br>_B|-|UART8_<br>CTS|-|-|-|FMC_D0/<br>FMC_DA0|-|-|EVENT-<br>OUT|
|Port D|PD15|-|-|TIM4_CH4|-|-|-|SAI3_MCLK<br>_A|-|UART8_<br>RTS/<br>UART8_<br>DE|-|-|-|FMC_D1/<br>FMC_DA1|-|-|EVENT-<br>OUT|


**Table 14. Port E alternate functions**




































































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/1<br>7/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port E|PE0|-|LPTIM1_<br>ETR|TIM4_ETR|HRTIM_<br>SCIN|LPTIM2_<br>ETR|-|-|-|UART8_RX|-|SAI2_<br>MCLK_A|-|FMC_NBL0|DCMI_D2|-|EVENT-<br>OUT|
|Port E|PE1|-|LPTIM1_IN2|-|HRTIM_<br>SCOUT|-|-|-|-|UART8_TX|-|-|-|FMC_NBL1|DCMI_D3|-|EVENT-<br>OUT|
|Port E|PE2|TRACE<br>CLK|-|SAI1_CK1|-|-|SPI4_SCK|SAI1_MCLK<br>_A|-|SAI4_<br>MCLK_A|QUADSPI_<br>BK1_IO2|SAI4_CK1|ETH_MII_<br>TXD3|FMC_A23|-|-|EVENT-<br>OUT|
|Port E|PE3|TRACED0|-|-|-|TIM15_BKIN|-|SAI1_SD_B|-|SAI4_SD_<br>B|-|-|-|FMC_A19|-|-|EVENT-<br>OUT|
|Port E|PE4|TRACED1|-|SAI1_D2|DFSDM1_<br>DATIN3|TIM15_CH1<br>N|SPI4_NSS|SAI1_FS_A|-|SAI4_FS_A|-|SAI4_D2|-|FMC_A20|DCMI_D4|LCD_B0|EVENT-<br>OUT|
|Port E|PE5|TRACED2|-|SAI1_CK2|DFSDM1_<br>CKIN3|TIM15_CH1|SPI4_<br>MISO|SAI1_SCK_<br>A|-|SAI4_SCK<br>_A|-|SAI4_CK2|-|FMC_A21|DCMI_D6|LCD_G0|EVENT-<br>OUT|
|Port E|PE6|TRACED3|TIM1_<br>BKIN2|SAI1_D1|-|TIM15_CH2|SPI4_<br>MOSI|SAI1_SD_A|-|SAI4_SD_<br>A|SAI4_D1|SAI2_<br>MCLK_B|TIM1_BKIN<br>2_COMP12|FMC_A22|DCMI_D7|LCD_G1|EVENT-<br>OUT|
|Port E|PE7|-|TIM1_ETR|-|DFSDM1_<br>DATIN2|-|-|-|UART7_RX|-|-|QUADSPI_<br>BK2_IO0|-|FMC_D4/<br>FMC_DA4|-|-|EVENT-<br>OUT|
|Port E|PE8|-|TIM1_CH1N|-|DFSDM1_<br>CKIN2|-|-|-|UART7_TX|-|-|QUADSPI_<br>BK2_IO1|-|FMC_D5/<br>FMC_DA5|COMP2_<br>OUT|-|EVENT-<br>OUT|
|Port E|PE9|-|TIM1_CH1|-|DFSDM1_<br>CKOUT|-|-|-|UART7_<br>RTS/<br>UART7_<br>DE|-|-|QUADSPI_<br>BK2_IO2|-|FMC_D6/<br>FMC_DA6|-|-|EVENT-<br>OUT|
|Port E|PE10|-|TIM1_CH2N|-|DFSDM1_<br>DATIN4|-|-|-|UART7_<br>CTS|-|-|QUADSPI_<br>BK2_IO3|-|FMC_D7/<br>FMC_DA7|-|-|EVENT-<br>OUT|
|Port E|PE11|-|TIM1_CH2|-|DFSDM1_<br>CKIN4|-|SPI4_NSS|-|-|-|-|SAI2_SD_B|-|FMC_D8/<br>FMC_DA8|-|LCD_G3|EVENT-<br>OUT|
|Port E|PE12|-|TIM1_CH3N|-|DFSDM1_<br>DATIN5|-|SPI4_SCK|-|-|-|-|SAI2_SCK_<br>B|-|FMC_D9/<br>FMC_DA9|COMP1_<br>OUT|LCD_B4|EVENT-<br>OUT|
|Port E|PE13|-|TIM1_CH3|-|DFSDM1_<br>CKIN5|-|SPI4_<br>MISO|-|-|-|-|SAI2_FS_B|-|FMC_D10/<br>FMC_DA10|COMP2_<br>OUT|LCD_DE|EVENT-<br>OUT|
|Port E|PE14|-|TIM1_CH4|-|-|-|SPI4_<br>MOSI|-|-|-|-|SAI2_<br>MCLK_B|-|FMC_D11/<br>FMC_DA11|-|LCD_CLK|EVENT-<br>OUT|
|Port E|PE15|-|TIM1_BKIN|-|-|-|-|-|-|-|-||-|FMC_D12/<br>FMC_DA12|TIM1_BKIN<br>_COMP12/<br>COMP_<br>TIM1_BKIN|LCD_R7|EVENT-<br>OUT|


**Table 15. Port F alternate functions**
















































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port F|PF0|-|-|-|-|I2C2_SDA|-|-|-|-|-|-|-|FMC_A0|-|-|EVENT-<br>OUT|
|Port F|PF1|-|-|-|-|I2C2_SCL|-|-|-|-|-|-|-|FMC_A1|-|-|EVENT-<br>OUT|
|Port F|PF2|-|-|-|-|I2C2_SMBA|-|-|-|-|-|-|-|FMC_A2|-|-|EVENT-<br>OUT|
|Port F|PF3|-|-|-|-|-|-|-|-|-|-|-|-|FMC_A3|-|-|EVENT-<br>OUT|
|Port F|PF4|-|-|-|-|-|-|-|-|-|-|-|-|FMC_A4|-|-|EVENT-<br>OUT|
|Port F|PF5|-|-|-|-|-|-|-|-|-|-|-|-|FMC_A5|-|-|EVENT-<br>OUT|
|Port F|PF6|-|TIM16_CH1|-|-|-|SPI5_NSS|SAI1_SD_B|UART7_RX|SAI4_SD_<br>B|QUADSPI_<br>BK1_IO3|-|-|-|-|-|EVENT-<br>OUT|
|Port F|PF7|-|TIM17_CH1|-|-|-|SPI5_SCK|SAI1_MCLK<br>_B|UART7_TX|SAI4_<br>MCLK_B|QUADSPI_<br>BK1_IO2|-|-|-|-|-|EVENT-<br>OUT|
|Port F|PF8|-|TIM16_<br>CH1N|-|-|-|SPI5_<br>MISO|SAI1_SCK_<br>B|UART7_<br>RTS/<br>UART7_<br>DE|SAI4_SCK<br>_B|TIM13_<br>CH1|QUADSPI_<br>BK1_IO0|-|-|-|-|EVENT-<br>OUT|
|Port F|PF9|-|TIM17_<br>CH1N|-|-|-|SPI5_<br>MOSI|SAI1_FS_B|UART7_<br>CTS|SAI4_FS_B|TIM14_CH<br>1|QUADSPI_<br>BK1_IO1|-|-|-|-|EVENT-<br>OUT|
|Port F|PF10|-|TIM16_<br>BKIN|SAI1_D3|-|-|-|-|-|-|QUADSPI_<br>CLK|SAI4_D3|-|-|DCMI_D11|LCD_DE|EVENT-<br>OUT|
|Port F|PF11|-|-|-|-|-|SPI5_<br>MOSI|-|-|-|-|SAI2_SD_B|-|FMC_<br>SDNRAS|DCMI_D12|-|EVENT-<br>OUT|
|Port F|PF12|-|-|-|-|-|-|-|-|-|-|-|-|FMC_A6|-|-|EVENT-<br>OUT|
|Port F|PF13|-|-|-|DFSDM1_<br>DATIN6|I2C4_SMBA|-|-|-|-|-|-|-|FMC_A7|-|-|EVENT-<br>OUT|
|Port F|PF14|-|-|-|DFSDM1_<br>CKIN6|I2C4_SCL|-|-|-|-|-|-|-|FMC_A8|-|-|EVENT-<br>OUT|
|Port F|PF15|-|-|-|-|I2C4_SDA|-|-|-|-|-|-|-|FMC_A9|-|-|EVENT-<br>OUT|


**Table 16. Port G alternate functions**
















































































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/UART7<br>/SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/<br>DCMI/LCD<br>/COMP|UART5/<br>LCD|SYS|
|Port G|PG0|-|-|-|-|-|-|-|-|-|-|-|-|FMC_A10|-|-|EVENT<br>-OUT|
|Port G|PG1|-|-|-|-|-|-|-|-|-|-|-|-|FMC_A11|-|-|EVENT<br>-OUT|
|Port G|PG2|-|-|-|TIM8_BKIN|-|-|-|-|-|-|-|TIM8_BKIN_<br>COMP12|FMC_A12|-|-|EVENT<br>-OUT|
|Port G|PG3|-|-|-|TIM8_<br>BKIN2|-|-|-|-|-|-|-|TIM8_BKIN2<br>_COMP12|FMC_A13|-|-|EVENT<br>-OUT|
|Port G|PG4|-|TIM1_<br>BKIN2|-|-|-|-|-|-|-|-|-|TIM1_BKIN2<br>_COMP12|FMC_A14/<br>FMC_BA0|-|-|EVENT<br>-OUT|
|Port G|PG5|-|TIM1_ETR|-|-|-|-|-|-|-|-|-|-|FMC_A15/<br>FMC_BA1|-|-|EVENT<br>-OUT|
|Port G|PG6|-|TIM17_<br>BKIN|HRTIM_<br>CHE1|-|-|-|-|-|-|-|QUADSPI_<br>BK1_NCS|-|FMC_NE3|DCMI_<br>D12|LCD_<br>R7|EVENT<br>-OUT|
|Port G|PG7|-|-|HRTIM_<br>CHE2|-|-|-|SAI1_<br>MCLK_A|USART6_<br>CK|-|-|-|-|FMC_INT|DCMI_<br>D13|LCD_<br>CLK|EVENT<br>-OUT|
|Port G|PG8|-|-|-|TIM8_ETR|-|SPI6_NSS|-|USART6_<br>RTS/<br>USART6_<br>DE|SPDIFRX1<br>_IN3|-|-|ETH_PPS_<br>OUT|FMC_<br>SDCLK|-|LCD_<br>G7|EVENT<br>-OUT|
|Port G|PG9|-|-|-|-|-|SPI1_<br>MISO/I2S1<br>_SDI|-|USART6_<br>RX|SPDIFRX1<br>_IN4|QUADSPI_<br>BK2_IO2|SAI2_FS_B|-|FMC_NE2/<br>FMC_NCE|DCMI_<br>VSYNC|-|EVENT<br>-OUT|
|Port G|PG10|-|-|HRTIM_<br>FLT5|-|-|SPI1_NSS/<br>I2S1_WS|-|-|-|LCD_G3|SAI2_SD_B|-|FMC_NE3|DCMI_D2|LCD_<br>B2|EVENT<br>-OUT|
|Port G|PG11|-|LPTIM1_IN2|HRTIM_<br>EEV4|-|-|SPI1_SCK/<br>I2S1_CK|-|-|SPDIFRX1<br>_IN1|-|SDMMC2_D2|ETH_MII_<br>TX_EN/<br>ETH_RMII_<br>TX_EN|-|DCMI_D3|LCD_<br>B3|EVENT<br>-OUT|
|Port G|PG12|-|LPTIM1_IN1|HRTIM_<br>EEV5|-|-|SPI6_<br>MISO||USART6_<br>RTS/<br>USART6_<br>DE|SPDIFRX1<br>_IN2|LCD_B4|-|ETH_MII_<br>TXD1/ETH_<br>RMII_TXD1|FMC_NE4|-|LCD_<br>B1|EVENT<br>-OUT|
|Port G|PG13|TRACED0|LPTIM1_<br>OUT|HRTIM_<br>EEV10|-|-|SPI6_SCK|-|USART6_<br>CTS/<br>USART6_<br>NSS|-|-|-|ETH_MII_<br>TXD0/ETH_<br>RMII_TXD0|FMC_A24|-|LCD_<br>R0|EVENT<br>-OUT|


**Table 16. Port G alternate functions (continued)**
















































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/UART7<br>/SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/<br>DCMI/LCD<br>/COMP|UART5/<br>LCD|SYS|
|Port G|PG14|TRACED1|LPTIM1_<br>ETR|-|-|-|SPI6_<br>MOSI|-|USART6_<br>TX||QUADSPI_<br>BK2_IO3|-|ETH_MII_<br>TXD1/ETH_<br>RMII_TXD1|FMC_A25|-|LCD_<br>B0|EVENT<br>-OUT|
|Port G|PG15|-|-|-|-|-|-|-|USART6_<br>CTS/<br>USART6_<br>NSS|-|-|-|-|FMC_<br>SDNCAS|DCMI_<br>D13|-|EVENT<br>-OUT|


**Table 17. Port H alternate functions**


















































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port H|PH0|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|
|Port H|PH1|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|
|Port H|PH2|-|LPTIM1_IN2|-|-|-|-|-|-|-|QUADSPI_<br>BK2_IO0|SAI2_SCK_<br>B|ETH_MII_<br>CRS|FMC_<br>SDCKE0|-|LCD_R0|EVENT-<br>OUT|
|Port H|PH3|-|-|-|-|-|-|-|-|-|QUADSPI_<br>BK2_IO1|SAI2_<br>MCLK_B|ETH_MII_<br>COL|FMC_<br>SDNE0|-|LCD_R1|EVENT-<br>OUT|
|Port H|PH4|-|-|-|-|I2C2_SCL|-|-|-|-|LCD_G5|OTG_HS_<br>ULPI_NXT|-|-|-|LCD_G4|EVENT-<br>OUT|
|Port H|PH5|-|-|-|-|I2C2_SDA|SPI5_NSS|-|-|-|-|-|-|FMC_<br>SDNWE|-|-|EVENT-<br>OUT|
|Port H|PH6|-|-|TIM12_<br>CH1|-|I2C2_SMBA|SPI5_SCK|-|-|-|-|-|ETH_MII_<br>RXD2|FMC_<br>SDNE1|DCMI_D8|-|EVENT-<br>OUT|
|Port H|PH7|-|-|-|-|I2C3_SCL|SPI5_<br>MISO|-|-|-|-|-|ETH_MII_<br>RXD3|FMC_<br>SDCKE1|DCMI_D9|-|EVENT-<br>OUT|
|Port H|PH8|-|-|TIM5_ETR|-|I2C3_SDA|-|-|-|-|-|-|-|FMC_D16|DCMI_<br>HSYNC|LCD_R2|EVENT-<br>OUT|
|Port H|PH9|-|-|TIM12_<br>CH2|-|I2C3_SMBA|-|-|-|-|-|-|-|FMC_D17|DCMI_D0|LCD_R3|EVENT-<br>OUT|
|Port H|PH10|-|-|TIM5_CH1|-|I2C4_SMBA|-|-|-|-|-|-|-|FMC_D18|DCMI_D1|LCD_R4|EVENT-<br>OUT|
|Port H|PH11|-|-|TIM5_CH2|-|I2C4_SCL|-|-|-|-|-|-|-|FMC_D19|DCMI_D2|LCD_R5|EVENT-<br>OUT|
|Port H|PH12|-|-|TIM5_CH3|-|I2C4_SDA|-|-|-|-|-|-|-|FMC_D20|DCMI_D3|LCD_R6|EVENT-<br>OUT|
|Port H|PH13|-|-|-|TIM8_<br>CH1N|-|-|-|-|UART4_TX|FDCAN1_<br>TX|-|-|FMC_D21|-|LCD_G2|EVENT-<br>OUT|
|Port H|PH14|-|-|-|TIM8_<br>CH2N|-|-|-|-|UART4_RX|FDCAN1_<br>RX|-|-|FMC_D22|DCMI_D4|LCD_G3|EVENT-<br>OUT|
|Port H|PH15|-|-|-|TIM8_<br>CH3N|-|-|-|-|-|-|-|-|FMC_D23|DCMI_D11|LCD_G4|EVENT-<br>OUT|


**Table 18. Port I alternate functions**
























































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>FDCAN1/2/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port I|PI0|-|-|TIM5_CH4|-|-|SPI2_NSS/<br>I2S2_WS|-|-|-|-|-|-|FMC_D24|DCMI_D13|LCD_G5|EVENT-<br>OUT|
|Port I|PI1|-|-|-|TIM8_<br>BKIN2|-|SPI2_SCK/<br>I2S2_CK|-|-|-|-|-|TIM8_BKIN<br>2_COMP12|FMC_D25|DCMI_D8|LCD_G6|EVENT-<br>OUT|
|Port I|PI2|-|-|-|TIM8_CH4|-|SPI2_<br>MISO/I2S2<br>_SDI|-|-|-|-|-|-|FMC_D26|DCMI_D9|LCD_G7|EVENT-<br>OUT|
|Port I|PI3|-|-|-|TIM8_ETR|-|SPI2_<br>MOSI/I2S2<br>_SDO|-|-|-|-|-|-|FMC_D27|DCMI_D10|-|EVENT-<br>OUT|
|Port I|PI4|-|-|-|TIM8_BKIN|-|-|-|-|-|-|SAI2_<br>MCLK_A|TIM8_BKIN<br>_COMP12|FMC_NBL2|DCMI_D5|LCD_B4|EVENT-<br>OUT|
|Port I|PI5|-|-|-|TIM8_CH1|-|-|-|-|-|-|SAI2_SCK_<br>A|-|FMC_NBL3|DCMI_<br>VSYNC|LCD_B5|EVENT-<br>OUT|
|Port I|PI6|-|-|-|TIM8_CH2|-|-|-|-|-|-|SAI2_SD_A|-|FMC_D28|DCMI_D6|LCD_B6|EVENT-<br>OUT|
|Port I|PI7|-|-|-|TIM8_CH3|-|-|-|-|-|-|SAI2_FS_A|-|FMC_D29|DCMI_D7|LCD_B7|EVENT-<br>OUT|
|Port I|PI8|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT-<br>OUT|
|Port I|PI9|-|-|-|-|-|-|-|-|UART4_RX|FDCAN1_<br>RX|-|-|FMC_D30|-|LCD_<br>VSYNC|EVENT-<br>OUT|
|Port I|PI10|-|-|-|-|-|-|-|-|-|-|-|ETH_MII_<br>RX_ER|FMC_D31|-|LCD_<br>HSYNC|EVENT-<br>OUT|
|Port I|PI11|-|-|-|-|-|-|-|-|-|LCD_G6|OTG_HS_<br>ULPI_DIR|-|-|-|-|EVENT-<br>OUT|
|Port I|PI12|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_<br>HSYNC|EVENT-<br>OUT|
|Port I|PI13|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_<br>VSYNC|EVENT-<br>OUT|
|Port I|PI14|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_CLK|EVENT-<br>OUT|
|Port I|PI15|-|-|-|-|-|-|-|-|-|LCD_G2|-|-|-|-|LCD_R0|EVENT-<br>OUT|


**Table 19. Port J alternate functions**


































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/<br>17/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port J|PJ0|-|-|-|-|-|-|-|-|-|LCD_R7|-|-|-|-|LCD_R1|EVENT-<br>OUT|
|Port J|PJ1|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_R2|EVENT-<br>OUT|
|Port J|PJ2|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_R3|EVENT-<br>OUT|
|Port J|PJ3|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_R4|EVENT-<br>OUT|
|Port J|PJ4|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_R5|EVENT-<br>OUT|
|Port J|PJ5|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_R6|EVENT-<br>OUT|
|Port J|PJ6|-|-|-|TIM8_CH2|-|-|-|-|-|-|-|-|-|-|LCD_R7|EVENT-<br>OUT|
|Port J|PJ7|TRGIN|-|-|TIM8_<br>CH2N|-|-|-|-|-|-|-|-|-|-|LCD_G0|EVENT-<br>OUT|
|Port J|PJ8|-|TIM1_CH3N|-|TIM8_CH1|-|-|-|-|UART8_TX|-|-|-|-|-|LCD_G1|EVENT-<br>OUT|
|Port J|PJ9|-|TIM1_CH3|-|TIM8_<br>CH1N|-|-|-|-|UART8_RX|-|-|-|-|-|LCD_G2|EVENT-<br>OUT|
|Port J|PJ10|-|TIM1_CH2N|-|TIM8_CH2|-|SPI5_<br>MOSI|-|-|-|-|-|-|-|-|LCD_G3|EVENT-<br>OUT|
|Port J|PJ11|-|TIM1_CH2|-|TIM8_<br>CH2N|-|SPI5_<br>MISO|-|-|-|-|-|-|-|-|LCD_G4|EVENT-<br>OUT|
|Port J|PJ12|TRGOUT|-|-|-|-|-|-|-|-|LCD_G3|-|-|-|-|LCD_B0|EVENT-<br>OUT|
|Port J|PJ13|-|-|-|-|-|-|-|-|-|LCD_B4|-|-|-|-|LCD_B1|EVENT-<br>OUT|
|Port J|PJ14|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_B2|EVENT-<br>OUT|
|Port J|PJ15|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_B3|EVENT-<br>OUT|


**Table 20. Port K alternate functions**








































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Port|Port|SYS|TIM1/2/16/1<br>7/LPTIM1/<br>HRTIM1|SAI1/TIM3/<br>4/5/12/<br>HRTIM1|LPUART/<br>TIM8/<br>LPTIM2/3/4<br>/5/HRTIM1/<br>DFSDM1|I2C1/2/3/4/<br>USART1/<br>TIM15/<br>LPTIM2/<br>DFSDM1/<br>CEC|SPI1/2/3/4/<br>5/6/CEC|SPI2/3/SAI1<br>/3/I2C4/<br>UART4/<br>DFSDM1|SPI2/3/6/<br>USART1/2/<br>3/6/UART7/<br>SDMMC1|SPI6/SAI2/<br>4/UART4/5/<br>8/LPUART/<br>SDMMC1/<br>SPDIFRX1|SAI4/<br>TIM13/14/<br>QUADSPI/<br>FMC/<br>SDMMC2/<br>LCD/<br>SPDIFRX1|SAI2/4/<br>TIM8/<br>QUADSPI/<br>SDMMC2/<br>OTG1_HS/<br>OTG2_FS/<br>LCD|I2C4/<br>UART7/<br>SWPMI1/<br>TIM1/8/<br>DFSDM1/<br>SDMMC2/<br>MDIOS/<br>ETH|TIM1/8/FMC<br>/SDMMC1/<br>MDIOS/<br>OTG1_FS/<br>LCD|TIM1/DCMI<br>/LCD/<br>COMP|UART5/<br>LCD|SYS|
|Port K|PK0|-|TIM1_CH1N|-|TIM8_CH3|-|SPI5_SCK|-|-|-|-|-|-|-|-|LCD_G5|EVENT-<br>OUT|
|Port K|PK1|-|TIM1_CH1|-|TIM8_<br>CH3N|-|SPI5_NSS|-|-|-|-|-|-|-|-|LCD_G6|EVENT-<br>OUT|
|Port K|PK2|-|TIM1_BKIN|-|TIM8_BKIN|-|-|-|-|-|-|TIM8_BKIN<br>_COMP12|TIM1_BKIN<br>_COMP12|-|-|LCD_G7|EVENT-<br>OUT|
|Port K|PK3|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_B4|EVENT-<br>OUT|
|Port K|PK4|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_B5|EVENT-<br>OUT|
|Port K|PK5|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_B6|EVENT-<br>OUT|
|Port K|PK6|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_B7|EVENT-<br>OUT|
|Port K|PK7|-|-|-|-|-|-|-|-|-|-|-|-|-|-|LCD_DE|EVENT-<br>OUT|


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**

#### **6 Electrical characteristics (rev Y)**

###### **6.1 Parameter conditions**


Unless otherwise specified, all voltages are referenced to V SS .


**6.1.1** **Minimum and maximum values**


Unless otherwise specified the minimum and maximum values are guaranteed in the worst
conditions of junction temperature, supply voltage and frequencies by tests in production on
100% of the devices with an junction temperature at T J = 25 °C and T J = T Jmax (given by the
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


The loading conditions used for pin parameter measurement are shown in _Figure 13_ .


**6.1.5** **Pin input voltage**


The input voltage measurement on a pin of the device is described in _Figure 14_ .







102/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.1.6** **Power supply scheme**



**Figure 15. Power supply scheme**
























|Col1|Col2|
|---|---|
||IOs|




|Col1|Core domain (V )<br>CORE|Col3|
|---|---|---|
||D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>D1 domain<br>(CPU, peripherals,<br>RAM)<br>Level shifter<br>Flash<br>D2 domain<br>(peripherals,<br>RAM)<br>Power<br>switch<br>Power<br>switch<br>IO<br>logic|D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>D1 domain<br>(CPU, peripherals,<br>RAM)<br>Level shifter<br>Flash<br>D2 domain<br>(peripherals,<br>RAM)<br>Power<br>switch<br>Power<br>switch<br>IO<br>logic|
||D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>D1 domain<br>(CPU, peripherals,<br>RAM)<br>Level shifter<br>Flash<br>D2 domain<br>(peripherals,<br>RAM)<br>Power<br>switch<br>Power<br>switch<br>IO<br>logic|D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>IO<br>logic|
||Level shifter|IO<br>logic|
||||












|Col1|BKUP<br>IOs|
|---|---|
|||
















|Col1|Col2|Col3|
|---|---|---|
||||
||||



1. N corresponds to the number of VDD pins available on the package.


2. A tolerance of +/- 20% is acceptable on decoupling capacitors.


**Caution:** Each power supply pair (V DD /V SS, V DDA /V SSA ...) must be decoupled with filtering ceramic
capacitors as shown above. These capacitors must be placed as close as possible to, or
below, the appropriate pins on the underside of the PCB to ensure good operation of the


DS12110 Rev 10 103/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


device. It is not recommended to remove filtering capacitors to reduce PCB size or cost.
This might cause incorrect operation of the device.


**6.1.7** **Current consumption measurement**


**Figure 16. Current consumption measurement scheme**

###### **6.2 Absolute maximum ratings**


Stresses above the absolute maximum ratings listed in _Table 21: Voltage characteristics_,
_Table 22: Current characteristics_, and _Table 23: Thermal characteristics_ may cause
permanent damage to the device. These are stress ratings only and the functional operation
of the device at these conditions is not implied. Exposure to maximum rating conditions for
extended periods may affect device reliability. Device mission profile (application conditions)
is compliant with JEDEC JESD47 Qualification Standard, extended mission profiles are
available on demand.


**Table 21. Voltage characteristics** **[(1)]**







|Symbols|Ratings|Min|Max|Unit|
|---|---|---|---|---|
|VDDX- VSS|External main supply voltage (including VDD, <br>VDDLDO, VDDA, VDD33USB, VBAT)|−0.3|4.0|V|
|VIN<br>(2)|Input voltage on FT_xxx pins|VSS−0.3|Min(VDD, VDDA, <br>VDD33USB, VBAT) <br>+4.0(3)(4)|V|
|VIN<br>(2)|Input voltage on TT_xx pins|VSS-0.3|4.0|V|
|VIN<br>(2)|Input voltage on BOOT0 pin|VSS|9.0|V|
|VIN<br>(2)|Input voltage on any other pins|VSS-0.3|4.0|V|
||∆VDDX||Variations between different VDDX power pins<br>of the same domain|-|50|mV|
||VSSx-VSS||Variations between all the different ground pins|-|50|mV|


1. All main power (V DD, V DDA, V DD33USB, V BAT ) and ground (V SS, V SSA ) pins must always be connected to
the external power supply, in the permitted range.


2. V IN maximum must always be respected. Refer to _Table 59_ for the maximum allowed injected current
values.


104/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


3. This formula has to be applied on power supplies related to the IO structure described by the pin definition
table.


4. To sustain a voltage higher than 4V the internal pull-up/pull-down resistors must be disabled.


**Table 22. Current characteristics**
























|Symbols|Ratings|Max|Unit|
|---|---|---|---|
|ΣIVDD|Total current into sum of all VDD power lines (source)(1)|620|mA|
|ΣIVSS|Total current out of sum of all VSS ground lines (sink)(1)|620|620|
|IVDD|Maximum current into each VDD power pin (source)(1)|100|100|
|IVSS|Maximum current out of each VSS ground pin (sink)(1)|100|100|
|IIO|Output current sunk by any I/O and control pin, except Px_C|20|20|
|IIO|Output current sunk by Px_C pins|1|1|
|ΣI(PIN)|Total output current sunk by sum of all I/Os and control pins(2)|140|140|
|ΣI(PIN)|Total output current sourced by sum of all I/Os and control pins(2)|140|140|
|IINJ(PIN)<br>(3)(4)|Injected current on FT_xxx, TT_xx, RST and B pins except PA4,<br>PA5|−5/+0|−5/+0|
|IINJ(PIN)<br>(3)(4)|Injected current on PA4, PA5|−0/0|−0/0|
|ΣIINJ(PIN)|Total injected current (sum of all I/Os and control pins)(5)|±25|±25|



1. All main power (V DD, V DDA, V DD33USB ) and ground (V SS, V SSA ) pins must always be connected to the
external power supplies, in the permitted range.


2. This current consumption must be correctly distributed over all I/Os and control pins. The total output
current must not be sunk/sourced between two consecutive power supply pins referring to high pin count
QFP packages.


3. Positive injection is not possible on these I/Os and does not occur for input voltages lower than the
specified maximum value.


4. A positive injection is induced by V IN >V DD while a negative injection is induced by V IN <V SS . I INJ(PIN) must
never be exceeded. Refer also to _Table 21: Voltage characteristics_ for the maximum allowed input voltage
values.


5. When several inputs are submitted to a current injection, the maximum ∑I INJ(PIN) is the absolute sum of the
positive and negative injected currents (instantaneous values).


**Table 23. Thermal characteristics**

|Symbol|Ratings|Value|Unit|
|---|---|---|---|
|TSTG|Storage temperature range|−65 to +150|°C|
|TJ|Maximum junction temperature|125|125|



DS12110 Rev 10 105/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**

###### **6.3 Operating conditions**


**6.3.1** **General operating conditions**


**Table 24. General operating conditions**



















|Symbol|Parameter|Col3|Operating conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|VDD|Standard operating voltage|Standard operating voltage|-|1.62(1)|3.6|V|
|VDDLDO|Supply voltage for the internal regulator|Supply voltage for the internal regulator|VDDLDO≤ VDD|1.62(1)|3.6|3.6|
|VDD33USB|Standard operating voltage, USB domain|Standard operating voltage, USB domain|USB used|3.0|3.6|3.6|
|VDD33USB|Standard operating voltage, USB domain|Standard operating voltage, USB domain|USB not used|0|3.6|3.6|
|VDDA|Analog operating voltage|Analog operating voltage|ADC or COMP used|1.62|3.6|3.6|
|VDDA|Analog operating voltage|Analog operating voltage|DAC used|1.8|1.8|1.8|
|VDDA|Analog operating voltage|Analog operating voltage|OPAMP used|2.0|2.0|2.0|
|VDDA|Analog operating voltage|Analog operating voltage|VREFBUF used|1.8|1.8|1.8|
|VDDA|Analog operating voltage|Analog operating voltage|ADC, DAC, OPAMP,<br>COMP, VREFBUF not<br>used|0|0|0|
|VIN|I/O Input voltage|I/O Input voltage|TT_xx I/O|−0.3|VDD+0.3|VDD+0.3|
|VIN|I/O Input voltage|I/O Input voltage|BOOT0|0|9|9|
|VIN|I/O Input voltage|I/O Input voltage|All I/O except BOOT0<br>and TT_xx|−0.3|Min(VDD, VDDA, <br>VDD33USB) +3.6V<br>< 5.5V(2)(3)|Min(VDD, VDDA, <br>VDD33USB) +3.6V<br>< 5.5V(2)(3)|
|TA|Ambient temperature for<br>the suffix 6 version|Maximum power dissipation|Maximum power dissipation|–40|85|°C|
|TA|Ambient temperature for<br>the suffix 6 version|Low-power dissipation(4)|Low-power dissipation(4)|–40|105|105|
|TA|Ambient temperature for<br>the suffix 3 version|Maximum power dissipation|Maximum power dissipation|–40|125|125|
|TA|Ambient temperature for<br>the suffix 3 version|Low-power dissipation(4)|Low-power dissipation(4)|–40|130|130|
|TJ|Junction temperature<br>range|Suffix 6 version|Suffix 6 version|–40|125|°C|


1. When RESET is released functionality is guaranteed down to V BOR0 min


2. This formula has to be applied on power supplies related to the IO structure described by the pin definition table.


3. For operation with voltage higher than Min (V DD, V DDA, V DD33USB ) +0.3V, the internal Pull-up and Pull-Down resistors must
be disabled.


4. In low-power dissipation state, T A can be extended to this range as long as T J does not exceed T Jmax (see _Section 8.10:_
_Thermal characteristics_ ).


106/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.2** **VCAP external capacitor**


Stabilization for the main regulator is achieved by connecting an external capacitor C EXT to
the VCAP pin. C EXT is specified in _Table 25_ . Two external capacitors can be connected to
VCAP pins.


**Figure 17. External capacitor C** **EXT**


1. Legend: ESR is the equivalent series resistance.


**Table 25. VCAP operating conditions** **[(1)]**

|Symbol|Parameter|Conditions|
|---|---|---|
|CEXT|Capacitance of external capacitor|2.2 µF(2)|
|ESR|ESR of external capacitor|< 100 mΩ|



1. When bypassing the voltage regulator, the two 2.2 µF V CAP capacitors are not required and should be
replaced by two 100 nF decoupling capacitors.


2. This value corresponds to CEXT typical value. A variation of +/-20% is tolerated.


**6.3.3** **Operating conditions at power-up / power-down**


Subject to general operating conditions for T A .


**Table 26. Operating conditions at power-up / power-down (regulator ON)**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tVDD|VDD rise time rate|0|∞|µs/V|
|tVDD|VDD fall time rate|10|∞|∞|
|tVDDA|VDDA rise time rate|0|∞|∞|
|tVDDA|VDDA fall time rate|10|∞|∞|
|tVDDUSB|VDDUSB rise time rate|0|∞|∞|
|tVDDUSB|VDDUSB fall time rate|10|∞|∞|


DS12110 Rev 10 107/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.4** **Embedded reset and power control block characteristics**


The parameters given in _Table 27_ are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in _Table 24: General operating_
_conditions_ .


**Table 27. Reset and power control block characteristics**



















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tRSTTEMPO<br>(1)|Reset temporization<br>after BOR0 released|-|-|377|-|µs|
|VBOR0/POR/PDR|Brown-out reset threshold 0<br>(VPOR/VPDR thresholds)|Rising edge(1)|1.62|1.67|1.71|V|
|VBOR0/POR/PDR|Brown-out reset threshold 0<br>(VPOR/VPDR thresholds)|Falling edge|1.58|1.62|1.68|1.68|
|VBOR1|Brown-out reset threshold 1|Rising edge|2.04|2.10|2.15|2.15|
|VBOR1|Brown-out reset threshold 1|Falling edge|1.95|2.00|2.06|2.06|
|VBOR2|Brown-out reset threshold 2|Rising edge|2.34|2.41|2.47|2.47|
|VBOR2|Brown-out reset threshold 2|Falling edge|2.25|2.31|2.37|2.37|
|VBOR3|Brown-out reset threshold 3|Rising edge|2.63|2.70|2.78|2.78|
|VBOR3|Brown-out reset threshold 3|Falling edge|2.54|2.61|2.68|2.68|
|VPVD0|Programmable Voltage<br>Detector threshold 0|Rising edge|1.90|1.96|2.01|2.01|
|VPVD0|Programmable Voltage<br>Detector threshold 0|Falling edge|1.81|1.86|1.91|1.91|
|VPVD1|Programmable Voltage<br>Detector threshold 1|Rising edge|2.05|2.10|2.16|2.16|
|VPVD1|Programmable Voltage<br>Detector threshold 1|Falling edge|1.96|2.01|2.06|2.06|
|VPVD2|Programmable Voltage<br>Detector threshold 2|Rising edge|2.19|2.26|2.32|2.32|
|VPVD2|Programmable Voltage<br>Detector threshold 2|Falling edge|2.10|2.15|2.21|2.21|
|VPVD3|Programmable Voltage<br>Detector threshold 3|Rising edge|2.35|2.41|2.47|2.47|
|VPVD3|Programmable Voltage<br>Detector threshold 3|Falling edge|2.25|2.31|2.37|2.37|
|VPVD4|Programmable Voltage<br>Detector threshold 4|Rising edge|2.49|2.56|2.62|2.62|
|VPVD4|Programmable Voltage<br>Detector threshold 4|Falling edge|2.39|2.45|2.51|2.51|
|VPVD5|Programmable Voltage<br>Detector threshold 5|Rising edge|2.64|2.71|2.78|2.78|
|VPVD5|Programmable Voltage<br>Detector threshold 5|Falling edge|2.55|2.61|2.68|2.68|
|VPVD6|Programmable Voltage<br>Detector threshold 6|Rising edge|2.78|2.86|2.94|2.94|
|VPVD6|Programmable Voltage<br>Detector threshold 6|Falling edge in Run mode|2.69|2.76|2.83|2.83|
|Vhyst_BOR_PVD|Hysteresis voltage of BOR<br>(unless BOR0) and PVD|Hysteresis in Run mode|-|100|-|mV|
|IDD_BOR_PVD<br>(1)|BOR(2)(unless BOR0) and<br>PVD consumption from VDD|-|-|-|0.630|µA|


108/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 27. Reset and power control block characteristics (continued)**









|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VAVM_0|Analog voltage detector for<br>VDDA threshold 0|Rising edge|1.66|1.71|1.76|V|
|VAVM_0|Analog voltage detector for<br>VDDA threshold 0|Falling edge|1.56|1.61|1.66|1.66|
|VAVM_1|Analog voltage detector for<br>VDDA threshold 1|Rising edge|2.06|2.12|2.19|2.19|
|VAVM_1|Analog voltage detector for<br>VDDA threshold 1|Falling edge|1.96|2.02|2.08|2.08|
|VAVM_2|Analog voltage detector for<br>VDDA threshold 2|Rising edge|2.42|2.50|2.58|2.58|
|VAVM_2|Analog voltage detector for<br>VDDA threshold 2|Falling edge|2.35|2.42|2.49|2.49|
|VAVM_3|Analog voltage detector for<br>VDDA threshold 3|Rising edge|2.74|2.83|2.91|2.91|
|VAVM_3|Analog voltage detector for<br>VDDA threshold 3|Falling edge|2.64|2.72|2.80|2.80|
|Vhyst_VDDA|Hysteresis of VDDA voltage<br>detector|-|-|100|-|mV|
|IDD_PVM|PVM consumption from<br>VDD(1)|-|-|-|0.25|µA|
|IDD_VDDA|Voltage detector<br>consumption on VDDA<br>(1)|Resistor bridge|-|-|2.5|µA|


1. Guaranteed by design.


2. BOR0 is enabled in all modes and its consumption is therefore included in the supply current characteristics tables (refer to
_Section 6.3.6: Supply current characteristics_ ).


**6.3.5** **Embedded reference voltage**


The parameters given in _Table 28_ are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in _Table 24: General operating_
_conditions_ .


**Table 28. Embedded reference voltage**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VREFINT|Internal reference voltages|-40°C < TJ < 105°C,<br>VDD = 3.3 V|1.180|1.216|1.255|V|
|tS_vrefint<br>(1)(2)|ADC sampling time when<br>reading the internal reference<br>voltage|-|4.3|-|-|µs|
|tS_vbat<br>(1)(2)|VBAT sampling time when<br>reading the internal VBAT<br>reference voltage|-|9|-|-|-|
|Irefbuf<br>(2)|Reference Buffer<br>consumption for ADC|VDDA=3.3 V|9|13.5|23|µA|
|ΔVREFINT<br>(2)|Internal reference voltage<br>spread over the temperature<br>range|-40°C < TJ < 105°C|-|5|15|mV|
|Tcoeff<br>(2)|Average temperature<br>coefficient|Average temperature<br>coefficient|-|20|70|ppm/°C|
|VDDcoeff<br>(2)|Average Voltage coefficient|3.0V < VDD < 3.6V|-|10|1370|ppm/V|



DS12110 Rev 10 109/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 28. Embedded reference voltage (continued)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VREFINT_DIV1|1/4 reference voltage|-|-|25|-|% <br>VREFINT|
|VREFINT_DIV2|1/2 reference voltage|-|-|50|-|-|
|VREFINT_DIV3|3/4 reference voltage|-|-|75|-|-|



1. The shortest sampling time for the application can be determined by multiple iterations.


2. Guaranteed by design.


**Table 29. Internal reference voltage calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|VREFIN_CAL|Raw data acquired at temperature of 30 °C, VDDA = 3.3 V|1FF1E860 - 1FF1E861|



**6.3.6** **Supply current characteristics**


The current consumption is a function of several parameters and factors such as the
operating voltage, ambient temperature, I/O pin loading, device software configuration,
operating frequencies, I/O pin switching rate, program location in memory and executed
binary code.


The current consumption is measured as described in _Figure 16: Current consumption_
_measurement scheme_ .


All the run-mode current consumption measurements given in this section are performed
with a CoreMark code.


**Typical and maximum current consumption**


The MCU is placed under the following conditions:


      - All I/O pins are in analog input mode.


      - All peripherals are disabled except when explicitly mentioned.


      - The flash memory access time is adjusted with the minimum wait states number,
depending on the f ACLK frequency (refer to the table “Number of wait states according to
CPU clock (f rcc_c_ck ) frequency and V CORE range” available in the reference manual).

      - When the peripherals are enabled, the AHB clock frequency is the CPU frequency
divided by 2 and the APB clock frequency is AHB clock frequency divided by 2.


The parameters given in _Table 30_ to _Table 38_ are derived from tests performed under
ambient temperature and supply voltage conditions summarized in _Table 24: General_
_operating conditions_ .


110/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 30. Typical and maximum current consumption in Run mode, code with data processing**
**running from ITCM, regulator ON** **[(1)]**




















|Symbol|Parameter|Conditions|Col4|f<br>rcc_c_ck<br>(MHz)|Typ|Max(2)|Col8|Col9|Col10|unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**frcc_c_ck **<br>**(MHz)**|**Typ**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS1|400|71|110|210|290|540|mA|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS1|300|56|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|300|50|72|170|230|370|370|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|216|37|58|150|210|380|380|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|200|35.5|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|200|33|50|130|190|300|300|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|180|30|47|130|180|290|290|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|168|28|45|130|180|290|290|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|144|25|41|120|180|290|290|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|60|13|28|110|160|280|280|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|25|10|24|99|160|270|270|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS1|400|165|220(3)|400|500(3)|840|840|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS1|300|130|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS2|300|120|170|300|390|570|570|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS2|200|83|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS3|200|78|110|220|300|470|470|



1. Data are in DTCM for best computation performance, cache has no influence on consumption in this case.


2. Guaranteed by characterization results unless otherwise specified.


3. Guaranteed by test in production.


DS12110 Rev 10 111/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 31. Typical and maximum current consumption in Run mode, code with data processing**
**running from flash memory, cache ON, regulator ON**




















|Symbol|Parameter|Conditions|Col4|f<br>rcc_c_ck<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**frcc_c_ck **<br>**(MHz)**|**Typ**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS1|400|105|160|310|420|750|mA|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS1|300|55|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|300|50|72|160|230|370|370|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|216|38|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|200|36|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|200|33|50|130|190|300|300|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|180|30|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|168|29|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|144|26|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|60|14|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|25|14|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS1|400|160|220|400|500|750|750|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS1|300|130|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS2|300|120|160|300|390|560|560|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS2|200|81|-|-|-|-|-|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS3|200|77|110|220|300|460|460|



1. Guaranteed by characterization results unless otherwise specified.


**Table 32. Typical and maximum current consumption in Run mode, code with data processing**
**running from flash memory, cache OFF, regulator ON**














|Symbol|Parameter|Conditions|Col4|f<br>rcc_c_ck<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**frcc_c_ck **<br>**(MHz)**|**Typ**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS1|400|73|110|220|290|540|mA|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS2|300|52|75|170|230|370|370|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>disabled|VOS3|200|34|52|130|190|300|300|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS1|400|135|190|360|470|730|730|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS2|300|100|150|270|370|550|550|
|IDD|Supply<br>current in Run<br>mode|All<br>peripherals<br>enabled|VOS3|200|70|100|210|300|460|460|



1. Guaranteed by characterization results.


112/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 33. Typical consumption in Run mode and corresponding performance**
**versus code position**














|Symbol|Parameter|Conditions|Col4|f<br>rcc_c_ck<br>(MHz)|CoreMark|Typ|Unit|IDD/<br>CoreMark|Unit|
|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Peripheral**|**Code**|**Code**|**Code**|**Code**|**Code**|**Code**|**Code**|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled,<br>cache ON|ITCM|400|2012|71|mA|35|µA/<br>CoreMark|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled,<br>cache ON|FLASH<br>A|400|2012|105|105|52|52|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled,<br>cache ON|AXI<br>SRAM|400|2012|105|105|52|52|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled,<br>cache ON|SRAM1|400|2012|105|105|52|52|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled,<br>cache ON|SRAM4|400|2012|105|105|52|52|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled<br>cache OFF|ITCM|400|2012|71|71|35|35|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled<br>cache OFF|FLASH<br>A|400|593|70.5|70.5|119|119|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled<br>cache OFF|AXI<br>SRAM|400|344|70.5|70.5|205|205|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled<br>cache OFF|SRAM1|400|472|74.5|74.5|158|158|
|IDD|Supply current<br>in Run mode|All<br>peripherals<br>disabled<br>cache OFF|SRAM4|400|432|72|72|167|167|



**Table 34. Typical current consumption batch acquisition mode**








|Symbol|Parameter|Conditions|Col4|f<br>rcc_ahb_ck(AHB4)<br>(MHz)|Typ|unit|
|---|---|---|---|---|---|---|
|IDD|Supply current in<br>batch acquisition<br>mode|D1Standby,<br>D2Standby,<br>D3Run|VOS3|64|6.5|mA|
|IDD|Supply current in<br>batch acquisition<br>mode|D1Stop, D2Stop,<br>D3Run|VOS3|64|12|12|



**Table 35. Typical and maximum current consumption in Sleep mode, regulator ON**














|Symbol|Parameter|Conditions|Col4|f<br>rcc_c_ck<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**frcc_c_ck **<br>**(MHz)**|**Typ**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD(Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS1|400|31.0|64|220|330|660|mA|
|IDD(Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS1|300|24.5|57|210|330|650|650|
|IDD(Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS2|300|22.0|48|180|270|500|500|
|IDD(Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS2|200|17.0|42|170|270|490|490|
|IDD(Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS3|200|15.5|37|150|230|400|400|



1. Guaranteed by characterization results.



DS12110 Rev 10 113/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 36. Typical and maximum current consumption in Stop mode, regulator ON**

















|Symbol|Parameter|Conditions|Col4|Typ|Max(1)|Col7|Col8|Col9|unit|
|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**Typ**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD(Stop)|D1Stop,<br>D2Stop,<br>D3Stop|Flash<br>memory in<br>low-power<br>mode, no<br>IWDG|SVOS5|1.4|7.2(2)|49|75(2)|140|mA|
|IDD(Stop)|D1Stop,<br>D2Stop,<br>D3Stop|Flash<br>memory in<br>low-power<br>mode, no<br>IWDG|SVOS4|1.95|11|66|110|200|200|
|IDD(Stop)|D1Stop,<br>D2Stop,<br>D3Stop|Flash<br>memory in<br>low-power<br>mode, no<br>IWDG|SVOS3|2.85|16(2)|91|150(2)|240|240|
|IDD(Stop)|D1Stop,<br>D2Stop,<br>D3Stop|Flash<br>memory ON,<br>no IWDG|SVOS5|1.65|7.2|49|75|140|140|
|IDD(Stop)|D1Stop,<br>D2Stop,<br>D3Stop|Flash<br>memory ON,<br>no IWDG|SVOS4|2.2|11|66|110|180|180|
|IDD(Stop)|D1Stop,<br>D2Stop,<br>D3Stop|Flash<br>memory ON,<br>no IWDG|SVOS3|3.15|16|91|150|300|300|
|IDD(Stop)|D1Stop,<br>D2Standby,<br>D3Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS5|0.99|5.1|35|60|97|97|
|IDD(Stop)|D1Stop,<br>D2Standby,<br>D3Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS4|1.4|7.5|47|79|130|130|
|IDD(Stop)|D1Stop,<br>D2Standby,<br>D3Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS3|2.05|12|64|110|170|170|
|IDD(Stop)|D1Stop,<br>D2Standby,<br>D3Stop|Flash<br>memory ON,<br>no IWDG|SVOS5|1.25|5.5|35|61|98|98|
|IDD(Stop)|D1Stop,<br>D2Standby,<br>D3Stop|Flash<br>memory ON,<br>no IWDG|SVOS4|1.65|7.8|47|80|130|130|
|IDD(Stop)|D1Stop,<br>D2Standby,<br>D3Stop|Flash<br>memory ON,<br>no IWDG|SVOS3|2.3|12|65|110|170|170|
|IDD(Stop)|D1Standby,<br>D2Stop,<br>D3Stop|Flash OFF,<br>no IWDG|SVOS5|0.57|3|21|36|57|57|
|IDD(Stop)|D1Standby,<br>D2Stop,<br>D3Stop|Flash OFF,<br>no IWDG|SVOS4|0.805|4.5|27|47|74|74|
|IDD(Stop)|D1Standby,<br>D2Stop,<br>D3Stop|Flash OFF,<br>no IWDG|SVOS3|1.2|6.7|37|63|99|99|
|IDD(Stop)|D1Standby,<br>D2Standby,<br>D3Stop|D1Standby,<br>D2Standby,<br>D3Stop|SVOS5|0.17|1.1(2)|8|13(2)|20|20|
|IDD(Stop)|D1Standby,<br>D2Standby,<br>D3Stop|D1Standby,<br>D2Standby,<br>D3Stop|SVOS4|0.245|1.5|11|17|26|26|
|IDD(Stop)|D1Standby,<br>D2Standby,<br>D3Stop|D1Standby,<br>D2Standby,<br>D3Stop|SVOS3|0.405|2.4(2)|15|23(2)|35|35|


1. Guaranteed by characterization results.


2. Guaranteed by test in production.



**Table 37. Typical and maximum current consumption in Standby mode**










|Symbol|Parameter|Conditions|Col4|Typ(3)|Col6|Col7|Col8|Max (3 V)(1)|Col10|Col11|Col12|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Backup**<br>**SRAM**|**RTC**<br>**& LSE**|**1.62 V**|**2.4 V**|**3 V**|**3.3 V**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|OFF|OFF|1.8|1.9|1.95|2.05|4(2)|18(3)|40(2)|90(3)|µA|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|ON|OFF|3.4|3.4|3.5|3.7|8.2(3)|47(3)|83(3)|141(3)|141(3)|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|OFF|ON|2.4|3.5|3.86|4.12|-|-|-|-|-|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|ON|ON|3.95|5.1|5.46|5.97|-|-|-|-|-|



1. The maximum current consumption values are given for PDR OFF (internal reset OFF). When the PDR is OFF (internal
reset OFF), the current consumption is reduced by 1.2 µA compared to PDR ON.


2. Guaranteed by test in production.


3. Guaranteed by characterization results.


114/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 38. Typical and maximum current consumption in VBAT mode**










|Symbol|Parameter|Conditions|Col4|Typ(1)|Col6|Col7|Col8|Max (3 V)|Col10|Col11|Col12|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Backup**<br>**SRAM**|**RTC &**<br>**LSE**|**1.2 V**|**2 V**|**3 V**|**3.4 V**|**TJ =**<br>**25°C**|**TJ =**<br>**85°C**|**TJ =**<br>**105°C**|**TJ =**<br>**125°C**|**TJ =**<br>**125°C**|
|IDD<br>(VBAT)|Supply<br>current in<br>standby<br>mode|OFF|OFF|0.024|0.035|0.062|0.096|0.5(1)|4.1(1)|10(1)|24(1)|µA|
|IDD<br>(VBAT)|Supply<br>current in<br>standby<br>mode|ON|OFF|1.4|1.6|1.8|1.8|4.4(1)|22(1)|48(1)|87(1)|87(1)|
|IDD<br>(VBAT)|Supply<br>current in<br>standby<br>mode|OFF|ON|0.24|0.45|0.62|0.73|-|-|-|-|-|
|IDD<br>(VBAT)|Supply<br>current in<br>standby<br>mode|ON|ON|1.97|2.37|2.57|2.77|-|-|-|-|-|



1. Guaranteed by characterization results.


**I/O system current consumption**


The current consumption of the I/O system has two components: static and dynamic.


**I/O static current consumption**


All the I/Os used as inputs with pull-up or pull-down generate a current consumption when
the pin is externally held low. The value of this current consumption can be simply computed
by using the pull-up/pull-down resistors values given in _Table 60: I/O static characteristics_ .


For the output pins, any internal or external pull-up or pull-down, and any external load must
also be considered to estimate the current consumption.


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


In addition to the internal peripheral current consumption (see _Table 39: Peripheral current_
_consumption in Run mode_ ), the I/Os used by an application also contribute to the current
consumption. When an I/O pin switches, it uses the current from the MCU supply voltage to
supply the I/O pin circuitry and to charge/discharge the internal or external capacitive load
connected to the pin:


I = V × f × C
SW DDx SW L


where


I SW is the current sunk by a switching I/O to charge/discharge the capacitive load


V DDx is the MCU supply voltage


f SW is the I/O switching frequency


C L is the total capacitance seen by the I/O pin: C = C INT + C EXT


DS12110 Rev 10 115/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


The test pin is configured in push-pull output mode and is toggled by software at a fixed
frequency.


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

– f rcc_c_ck = 400 MHz (Scale 1), f rcc_c_ck = 300 MHz (Scale 2),
f rcc_c_ck = 200 MHz (Scale 3)

      - The ambient operating temperature is 25 °C and V DD =3.3 V.


116/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 39. Peripheral current consumption in Run mode**








|Peripheral|Col2|I (Typ)<br>DD|Col4|Col5|Unit|
|---|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**VOS1**|**VOS2**|**VOS3**|**VOS3**|
|AHB3|MDMA|8.3|7.6|7|µA/MHz|
|AHB3|DMA2D|21|20|18|18|
|AHB3|JPEG|24|23|21|21|
|AHB3|FLASH|9.9|9|8.3|8.3|
|AHB3|FMC registers|0.9|0.9|0.8|0.8|
|AHB3|FMC kernel|6.1|5.5|5.3|5.3|
|AHB3|QUADSPI<br>registers|1.5|1.4|1.3|1.3|
|AHB3|QUADSPI kernel|0.9|0.8|0.7|0.7|
|AHB3|SDMMC1<br>registers|8|7.2|6.8|6.8|
|AHB3|SDMMC1 kernel|2.4|2|1.8|1.8|
|AHB3|DTCM1|5.7|5|4.5|4.5|
|AHB3|DTCM2|5.5|4.8|4.3|4.3|
|AHB3|ITCM|3.2|2.9|2.6|2.6|
|AHB3|D1SRAM1|7.6|6.8|6.1|6.1|
|AHB3|AHB3 bridge|7.5|6.8|6.3|6.3|
|AHB1|DMA1|1.1|1|1|1|
|AHB1|DMA2|1.7|1.4|1.1|1.1|
|AHB1|ADC1/2 registers|3.9|3.2|3.1|3.1|
|AHB1|ADC1/2 kernel|0.9|0.8|0.7|0.7|
|AHB1|ART accelerator|5.5|4.5|4.2|4.2|
|AHB1|ETH1MAC|16|14|13|13|
|AHB1|ETH1TX|ETH1TX|ETH1TX|ETH1TX|ETH1TX|
|AHB1|ETH1RX|ETH1RX|ETH1RX|ETH1RX|ETH1RX|
|AHB1|USB1 OTG<br>registers|15|14|13|13|
|AHB1|USB1 OTG kernel|-|8.5|8.5|8.5|
|AHB1|USB1 ULPI|0.3|0.3|0.1|0.1|
|AHB1|USB2 OTG<br>registers|15|13|12|12|
|AHB1|USB2 OTG kernel|-|8.6|8.6|8.6|
|AHB1|USB2 ULPI|16|16|16|16|
|AHB1|AHB1 Bridge|10|9.6|8.6|8.6|



DS12110 Rev 10 117/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 39. Peripheral current consumption in Run mode (continued)**










|Peripheral|Col2|I (Typ)<br>DD|Col4|Col5|Unit|
|---|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**VOS1**|**VOS2**|**VOS3**|**VOS3**|
|AHB2|DCMI|1.7|1.7|1.7|µA/MHz|
|AHB2|RNG registers|1.8|1.4|1.2|1.2|
|AHB2|RNG kernel|-|9.6|9.6|9.6|
|AHB2|SDMMC2<br>registers|13|12|11|11|
|AHB2|SDMMC2 kernel|2.7|2.5|2.4|2.4|
|AHB2|D2SRAM1|3.3|3.1|2.8|2.8|
|AHB2|D2SRAM2|2.9|2.7|2.5|2.5|
|AHB2|D2SRAM3|1.9|1.8|1.7|1.7|
|AHB2|AHB2 bridge|0.1|0.1|0.1|0.1|
|AHB4|GPIOA|1.1|1|0.9|0.9|
|AHB4|GPIOB|1|0.9|0.9|0.9|
|AHB4|GPIOC|1.4|1.3|1.3|1.3|
|AHB4|GPIOD|1.1|1|0.9|0.9|
|AHB4|GPIOE|1|0.9|0.8|0.8|
|AHB4|GPIOF|0.9|0.8|0.8|0.8|
|AHB4|GPIOG|0.9|0.7|0.7|0.7|
|AHB4|GPIOH|1|0.9|0.9|0.9|
|AHB4|GPIOI|0.9|0.9|0.8|0.8|
|AHB4|GPIOJ|0.9|0.8|0.8|0.8|
|AHB4|GPIOK|0.9|0.8|0.7|0.7|
|AHB4|CRC|0.5|0.4|0.4|0.4|
|AHB4|BDMA|6.2|5.8|5.5|5.5|
|AHB4|ADC3 registers|1.8|1.7|1.7|1.7|
|AHB4|ADC3 kernel|0.1|0.1|0.1|0.1|
|AHB4|Backup SRAM|1.9|1.8|1.8|1.8|
|AHB4|Bridge AHB4|0.1|0.1|0.1|0.1|
|APB3|LCD-TFT|12|11|10|µA/MHz|
|APB3|WWDG1|0.5|0.4|0.3|0.3|
|APB3|APB3 bridge|0.5|0.2|0.1|0.1|



118/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 39. Peripheral current consumption in Run mode (continued)**








|Peripheral|Col2|I (Typ)<br>DD|Col4|Col5|Unit|
|---|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**VOS1**|**VOS2**|**VOS3**|**VOS3**|
|APB1|TIM2|3.5|3.2|2.9|µA/MHz|
|APB1|TIM3|3.4|3.1|2.7|2.7|
|APB1|TIM4|2.7|2.5|1.9|1.9|
|APB1|TIM5|3.2|2.9|2.5|2.5|
|APB1|TIM6|1|0.8|0.7|0.7|
|APB1|TIM7|1|0.9|0.7|0.7|
|APB1|TIM12|1.7|1.5|1.2|1.2|
|APB1|TIM13|1.5|1.3|1|1|
|APB1|TIM14|1.4|1.3|0.9|0.9|
|APB1|LPTIM1 registers|0.7|0.6|0.5|0.5|
|APB1|LPTIM1 kernel|2.3|2.1|1.9|1.9|
|APB1|WWDG2|0.6|0.4|0.4|0.4|
|APB1|SPI2 registers|1.8|1.5|1.2|1.2|
|APB1|SPI2 kernel|0.6|0.5|0.5|0.5|
|APB1|SPI3 registers|1.5|1.3|1.1|1.1|
|APB1|SPI3 kernel|0.6|0.5|0.5|0.5|
|APB1|SPDIFRX1<br>registers|0.6|0.5|0.3|0.3|
|APB1|SPDIFRX1 kernel|2.9|2.4|2.4|2.4|
|APB1|USART2 registers|1.4|1.3|1|1|
|APB1|USART2 kernel|4.7|4.1|4|4|
|APB1|USART3 registers|1.4|1.3|1|1|
|APB1|USART3 kernel|4.2|3.8|3.5|3.5|
|APB1|UART4 registers|1.5|1.1|1|1|
|APB1|UART4 kernel|3.7|3.6|3.2|3.2|



DS12110 Rev 10 119/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 39. Peripheral current consumption in Run mode (continued)**








|Peripheral|Col2|I (Typ)<br>DD|Col4|Col5|Unit|
|---|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**VOS1**|**VOS2**|**VOS3**|**VOS3**|
|APB1<br>(continued)|UART5 registers|1.4|1.4|1|µA/MHz|
|APB1<br>(continued)|UART5 kernel|3.6|3.2|3.1|3.1|
|APB1<br>(continued)|I2C1 registers|0.8|0.8|0.6|0.6|
|APB1<br>(continued)|I2C1 kernel|2|1.8|1.7|1.7|
|APB1<br>(continued)|I2C2 registers|0.7|0.7|0.4|0.4|
|APB1<br>(continued)|I2C2 kernel|1.9|1.7|1.6|1.6|
|APB1<br>(continued)|I2C3 registers|0.9|0.7|0.6|0.6|
|APB1<br>(continued)|I2C3 kernel|2.1|1.9|1.9|1.9|
|APB1<br>(continued)|HDMI-CEC<br>registers|0.5|0.3|0.3|0.3|
|APB1<br>(continued)|DAC1/2|1.4|1.1|0.9|0.9|
|APB1<br>(continued)|USART7 registers|1.9|1.8|1.3|1.3|
|APB1<br>(continued)|USART7 kernel|4|3.5|3.3|3.3|
|APB1<br>(continued)|USART8 registers|1.6|1.5|1.2|1.2|
|APB1<br>(continued)|USART8 kernel|4|3.6|3.3|3.3|
|APB1<br>(continued)|CRS|3.4|3.1|2.9|2.9|
|APB1<br>(continued)|SWPMI registers|2.3|2|2|2|
|APB1<br>(continued)|SWPMI kernel|0.1|0.1|0.1|0.1|
|APB1<br>(continued)|OPAMP|0.5|0.4|0.4|0.4|
|APB1<br>(continued)|MDIO|2.7|2.4|2.3|2.3|
|APB1<br>(continued)|FDCAN registers|16|15|14|14|
|APB1<br>(continued)|FDCAN kernel|7.8|7.6|7.1|7.1|
|APB1<br>(continued)|Bridge APB1|0.1|0.1|0.1|0.1|



120/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 39. Peripheral current consumption in Run mode (continued)**








|Peripheral|Col2|I (Typ)<br>DD|Col4|Col5|Unit|
|---|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**VOS1**|**VOS2**|**VOS3**|**VOS3**|
|APB2|TIM1|5.1|4.8|4.3|µA/MHz|
|APB2|TIM8|5.4|4.9|4.6|4.6|
|APB2|USART1 registers|2.7|2.6|2.5|2.5|
|APB2|USART1 kernel|0.1|0.1|0.1|0.1|
|APB2|USART6 registers|2.6|2.5|2.5|2.5|
|APB2|USART6 kernel|0.1|0.1|0.1|0.1|
|APB2|SPI1 registers|1.8|1.6|1.6|1.6|
|APB2|SPI1 kernel|1|0.8|0.6|0.6|
|APB2|SPI4 registers|1.6|1.5|1.5|1.5|
|APB2|SPI4 kernel|0.5|0.4|0.4|0.4|
|APB2|TIM15|3.1|2.8|2.7|2.7|
|APB2|TIM16|2.4|2.1|2.1|2.1|
|APB2|TIM17|2.2|2|1.9|1.9|
|APB2|SPI5 registers|1.8|1.7|1.7|1.7|
|APB2|SPI5 kernel|0.6|0.5|0.3|0.3|
|APB2|SAI1 registers|1.5|1.4|1.4|1.4|
|APB2|SAI1 kernel|2|1.7|1.5|1.5|
|APB2|SAI2 registers|1.5|1.5|1.3|1.3|
|APB2|SAI2 kernel|2.2|1.9|1.8|1.8|
|APB2|SAI3 registers|1.8|1.6|1.6|1.6|
|APB2|SAI3 kernel|2.5|2.3|2.1|2.1|
|APB2|DFSDM1 registers|6|5.4|5.2|5.2|
|APB2|DFSDM1 kernel|0.9|0.8|0.7|0.7|
|APB2|HRTIM|40|37|35|35|
|APB2|Bridge APB2|0.1|0.1|0.1|0.1|



DS12110 Rev 10 121/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 39. Peripheral current consumption in Run mode (continued)**








|Peripheral|Col2|I (Typ)<br>DD|Col4|Col5|Unit|
|---|---|---|---|---|---|
|**Peripheral**|**Peripheral**|**VOS1**|**VOS2**|**VOS3**|**VOS3**|
|APB4|SYSCFG|1|0.7|0.7|µA/MHz|
|APB4|LPUART1<br>registers|1.1|1.1|1.1|1.1|
|APB4|LPUART1 kernel|2.6|2.4|2.1|2.1|
|APB4|SPI6 registers|1.6|1.5|1.4|1.4|
|APB4|SPI6 kernel|0.2|0.2|0.2|0.2|
|APB4|I2C4 registers|0.1|0.1|0.1|0.1|
|APB4|I2C4 kernel|2.4|2.1|2|2|
|APB4|LPTIM2 registers|0.5|0.5|0.5|0.5|
|APB4|LPTIM2 kernel|2.3|2.1|1.8|1.8|
|APB4|LPTIM3 registers|0.5|0.5|0.5|0.5|
|APB4|LPTIM3 kernel|2|2.1|1.5|1.5|
|APB4|LPTIM4 registers|0.5|0.5|0.5|0.5|
|APB4|LPTIM4 kernel|2|2|1.9|1.9|
|APB4|LPTIM5 registers|0.5|0.5|0.5|0.5|
|APB4|LPTIM5 kernel|2|1.8|1.5|1.5|
|APB4|COMP1/2|0.7|0.5|0.5|0.5|
|APB4|VREFBUF|0.6|0.4|0.4|0.4|
|APB4|RTC|1.2|1.1|1.1|1.1|
|APB4|SAI4 registers|1.6|1.5|1.4|1.4|
|APB4|SAI4 kernel|1.3|1.3|1.2|1.2|
|APB4|Bridge APB4|0.1|0.1|0.1|0.1|



**Table 40. Peripheral current consumption in Stop, Standby and VBAT mode**








|Symbol|Parameter|Conditions|Typ|Unit|
|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**3 V**|**3 V**|
|IDD|RTC+LSE low drive|-|2.32|µA|
|IDD|RTC+LSE medium-<br>low drive|-|2.4|2.4|
|IDD|RTC+LSE medium-<br>high drive|-|2.7|2.7|
|IDD|RTC+LSE High drive|-|3|3|



122/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.7** **Wakeup time from low-power modes**


The wakeup times given in _Table 41_ are measured starting from the wakeup event trigger up
to the first instruction executed by the CPU:


       - For Stop or Sleep modes: the wakeup event is WFE.


       - WKUP (PC1) pin is used to wakeup from Standby, Stop and Sleep modes.


All timings are derived from tests performed under ambient temperature and V DD =3.3 V.


**Table 41. Low-power mode wakeup timings**









|Symbol|Parameter|Conditions|Typ(1)|Max(1)|Unit|
|---|---|---|---|---|---|
|tWUSLEEP<br>(2)|Wakeup from Sleep|-|9|10|CPU<br>clock<br>cycles|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS3, HSI, flash memory in normal mode|4.4|5.6|µs|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS3, HSI, flash memory in low-power<br>mode|12|15|15|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS4, HSI, flash memory in normal mode|15|20|20|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS4, HSI, flash memory in low-power<br>mode|23|28|28|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS5, HSI, flash memory in normal mode|30|71|71|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS5, HSI, flash memory in low-power<br>mode|38|47|47|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS3, CSI, flash memory in normal mode|27|37|37|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS3, CSI, flash memory in low power<br>mode|36|50|50|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS4, CSI, flash memory in normal mode|38|48|48|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS4, CSI, flash memory in low-power<br>mode|47|61|61|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS5, CSI, flash memory in normal mode|52|64|64|
|tWUSTOP<br>(2)|Wakeup from Stop|VOS5, CSI, flash memory in low-power<br>mode|62|77|77|
|tWUSTOP2<br>(2)|Wakeup from Stop,<br>clock kept running|VOS3, HSI, flash memory in normal mode|2.6|3.4|3.4|
|tWUSTOP2<br>(2)|Wakeup from Stop,<br>clock kept running|VOS3, CSI, flash memory in normal mode|26|36|36|
|tWUSTDBY<br>(2)|Wakeup from Standby<br>mode|-|390|500|500|


1. Guaranteed by characterization results.


2. The wakeup times are measured from the wakeup event to the point in which the application code reads the first instruction.


DS12110 Rev 10 123/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.8** **External clock source characteristics**


**High-speed external user clock generated from an external source**


In bypass mode the HSE oscillator is switched off and the input pin is a standard I/O.


The external clock signal has to respect the _Table 60: I/O static characteristics_ . However,
the recommended clock input waveform is shown in _Figure 18_ .


**Table 42. High-speed external user clock characteristics** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|fHSE_ext|User external clock source frequency|4|25|50|MHz|
|VHSEH|Digital OSC_IN input high-level<br>voltage|0.7 VDD|-|VDD|V|
|VHSEL|Digital OSC_IN input low-level voltage|VSS|-|0.3 VDD|0.3 VDD|
|tW(HSE)|OSC_IN high or low time|7|-|-|ns|



1. Guaranteed by design.


**Figure 18. High-speed external clock source AC timing diagram**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||















124/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Low-speed external user clock generated from an external source**


In bypass mode the LSE oscillator is switched off and the input pin is a standard I/O. The
external clock signal has to respect the _Table 60: I/O static characteristics_ . However, the
recommended clock input waveform is shown in _Figure 19_ .


**Table 43. Low-speed external user clock characteristics** **[(1)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fLSE_ext|User external clock source frequency|-|-|32.768|1000|kHz|
|VLSEH|OSC32_IN input pin high level voltage|-|0.7 VDDIOx|-|VDDIOx|V|
|VLSEL|OSC32_IN input pin low level voltage|-|VSS|-|0.3 VDDIOx|0.3 VDDIOx|
|tw(LSEH)<br>tw(LSEL)|OSC32_IN high or low time|-|250|-|-|ns|



1. Guaranteed by design.


_Note:_ _For information on selecting the crystal, refer to the application note AN2867 “Oscillator_
_design guide for STM8AF/AL/S, STM32 MCUs and MPUs” available from the ST website_
_www.st.com._


**Figure 19. Low-speed external clock source AC timing diagram**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||











DS12110 Rev 10 125/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**High-speed external clock generated from a crystal/ceramic resonator**


The high-speed external (HSE) clock can be supplied with a 4 to 48 MHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
characterization results obtained with typical external components specified in _Table 44_ . In
the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).


**Table 44. 4-48 MHz HSE oscillator characteristics** **[(1)]**









|Symbol|Parameter|Operating<br>conditions(2)|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F|Oscillator frequency|-|4|-|48|MHz|
|RF|Feedback resistor|-|-|200|-|kΩ|
|IDD(HSE)|HSE current consumption|During startup(3)|-|-|4|mA|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10pF@4MHz|-|0.35|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 8 MHz|-|0.40|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 16 MHz|-|0.45|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 32 MHz|-|0.65|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 48 MHz|-|0.95|-|-|
|Gmcritmax|Maximum critical crystal gm|Startup|-|-|1.5|mA/V|
|tSU<br>(4)|Start-up time|VDD is stabilized|-|2|-|ms|


1. Guaranteed by design.


2. Resonator characteristics given by the crystal/ceramic resonator manufacturer.


3. This consumption level occurs during the first 2/3 of the t SU(HSE) startup time.

4. t SU(HSE) is the startup time measured from the moment it is enabled (by software) to a stabilized 8 MHz oscillation is
reached. This value is measured for a standard crystal resonator and it can vary significantly with the crystal manufacturer.


For C L1 and C L2, it is recommended to use high-quality external ceramic capacitors,
designed for high-frequency applications, and selected to match the requirements of the
crystal or resonator (see _Figure 20_ ). C L1 and C L2 are usually the same size. The crystal
manufacturer typically specifies a load capacitance which is the series combination of C L1
and C L2 . The PCB and MCU pin capacitance must be included (10 pF can be used as a
rough estimate of the combined pin and board capacitance) when sizing C L1 and C L2 .


_Note:_ _For information on selecting the crystal, refer to the application note AN2867 “Oscillator_
_design guide for STM8AF/AL/S, STM32 MCUs and MPUs” available from the ST website_
_www.st.com._


126/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 20. Typical application with an 8 MHz crystal**










|8 MHz<br>resonator|Col2|Col3|
|---|---|---|
|8 MHz<br>resonator|||


|Col1|Col2|Col3|
|---|---|---|
||RF|Bias<br>controlled<br>gain|
||||



1. R EXT value depends on the crystal characteristics.


**Low-speed external clock generated from a crystal/ceramic resonator**


The low-speed external (LSE) clock can be supplied with a 32.768 kHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
characterization results obtained with typical external components specified in _Table 45_ . In
the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).


**Table 45. Low-speed external user clock characteristics** **[(1)]**









|Symbol|Parameter|Operating conditions(2)|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F|Oscillator frequency|-|-|32.768|-|kHz|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 00,<br>Low drive capability|-|290|-|nA|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 01,<br>Medium Low drive capability|-|390|-|-|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 10,<br>Medium high drive capability|-|550|-|-|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 11,<br>High drive capability|-|900|-|-|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 00,<br>Low drive capability|-|-|0.5|µA/V|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 01,<br>Medium Low drive capability|-|-|0.75|0.75|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 10,<br>Medium high drive capability|-|-|1.7|1.7|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 11,<br>High drive capability|-|-|2.7|2.7|
|tSU<br>(3)|Startup time|VDD is stabilized|-|2|-|s|


1. Guaranteed by design.


DS12110 Rev 10 127/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


2. Refer to the note and caution paragraphs below the table, and to the application note AN2867 “Oscillator design guide for
STM8AL/AF/S, STM32 MCUs and MPUs”.


3. t SU is the startup time measured from the moment it is enabled (by software) to a stabilized 32.768k Hz oscillation is
reached. This value is measured for a standard crystal resonator and it can vary significantly with the crystal manufacturer.


_Note:_ _For information on selecting the crystal, refer to the application note AN2867 “Oscillator_
_design guide for STM8AL/AF/S, STM32 MCUs and MPUs” available from the ST website_
_www.st.com._


**Figure 21. Typical application with a 32.768 kHz crystal**












|Col1|Col2|Col3|
|---|---|---|
|32.768 kHz<br>resonator|||
|32.768 kHz<br>resonator|||


|Col1|Col2|Col3|
|---|---|---|
||RF|Bias<br>controlled<br>gain|
||||







_1._ _An external resistor is not required between OSC32_IN and OSC32_OUT and it is forbidden to add one._


**6.3.9** **Internal clock source characteristics**


The parameters given in _Table 46_ and _Table 49_ are derived from tests performed under
ambient temperature and V DD supply voltage conditions summarized in _Table 24: General_
_operating conditions_ .


**48 MHz high-speed internal RC oscillator (HSI48)**


**Table 46. HSI48 oscillator characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHSI48|HSI48 frequency|VDD=3.3 V, TJ=30 °C|47.5(1)|48|48.5(1)|MHz|
|TRIM(2)|USER trimming step|-|-|0.17|-|%|
|USER TRIM<br>COVERAGE(3)|USER TRIMMING Coverage|± 32 steps|-|±5.45|-|%|
|DuCy(HSI48)(2)|Duty Cycle|-|45|-|55|%|
|ACCHSI48_REL(3)|Accuracy of the HSI48 oscillator over<br>temperature (factory calibrated)|VDD=1.62 to 3.6 V,<br>TJ=-40 to 125 °C|–4.5|-|3.5|%|
|∆VDD(HSI48)(3)|HSI48 oscillator frequency drift with<br>VDD<br>(4)|VDD=3 to 3.6 V|-|0.025|0.05|%|
|∆VDD(HSI48)(3)|HSI48 oscillator frequency drift with<br>VDD<br>(4)|VDD=1.62 V to 3.6 V|-|0.05|0.1|0.1|
|tsu(HSI48)<br>(2)|HSI48 oscillator start-up time|-|-|2.1|3.5|µs|
|IDD(HSI48)<br>(2)|HSI48 oscillator power consumption|-|-|350|400|µA|
|NT jitter|Next transition jitter<br>Accumulated jitter on 28 cycles(5)|-|-|± 0.15|-|ns|
|PT jitter|Paired transition jitter<br>Accumulated jitter on 56 cycles(5)|-|-|± 0.25|-|ns|



128/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


1. Guaranteed by test in production.


2. Guaranteed by design.


3. Guaranteed by characterization.


4. These values are obtained by using the formula:
(Freq(3.6V) - Freq(3.0V)) / Freq(3.0V) or (Freq(3.6V) - Freq(1.62V)) / Freq(1.62V).


5. Jitter measurements are performed without clock source activated in parallel.


**64 MHz high-speed internal RC oscillator (HSI)**


**Table 47. HSI oscillator characteristics** **[(1)]**



















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHSI|HSI frequency|VDD=3.3 V, TJ=30 °C|63.7(2)|64|64.3(2)|MHz|
|TRIM|HSI user trimming step|Trimming is not a multiple<br>of 32|-|0.24|0.32|%|
|TRIM|HSI user trimming step|Trimming is 128, 256 and<br>384|−5.2|−1.8|-|-|
|TRIM|HSI user trimming step|Trimming is 64, 192, 320<br>and 448|−1.4|−0.8|-|-|
|TRIM|HSI user trimming step|Other trimming are a<br>multiple of 32 (not<br>including multiple of 64<br>and 128)|−0.6|−0.25|-|-|
|DuCy(HSI)|Duty Cycle|-|45|-|55|%|
|ΔVDD (HSI)|HSI oscillator frequency drift over<br>VDD(reference is 3.3 V)|VDD=1.62 to 3.6 V|−0.12|-|0.03|%|
|ΔTEMP (HSI)|HSI oscillator frequency drift over<br>temperature (reference is 64 MHz)|TJ=-20 to 105 °C|−1(3)|-|1(3)|%|
|ΔTEMP (HSI)|HSI oscillator frequency drift over<br>temperature (reference is 64 MHz)|TJ=−40 to TJmax °C|−2(3)|-|1(3)||
|tsu(HSI)|HSI oscillator start-up time|-|-|1.4|2|µs|
|tstab(HSI)|HSI oscillator stabilization time|at 1% of target frequency|-|4|8|µs|
|IDD(HSI)|HSI oscillator power consumption|-|-|300|400|µA|


1. Guaranteed by design unless otherwise specified.


2. Guaranteed by test in production.


3. Guaranteed by characterization.


**4 MHz low-power internal RC oscillator (CSI)**


**Table 48. CSI oscillator characteristics** **[(1)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fCSI|CSI frequency|VDD=3.3 V, TJ=30 °C|3.96(2)|4|4.04(2)|MHz|
|TRIM|Trimming step|-|-|0.35|-|%|
|DuCy(CSI)|Duty Cycle|-|45|-|55|%|



DS12110 Rev 10 129/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 48. CSI oscillator characteristics** **[(1)]** **(continued)**







|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|∆TEMP (CSI)|CSI oscillator frequency drift over<br>temperature|TJ = 0 to 85 °C|-|−3.7(3)|4.5(3)|%|
|∆TEMP (CSI)|CSI oscillator frequency drift over<br>temperature|TJ = −40 to 125 °C|-|−11(3)|7.5(3)|7.5(3)|
|DVDD (CSI)|CSI oscillator frequency drift over<br>VDD|VDD= 1.62 to 3.6 V|-|−0.06|0.06|%|
|tsu(CSI)|CSI oscillator startup time|-|-|1|2|µs|
|tstab(CSI)|CSI oscillator stabilization time<br>(to reach ±3% of fCSI)|-|-|4|8|cycle|
|IDD(CSI)|CSI oscillator power consumption|-|-|23|30|µA|


1. Guaranteed by design.


2. Guaranteed by test in production.


3. Guaranteed by characterization.


**Low-speed internal (LSI) RC oscillator**


**Table 49. LSI oscillator characteristics**











|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fLSI<br>(1)|LSI frequency|VDD = 3.3 V, TJ = 25 °C|31.4|32|32.6|kHz|
|fLSI<br>(1)|LSI frequency|TJ = –40 to 105 °C, VDD =<br>1.62 to 3.6 V|29.76|-|33.60|33.60|
|tsu(LSI)<br>(2)|LSI oscillator startup time|-|-|80|130|µs|
|tstab(LSI)<br>(2)|LSI oscillator stabilization<br>time (5% of final value)|-|-|120|170|170|
|IDD(LSI)<br>(2)|LSI oscillator power<br>consumption|-|-|130|280|nA|


1. Guaranteed by characterization results.


2. Guaranteed by design.


**6.3.10** **PLL characteristics**


The parameters given in _Table 50_ are derived from tests performed under temperature and
V DD supply voltage conditions summarized in _Table 24: General operating conditions_ .


**Table 50. PLL characteristics (wide VCO frequency range)** **[(1)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPLL_IN|PLL input clock|-|2|-|16|MHz|
|fPLL_IN|PLL input clock duty cycle|-|10|-|90|%|



130/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 50. PLL characteristics (wide VCO frequency range)** **[(1)]** **(continued)**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|fPLL_P_OUT|PLL multiplier output clock P|VOS1|VOS1|1.5|-|400(2)|MHz|
|fPLL_P_OUT|PLL multiplier output clock P|VOS2|VOS2|1.5|-|300|300|
|fPLL_P_OUT|PLL multiplier output clock P|VOS3|VOS3|1.5|-|200|200|
|fPLL_Q_OUT|PLL multiplier output clock Q/R|VOS1|VOS1|1.5|-|400(2)|400(2)|
|fPLL_Q_OUT|PLL multiplier output clock Q/R|VOS2|VOS2|1.5|-|300|300|
|fPLL_Q_OUT|PLL multiplier output clock Q/R|VOS3|VOS3|1.5|-|200|200|
|fVCO_OUT|PLL VCO output|-|-|192|-|836|836|
|tLOCK|PLL lock time|Normal mode|Normal mode|-|50(3)|150(3)|µs|
|tLOCK|PLL lock time|Sigma-delta mode<br>(CKIN≥ 8 MHz)|Sigma-delta mode<br>(CKIN≥ 8 MHz)|-|58(3)|166(3)|166(3)|
|Jitter|Cycle-to-cycle jitter(4)|VCO = 192 MHz|VCO = 192 MHz|-|134|-|±ps|
|Jitter|Cycle-to-cycle jitter(4)|VCO = 200 MHz|VCO = 200 MHz|-|134|-|-|
|Jitter|Cycle-to-cycle jitter(4)|VCO = 400 MHz|VCO = 400 MHz|-|76|-|-|
|Jitter|Cycle-to-cycle jitter(4)|VCO = 800 MHz|VCO = 800 MHz|-|39|-|-|
|Jitter|Long term jitter|Normal mode|Normal mode|-|±0.7|-|%|
|Jitter|Long term jitter|Sigma-delta mode<br>(CKIN = 16 MHz)|Sigma-delta mode<br>(CKIN = 16 MHz)|-|±0.8|-|-|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>420 MHz|VDDA|-|440|1150|µA|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>420 MHz|VCORE|-|530|-|-|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>150 MHz|VDDA|-|180|500|500|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>150 MHz|VCORE|-|200|-|-|


1. Guaranteed by design unless otherwise specified.









2. This value must be limited to the maximum frequency due to the product limitation (400 MHz for VOS1, 300 MHz for VOS2,
200 MHz for VOS3).


3. Guaranteed by characterization results.


4. Integer mode only.


**Table 51. PLL characteristics (medium VCO frequency range)** **[(1)]**







|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPLL_IN|PLL input clock|-|1|-|2|MHz|
|fPLL_IN|PLL input clock duty cycle|-|10|-|90|%|
|fPLL_OUT|PLL multiplier output clock P, Q,<br>R|VOS1|1.17|-|210|MHz|
|fPLL_OUT|PLL multiplier output clock P, Q,<br>R|VOS2|1.17|-|210|210|
|fPLL_OUT|PLL multiplier output clock P, Q,<br>R|VOS3|1.17|-|200|200|
|fVCO_OUT|PLL VCO output|-|150|-|420|MHz|
|tLOCK|PLL lock time|Normal mode|-|60(2)|100(2)|µs|
|tLOCK|PLL lock time|Sigma-delta mode|forbidden|-|-|µs|


DS12110 Rev 10 131/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 51. PLL characteristics (medium VCO frequency range)** **[(1)]** **(continued)**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>150 MHz|-|145|-|+/-<br>ps|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>300 MHz|-|91|-|-|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>400 MHz|-|64|-|-|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>420 MHz|-|63|-|-|
|Jitter|Period jitter|fPLL_OUT =<br>50 MHz|VCO =<br>150 MHz|-|55|-|+/-<br>ps|
|Jitter|Period jitter|fPLL_OUT =<br>50 MHz|VCO =<br>400 MHz|-|30|-|-|
|Jitter|Long term jitter|Normal mode|VCO =<br>150 MHz|-|-|-|%|
|Jitter|Long term jitter|Normal mode|VCO =<br>300 MHz|-|-|-|-|
|Jitter|Long term jitter|Normal mode|VCO =<br>400 MHz|-|+/-0.3|-|-|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>420MHz|VDD|-|440|1150|µA|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>420MHz|VCORE|-|530|-|-|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>150MHz|VDD|-|180|500|500|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>150MHz|VCORE|-|200|-|-|


1. Guaranteed by design unless otherwise specified.


2. Guaranteed by characterization results.


3. Integer mode only.


**6.3.11** **Memory characteristics**


**Flash memory**







The characteristics are given at T J = –40 to 125 °C unless otherwise specified.


The devices are shipped to customers with the flash memory erased.


**Table 52. Flash memory characteristics**






|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|IDD|Supply current|Write / Erase 8-bit mode|-|6.5|-|mA|
|IDD|Supply current|Write / Erase 16-bit mode|-|11.5|-|-|
|IDD|Supply current|Write / Erase 32-bit mode|-|20|-|-|
|IDD|Supply current|Write / Erase 64-bit mode|-|35|-|-|



132/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 53. Flash memory** **programming**



|Symbol|Parameter|Conditions|Min(1)|Typ|Max(1)|Unit|
|---|---|---|---|---|---|---|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 8|-|290|580(2)|µs|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 16|-|180|360|360|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 32|-|130|260|260|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 64|-|100|200|200|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 8|-|2|4|s|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 16|-|1.8|3.6|3.6|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 32|-|1.1|2.2|2.2|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 64|-|1|2|2|
|tME|Mass erase time|Program/erase parallelism x 8|-|13|26|26|
|tME|Mass erase time|Program/erase parallelism x 16|-|8|16|16|
|tME|Mass erase time|Program/erase parallelism x 32|-|6|12|12|
|tME|Mass erase time|Program/erase parallelism x 64|-|5|10|10|
|Vprog|Programming voltage|Program parallelism x 8|1.62|-|3.6|V|
|Vprog|Programming voltage|Program parallelism x 16|Program parallelism x 16|Program parallelism x 16|Program parallelism x 16|Program parallelism x 16|
|Vprog|Programming voltage|Program parallelism x 32|Program parallelism x 32|Program parallelism x 32|Program parallelism x 32|Program parallelism x 32|
|Vprog|Programming voltage|Program parallelism x 64|1.8|-|3.6|3.6|


1. Guaranteed by characterization results.





2. The maximum programming time is measured after 10K erase operations.

|Col1|Table|54. Flash memory endurance and data|retention|Col5|
|---|---|---|---|---|
|**Symbol**|**Parameter**|** Conditions**|**Value**|**Unit**|
|**Symbol**|**Parameter**|** Conditions**|**Min(1)**|**Min(1)**|
|NEND|Endurance|TJ = –40 to +125 °C (6 suffix versions)|10|kcycles|
|tRET|Data retention|1 kcycle at TA = 85 °C|30|Years|
|tRET|Data retention|10 kcycles at TA = 55 °C|20|20|



1. Guaranteed by characterization results.


DS12110 Rev 10 133/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.12** **EMC characteristics**


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


The test results are given in _Table 55_ . They are based on the EMS levels and classes
defined in application note AN1709.


**Table 55. EMS characteristics**








|Symbol|Parameter|Conditions|Level/<br>Class|
|---|---|---|---|
|VFESD|Voltage limits to be applied on any I/O pin to induce<br>a functional disturbance|VDD= 3.3 V, TA = +25 °C,<br>UFBGA240, frcc_c_ck =<br>400 MHz, conforms to<br>IEC 61000-4-2|3B|
|VFTB|Fast transient voltage burst limits to be applied<br>through 100 pF on VDD and VSSpins to induce a<br>functional disturbance|Fast transient voltage burst limits to be applied<br>through 100 pF on VDD and VSSpins to induce a<br>functional disturbance|4B|



As a consequence, it is recommended to add a serial resistor (1 kΏ) located as close as
possible to the MCU to the pins exposed to noise (connected to tracks longer than 50 mm
on PCB).


**Designing hardened software to avoid noise problems**


EMC characterization and optimization are performed at component level with a typical
application environment and simplified MCU software. It should be noted that good EMC
performance is highly dependent on the user application and the software in particular.


Therefore it is recommended that the user applies EMC software optimization and
prequalification tests in relation with the EMC level requested for his application.


**Software recommendations**


The software flowchart must include the management of runaway conditions such as:


      - Corrupted program counter


      - Unexpected reset


      - Critical Data corruption (control registers...)


134/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Prequalification trials**


Most of the common failures (unexpected reset and program counter corruption) can be
reproduced by manually forcing a low state on the NRST pin or the Oscillator pins for 1
second.


To complete these trials, ESD stress can be applied directly on the device, over the range of
specification values. When unexpected behavior is detected, the software can be hardened
to prevent unrecoverable errors occurring (see application note AN1015).


**Electromagnetic Interference (EMI)**


The electromagnetic field emitted by the device are monitored while a simple application,
executing EEMBC code, is running. This emission test is compliant with SAE IEC61967-2
standard which specifies the test board and the pin loading.


**Table 56. EMI characteristics for f** **HSE** **= 8 MHz and f** **CPU** **= 400 MHz**











|Symbol|Parameter|Conditions|Monitored<br>frequency band|Max vs.<br>[f /f ]<br>HSE CPU|Unit|
|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Monitored**<br>**frequency band**|**8/400 MHz**|**8/400 MHz**|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240 package,<br>compliant with IEC61967-2|0.1 MHz to<br>30 MHz|6|dBµV|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240 package,<br>compliant with IEC61967-2|30 MHz to<br>130 MHz|5|5|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240 package,<br>compliant with IEC61967-2|130 MHz to 1 GHz|13|13|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240 package,<br>compliant with IEC61967-2|1 GHz to 2 GHz|7|7|
|SEMI|Level(2)|Level(2)|0.1 MHz to 2 GHz|2.5|-|


1. Refer to AN1709 “EMI radiated test” chapter.


2. Refer to AN1709 “EMI level classification” chapter.


DS12110 Rev 10 135/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.13** **Absolute maximum ratings (electrical sensitivity)**


Based on three different tests (ESD, LU) using specific measurement methods, the device is
stressed in order to determine its performance in terms of electrical sensitivity.


**Electrostatic discharge (ESD)**


Electrostatic discharges (a positive then a negative pulse) are applied to the pins of each
sample according to each pin combination. This test conforms to the ANSI/ESDA/JEDEC
JS-001 and ANSI/ESDA/JEDEC JS-002 standards.


**Table 57. ESD absolute maximum ratings**



|Symbol|Ratings|Conditions|Packages|Class|Maximum<br>value(1)|Unit|
|---|---|---|---|---|---|---|
|VESD(HBM)|Electrostatic discharge<br>voltage (human body<br>model)|TA = +25 °C conforming to<br>ANSI/ESDA/JEDEC JS-<br>001|All|1C|1000|V|
|VESD(CDM)|Electrostatic discharge<br>voltage (charge device<br>model)|TA = +25 °C conforming to<br>ANSI/ESDA/JEDEC JS-<br>002|All|C1|250|250|


1. Guaranteed by characterization results.


**Static latchup**







Two complementary static tests are required on six parts to assess the latchup
performance:


       - A supply overvoltage is applied to each power supply pin


       - A current injection is applied to each input, output and configurable I/O pin


These tests are compliant with JESD78 IC latchup standard.


**Table 58. Electrical sensitivities**

|Symbol|Parameter|Conditions|Class|
|---|---|---|---|
|LU|Static latchup class|TA = +25 °C conforming to JESD78|II level A|



**6.3.14** **I/O current injection characteristics**


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


136/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


of –5 µA/+0 µA range), or other functional failure (for example reset, oscillator frequency
deviation).


The following tables are the compilation of the SIC1/SIC2 and functional ESD results.


Negative induced A negative induced leakage current is caused by negative injection and
positive induced leakage current by positive injection.


**Table 59. I/O current injection susceptibility** **[(1)]**










|Symbol|Description|Functional susceptibility|Col4|Unit|
|---|---|---|---|---|
|**Symbol**|**Description**|**Negative**<br>**injection**|**Positive**<br>**injection**|**Positive**<br>**injection**|
|IINJ|PA7, PC5, PG1, PB14, PJ7, PA11, PA12, PA13, PA14, PA15,<br>PJ12, PB4|5|0|mA|
|IINJ|PA2, PH2, PH3, PE8, PA6, PA7, PC4, PE7, PE10, PE11|0|NA|NA|
|IINJ|PA0, PA_C, PA1, PA1_C, PC2, PC2_C, PC3, PC3_C, PA4,<br>PA5, PH4, PH5, BOOT0|0|0|0|
|IINJ|All other I/Os|5|NA|NA|



1. Guaranteed by characterization .


**6.3.15** **I/O port characteristics**


**General input/output characteristics**


Unless otherwise specified, the parameters given in _Table 60: I/O static characteristics_ are
derived from tests performed under the conditions summarized in _Table 24: General_
_operating conditions_ . All I/Os are CMOS and TTL compliant (except for BOOT0).


For information on GPIO configuration, refer to the application note AN4899 “STM32 GPIO
configuration for hardware settings and low-power consumption” available from the ST
website www.st.com.


**Table 60. I/O static characteristics**











|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VIL|I/O input low level voltage except<br>BOOT0|1.62 V<VDDIOx<3.6 V|-|-|0.3VDD<br>(1)|V|
|VIL|I/O input low level voltage except<br>BOOT0|I/O input low level voltage except<br>BOOT0|-|-|0.4VDD−<br>0.1(2)|0.4VDD−<br>0.1(2)|
|VIL|BOOT0 I/O input low level voltage|BOOT0 I/O input low level voltage|-|-|0.19VDD+<br>0.1(2)|0.19VDD+<br>0.1(2)|
|VIH|I/O input high level voltage except<br>BOOT0|1.62 V<VDDIOx<3.6 V|0.7VDD<br>(1)|-|-|V|
|VIH|I/O input high level voltage except<br>BOOT0(3)|I/O input high level voltage except<br>BOOT0(3)|0.47VDD+<br>0.25(2)|-|-|-|
|VIH|BOOT0 I/O input high level<br>voltage(3)|BOOT0 I/O input high level<br>voltage(3)|0.17VDD+<br>0.6(2)|-|-|-|


DS12110 Rev 10 137/357







320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 60. I/O static characteristics (continued)**













|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VHYS<br>(2)|TT_xx, FT_xxx and NRST I/O<br>input hysteresis|1.62 V< VDDIOx <3.6 V|-|250|-|mV|
|VHYS<br>(2)|BOOT0 I/O input hysteresis|BOOT0 I/O input hysteresis|-|200|-|-|
|Ilkg<br>(4)|FT_xx Input leakage current(2)|0< VIN≤ Max(VDDXXX)(9)|-|-|+/-250|nA|
|Ilkg<br>(4)|FT_xx Input leakage current(2)|Max(VDDXXX) < VIN≤ 5.5 V<br>(5)(6)(9)|-|-|1500|1500|
|Ilkg<br>(4)|FT_u IO|0< VIN≤ Max(VDDXXX)(9)|-|-|+/- 350|+/- 350|
|Ilkg<br>(4)|FT_u IO|Max(VDDXXX) < VIN≤ 5.5 V<br>(5)(6)(9)|-|-|5000(7)|5000(7)|
|Ilkg<br>(4)|TT_xx Input leakage current|0< VIN≤ Max(VDDXXX) (9)|-|-|+/-250|+/-250|
|Ilkg<br>(4)|VPP (BOOT0 alternate function)|0< VIN≤ VDDIOX|-|-|15|15|
|Ilkg<br>(4)|VPP (BOOT0 alternate function)|VDDIOX < VIN≤ 9 V|-|-|35|35|
|RPU|Weak pull-up equivalent<br>resistor(8)|VIN=VSS|30|40|50|kΩ|
|RPD|Weak pull-down equivalent<br>resistor(8)|VIN=VDD<br>(9)|30|40|50|50|
|CIO|I/O pin capacitance|-|-|5|-|pF|


1. Compliant with CMOS requirement.


2. Guaranteed by design.


3. V DDIOx represents V DDIO1, V DDIO2 or V DDIO3 . V DDIOx = V DD .


4. This parameter represents the pad leakage of the I/O itself. The total product pad leakage is provided by the following
formula: I Total_Ikg_max = 10 μA + [number of I/Os where V IN is applied on the pad] ₓ I lkg(Max) .


5. All FT_xx IO except FT_lu, FT_u and PC3.


6. V IN must be less than Max(VDDXXX) + 3.6 V.


7. To sustain a voltage higher than MIN(V DD, V DDA, V DD33USB ) +0.3 V, the internal pull-up and pull-down resistors must be
disabled.


8. The pull-up and pull-down resistors are designed with a true resistance in series with a switchable PMOS/NMOS. This
PMOS/NMOS contribution to the series resistance is minimal (~10% order).


9. Max(VDDXXX) is the maximum value of all the I/O supplies.


All I/Os are CMOS and TTL compliant (no software configuration required). Their
characteristics cover more than the strict CMOS-technology or TTL parameters. The
coverage of these requirements for FT I/Os is shown in _Figure 22_ .


138/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 22. V** **IL** **/V** **IH** **for all I/Os except BOOT0**







|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||||||.7VDD||TLL re|quirement:|VIHmin = 2 V|
||||CMOS req<br>|uirement: V<br> on simu|IHmin=0<br>lation VIHmin|=0.47VDD+0|.25|||
||||Ba|sed<br>|n simulation|.3<br><br> VILmax=0.4V|VDD <br><br>DD-0.1|||
|||||CMOS<br>Based|requiremen<br>|t: VILmax=0<br>||||
|||||CMOS<br>Based|requiremen<br>||TLL req<br>|uirement: VI|Lmin = 0.8 V|
|||||||||||


**Output driving current**





The GPIOs (general purpose input/outputs) can sink or source up to ± 8 mA, and sink or
source up to ± 20 mA (with a relaxed V OL /V OH ).


In the user application, the number of I/O pins which can drive current must be limited to
respect the absolute maximum rating specified in _Section 6.2_ . In particular:


- The sum of the currents sourced by all the I/Os on V DD, plus the maximum Run
consumption of the MCU sourced on V DD, cannot exceed the absolute maximum rating
ΣI VDD (see _Table 22_ ).


- The sum of the currents sunk by all the I/Os on V SS plus the maximum Run
consumption of the MCU sunk on V SS cannot exceed the absolute maximum rating
ΣI VSS (see _Table 22_ ).


DS12110 Rev 10 139/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Output voltage levels**


Unless otherwise specified, the parameters given in _Table 61_ are derived from tests
performed under ambient temperature and V DD supply voltage conditions summarized in
_Table 24: General operating conditions_ . All I/Os are CMOS and TTL compliant.


**Table 61. Output voltage characteristics for all I/Os except PC13, PC14, PC15 and PI8** **[(1)]**










|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|VOL|Output low level voltage|CMOS port(2)<br>IIO=8 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|V|
|VOH|Output high level voltage|CMOS port(2)<br>IIO=-8 mA<br>2.7 V≤ VDD ≤3.6 V|VDD−0.4|-|-|
|VOL<br>(3)|Output low level voltage|TTL port(2)<br>IIO=8 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH<br>(3)|Output high level voltage|TTL port(2)<br>IIO=-8 mA<br>2.7 V≤ VDD ≤3.6 V|2.4|-|-|
|VOL<br>(3)|Output low level voltage|IIO=20 mA<br>2.7 V≤ VDD ≤3.6 V|-|1.3|1.3|
|VOH<br>(3)|Output high level voltage|IIO=-20 mA<br>2.7 V≤ VDD ≤3.6 V|VDD−1.3|-|-|
|VOL<br>(3)|Output low level voltage|IIO=4 mA<br>1.62 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH (3)|Output high level voltage|IIO=-4 mA<br>1.62 V≤VDD<3.6 V|VDD−-0.4|-|-|
|VOLFM+<br>(3)|Output low level voltage for an FTf<br>I/O pin in FM+ mode|IIO= 20 mA<br>2.3 V≤ VDD≤3.6 V|-|0.4|0.4|
|VOLFM+<br>(3)|Output low level voltage for an FTf<br>I/O pin in FM+ mode|IIO= 10 mA<br>1.62 V≤ VDD ≤3.6 V|-|0.4|0.4|



1. The IIO current sourced or sunk by the device must always respect the absolute maximum rating specified in _Table 21:_
_Voltage characteristics_, and the sum of the currents sourced or sunk by all the I/Os (I/O ports and control pins) must always
respect the absolute maximum ratings ΣIIO.


2. TTL and CMOS outputs are compatible with JEDEC standards JESD36 and JESD52.


3. Guaranteed by design.


140/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 62. Output voltage characteristics for PC13, PC14, PC15 and PI8** **(1)**







|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|VOL|Output low level voltage|CMOS port(2)<br>IIO=3 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|V|
|VOH|Output high level voltage|CMOS port(2)<br>IIO=-3 mA<br>2.7 V≤ VDD ≤3.6 V|VDD−0.4|-|-|
|VOL<br>(3)|Output low level voltage|TTL port(2)<br>IIO=3 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH<br>(3)|Output high level voltage|TTL port(2)<br>IIO=-3 mA<br>2.7 V≤ VDD ≤3.6 V|2.4|-|-|
|VOL<br>(3)|Output low level voltage|IIO=1.5 mA<br>1.62 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH<br>(3)|Output high level voltage|IIO=-1.5 mA<br>1.62 V≤ VDD ≤3.6 V|VDD−0.4|-|-|


1. The IIO current sourced or sunk by the device must always respect the absolute maximum rating specified in _Table 21:_
_Voltage characteristics_, and the sum of the currents sourced or sunk by all the I/Os (I/O ports and control pins) must always
respect the absolute maximum ratings ΣIIO.


2. TTL and CMOS outputs are compatible with JEDEC standards JESD36 and JESD52.


3. Guaranteed by design.


DS12110 Rev 10 141/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Output buffer timing characteristics (HSLV option disabled)**


The HSLV bit of SYSCFG_CCCSR register can be used to optimize the I/O speed when the
product voltage is below 2.5 V.


**Table 63. Output timing characteristics (HSLV OFF)** **[(1)(2)]**










|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|00|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|12|MHz|
|00|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|3|3|
|00|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V|-|12|12|
|00|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|3|3|
|00|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V|-|16|16|
|00|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|4|4|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|16.6|ns|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|33.3|33.3|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V|-|13.3|13.3|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|25|25|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V|-|10|10|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|20|20|
|01|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|60|MHz|
|01|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|15|15|
|01|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V|-|80|80|
|01|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|15|15|
|01|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V|-|110|110|
|01|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|20|20|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|5.2|ns|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|10|10|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V|-|4.2|4.2|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|7.5|7.5|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V|-|2.8|2.8|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|5.2|5.2|



142/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 63. Output timing characteristics (HSLV OFF)** **[(1)(2)]** **(continued)**










|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|10|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|85|MHz|
|10|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|35|35|
|10|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|110|110|
|10|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|40|40|
|10|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|166|166|
|10|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|85|85|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|3.8|ns|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|6.9|6.9|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|2.8|2.8|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|5.2|5.2|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|1.8|1.8|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|3.3|3.3|
|11|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|100|MHz|
|11|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|50|50|
|11|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|133|133|
|11|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|66|66|
|11|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|220|220|
|11|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|100|100|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|3.3|ns|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|6.6|6.6|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|2.4|2.4|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|4.5|4.5|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|1.5|1.5|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|2.7|2.7|



1. Guaranteed by design.


2. The frequency of the GPIOs that can be supplied in V BAT mode (PC13, PC14, PC15 and PI8) is limited to 2 MHz


3. The maximum frequency is defined with the following conditions:
(t r +t f ) ≤ 2/3 T
Skew ≤ 1/20 T
45%<Duty cycle<55%


4. The fall and rise times are defined between 90% and 10% and between 10% and 90% of the output waveform, respectively.


5. Compensation system enabled.


DS12110 Rev 10 143/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Output buffer timing characteristics (HSLV option enabled)**


**Table 64. Output timing characteristics (HSLV ON)** **[(1)]**








|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|00|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|10|MHz|
|00|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|10|10|
|00|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|10|10|
|00|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|11|ns|
|00|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|9|9|
|00|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|6.6|6.6|
|01|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|50|MHz|
|01|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|58|58|
|01|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|66|66|
|01|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|6.6|ns|
|01|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|4.8|4.8|
|01|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|3|3|
|10|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|55|MHz|
|10|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|80|80|
|10|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|133|133|
|10|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|5.8|ns|
|10|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|4|4|
|10|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|2.4|2.4|
|11|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|60|MHz|
|11|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|90|90|
|11|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|175|175|
|11|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|5.3|ns|
|11|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|3.6|3.6|
|11|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|1.9|1.9|



1. Guaranteed by design.


2. The maximum frequency is defined with the following conditions:
(t r +t f ) ≤ 2/3 T
Skew ≤ 1/20 T
45%<Duty cycle<55%


3. The fall and rise times are defined between 90% and 10% and between 10% and 90% of the output waveform, respectively.


4. Compensation system enabled.


144/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.16** **NRST pin characteristics**


The NRST pin input driver uses CMOS technology. It is connected to a permanent pull-up
resistor, R PU (see _Table 60: I/O static characteristics_ ).


Unless otherwise specified, the parameters given in _Table 65_ are derived from tests
performed under the ambient temperature and V DD supply voltage conditions summarized
in _Table 24: General operating conditions_ .


**Table 65. NRST pin characteristics**












|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|RPU<br>(2)|Weak pull-up equivalent<br>resistor(1)|VIN= VSS|30|40|50|㏀|
|VF(NRST)<br>(2)|NRST Input filtered pulse|1.71 V < VDD < 3.6 V|-|-|50|ns|
|VNF(NRST)<br>(2)|NRST Input not filtered pulse|1.71 V < VDD < 3.6 V|300|-|-|-|
|VNF(NRST)<br>(2)|NRST Input not filtered pulse|1.62 V < VDD < 3.6 V|1000|-|-|-|



1. The pull-up is designed with a true resistance in series with a switchable PMOS. This PMOS contribution
to the series resistance must be minimum (~10% order) .


2. Guaranteed by design.


**Figure 23. Recommended NRST pin protection**













1. The reset network protects the device against parasitic resets.


2. The user must ensure that the level on the NRST pin can go below the V IL(NRST) max level specified in
_Table 60_ . Otherwise the reset is not taken into account by the device.


DS12110 Rev 10 145/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.17** **FMC characteristics**


Unless otherwise specified, the parameters given in _Table 66_ to _Table 79_ for the FMC
interface are derived from tests performed under the ambient temperature, f rcc_c_ck
frequency and V DD supply voltage conditions summarized in _Table 24: General operating_
_conditions_, with the following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Measurement points are done at CMOS levels: 0.5V DD


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output
characteristics.


**Asynchronous waveforms and timings**


_Figure 24_ through _Figure 27_ represent asynchronous waveforms and _Table 66_ through
_Table 73_ provide the corresponding timings. The results shown in these tables are obtained
with the following FMC configuration:


      - AddressSetupTime = 0x1


      - AddressHoldTime = 0x1


      - DataSetupTime = 0x1 (except for asynchronous NWAIT mode, DataSetupTime = 0x5)


      - BusTurnAroundDuration = 0x0


      - Capcitive load C L = 30 pF


In all timing tables, the T KERCK is the f mc_ker_ck clock period.


146/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 24. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms**



|tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||


1. Mode 2/B, C and D only. In Mode 1, FMC_NADV is not used.













DS12110 Rev 10 147/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 66. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|2Tfmc_ker_ck− 1|2 Tfmc_ker_ck+1|ns|
|tv(NOE_NE)|FMC_NEx low to FMC_NOE low|0|0.5|0.5|
|tw(NOE)|FMC_NOE low time|2Tfmc_ker_ck− 1|2Tfmc_ker_ck+ 1|2Tfmc_ker_ck+ 1|
|th(NE_NOE)|FMC_NOE high to FMC_NE high hold time|0|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|0.5|0.5|
|th(A_NOE)|Address hold time after FMC_NOE high|0|-|-|
|tv(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5|0.5|
|th(BL_NOE)|FMC_BL hold time after FMC_NOE high|0|-|-|
|tsu(Data_NE)|Data to FMC_NEx high setup time|11|-|-|
|tsu(Data_NOE)|Data to FMC_NOEx high setup time|11|-|-|
|th(Data_NOE)|Data hold time after FMC_NOE high|0|-|-|
|th(Data_NE)|Data hold time after FMC_NEx high|0|-|-|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|-|0|0|
|tw(NADV)|FMC_NADV low time|-|Tfmc_ker_ck + 1|Tfmc_ker_ck + 1|


1. Guaranteed by characterization results.


**Table 67. Asynchronous non-multiplexed SRAM/PSRAM/NOR read - NWAIT timings** **[(1)(2)]**





|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|7Tfmc_ker_ck+1|7Tfmc_ker_ck+1|ns|
|tw(NOE)|FMC_NWE low time|5Tfmc_ker_ck−1|5Tfmc_ker_ck +1|5Tfmc_ker_ck +1|
|tw(NWAIT)|FMC_NWAIT low time|Tfmc_ker_ck−0.5|||
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|4Tfmc_ker_ck+11|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|3Tfmc_ker_ck+11.5|-|-|


1. Guaranteed by characterization results.


2. N WAIT pulse width is equal to 1 AHB cycle.


148/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 25. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms**



















1. Mode 2/B, C and D only. In Mode 1, FMC_NADV is not used.


**Table 68. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|3Tfmc_ker_ck −1|3Tfmc_ker_ck|ns|
|tv(NWE_NE)|FMC_NEx low to FMC_NWE low|Tfmc_ker_ck|Tfmc_ker_ck+ 1|Tfmc_ker_ck+ 1|
|tw(NWE)|FMC_NWE low time|Tfmc_ker_ck −0.5|Tfmc_ker_ck+ 0.5|Tfmc_ker_ck+ 0.5|
|th(NE_NWE)|FMC_NWE high to FMC_NE high hold time|Tfmc_ker_ck|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|2|2|
|th(A_NWE)|Address hold time after FMC_NWE high|Tfmc_ker_ck −0.5|-|-|
|tv(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5|0.5|
|th(BL_NWE)|FMC_BL hold time after FMC_NWE high|Tfmc_ker_ck −0.5|-|-|
|tv(Data_NE)|Data to FMC_NEx low to Data valid|-|Tfmc_ker_ck+ 2.5|Tfmc_ker_ck+ 2.5|
|th(Data_NWE)|Data hold time after FMC_NWE high|Tfmc_ker_ck+0.5|-|-|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|-|0|0|
|tw(NADV)|FMC_NADV low time|-|Tfmc_ker_ck+ 1|Tfmc_ker_ck+ 1|


1. Guaranteed by characterization results.





DS12110 Rev 10 149/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 69. Asynchronous non-multiplexed SRAM/PSRAM/NOR write - NWAIT timings** **[(1)(2)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|8Tfmc_ker_ck −1|8Tfmc_ker_ck+ 1|ns|
|tw(NWE)|FMC_NWE low time|6Tfmc_ker_ck −1.5|6Tfmc_ker_ck+ 0.5|6Tfmc_ker_ck+ 0.5|
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|5Tfmc_ker_ck+ 13|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|4Tfmc_ker_ck+ 13|-|-|



1. Guaranteed by characterization results.


2. N WAIT pulse width is equal to 1 AHB cycle.


**Figure 26. Asynchronous multiplexed PSRAM/NOR read waveforms**






|tv(NOE_NE) th(NE_NOE)<br>tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||





















150/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 70. Asynchronous multiplexed PSRAM/NOR read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|3Tfmc_ker_ck −1|3Tfmc_ker_ck+ 1|ns|
|tv(NOE_NE)|FMC_NEx low to FMC_NOE low|2Tfmc_ker_ck|2Tfmc_ker_ck+ 0.5|2Tfmc_ker_ck+ 0.5|
|ttw(NOE)|FMC_NOE low time|Tfmc_ker_ck −1|Tfmc_ker_ck+ 1|Tfmc_ker_ck+ 1|
|th(NE_NOE)|FMC_NOE high to FMC_NE high hold time|0|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|0.5|0.5|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|0|0.5|0.5|
|tw(NADV)|FMC_NADV low time|Tfmc_ker_ck −0.5|Tfmc_ker_ck+1|Tfmc_ker_ck+1|
|th(AD_NADV)|FMC_AD(address) valid hold time after<br>FMC_NADV high|Tfmc_ker_ck+ 0.5|-|-|
|th(A_NOE)|Address hold time after FMC_NOE high|Tfmc_ker_ck −0.5|-|-|
|th(BL_NOE)|FMC_BL time after FMC_NOE high|0|-|-|
|tv(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5|0.5|
|tsu(Data_NE)|Data to FMC_NEx high setup time|Tfmc_ker_ck −2|-|-|
|tsu(Data_NOE)|Data to FMC_NOE high setup time|Tfmc_ker_ck −2|-|-|
|th(Data_NE)|Data hold time after FMC_NEx high|0|-|-|
|th(Data_NOE)|Data hold time after FMC_NOE high|0|-|-|


1. Guaranteed by characterization results.


**Table 71. Asynchronous multiplexed PSRAM/NOR read-NWAIT timings** **[(1)]**





|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|8Tfmc_ker_ck −1|8Tfmc_ker_ck|ns|
|tw(NOE)|FMC_NWE low time|5Tfmc_ker_ck −1.5|5Tfmc_ker_ck + 0.5|5Tfmc_ker_ck + 0.5|
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|5Tfmc_ker_ck + 3|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT<br>invalid|4Tfmc_ker_ck|-|-|


1. Guaranteed by characterization results.


DS12110 Rev 10 151/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 27. Asynchronous multiplexed PSRAM/NOR write waveforms**





























**Table 72. Asynchronous multiplexed PSRAM/NOR write timings** **[(1)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|4Tfmc_ker_c −1|4Tfmc_ker_ck|ns|
|tv(NWE_NE)|FMC_NEx low to FMC_NWE low|Tfmc_ker_c −1|Tfmc_ker_ck+ 0.5|Tfmc_ker_ck+ 0.5|
|tw(NWE)|FMC_NWE low time|2Tfmc_ker_ck− 0.5|2Tfmc_ker_ck+ 0.5|2Tfmc_ker_ck+ 0.5|
|th(NE_NWE)|FMC_NWE high to FMC_NE high hold time|Tfmc_ker_ck− 0.5|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|0|0|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|0|0.5|0.5|
|tw(NADV)|FMC_NADV low time|Tfmc_ker_ck|Tfmc_ker_ck+ 1|Tfmc_ker_ck+ 1|
|th(AD_NADV)|FMC_AD(address) valid hold time after FMC_NADV high|Tfmc_ker_ck+0.5|-|-|
|th(A_NWE)|Address hold time after FMC_NWE high|Tfmc_ker_ck+0.5|-|-|
|th(BL_NWE)|FMC_BL hold time after FMC_NWE high|Tfmc_ker_ck −0.5|-|-|
|tv(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5|0.5|
|tv(Data_NADV)|FMC_NADV high to Data valid|-|Tfmc_ker_ck + 2|Tfmc_ker_ck + 2|
|th(Data_NWE)|Data hold time after FMC_NWE high|Tfmc_ker_ck+0.5|-|-|


1. Guaranteed by characterization results.


152/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 73. Asynchronous multiplexed PSRAM/NOR write-NWAIT timings** **[(1)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|9Tfmc_ker_ck– 1|9Tfmc_ker_ck|ns|
|tw(NWE)|FMC_NWE low time|7Tfmc_ker_ck– 0.5|7Tfmc_ker_ck+ 0.5|7Tfmc_ker_ck+ 0.5|
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|6Tfmc_ker_ck+ 3|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|4Tfmc_ker_ck|-|-|



1. Guaranteed by characterization results.


**Synchronous waveforms and timings**


_Figure 28_ through _Figure 31_ represent synchronous waveforms and _Table 74_ through
_Table 77_ provide the corresponding timings. The results shown in these tables are obtained
with the following FMC configuration:


      - BurstAccessMode = FMC_BurstAccessMode_Enable


      - MemoryType = FMC_MemoryType_CRAM


      - WriteBurst = FMC_WriteBurst_Enable


      - CLKDivision = 1


      - DataLatency = 1 for NOR flash; DataLatency = 0 for PSRAM


In all the timing tables, the T fmc_ker_ck is the f mc_ker_ck clock period, with the following
FMC_CLK maximum values:


      - For 2.7 V<V DD <3.6 V, FMC_CLK =100 MHz at 20 pF


      - For 1.8 V<V DD <1.9 V, FMC_CLK =100 MHz at 20 pF


      - For 1.62 V<V DD <1.8 V, FMC_CLK =100 MHz at 15 pF


DS12110 Rev 10 153/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 28. Synchronous multiplexed NOR/PSRAM read timings**


























|td(CL<br>td(CL|Da<br>KL-NExL)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|td(CL<br>td(CL|Da<br>KL-NExL)|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|
|td(CL<br>td(CL|KL-AV)<br>td(CL|KL-NADVH)|||||
|td(CL<br>td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)|KH-AIV)|
|td(CL<br>td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)||
|td(CL<br>td(CL|||||||
|td(CL<br>td(CL|||OEL)|td(CLKH|-NOEH)|-NOEH)|
|AD<br>td(CLK|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|
|AD<br>td(CLK|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|2<br>th(CL<br>ITV)|2<br>th(CL<br>ITV)|
|AD<br>td(CLK|L-ADIV~~)~~<br>tsu(A||||||
|AD<br>td(CLK|[15:0]||||||
|AD<br>td(CLK|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|
||||||||
||||||||
||||||||


|Col1|LKH)|
|---|---|
|TV-C|TV-C|
|||



154/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 74. Synchronous multiplexed NOR/PSRAM read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FMC_CLK period|2Tfmc_ker_ck − 1|-|ns|
|td(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|1|1|
|td(CLKH_NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)|Tfmc_ker_ck+ 0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|1.|1.|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)|-|2.5|2.5|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NOEL)|FMC_CLK low to FMC_NOE low|-|1.5|1.5|
|td(CLKH-NOEH)|FMC_CLK high to FMC_NOE high|Tfmc_ker_ck −0.5|-|-|
|td(CLKL-ADV)|FMC_CLK low to FMC_AD[15:0] valid|-|3|3|
|td(CLKL-ADIV)|FMC_CLK low to FMC_AD[15:0] invalid|0|-|-|
|tsu(ADV-CLKH)|FMC_A/D[15:0] valid data before FMC_CLK high|3|-|-|
|th(CLKH-ADV)|FMC_A/D[15:0] valid data after FMC_CLK high|0|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|3|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|1|-|-|


1. Guaranteed by characterization results.





DS12110 Rev 10 155/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 29. Synchronous multiplexed PSRAM write timings**
























|td(CL<br>td(CL<br>td(CL<br>td(CLK<br>AD|Da<br>KL-NExL)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|Da<br>KL-NExL)|Da<br>KL-NExL)|Da<br>KL-NExL)|Da<br>KL-NExL)|Da<br>KL-NExL)|CLK|CLK|CLK|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|Da<br>KL-NExL)|ta latency|= 0|= 0|= 0|= 0|= 0|= 0|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-AV)<br>td(CL|KL-NADVH|)|)|||||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-AV)<br>td(CL||||t|d(CL|KH-AIV)|KH-AIV)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|||||||||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||td(C|LKH|-NWEH)|-NWEH)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||td(C|LKH|-NWEH)||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||d(CLKL-Data~~)~~|LKH<br>-NW|D2<br>-NBLH)<br>AITV)|D2<br>-NBLH)<br>AITV)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||D1|D1|D1|D1|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||td(C<br>th(CLKH|td(C<br>th(CLKH|td(C<br>th(CLKH|td(C<br>th(CLKH|
||||||||||
||||||||||





156/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 75. Synchronous multiplexed PSRAM write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FMC_CLK period|2Tfmc_ker_ck −1|-|ns|
|td(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|1|1|
|td(CLKH-NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)|Tfmc_ker_ck+ 0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|1.5|1.5|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)|-|2|2|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NWEL)|FMC_CLK low to FMC_NWE low|-|1.5|1.5|
|t(CLKH-NWEH)|FMC_CLK high to FMC_NWE high|Tfmc_ker_ck + 0.5|-|-|
|td(CLKL-ADV)|FMC_CLK low to FMC_AD[15:0] valid|-|2.5|2.5|
|td(CLKL-ADIV)|FMC_CLK low to FMC_AD[15:0] invalid|0|-|-|
|td(CLKL-DATA)|FMC_A/D[15:0] valid data after FMC_CLK low|-|2.5|2.5|
|td(CLKL-NBLL)|FMC_CLK low to FMC_NBL low|-|2|2|
|td(CLKH-NBLH)|FMC_CLK high to FMC_NBL high|Tfmc_ker_ck+ 0.5|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|2|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|2|-|-|


1. Guaranteed by characterization results.





DS12110 Rev 10 157/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 30. Synchronous non-multiplexed NOR/PSRAM read timings**






|td(CL|Da|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|td(CL|Da|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|
|td(CL|KL-AV)<br>td(CL|KL-NADVH)||||
|td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)|
|td(CL||||||
|td(CL|||OEL)|td(CLK|H-NOEH~~)~~|
||tsu(|tsu(|tsu(|tsu(|tsu(|
||tsu(|tsu(|tsu(|tsu(|2<br>th(CL<br>ITV)|
||tsu(NW|tsu(NW|tsu(NW|tsu(NW|tsu(NW|
|||||||
|||||||
|||||||


|Col1|CLKH)|
|---|---|
|ITV-|ITV-|
|||



**Table 76. Synchronous non-multiplexed NOR/PSRAM read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FMC_CLK period|2Tfmc_ker_ck −1|-|ns|
|t(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|2|2|
|td(CLKH-NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)|Tfmc_ker_ck+ 0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|0.5|0.5|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)|-|2|2|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NOEL)|FMC_CLK low to FMC_NOE low|-|1.5|1.5|
|td(CLKH-NOEH)|FMC_CLK high to FMC_NOE high|Tfmc_ker_ck+ 0.5|-|-|
|tsu(DV-CLKH)|FMC_D[15:0] valid data before FMC_CLK high|3|-|-|
|th(CLKH-DV)|FMC_D[15:0] valid data after FMC_CLK high|0|-|-|
|tSU(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|3|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|1|-|-|


1. Guaranteed by characterization results.


158/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 31. Synchronous non-multiplexed PSRAM write timings**














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|td(CL<br>td(CL|Da|Da|Da|Da|Da|Da|Da|
|td(CL<br>td(CL|Da|ta latency =|0|0|0|0|0|
|td(CL<br>td(CL|KL-AV)<br>td(CL|KL-NADVH|)|||||
|td(CL<br>td(CL|KL-AV)<br>td(CL|||t|d(CLKH-A|IV)|IV)|
|td(CL<br>td(CL|KL-AV)<br>td(CL|||t|d(CLKH-A|IV)||
|td(CL<br>td(CL||||||||
|td(CL<br>td(CL|KL-NWEL)|||td(C|LKH-NWE|H)|H)|
|td(CL<br>td(CL|KL-NWEL)|||td(C|LKH-NWE|H)||
|td(CL<br>td(CL|td(CL|KL-Data~~)~~|KL-Data~~)~~||D2<br>td(CLK<br>-NWAITV)<br>CLKH-NB|L-Da<br>LH~~)~~|L-Da<br>LH~~)~~|
|td(CL<br>td(CL|td(CL|KL-Data~~)~~|KL-Data~~)~~|D1|D1|D1|D1|
|||||||||
|||||||||
||tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|



**Table 77. Synchronous non-multiplexed PSRAM write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t(CLK)|FMC_CLK period|2Tfmc_ker_ck−1|-|ns|
|td(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|2|2|
|t(CLKH-NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)|Tfmc_ker_ck+ 0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|0.5|0.5|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)|-|2|2|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NWEL)|FMC_CLK low to FMC_NWE low|-|1.5|1.5|
|td(CLKH-NWEH)|FMC_CLK high to FMC_NWE high|Tfmc_ker_ck+ 1|-|-|
|td(CLKL-Data)|FMC_D[15:0] valid data after FMC_CLK low|-|3.5|3.5|
|td(CLKL-NBLL)|FMC_CLK low to FMC_NBL low|-|2|2|
|td(CLKH-NBLH)|FMC_CLK high to FMC_NBL high|Tfmc_ker_ck+ 1|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|2|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|2|-|-|


1. Guaranteed by characterization results.





DS12110 Rev 10 159/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**NAND controller waveforms and timings**


_Figure 32_ through _Figure 35_ represent synchronous waveforms, and _Table 78_ and _Table 79_
provide the corresponding timings. The results shown in this table are obtained with the
following FMC configuration:


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


      - C L = 30 pF


In all timing tables, the T fmc_ker_ck is the fmc_ker_ck clock period.


**Figure 32. NAND controller waveforms for read access**


160/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 33. NAND controller waveforms for write access**


**Figure 34. NAND controller waveforms for common memory read access**


DS12110 Rev 10 161/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 35. NAND controller waveforms for common memory write access**







**Table 78. Switching characteristics for NAND flash read cycles** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(N0E)|FMC_NOE low width|4Tfmc_ker_ck–0.5|4Tfmc_ker_ck+ 0.5|ns|
|tsu(D-NOE)|FMC_D[15-0] valid data before FMC_NOE high|8|-|-|
|th(NOE-D)|FMC_D[15-0] valid data after FMC_NOE high|0|-|-|
|td(ALE-NOE)|FMC_ALE valid before FMC_NOE low|-|3Tfmc_ker_ck+ 1|3Tfmc_ker_ck+ 1|
|th(NOE-ALE)|FMC_NWE high to FMC_ALE invalid|4Tfmc_ker_ck −2|-|-|


1. Guaranteed by characterization results.


**Table 79. Switching characteristics for NAND flash write cycles** **[(1)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NWE)|FMC_NWE low width|4Tfmc_ker_ck −0.5|4Tfmc_ker_ck + 0.5|ns|
|tv(NWE-D)|FMC_NWE low to FMC_D[15-0] valid|0|-|-|
|th(NWE-D)|FMC_NWE high to FMC_D[15-0] invalid|2Tfmc_ker_ck −0.5|-|-|
|td(D-NWE)|FMC_D[15-0] valid before FMC_NWE high|5Tfmc_ker_ck −1|-|-|
|td(ALE-NWE)|FMC_ALE valid before FMC_NWE low|-|3Tfmc_ker_ck+ 0.5|3Tfmc_ker_ck+ 0.5|
|th(NWE-ALE)|FMC_NWE high to FMC_ALE invalid|2Tfmc_ker_ck −1|-|-|


1. Guaranteed by characterization results.


162/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**SDRAM waveforms and timings**


In all timing tables, the T fmc_ker_ck is the fmc_ker_ck clock period, with the following
FMC_SDCLK maximum values:


      - For 1.8 V < V DD < 3.6V: FMC_SDCLK = 100 MHz at 20 pF


      - For 1.62 V< V DD < 1.8 V, FMC_SDCLK = 100 MHz at 15 pF


**Figure 36. SDRAM read access waveforms (CL = 1)**





|Col1|Col2|Coln|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
|_NRAS)|||||
|_NCAS)|||||
|_NCAS)|||||
||||||


**Table 80. SDRAM read timings** **[(1)]**









|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck −1|2Tfmc_ker_ck+ 0.5|ns|
|tsu(SDCLKH _Data)|Data input setup time|3|-|-|
|th(SDCLKH_Data)|Data input hold time|0|-|-|
|td(SDCLKL_Add)|Address valid time|-|1.5|1.5|
|td(SDCLKL- SDNE)|Chip select valid time|-|1.5|1.5|
|th(SDCLKL_SDNE)|Chip select hold time|0.5|-|-|
|td(SDCLKL_SDNRAS)|SDNRAS valid time|-|1|1|
|th(SDCLKL_SDNRAS)|SDNRAS hold time|0.5|-|-|
|td(SDCLKL_SDNCAS)|SDNCAS valid time|-|0.5|0.5|
|th(SDCLKL_SDNCAS)|SDNCAS hold time|0|-|-|


1. Guaranteed by characterization results.


DS12110 Rev 10 163/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 81. LPSDR SDRAM read timings** **[(1)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tW(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck −1|2Tfmc_ker_ck+ 0.5|ns|
|tsu(SDCLKH_Data)|Data input setup time|3|-|-|
|th(SDCLKH_Data)|Data input hold time|0.5|-|-|
|td(SDCLKL_Add)|Address valid time|-|2.5|2.5|
|td(SDCLKL_SDNE)|Chip select valid time|-|2.5|2.5|
|th(SDCLKL_SDNE)|Chip select hold time|0|-|-|
|td(SDCLKL_SDNRAS|SDNRAS valid time|-|0.5|0.5|
|th(SDCLKL_SDNRAS)|SDNRAS hold time|0|-|-|
|td(SDCLKL_SDNCAS)|SDNCAS valid time|-|1.5|1.5|
|th(SDCLKL_SDNCAS)|SDNCAS hold time|0|-|-|



1. Guaranteed by characterization results.


**Figure 37. SDRAM write access waveforms**














|DCLK<br>DCLK|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||Col2|Col2|Col2|Coln|Coln|Coln|
|||th(S|th(S|th(S||||
|E)|E)|E)|E)|E)|E)|E)|E)|
|E)|E)|E)|E)|E)|E)|||
|DCLK|DCLK|L_NR|AS)|||||
|DCLK|DCLK|L_NC|AS)|||||
|DCLK|DCLK|L_NC|AS)|||||
|DCLK|DCLK|L_N|WE)|||||
|DCLK|DCLK|L_N|WE)|||||
|DCLK|DCLK|||||||
|DCLK|D|ata2|ata2|ata2|atan|atan|atan|



164/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 82. SDRAM write timings** **[(1)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck −1|2Tfmc_ker_ck+ 0.5|ns|
|td(SDCLKL _Data)|Data output valid time|-|3|3|
|th(SDCLKL _Data)|Data output hold time|0|-|-|
|td(SDCLKL_Add)|Address valid time|-|1.5|1.5|
|td(SDCLKL_SDNWE)|SDNWE valid time|-|1.5|1.5|
|th(SDCLKL_SDNWE)|SDNWE hold time|0.5|-|-|
|td(SDCLKL_ SDNE)|Chip select valid time|-|1.5|1.5|
|th(SDCLKL-_SDNE)|Chip select hold time|0.5|-|-|
|td(SDCLKL_SDNRAS)|SDNRAS valid time|-|1|1|
|th(SDCLKL_SDNRAS)|SDNRAS hold time|0.5|-|-|
|td(SDCLKL_SDNCAS)|SDNCAS valid time|-|1|1|
|td(SDCLKL_SDNCAS)|SDNCAS hold time|0.5|-|-|



1. Guaranteed by characterization results.


**Table 83. LPSDR SDRAM write timings** **[(1)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck −1|2Tfmc_ker_ck+ 0.5|ns|
|td(SDCLKL _Data)|Data output valid time|-|2.5|2.5|
|th(SDCLKL _Data)|Data output hold time|0|-|-|
|td(SDCLKL_Add)|Address valid time|-|2.5|2.5|
|td(SDCLKL-SDNWE)|SDNWE valid time|-|2.5|2.5|
|th(SDCLKL-SDNWE)|SDNWE hold time|0|-|-|
|td(SDCLKL- SDNE)|Chip select valid time|-|3|3|
|th(SDCLKL- SDNE)|Chip select hold time|0|-|-|
|td(SDCLKL-SDNRAS)|SDNRAS valid time|-|1.5|1.5|
|th(SDCLKL-SDNRAS)|SDNRAS hold time|0|-|-|
|td(SDCLKL-SDNCAS)|SDNCAS valid time|-|1.5|1.5|
|td(SDCLKL-SDNCAS)|SDNCAS hold time|0|-|-|



1. Guaranteed by characterization results.


DS12110 Rev 10 165/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.18** **Quad-SPI interface characteristics**


Unless otherwise specified, the parameters given in _Table 84_ and _Table 85_ for QUADSPI
are derived from tests performed under the ambient temperature, f rcc_c_ck frequency and

V DD supply voltage conditions summarized in _Table 24: General operating conditions_, with


the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 11


      - Measurement points are done at CMOS levels: 0.5V DD

      - I/O compensation cell enabled


      - HSLV activated when V DD ≤2.7 V

Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output alternate

function characteristics.


**Table 84. QUADSPI characteristics in SDR mode** **[(1)]**















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fck1/TCK|QUADSPI clock frequency|2.7 V ≤ VDD<3.6 V<br>CL=20 pF|-|-|133|MHz|
|Fck1/TCK|QUADSPI clock frequency|1.62 V<VDD<3.6 V<br>CL=15 pF|-|-|100|100|
|tw(CKH)|QUADSPI clock high and low<br>time|-|TCK/2–0.5|-|TCK/2|ns|
|tw(CKL)|tw(CKL)|tw(CKL)|TCK/2|-|TCK/2 + 0.5|TCK/2 + 0.5|
|ts(IN)|Data input setup time|2.7 V ≤ VDD< 3.6 V|2|-|-|-|
|ts(IN)|Data input setup time|1.62 V ≤ VDD< 3.6 V|2.5|-|-|-|
|th(IN)|Data input hold time|2.7 V ≤ VDD< 3.6 V|1|-|-|-|
|th(IN)|Data input hold time|1.62 V ≤ VDD< 3.6 V|1.5|-|-|-|
|tv(OUT)|Data output valid time|-|-|1.5|2|2|
|th(OUT)|Data output hold time|-|0.5|-|-|-|


1. Guaranteed by characterization results.


166/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 85. QUADSPI characteristics in DDR mode** **[(1)]**















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fck1/t(CK)|QUADSPI clock<br>frequency|2.7 V<VDD<3.6 V<br>CL=20 pF|-|-|100|MHz|
|Fck1/t(CK)|QUADSPI clock<br>frequency|1.62 V<VDD<3.6 V<br>CL=15 pF|-|-|100|100|
|tw(CKH)|QUADSPI clock high and<br>low time|-|TCK/2 –0.5|-|TCK/2|ns|
|tw(CKL)|tw(CKL)|tw(CKL)|TCK/2|-<br>|TCK/2+0.5|TCK/2+0.5|
|tsr(IN), tsf(IN)|Data input setup time|2.7 V ≤ VDD< 3.6 V|3|-|-|-|
|tsr(IN), tsf(IN)|Data input setup time|1.62 V ≤ VDD< 3.6 V|1|-|-|-|
|thr(IN), thf(IN)|Data input hold time|2.7 V ≤ VDD< 3.6 V|1|-|-|-|
|thr(IN), thf(IN)|Data input hold time|1.62 V ≤ VDD< 3.6 V|1.5|-|-|-|
|tvr(OUT), <br>tvf(OUT)|Data output valid time|DHHC=0|-|3.5|4|4|
|tvr(OUT), <br>tvf(OUT)|Data output valid time|DHHC=1<br>Pres=1, 2...|-|TCK/4+3.5|TCK/4+4|TCK/4+4|
|thr(OUT), <br>thf(OUT)|Data output hold time|DHHC=0|3|-|-|-|
|thr(OUT), <br>thf(OUT)|Data output hold time|DHHC=1<br>Pres=1, 2...|TCK/4+3|-|-|-|


1. Guaranteed by characterization results.





**Figure 38. Quad-SPI timing diagram - SDR mode**








|ts(IN)|th(IN)|
|---|---|
|||
||D1|





**Figure 39. Quad-SPI timing diagram - DDR mode**














|Col1|r(OU|
|---|---|
|||
|IO0||


|Col1|Col2|f(OU|
|---|---|---|
||||
|IO2|IO3||








|Col1|Col2|Col3|Col4|
|---|---|---|---|
|IO0||I|O1|


|Col1|Col2|
|---|---|
|IO|4|





DS12110 Rev 10 167/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.19** **Delay block (DLYB) characteristics**


Unless otherwise specified, the parameters given in _Table 87_ for the delay block are derived
from tests performed under the ambient temperature, f rcc_c_ck frequency and V DD supply
voltage summarized in _Table 24: General operating conditions_ .


**Table 86. Dynamics characteristics: Delay Block characteristics** **[(1)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tinit|Initial delay|-|1400|2200|2400|ps|
|t∆|Unit Delay|-|35|40|45|45|



1. Guaranteed by characterization results.


**6.3.20** **16-bit ADC characteristics**


Unless otherwise specified, the parameters given in _Table 87_ are derived from tests
performed under the ambient temperature, f PCLK2 frequency and V DDA supply voltage
conditions summarized in _Table 24: General operating conditions_ .

**Table 87. ADC characteristics** **[(1)]**










|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog power supply|-|-|1.62|-|3.6|V|
|VREF+|Positive reference voltage|VDDA ≥2 V|VDDA ≥2 V|2|-|VDDA|VDDA|
|VREF+|Positive reference voltage|VDDA< 2 V|VDDA< 2 V|VDDA|VDDA|VDDA|VDDA|
|VREF-|Negative reference voltage|-|-|VSSA|VSSA|VSSA|VSSA|
|fADC|ADC clock frequency|2 V ≤VDDA ≤3.3 V|BOOST = 1|-|-|36|MHz|
|fADC|ADC clock frequency|2 V ≤VDDA ≤3.3 V|BOOST = 0|-|-|20|20|
|fS|Sampling rate for Fast<br>channels, BOOST = 1,<br>fADC= 36 MHz(2)|16-bit resolution|16-bit resolution|-|-|3.60(2)|MSPS|
|fS|Sampling rate for Fast<br>channels, BOOST = 1,<br>fADC= 36 MHz(2)|14-bit resolution|14-bit resolution|-|-|4.00(2)|4.00(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 1,<br>fADC= 36 MHz(2)|12-bit resolution|12-bit resolution|-|-|4.50(2)|4.50(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 1,<br>fADC= 36 MHz(2)|10-bit resolution|10-bit resolution|-|-|5.00(2)|5.00(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 1,<br>fADC= 36 MHz(2)|8-bit resolution|8-bit resolution|-|-|6.00(2)|6.00(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 0,<br>fADC= 20 MHz|16-bit resolution|16-bit resolution|-|-|2.00(2)|2.00(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 0,<br>fADC= 20 MHz|14-bit resolution|14-bit resolution|-|-|2.20(2)|2.20(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 0,<br>fADC= 20 MHz|12-bit resolution|12-bit resolution|-|-|2.50(2)|2.50(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 0,<br>fADC= 20 MHz|10-bit resolution|10-bit resolution|-|-|2.80(2)|2.80(2)|
|fS|Sampling rate for Fast<br>channels, BOOST = 0,<br>fADC= 20 MHz|8-bit resolution|8-bit resolution|-|-|3.30(2)|3.30(2)|
|fS|Sampling rate for Slow<br>channels, BOOST = 0,<br>fADC= 10 MHz|16-bit resolution|16-bit resolution|-|-|1.00|1.00|
|fS|Sampling rate for Slow<br>channels, BOOST = 0,<br>fADC= 10 MHz|14-bit resolution|14-bit resolution|-|-|1.00|1.00|
|fS|Sampling rate for Slow<br>channels, BOOST = 0,<br>fADC= 10 MHz|12-bit resolution|12-bit resolution|-|-|1.00|1.00|
|fS|Sampling rate for Slow<br>channels, BOOST = 0,<br>fADC= 10 MHz|10-bit resolution|10-bit resolution|-|-|1.00|1.00|
|fS|Sampling rate for Slow<br>channels, BOOST = 0,<br>fADC= 10 MHz|8-bit resolution|8-bit resolution|-|-|1.00|1.00|



168/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 87. ADC characteristics** **[(1)]** **(continued)**











|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fTRIG|External trigger frequency|fADC = 36 MHz|-|-|3.6|MHz|
|fTRIG|External trigger frequency|16-bit resolution|-|-|10|1/fADC|
|VAIN<br>(3)|Conversion voltage range|-|0|-|VREF+|V|
|VCMIV|Common mode input<br>voltage|-|VREF/2−<br>10%|VREF/2|VREF/2+<br>10%|VREF/2+<br>10%|
|RAIN|External input impedance|-|-|-|50|㏀|
|CADC|Internal sample and hold<br>capacitor|-|-|4|-|pF|
|tADCREG_<br>STUP|ADC LDO startup time|-|-|5|10|µs|
|tSTAB|ADC power-up time|LDO already started|1|1|1|conversion<br>cycle|
|tCAL|Offset and linearity<br>calibration time|-|165,010|165,010|165,010|1/fADC|
|tOFF_CAL|Offset calibration time|-|1,280|1,280|1,280|1,280|
|tLATR|Trigger conversion latency<br>for regular and injected<br>channels without aborting<br>the conversion|CKMODE = 00|1.5|2|2.5|2.5|
|tLATR|Trigger conversion latency<br>for regular and injected<br>channels without aborting<br>the conversion|CKMODE = 01|-|-|2|2|
|tLATR|Trigger conversion latency<br>for regular and injected<br>channels without aborting<br>the conversion|CKMODE = 10|||2.25|2.25|
|tLATR|Trigger conversion latency<br>for regular and injected<br>channels without aborting<br>the conversion|CKMODE = 11|||2.125|2.125|
|tLATRINJ|Trigger conversion latency<br>for regular and injected<br>channels when a regular<br>conversion is aborted|CKMODE = 00|2.5|3|3.5|3.5|
|tLATRINJ|Trigger conversion latency<br>for regular and injected<br>channels when a regular<br>conversion is aborted|CKMODE = 01|-|-|3|3|
|tLATRINJ|Trigger conversion latency<br>for regular and injected<br>channels when a regular<br>conversion is aborted|CKMODE = 10|-|-|3.25|3.25|
|tLATRINJ|Trigger conversion latency<br>for regular and injected<br>channels when a regular<br>conversion is aborted|CKMODE = 11|-|-|3.125|3.125|
|tS|Sampling time|-|1.5|-|810.5|810.5|
|tCONV|Total conversion time<br>(including sampling time)|N-bit resolution|tS + 0.5 + N/2<br>(9 to 648 cycles in 14-bit<br>mode)|tS + 0.5 + N/2<br>(9 to 648 cycles in 14-bit<br>mode)|tS + 0.5 + N/2<br>(9 to 648 cycles in 14-bit<br>mode)||


1. Guaranteed by design.


2. These values are obtained using the following formula: f S = f ADC / t CONV,
where f ADC = 36 MHz and t CONV = 1,5 cycle sampling time + t SAR sampling time.
Refer to the product reference manual for the value of t SAR depending on resolution.


3. Depending on the package, V REF+ can be internally connected to V DDA and V REF- to V SSA .


DS12110 Rev 10 169/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 88. ADC accuracy** **[(1)(2)(3)]**




























































|Symbol|Parameter|Conditions(4)|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|ET|Total<br>unadjusted<br>error|Single<br>ended|BOOST = 1|-|±6|-|±LSB|
|ET|Total<br>unadjusted<br>error|Single<br>ended|BOOST = 0|-|±8|-|-|
|ET|Total<br>unadjusted<br>error|Differential|BOOST = 1|-|±10|-|-|
|ET|Total<br>unadjusted<br>error|Differential|BOOST = 0|-|±16|-|-|
|ED|Differential<br>linearity<br>error|Single<br>ended|BOOST = 1|-|2|-|-|
|ED|Differential<br>linearity<br>error|Single<br>ended|BOOST = 0|-|1|-|-|
|ED|Differential<br>linearity<br>error|Differential|BOOST = 1|-|8|-|-|
|ED|Differential<br>linearity<br>error|Differential|BOOST = 0|-|2|-|-|
|EL|Integral<br>linearity<br>error|Single<br>ended|BOOST = 1|-|±6|-|-|
|EL|Integral<br>linearity<br>error|Single<br>ended|BOOST = 0|-|±4|-|-|
|EL|Integral<br>linearity<br>error|Differential|BOOST = 1|-|±6|-|-|
|EL|Integral<br>linearity<br>error|Differential|BOOST = 0|-|±4|-|-|
|ENOB(5)|Effective<br>number of<br>bits<br>(2 MSPS)|Single<br>ended|BOOST = 1|-|11.6|-|bits|
|ENOB(5)|Effective<br>number of<br>bits<br>(2 MSPS)|Single<br>ended|BOOST = 0|-|12|-|-|
|ENOB(5)|Effective<br>number of<br>bits<br>(2 MSPS)|Differential|BOOST = 1|-|13.3|-|-|
|ENOB(5)|Effective<br>number of<br>bits<br>(2 MSPS)|Differential|BOOST = 0|-|13.5|-|-|
|SINAD(5)|Signal-to-<br>noise and<br>distortion<br>ratio<br>(2 MSPS)|Single<br>ended|BOOST = 1|-|71.6|-|dB|
|SINAD(5)|Signal-to-<br>noise and<br>distortion<br>ratio<br>(2 MSPS)|Single<br>ended|BOOST = 0|-|74|-|-|
|SINAD(5)|Signal-to-<br>noise and<br>distortion<br>ratio<br>(2 MSPS)|Differential|BOOST = 1|-|81.83|-|-|
|SINAD(5)|Signal-to-<br>noise and<br>distortion<br>ratio<br>(2 MSPS)|Differential|BOOST = 0|-|83|-|-|
|SNR(5)|Signal-to-<br>noise ratio<br>(2 MSPS)|Single<br>ended|BOOST = 1|-|72|-|-|
|SNR(5)|Signal-to-<br>noise ratio<br>(2 MSPS)|Single<br>ended|BOOST = 0|-|74|-|-|
|SNR(5)|Signal-to-<br>noise ratio<br>(2 MSPS)|Differential|BOOST = 1|-|82|-|-|
|SNR(5)|Signal-to-<br>noise ratio<br>(2 MSPS)|Differential|BOOST = 0|-|83|-|-|
|THD(5)|Total<br>harmonic<br>distortion|Single<br>ended|BOOST = 1|-|−78|-|-|
|THD(5)|Total<br>harmonic<br>distortion|Single<br>ended|BOOST = 0|-|−80|-|-|
|THD(5)|Total<br>harmonic<br>distortion|Differential|BOOST = 1|-|−90|-|-|
|THD(5)|Total<br>harmonic<br>distortion|Differential|BOOST = 0|-|−95|-|-|



1. Guaranteed by characterization for BGA packages, the values for LQFP packages might differ.


2. ADC DC accuracy values are measured after internal calibration.


3. The above table gives the ADC performance in 16-bit mode.


4. ADC clock frequency ≤ 36 MHz, 2 V ≤ V DDA ≤3.3 V, 1.6 V ≤ V REF ≤ V DDA, BOOSTEN (for I/O) = 1.


5. ENOB, SINAD, SNR and THD are specified for V DDA = V REF = 3.3 V.


Note: ADC accuracy vs. negative injection current: injecting a negative current on any analog
input pins should be avoided as this significantly reduces the accuracy of the conversion


170/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


being performed on another analog input. It is recommended to add a Schottky diode (pin to
ground) to analog pins which may potentially inject negative currents.



Any positive injection current within the limits specified for I INJ(PIN) and ΣI INJ(PIN) in
_Section 6.3.14_ does not affect the ADC accuracy.


**Figure 40. ADC accuracy characteristics**

































**Figure 41. Typical connection diagram when using the ADC with FT/TT pins featuring**
**analog switch function**

























1. Refer to _Section 6.3.20: 16-bit ADC characteristics_ for the values of R AIN and C ADC .


2. C parasitic represents the capacitance of the PCB (dependent on soldering and PCB layout quality) plus the
pad capacitance (refer to _Table 60: I/O static characteristics_ for the value of the pad capacitance). A high
C parasitic value downgrades conversion accuracy. To remedy this, f ADC should be reduced.


3. Refer to _Table 60: I/O static characteristics_ for the value of I .
lkg


4. Refer to _Figure 15: Power supply scheme_ .


DS12110 Rev 10 171/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**General PCB design guidelines**


Power supply decoupling should be performed as shown in _Figure 42_ or _Figure 43_,
depending on whether V REF+ is connected to V DDA or not. The 100 nF capacitors should be
ceramic (good quality). They should be placed them as close as possible to the chip.


**Figure 42. Power supply and reference decoupling** **(V** **REF+** **not connected to** **V** **DDA** **)**













1. V REF+ input is available on all package whereas the V REF– s available only on UFBGA176+25 and
TFBGA240+25. When V REF- is not available, it is internally connected to V DDA and V SSA .


**Figure 43. Power supply and reference decoupling** **(V** **REF+** **connected to** **V** **DDA** **)**









1. V REF+ input is available on all package whereas the V REF– s available only on UFBGA176+25 and
TFBGA240+25. When V REF- is not available, it is internally connected to V DDA and V SSA .


172/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.21** **DAC electrical characteristics**


**Table 89. DAC characteristics** **[(1)]**



















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|-|-|1.8|3.3|3.6|V|
|VREF+|Positive reference voltage|-|-|1.80|-|VDDA|VDDA|
|VREF-|Negative reference<br>voltage|-|-|-|VSSA|-|-|
|RL|Resistive Load|DAC output<br>buffer ON|connected to<br>VSSA|5|-|-|㏀|
|RL|Resistive Load|DAC output<br>buffer ON|connected to<br>VDDA|25|-|-|-|
|RO<br>(2)|Output Impedance|DAC output buffer OFF|DAC output buffer OFF|10.3|13|16|16|
|RBON|Output impedance sample<br>and hold mode, output<br>buffer ON|DAC output<br>buffer ON|VDD = 2.7 V|-|-|1.6|㏀|
|RBON|Output impedance sample<br>and hold mode, output<br>buffer ON|DAC output<br>buffer ON|VDD = 2.0 V|-|-|2.6|2.6|
|RBOFF|Output impedance sample<br>and hold mode, output<br>buffer OFF|DAC output<br>buffer OFF|VDD = 2.7 V|-|-|17.8|㏀|
|RBOFF|Output impedance sample<br>and hold mode, output<br>buffer OFF|DAC output<br>buffer OFF|VDD = 2.0 V|-|-|18.7|18.7|
|CL<br>(2)|Capacitive Load|DAC output buffer OFF|DAC output buffer OFF|-|-|50|pF|
|CSH<br>(2)|CSH<br>(2)|Sample and Hold mode|Sample and Hold mode|-|0.1|1|µF|
|VDAC_OUT|Voltage on DAC_OUT<br>output|DAC output buffer ON|DAC output buffer ON|0.2|-|VREF+ <br>−0.2|V|
|VDAC_OUT|Voltage on DAC_OUT<br>output|DAC output buffer OFF|DAC output buffer OFF|0|-|VREF+|VREF+|
|tSETTLING|Settling time (full scale: for<br>a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC output buffer<br>OFF, ±1LSB CL=10 pF|Normal mode, DAC output buffer<br>OFF, ±1LSB CL=10 pF|-|1.7(2)|2(2)|µs|
|tWAKEUP<br>(3)|Wakeup time from off<br>state (setting the Enx bit in<br>the DAC Control register)<br>until the ±1LSB final value|Normal mode, DAC output buffer<br>ON, CL ≤ 50 pF, RL = 5㏀|Normal mode, DAC output buffer<br>ON, CL ≤ 50 pF, RL = 5㏀|-|5|7.5|µs|
|Voffset<br>(2)|Middle code offset for 1<br>trim code step|VREF+ = 3.6 V|VREF+ = 3.6 V|-|850|-|µV|
|Voffset<br>(2)|Middle code offset for 1<br>trim code step|VREF+ = 1.8 V|VREF+ = 1.8 V|-|425|-|-|


DS12110 Rev 10 173/357









320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 89. DAC characteristics** **[(1)]** **(continued)**





|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|DAC output<br>buffer ON|No load, middle<br>code (0x800)|-|360|-|µA|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|DAC output<br>buffer ON|No load, worst<br>code (0xF1C)|-|490|-|-|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|DAC output<br>buffer OFF|No load,<br>middle/worst<br>code (0x800)|-|20|-|-|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|Sample and Hold mode,<br>CSH=100 nF|Sample and Hold mode,<br>CSH=100 nF|-|360*TON/<br>(TON+TOFF)|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|DAC output<br>buffer ON|No load, middle<br>code (0x800)|-|170|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|DAC output<br>buffer ON|No load, worst<br>code (0xF1C)|-|170|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|DAC output<br>buffer OFF|No load,<br>middle/worst<br>code (0x800)|-|160|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|Sample and Hold mode, Buffer<br>ON, CSH=100 nF (worst code)|Sample and Hold mode, Buffer<br>ON, CSH=100 nF (worst code)|-|170*TON/<br>(TON+TOFF)|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|Sample and Hold mode, Buffer<br>OFF, CSH=100 nF (worst code)|Sample and Hold mode, Buffer<br>OFF, CSH=100 nF (worst code)|-|160*TON/<br>(TON+TOFF)|-|-|


1. Guaranteed by characterization results.


2. Guaranteed by design.















3. In buffered mode, the output can overshoot above the final value for low input code (starting from the minimum value).


**Table 90. DAC accuracy** **[(1)]**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|DNL|Differential non<br>linearity(2)|DAC output buffer ON|DAC output buffer ON|-|±2|-|LSB|
|DNL|Differential non<br>linearity(2)|DAC output buffer OFF|DAC output buffer OFF|-|±2|-|-|
|INL|Integral non linearity(3)|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀|-|±4|-|LSB|
|INL|Integral non linearity(3)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|±4|-|-|
|Offset|Offset error at code<br>0x800(3)|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 3.6 V|-|-|±12|LSB|
|Offset|Offset error at code<br>0x800(3)|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 1.8 V|-|-|±25|±25|
|Offset|Offset error at code<br>0x800(3)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±8|±8|


174/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 90. DAC accuracy** **[(1)]** **(continued)**













|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|Offset1|Offset error at code<br>0x001(4)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±5|LSB|
|OffsetCal|Offset error at code<br>0x800 after factory<br>calibration|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 3.6 V|-|-|±5|LSB|
|OffsetCal|Offset error at code<br>0x800 after factory<br>calibration|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 1.8 V|-|-|±7|±7|
|Gain|Gain error(5)|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀|-|-|±1|%|
|Gain|Gain error(5)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±1|±1|
|TUE|Total unadjusted error|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±12|LSB|
|SNR|Signal-to-noise ratio(6)|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz, BW = 500 KHz|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz, BW = 500 KHz|-|67.8|-|dB|
|SINAD|Signal-to-noise and<br>distortion ratio(6)|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz|-|67.5|-|dB|
|ENOB|Effective number of<br>bits|DAC output buffer ON,<br>CL ≤50 pF, RL ≥5 ㏀, 1 kHz|DAC output buffer ON,<br>CL ≤50 pF, RL ≥5 ㏀, 1 kHz|-|10.9|-|bits|


1. Guaranteed by characterization.


2. Difference between two consecutive codes minus 1 LSB.


3. Difference between the value measured at Code i and the value measured at Code i on a line drawn between Code 0 and
last Code 4095.


4. Difference between the value measured at Code (0x001) and the ideal value.


5. Difference between the ideal slope of the transfer function and the measured slope computed from code 0x000 and 0xFFF
when the buffer is OFF, and from code giving 0.2 V and (V REF+   - 0.2 V) when the buffer is ON.


6. Signal is -0.5dBFS with F sampling =1 MHz.


DS12110 Rev 10 175/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 44. 12-bit buffered /non-buffered DAC**











1. The DAC integrates an output buffer that can be used to reduce the output impedance and to drive external loads directly
without the use of an external operational amplifier. The buffer can be bypassed by configuring the BOFFx bit in the
DAC_CR register.


**6.3.22** **Voltage reference buffer characteristics**


**Table 91. VREFBUF characteristics** **[(1)]**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 000|2.8|3.3|3.6|V|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 001|2.4|-|3.6|3.6|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 010|2.1|-|3.6|3.6|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 011|1.8|-|3.6|3.6|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 000|1.62|-|2.80|2.80|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 001|1.62|-|2.40|2.40|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 010|1.62|-|2.10|2.10|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 011|1.62|-|1.80|1.80|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Normal mode|VSCALE = 000|-|2.5|-|-|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Normal mode|VSCALE = 001|-|2.048|-|-|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Normal mode|VSCALE = 010|-|1.8|-|-|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Normal mode|VSCALE = 011|-|1.5|-|-|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Degraded mode(2)|VSCALE = 000|VDDA−<br>150 mV|-|VDDA|VDDA|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Degraded mode(2)|VSCALE = 001|VDDA−<br>150 mV|-|VDDA|VDDA|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Degraded mode(2)|VSCALE = 010|VDDA−<br>150 mV|-|VDDA|VDDA|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output|Degraded mode(2)|VSCALE = 011|VDDA−<br>150 mV|-|VDDA|VDDA|
|TRIM|Trim step resolution|-|-|-|±0.05|±0.2|%|
|CL|Load capacitor|-|-|0.5|1|1.50|uF|


176/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 91. VREFBUF characteristics** **[(1)]** **(continued)**




















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|esr|Equivalent Serial<br>Resistor of CL|-|-|-|-|2|Ω|
|Iload|Static load current|-|-|-|-|4|mA|
|Iline_reg|Line regulation|2.8 V ≤ VDDA ≤ 3.6 V|Iload = 500 µA|-|200|-|ppm/V|
|Iline_reg|Line regulation|2.8 V ≤ VDDA ≤ 3.6 V|Iload = 4 mA|-|100|-|-|
|Iload_reg|Load regulation|500 µA ≤ ILOAD ≤ 4 mA|Normal Mode|-|50|-|ppm/<br>mA|
|Tcoeff|Temperature coefficient|−40 °C < TJ < +125 °C|-|-|-|Tcoeff <br>xVREFINT <br>+ 75|ppm/<br>°C|
|PSRR|Power supply rejection|DC|-|-|60|-|dB|
|PSRR|Power supply rejection|100KHz|-|-|40|-|-|
|tSTART|Start-up time|CL=0.5 µF|-|-|300|-|µs|
|tSTART|Start-up time|CL=1 µF|-|-|500|-|-|
|tSTART|Start-up time|CL=1.5 µF|-|-|650|-|-|
|IINRUSH|Control of maximum<br>DC current drive on<br>VREFBUF_OUT during<br>startup phase(3)|-|-|-|8|-|mA|
|IDDA(VRE<br>FBUF)|VREFBUF<br>consumption from<br>VDDA|ILOAD = 0 µA|-|-|15|25|µA|
|IDDA(VRE<br>FBUF)|VREFBUF<br>consumption from<br>VDDA|ILOAD = 500 µA|-|-|16|30|30|
|IDDA(VRE<br>FBUF)|VREFBUF<br>consumption from<br>VDDA|ILOAD = 4 mA|-|-|32|50|50|



1. Guaranteed by design.


2. In degraded mode, the voltage reference buffer cannot accurately maintain the output voltage (V DDA −drop voltage).


3. To properly control VREFBUF I INRUSH current during the startup phase and the change of scaling, V DDA voltage should be in
the range of 1.8 V-3.6 V, 2.1 V-3.6 V, 2.4 V-3.6 V and 2.8 V-3.6 V for VSCALE = 011, 010, 001 and 000, respectively.


**6.3.23** **Temperature sensor characteristics**


**Table 92. Temperature sensor characteristics**







|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|TL<br>(1)|VSENSE linearity with temperature|-|-|±3|°C|
|Avg_Slope(2)|Average slope|-|2|-|mV/°C|
|V30<br>(3)|Voltage at 30°C ± 5 °C|-|0.62|-|V|
|tstart_run<br>(1)|Startup time in Run mode (buffer startup)|-|-|25.2|µs|
|tS_temp<br>(1)|ADC sampling time when reading the temperature|9|-|-|-|
|Isens<br>(1)|Sensor consumption|-|0.18|0.31|µA|
|Isensbuf<br>(1)|Sensor buffer consumption|-|3.8|6.5|6.5|


1. Guaranteed by design.


DS12110 Rev 10 177/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


2. Guaranteed by characterization.


3. Measured at V DDA = 3.3 V ± 10 mV. The V 30 ADC conversion result is stored in the TS_CAL1
byte.


**Table 93. Temperature sensor calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|TS_CAL1|Temperature sensor raw data acquired value at<br>30 °C, VDDA=3.3 V|0x1FF1 E820 -0x1FF1 E821|
|TS_CAL2|Temperature sensor raw data acquired value at<br>110 °C, VDDA=3.3 V|0x1FF1 E840 - 0x1FF1 E841|



**6.3.24** **Temperature and V** **BAT** **monitoring**


**Table 94. V** **BAT** **monitoring characteristics**







|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|R|Resistor bridge for VBAT|-|26|-|KΩ|
|Q|Ratio on VBAT measurement|-|4|-|-|
|Er(1)|Error on Q|–10|-|+10|%|
|tS_vbat<br>(1)|ADC sampling time when reading VBATinput|9|-|-|µs|
|VBAThigh|High supply monitoring|-|3.55|-|V|
|VBATlow|Low supply monitoring|-|1.36|-|-|


1. Guaranteed by design.


**Table 95. V** **BAT** **charging characteristics**

|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|RBC|Battery charging resistor|VBRS in PWR_CR3= 0|-|5|-|KΩ|
|RBC|Battery charging resistor|VBRS in PWR_CR3= 1|-|1.5|-|-|



**Table 96. Temperature monitoring characteristics**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|TEMPhigh|High temperature monitoring|-|117|-|°C|
|TEMPlow|Low temperature monitoring|-|**–**25|-|-|



178/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.25** **Voltage booster for analog switch**


**Table 97. Voltage booster for analog switch characteristics** **[(1)]**

|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD|Supply voltage|-|1.62|2-6|3.6|V|
|tSU(BOOST)|Booster startup time|-|-|-|50|µs|
|IDD(BOOST)|Booster consumption|1.62 V ≤ VDD ≤ 2.7 V|-|-|125|µA|
|IDD(BOOST)|Booster consumption|2.7 V < VDD < 3.6 V|-|-|250|250|



1. Guaranteed by characterization results.


DS12110 Rev 10 179/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.26** **Comparator characteristics**


**Table 98. COMP characteristics** **[(1)]**






















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|-|-|1.62|3.3|3.6|V|
|VIN|Comparator input voltage<br>range|-|-|0|-|VDDA|VDDA|
|VBG<br>(2)|Scaler input voltage|-|-|Refer to VREFINT|Refer to VREFINT|Refer to VREFINT|Refer to VREFINT|
|VSC|Scaler offset voltage|-|-|-|±5|±10|mV|
|IDDA(SCALER)|Scaler static consumption<br>from VDDA|BRG_EN=0 (bridge disable)|BRG_EN=0 (bridge disable)|-|0.2|0.3|µA|
|IDDA(SCALER)|Scaler static consumption<br>from VDDA|BRG_EN=1 (bridge enable)|BRG_EN=1 (bridge enable)|-|0.8|1|1|
|tSTART_SCALER|Scaler startup time|-|-|-|140|250|µs|
|tSTART|Comparator startup time to<br>reach propagation delay<br>specification|High-speed mode|High-speed mode|-|2|5|µs|
|tSTART|Comparator startup time to<br>reach propagation delay<br>specification|Medium mode|Medium mode|-|5|20|20|
|tSTART|Comparator startup time to<br>reach propagation delay<br>specification|Ultra-low-power mode|Ultra-low-power mode|-|15|80|80|
|tD|Propagation delay for<br>200 mV step with 100 mV<br>overdrive|High-speed mode|High-speed mode|-|50|80|ns|
|tD|Propagation delay for<br>200 mV step with 100 mV<br>overdrive|Medium mode|Medium mode|-|0.5|1.2|µs|
|tD|Propagation delay for<br>200 mV step with 100 mV<br>overdrive|Ultra-low-power mode|Ultra-low-power mode|-|2.5|7|7|
|tD|Propagation delay for step<br>> 200 mV with 100 mV<br>overdrive only on positive<br>inputs|High-speed mode|High-speed mode|-|50|120|ns|
|tD|Propagation delay for step<br>> 200 mV with 100 mV<br>overdrive only on positive<br>inputs|Medium mode|Medium mode|-|0.5|1.2|µs|
|tD|Propagation delay for step<br>> 200 mV with 100 mV<br>overdrive only on positive<br>inputs|Ultra-low-power mode|Ultra-low-power mode|-|2.5|7|7|
|Voffset|Comparator offset error|Full common mode range|Full common mode range|-|±5|±20|mV|
|Vhys|Comparator hysteresis|No hysteresis|No hysteresis|-|0|-|mV|
|Vhys|Comparator hysteresis|Low hysteresis|Low hysteresis|-|10|-|-|
|Vhys|Comparator hysteresis|Medium hysteresis|Medium hysteresis|-|20|-|-|
|Vhys|Comparator hysteresis|High hysteresis|High hysteresis|-|30|-|-|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Ultra-low-<br>power mode|Static|-|400|600|nA|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Ultra-low-<br>power mode|With 50 kHz<br>±100 mV overdrive<br>square signal|-|800|-|-|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Medium mode|Static|-|5|7|µA|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Medium mode|With 50 kHz<br>±100 mV overdrive<br>square signal|-|6|-|-|
|IDDA(COMP)|Comparator consumption<br>from VDDA|High-speed<br>mode|Static|-|70|100|100|
|IDDA(COMP)|Comparator consumption<br>from VDDA|High-speed<br>mode|With 50 kHz<br>±100 mV overdrive<br>square signal|-|75|-|-|



1. Guaranteed by design, unless otherwise specified.


2. Refer to _Table 28: Embedded reference voltage_ .


180/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.27** **Operational amplifier characteristics**


**Table 99. OPAMP characteristics** **[(1)]**



























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage<br>Range|-|2|3.3|3.6|V|
|CMIR|Common Mode Input<br>Range|-|0|-|VDDA|VDDA|
|VIOFFSET|Input offset voltage|25°C, no load on output|-|-|±1.5|mV|
|VIOFFSET|Input offset voltage|All voltages and<br>temperature, no load|-|-|±2.5|±2.5|
|ΔVIOFFSET|Input offset voltage drift|-|-|±3.0|-|μV/°C|
|TRIMOFFSETP<br>TRIMLPOFFSETP|Offset trim step at low<br>common input voltage<br>(0.1*VDDA)|-|-|1.1|1.5|mV|
|TRIMOFFSETN<br>TRIMLPOFFSETN|Offset trim step at high<br>common input voltage<br>(0.9*VDDA)|-|-|1.1|1.5|1.5|
|ILOAD|Drive current|-|-|-|500|μA|
|ILOAD_PGA|Drive current in PGA mode|-|-|-|270|270|
|CLOAD|Capacitive load|-|-|-|50|pF|
|CMRR|Common mode rejection<br>ratio|-|-|80|-|dB|
|PSRR|Power supply rejection<br>ratio|CLOAD ≤ 50pf /<br>RLOAD ≥ 4 kΩ(2) at 1 kHz,<br>Vcom=VDDA/2|50|66|-|dB|
|GBW|Gain bandwidth for high<br>supply range|-|4|7.3|12.3|MHz|
|SR|Slew rate (from 10% and<br>90% of output voltage)|Normal mode|-|3|-|V/µs|
|SR|Slew rate (from 10% and<br>90% of output voltage)|High-speed mode|-|30|-|-|
|AO|Open loop gain|-|59|90|129|dB|
|φm|Phase margin|-|-|55|-|°|
|GM|Gain margin|-|-|12|-|dB|


DS12110 Rev 10 181/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 99. OPAMP characteristics** **[(1)]** **(continued)**






























|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VOHSAT|High saturation voltage|Iload=max or RLOAD=min(2), <br>Input at VDDA|Iload=max or RLOAD=min(2), <br>Input at VDDA|VDDA <br>−100 mV|-|-|mV|
|VOLSAT|Low saturation voltage|Iload=max or RLOAD=min(2), <br>Input at 0 V|Iload=max or RLOAD=min(2), <br>Input at 0 V|-|-|100|100|
|tWAKEUP|Wake up time from OFF<br>state|Normal<br>mode|CLOAD ≤ 50pf,<br>RLOAD ≥ 4 kΩ(2), <br>follower<br>configuration|-|0.8|3.2|µs|
|tWAKEUP|Wake up time from OFF<br>state|High<br>speed|CLOAD ≤ 50pf,<br>RLOAD ≥ 4 kΩ(2), <br>follower<br>configuration|-|0.9|2.8|2.8|
|PGA gain|Non inverting gain value|-|-|-|2|-|-|
|PGA gain|Non inverting gain value|-|-|-|4|-|-|
|PGA gain|Non inverting gain value|-|-|-|8|-|-|
|PGA gain|Non inverting gain value|-|-|-|16|-|-|
|PGA gain|Inverting gain value|-|-|-|−1|-|-|
|PGA gain|Inverting gain value|-|-|-|−3|-|-|
|PGA gain|Inverting gain value|-|-|-|−7|-|-|
|PGA gain|Inverting gain value|-|-|-|−15|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(3)|PGA Gain=2|PGA Gain=2|-|10/10|-|kΩ/<br>kΩ|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(3)|PGA Gain=4|PGA Gain=4|-|30/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(3)|PGA Gain=8|PGA Gain=8|-|70/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(3)|PGA Gain=16|PGA Gain=16|-|150/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(3)|PGA Gain=-1|PGA Gain=-1|-|10/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(3)|PGA Gain=-3|PGA Gain=-3|-|30/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(3)|PGA Gain=-7|PGA Gain=-7|-|70/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(3)|PGA Gain=-15|PGA Gain=-15|-|150/10|-|-|
|Delta R|Resistance variation (R1 or<br>R2)|-|-|−15|-|15|%|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=2|Gain=2|-|GBW/2|-|MHz|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=4|Gain=4|-|GBW/4|-|-|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=8|Gain=8|-|GBW/8|-|-|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=16|Gain=16|-|GBW/16|-|-|



182/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 99. OPAMP characteristics** **[(1)]** **(continued)**



|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|en|Voltage noise density|at<br>1 KHz|output loaded<br>with 4 kΩ|-|140|-|nV/√<br>Hz|
|en|Voltage noise density|at<br>10 KHz|at<br>10 KHz|-|55|-|-|
|IDDA(OPAMP)|OPAMP consumption from<br>VDDA|Normal<br>mode|no Load,<br>quiescent mode,<br>follower|-|570|1000|µA|
|IDDA(OPAMP)|OPAMP consumption from<br>VDDA|High-<br>speed<br>mode|High-<br>speed<br>mode|-|610|1200|1200|


1. Guaranteed by design, unless otherwise specified.











2. R LOAD is the resistive load connected to VSSA or to VDDA.


3. R2 is the internal resistance between the OPAMP output and th OPAMP inverting input. R1 is the internal resistance
between the OPAMP inverting input and ground. PGA gain = 1 + R2/R1.


DS12110 Rev 10 183/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.28** **Digital filter for Sigma-Delta Modulators (DFSDM) characteristics**


Unless otherwise specified, the parameters given in _Table 100_ for DFSDM are derived from
tests performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
summarized in _Table 24: General operating conditions_, with the following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 10


      - Capacitive load C = 30 pF


      - Measurement points are done at CMOS levels: 0.5V DD


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (DFSDMx_CKINx, DFSDMx_DATINx, DFSDMx_CKOUT for
DFSDMx).


**Table 100. DFSDM measured timing - 1.62-3.6 V** **[(1)]**


















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|fDFSDMCLK|DFSDM clock|1.62 V < VDD < 3.6 V|1.62 V < VDD < 3.6 V|-|-|250|MHz|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>1.62 V < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>1.62 V < VDD < 3.6 V|-|-|20<br>(fDFSDMCLK/4)|20<br>(fDFSDMCLK/4)|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>2.7 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>2.7 < VDD < 3.6 V|-|-|20<br>(fDFSDMCLK/4)|20<br>(fDFSDMCLK/4)|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode<br>(SPICKSEL[1:0]≠0),<br>1.62 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode<br>(SPICKSEL[1:0]≠0),<br>1.62 < VDD < 3.6 V|-|-|20<br>(fDFSDMCLK/4)|20<br>(fDFSDMCLK/4)|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode<br>(SPICKSEL[1:0]≠0),<br>2.7 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode<br>(SPICKSEL[1:0]≠0),<br>2.7 < VDD < 3.6 V|-|-|20<br>(fDFSDMCLK/4)|20<br>(fDFSDMCLK/4)|
|fCKOUT|Output clock<br>frequency|1.62 < VDD < 3.6 V|1.62 < VDD < 3.6 V|-|-|20|20|
|DuCyCKOUT|Output clock<br>frequency duty<br>cycle|1.62 < VDD < 3.6 V|Even division,<br>CKOUTDIV[7:0]<br>= 1, 3, 5...|45|50|55|%|
|DuCyCKOUT|Output clock<br>frequency duty<br>cycle|1.62 < VDD < 3.6 V|Odd division,<br>CKOUTDIV[7:0]<br>= 2, 4, 6...|(((n/2+1)/(n+1))*<br>100)–5|(((n/2+1)/(n+1))<br>*100)|(((n/2+1)/(n+1))*<br>100)+5|(((n/2+1)/(n+1))*<br>100)+5|



184/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 100. DFSDM measured timing - 1.62-3.6 V** **[(1)]** **(continued)**


















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|twh(CKIN)<br>twl(CKIN)|Input clock<br>high and low<br>time|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|TCKIN/2 - 0.5|TCKIN/2|-|ns|
|tsu|Data input<br>setup time|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|4|-|-|-|
|th|Data input<br>hold time|SPI mode (SITP[1:0]=0,1),<br>External clock mode<br>(SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|0.5|-|-|-|
|TManchester|Manchester<br>data period<br>(recovered<br>clock period)|Manchester mode (SITP[1:0]=2,3),<br>Internal clock mode<br>(SPICKSEL[1:0]≠0),<br>1.62 < VDD < 3.6 V|(CKOUTDIV+1)<br>* TDFSDMCLK|-|(2*CKOUTDIV)<br>* TDFSDMCLK|(2*CKOUTDIV)<br>* TDFSDMCLK|



1. Guaranteed by characterization results.



DS12110 Rev 10 185/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 45. Channel transceiver timing diagrams**

















186/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.29** **Camera interface (DCMI) timing specifications**


Unless otherwise specified, the parameters given in _Table 101_ for DCMI are derived
from tests performed under the ambient temperature, f rcc_c_ck frequency and V DD
supply voltage summarized in _Table 24: General operating conditions_, with the following
configuration:


      - DCMI_PIXCLK polarity: falling


      - DCMI_VSYNC and DCMI_HSYNC polarity: high


      - Data formats: 14 bits


      - Capacitive load C=30 pF


      - Measurement points are done at CMOS levels: 0.5V DD


**Table 101. DCMI characteristics** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|-|Frequency ratio DCMI_PIXCLK/frcc_c_ck|-|0.4|-|
|DCMI_PIXCLK|Pixel clock input|-|80|MHz|
|DPixel|Pixel clock input duty cycle|30|70|%|
|tsu(DATA)|Data input setup time|1|-|ns|
|th(DATA)|Data input hold time|1|-|-|
|tsu(HSYNC)<br>tsu(VSYNC)|DCMI_HSYNC/DCMI_VSYNC input setup time|1.5|-|-|
|th(HSYNC)<br>th(VSYNC)|DCMI_HSYNC/DCMI_VSYNC input hold time|1|-|-|


1. Guaranteed by characterization results.


**Figure 46. DCMI timing diagram**










|Col1|Col2|
|---|---|
||tsu(VSY|
|||



DS12110 Rev 10 187/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.30** **LCD-TFT controller (LTDC) characteristics**


Unless otherwise specified, the parameters given in _Table 102_ for LCD-TFT are derived
from tests performed under the ambient temperature, f rcc_c_ck frequency and V DD supply
voltage summarized in _Table 24: General operating conditions_, with the following
configuration:


      - LCD_CLK polarity: high


      - LCD_DE polarity: low


      - LCD_VSYNC and LCD_HSYNC polarity: high

      - Pixel formats: 24 bits


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Capacitive load C=30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - I/O compensation cell enabled


**Table 102. LTDC characteristics** **[(1)]**














|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|fCLK|LTDC clock output frequency|2.7 V < VDD < 3.6 V,<br>20 pF|-|150|MHz|
|fCLK|LTDC clock output frequency|2.7 V < VDD < 3.6 V|-|133|133|
|fCLK|LTDC clock output frequency|1.62 V < VDD < 3.6 V|-|90|90|
|DCLK|LTDC clock output duty cycle|-|45|55|%|
|tw(CLKH),<br>tw(CLKL)|Clock High time, low time|-|tw(CLK)/2−0.5|tw(CLK)/2+0.5|ns|
|tv(DATA)|Data output valid time|-|-|0.5|0.5|
|th(DATA)|Data output hold time|-|0|-|-|
|tv(HSYNC),<br>tv(VSYNC),<br>tv(DE)|HSYNC/VSYNC/DE output valid<br>time|-|-|0.5|0.5|
|th(HSYNC),<br>th(VSYNC),<br>th(DE)|HSYNC/VSYNC/DE output hold<br>time|-|0.5|-|-|



1. Guaranteed by characterization results.


188/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 47. LCD-TFT horizontal timing diagram**








|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||tv(DE)|||t|v(HSYNC)|
||tv(DE)|||th(DE)|th(DE)|
||tv(D|tv(D|tv(D|tv(D|tv(D|
|||||||







**Figure 48. LCD-TFT vertical timing diagram**















DS12110 Rev 10 189/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**6.3.31** **Timer characteristics**


The parameters given in _Table 103_ are guaranteed by design.


Refer to _Section 6.3.15: I/O port characteristics_ for details on the input/output alternate
function characteristics (output compare, input capture, external clock, PWM output).


**Table 103. TIMx characteristics** **[(1)(2)]**











|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|tres(TIM)|Timer resolution time|AHB/APBx prescaler=1<br>or 2 or 4, fTIMxCLK =<br>240 MHz|1|-|tTIMxCLK|
|tres(TIM)|Timer resolution time|AHB/APBx<br>prescaler>4, fTIMxCLK =<br>140 MHz|1|-|tTIMxCLK|
|fEXT|Timer external clock<br>frequency on CH1 to CH4|fTIMxCLK = 240 MHz|0|fTIMxCLK/2|MHz|
|ResTIM|Timer resolution|Timer resolution|-|16/32|bit|
|tMAX_COUNT|Maximum possible count<br>with 32-bit counter|-|-|65536 ×<br>65536|tTIMxCLK|


1. TIMx is used as a general term to refer to the TIM1 to TIM17 timers.


2. Guaranteed by design.


3. The maximum timer frequency on APB1 or APB2 is up to 240 MHz, by setting the TIMPRE bit in the
RCC_CFGR register, if APBx prescaler is 1 or 2 or 4, then TIMxCLK = rcc_hclk1, otherwise TIMxCLK = 4x
F rcc_pclkx_d2 .


190/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**6.3.32** **Communications interfaces**


**I** **[2]** **C interface characteristics**


The I [2] C interface meets the timings requirements of the I [2] C-bus specification and user
manual revision 03 for:


      - Standard-mode (Sm): with a bit rate up to 100 kbit/s


      - Fast-mode (Fm): with a bit rate up to 400 kbit/s.


      - Fast-mode Plus (Fm+): with a bit rate up to 1Mbit/s.

The I [2] C timings requirements are guaranteed by design when the I2C peripheral is properly
configured (refer to RM0433 reference manual) and when the i2c_ker_ck frequency is
greater than the minimum shown in the table below:


**Table 104. Minimum i2c_ker_ck frequency in all I** **[2]** **C modes**










|Symbol|Parameter|Condition|Col4|Min|Unit|
|---|---|---|---|---|---|
|f(I2CCLK)|I2CCLK<br>frequency|Standard-mode||2|MHz|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode|Analog filter ON<br>DNF=0|8|8|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode|Analog filter OFF<br>DNF=1|9|9|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode Plus|Analog filter ON<br>DNF=0|17|17|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode Plus|Analog filter OFF<br>DNF=1|16|16|



The SDA and SCL I/O requirements are met with the following restrictions:


- The SDA and SCL I/O pins are not “true” open-drain. When configured as open-drain,
the PMOS connected between the I/O pin and V DD is disabled, but still present.


- The 20 mA output drive requirement in Fast-mode Plus is not supported. This limits the
maximum load C load supported in Fm+, which is given by these formulas:

t r(SDA/SCL) =0.8473xR p xC load
R p(min) = (V DD -V OL(max) )/I OL(max)
Where R p is the I2C lines pull-up. Refer to _Section 6.3.15: I/O port characteristics_ for
the I2C I/Os characteristics.


All I [2] C SDA and SCL I/Os embed an analog filter. Refer to _Table 105_ for the analog filter
characteristics:


**Table 105. I2C analog filter characteristics** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tAF|Maximum pulse width of spikes that<br>are suppressed by the analog filter|50(2)|260(3)|ns|


1. Guaranteed by design.


2. Spikes with widths below t AF(min) are filtered.

3. Spikes with widths above t AF(max) are not filtered.







DS12110 Rev 10 191/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**SPI interface characteristics**


Unless otherwise specified, the parameters given in _Table 106_ for the SPI interface are
derived from tests performed under the ambient temperature, f PCLKx frequency and V DD
supply voltage conditions summarized in _Table 24: General operating conditions_, with the
following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Capacitive load C = 30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - I/O compensation cell enabled


      - HSLV activated when VDD ≤ 2.7 V


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (NSS, SCK, MOSI, MISO for SPI).


**Table 106. SPI dynamic characteristics** **[(1)]**

















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Master mode<br>1.62 V≤VDD≤3.6 V|-|-|90|MHz|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Master mode<br>2.7 V≤VDD≤3.6 V<br>SPI1,2,3|Master mode<br>2.7 V≤VDD≤3.6 V<br>SPI1,2,3|Master mode<br>2.7 V≤VDD≤3.6 V<br>SPI1,2,3|133|133|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Master mode<br>2.7 V≤VDD≤3.6 V<br>SPI4,5,6|Master mode<br>2.7 V≤VDD≤3.6 V<br>SPI4,5,6|Master mode<br>2.7 V≤VDD≤3.6 V<br>SPI4,5,6|100|100|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Slave receiver mode<br>1.62 V≤VDD≤3.6 V<br>SPI1,2,3|Slave receiver mode<br>1.62 V≤VDD≤3.6 V<br>SPI1,2,3|Slave receiver mode<br>1.62 V≤VDD≤3.6 V<br>SPI1,2,3|150|150|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Slave receiver mode<br>1.62 V≤VDD≤3.6 V<br>SPI4,5,6|Slave receiver mode<br>1.62 V≤VDD≤3.6 V<br>SPI4,5,6|Slave receiver mode<br>1.62 V≤VDD≤3.6 V<br>SPI4,5,6|100|100|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Slave mode transmitter/full<br>duplex<br>2.7 V≤VDD≤3.6 V|Slave mode transmitter/full<br>duplex<br>2.7 V≤VDD≤3.6 V|Slave mode transmitter/full<br>duplex<br>2.7 V≤VDD≤3.6 V|31|31|
|fSCK<br>1/tc(SCK)|SPI clock frequency|Slave mode transmitter/full<br>duplex<br>1.62 V≤VDD≤3.6 V|Slave mode transmitter/full<br>duplex<br>1.62 V≤VDD≤3.6 V|Slave mode transmitter/full<br>duplex<br>1.62 V≤VDD≤3.6 V|25|25|
|tsu(NSS)|NSS setup time|Slave mode|2|-|-|ns|
|th(NSS)|NSS hold time|NSS hold time|1|-|-|-|
|tw(SCKH), <br>tw(SCKL)|SCK high and low time|Master mode|TPLCK- 2|TPLCK|TPLCK+ 2|TPLCK+ 2|


192/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 106. SPI dynamic characteristics** **[(1)]** **(continued)**











|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tsu(MI)|Data input setup time|Master mode|2|-|-|ns|
|tsu(SI)|tsu(SI)|Slave mode|2|-|-|-|
|th(MI)|Data input hold time|Master mode|1|-|-|-|
|th(SI)|th(SI)|Slave mode|1|-|-|-|
|ta(SO)|Data output access time|Slave mode|9|13|27|27|
|tdis(SO)|Data output disable time|Slave mode|0|1|5|5|
|tv(SO)|Data output valid time|Slave mode, 2.7 V≤VDD≤3.6 V|-|11.5|16|16|
|tv(SO)|Data output valid time|Slave mode 1.62 V≤VDD≤3.6 V|-|13|20|20|
|tv(MO)|tv(MO)|Master mode|-|1|3|3|
|th(SO)|Data output hold time|Slave mode, 1.62 V≤VDD≤3.6 V|9|-|-|-|
|th(MO)|th(MO)|Master mode|0|-|-|-|


1. Guaranteed by characterization results.


**Figure 49. SPI timing diagram - slave mode and CPHA = 0**

































DS12110 Rev 10 193/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 50. SPI timing diagram - slave mode and CPHA = 1** **[(1)]**





























1. Measurement points are done at 0.5V DD and with external C L = 30 pF.


**Figure 51. SPI timing diagram - master mode** **[(1)]**












|Col1|tw(SCKH)<br>tw(SCKL)|Col3|
|---|---|---|
||MSB IN||







|BIT1 OUT|Col2|
|---|---|
|BIT1 OUT||


1. Measurement points are done at 0.5V DD and with external C L = 30 pF.


194/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**I** **[2]** **S interface characteristics**


Unless otherwise specified, the parameters given in _Table 107_ for the I [2] S interface are
derived from tests performed under the ambient temperature, f PCLKx frequency and V DD
supply voltage conditions summarized in _Table 24: General operating conditions_, with the
following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 10


      - Capacitive load C = 30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - I/O compensation cell enabled


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (CK, SD, WS).


**Table 107. I** **[2]** **S dynamic characteristics** **[(1)]**



|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|fMCK|I2S Main clock output|-|256x8K|256FS|MHz|
|fCK|I2S clock frequency|Master data|-|64FS|MHz|
|fCK|I2S clock frequency|Slave data|-|64FS|64FS|
|tv(WS)|WS valid time|Master mode|-|3.5|ns|
|th(WS)|WS hold time|Master mode|0|-|-|
|tsu(WS)|WS setup time|Slave mode|1|-|-|
|th(WS)|WS hold time|Slave mode|1|-|-|
|tsu(SD_MR)|Data input setup time|Master receiver|1|-|-|
|tsu(SD_SR)|tsu(SD_SR)|Slave receiver|1|-|-|
|th(SD_MR)|Data input hold time|Master receiver|4|-|-|
|th(SD_SR)|th(SD_SR)|Slave receiver|2|-|-|
|tv(SD_ST)|Data output valid time|Slave transmitter (after enable edge)|-|20|20|
|tv(SD_MT)|tv(SD_MT)|Master transmitter (after enable edge)|-|3|3|
|th(SD_ST)|Data output hold time|Slave transmitter (after enable edge)|9|-|-|
|th(SD_MT)|th(SD_MT)|Master transmitter (after enable edge)|0|-|-|


1. Guaranteed by characterization results.





DS12110 Rev 10 195/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 52. I** **[2]** **S slave timing diagram (Philips protocol)** **[(1)]**


1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.


**Figure 53. I** **[2]** **S master timing diagram (Philips protocol)** **[(1)]**


1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.


196/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**SAI characteristics**


Unless otherwise specified, the parameters given in _Table 108_ for SAI are derived from tests
performed under the ambient temperature, f PCLKx frequency and VDD supply voltage
conditions summarized in _Table 24: General operating conditions_, with the following
configuration:


      - Output speed is set to OSPEEDRy[1:0] = 10


      - Capacitive load C=30 pF


      - Measurement points are performed at CMOS levels: 0.5V DD


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (SCK,SD,WS).


**Table 108. SAI characteristics** **[(1)]**





















|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|fMCK|SAI Main clock output|-|256 x 8K|256xFs|MHz|
|FCK|SAI clock frequency(2)|Master data: 32 bits|-|128xFs(3)|MHz|
|FCK|SAI clock frequency(2)|Slave data: 32 bits|-|128xFs|128xFs|
|tv(FS)|FS valid time|Master mode<br>2.7≤VDD≤3.6V|-|15|ns|
|tv(FS)|FS valid time|Master mode<br>1.71≤VDD≤3.6V|-|20|20|
|tsu(FS)|FS setup time|Slave mode|7|-|-|
|th(FS)|FS hold time|Master mode|1|-|-|
|th(FS)|FS hold time|Slave mode|1|-|-|
|tsu(SD_A_MR)|Data input setup time|Master receiver|0.5|-|-|
|tsu(SD_B_SR)|tsu(SD_B_SR)|Slave receiver|1|-|-|
|th(SD_A_MR)|Data input hold time|Master receiver|3.5|-|-|
|th(SD_B_SR)|th(SD_B_SR)|Slave receiver|2|-|-|
|tv(SD_B_ST)|Data output valid time|Slave transmitter (after enable edge)<br>2.7≤VDD≤3.6V|-|17|ns|
|tv(SD_B_ST)|Data output valid time|Slave transmitter (after enable edge)<br>1.62≤VDD≤3.6V|-|20|20|
|th(SD_B_ST)|Data output hold time|Slave transmitter (after enable edge)|7|-|-|
|tv(SD_A_MT)|Data output valid time|Master transmitter (after enable edge)<br>2.7≤VDD≤3.6V|-|17|17|
|tv(SD_A_MT)|Data output valid time|Master transmitter (after enable edge)<br>1.62≤VDD≤3.6V|-|20|20|
|th(SD_A_MT)|Data output hold time|Master transmitter (after enable edge)|7.55|-|-|


1. Guaranteed by characterization results.


2. APB clock frequency must be at least twice SAI clock frequency.


3. With F S =192 kHz.


DS12110 Rev 10 197/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 54. SAI master timing waveforms**



















**Figure 55. SAI slave timing waveforms**























**MDIO characteristics**


**Table 109. MDIO Slave timing** **parameters**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|FsDC|Management data clock|-|-|40|MHz|
|td(MDIO)|Management data input/output**output valid time**|7|8|20|ns|
|tsu(MDIO)|Management data input/output**setup time**|4|-|-|-|
|th(MDIO)|Management data input/output**hold time**|1|-|-|-|



The MDIO controller is mapped on APB2 domain. The frequency of the APB bus should at
least 1.5 times the MDC frequency: F PCLK2 ≥ 1.5 * F MDC .


198/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 56. MDIO Slave timing diagram**









**SD/SDIO MMC card host interface (SDMMC) characteristics**


Unless otherwise specified, the parameters given in _Table 110_ for the SDIO/MMC interface
are derived from tests performed under the ambient temperature, f PCLK2 frequency and V DD
supply voltage conditions summarized in _Table 24: General operating conditions_, with the
following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Capacitive load C = 30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - I/O compensation cell enabled


      - HSLV activated when VDD ≤ 2.7 V


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output
characteristics.


**Table 110. Dynamic characteristics: SD / MMC characteristics, V** **DD** **= 2.7 to 3.6 V** **[(1)(2)]**









|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPP|Clock frequency in data transfer mode|-|0|-|125|MHz|
|tW(CKL)|Clock low time|fPP =50 MHz|9.5|10.5|-|ns|
|tW(CKH)|Clock high time|Clock high time|8.5|9.5|-|-|
|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D inputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|
|tISU|Input setup time HS|fPP ≥50 MHz|3|-|-|ns|
|tIH|Input hold time HS|Input hold time HS|0.5|-|-|-|
|tIDW<br>(3)|Input valid window (variable window)|Input valid window (variable window)|3|-|-|-|
|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|**CMD, D outputs (referenced to CK) in MMC and SD HS/SDR/DDR mode**|
|tOV|Output valid time HS|fPP ≥50 MHz|-|3.5|5|ns|
|tOH|Output hold time HS|Output hold time HS|2|-|-|-|


DS12110 Rev 10 199/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 110. Dynamic characteristics: SD / MMC characteristics, V** **DD** **= 2.7 to 3.6 V** **[(1)(2)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|
|tISUD|Input setup time SD|fPP =25 MHz|3|-|-|ns|
|tIHD|Input hold time SD|Input hold time SD|0.5|-|-|-|
|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|
|tOVD|Output valid default time SD|fPP =25 MHz|-|1|2|ns|
|tOHD|Output hold default time SD|Output hold default time SD|0|-|-|-|



1. Guaranteed by characterization results.


2. Above 100 MHz, C L = 20 pF.


3. The minimum window of time where the data needs to be stable for proper sampling in tuning mode.


**Table 111. Dynamic characteristics: eMMC characteristics, V** **DD** **= 1.71 to 1.9 V** **[(1)(2)]**









|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPP|Clock frequency in data transfer mode|-|0|-|120|MHz|
|tW(CKL)|Clock low time|fPP =50 MHz|9.5|10.5|-|ns|
|tW(CKH)|Clock high time|Clock high time|8.5|9.5|-|-|
|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|
|tISU|Input setup time HS|fPP ≥50 MHz|2.5|-|-|ns|
|tIH|Input hold time HS|Input hold time HS|1|-|-|-|
|tIDW<br>(3)|Input valid window (variable window)|Input valid window (variable window)|3.5|-|-|-|
|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|
|tOV|Output valid time HS|fPP ≥50 MHz|-|5|7|ns|
|tOH|Output hold time HS|Output hold time HS|3|-|-|-|


1. Guaranteed by characterization results.


2. C L = 20 pF.


3. The minimum window of time where the data needs to be stable for proper sampling in tuning mode.


200/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 57. SDIO high-speed mode**


**Figure 58. SD default mode**


**Figure 59. DDR mode**




















|Col1|Col2|
|---|---|
|IO|1|


|Col1|Col2|thr(IN)|
|---|---|---|
||||
|IO3|I|O4|





**CAN (controller area network) interface**


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (FDCANx_TX and FDCANx_RX).


DS12110 Rev 10 201/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**USB OTG_FS characteristics**


The USB interface is fully compliant with the USB specification version 2.0 and is USB-IF
certified (for Full-speed device operation).


**Table 112. USB OTG_FS electrical characteristics**












|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD33USB|USB transceiver operating<br>voltage|-|3.0(1)|-|3.6|V|
|RPUI|Embedded USB_DP pull-up<br>value during idle|-|900|1250|1600|Ω|
|RPUR|Embedded USB_DP pull-up<br>value during reception|-|1400|2300|3200|3200|
|ZDRV|Output driver impedance(2)|Driver high<br>and low|28|36|44|44|



1. The USB functionality is ensured down to 2.7 V but not the full USB electrical characteristics which are
degraded in the 2.7 to 3.0 V voltage range.


2. No external termination series resistors are required on USB_DP (D+) and USB_DM (D-); the matching
impedance is already included in the embedded driver.


**USB OTG_HS characteristics**


Unless otherwise specified, the parameters given in _Table 113_ for ULPI are derived from
tests performed under the ambient temperature, f rcc_c_ck frequency and V DD supply voltage
conditions summarized in _Table 24: General operating conditions_, with the following
configuration:


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Capacitive load C = 20 pF


      - Measurement points are done at CMOS levels: 0.5V DD .


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output
characteristics.


**Table 113. Dynamic characteristics: USB ULPI** **[(1)]**





|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tSC|Control in (ULPI_DIR, ULPI_NXT) setup time|-|0.5|-|-|ns|
|tHC|Control in (ULPI_DIR, ULPI_NXT) hold time|-|6.5|-|-|-|
|tSD|Data in setup time|-|2.5|-|-|-|
|tHD|Data in hold time|-|0|-|-|-|
|tDC/tDD|Data/control output delay|2.7 V < VDD< 3.6 V,<br>CL = 20 pF|-|6.5|8.5|8.5|
|tDC/tDD|Data/control output delay|-|-|6.5|13|13|
|tDC/tDD|Data/control output delay|1.7 V < VDD< 3.6 V,<br>CL = 15 pF|-|-|-|-|


1. Guaranteed by characterization results.





202/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 60. ULPI timing diagram**













**Ethernet characteristics**


Unless otherwise specified, the parameters given in _Table 114_, _Table 115_ and _Table 116_ for
SMI, RMII and MII are derived from tests performed under the ambient temperature,
f rcc_c_ck frequency summarized in _Table 24: General operating conditions_, with the following
configuration:


- Output speed is set to OSPEEDRy[1:0] = 10


- Capacitive load C = 20 pF


- Measurement points are done at CMOS levels: 0.5V DD .


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output
characteristics.


_Table 114_ gives the list of Ethernet MAC signals for the SMI and _Figure 61_ shows the
corresponding timing diagram.


**Table 114. Dynamics characteristics: Ethernet MAC signals for SMI** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tMDC|MDC cycle time(2.5 MHz)|400|400|403|ns|
|Td(MDIO)|Write data valid time|1|1.5|3|3|
|tsu(MDIO)|Read data setup time|8|-|-|-|
|th(MDIO)|Read data hold time|0|-|-|-|



1. Guaranteed by characterization results.


DS12110 Rev 10 203/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Figure 61. Ethernet SMI timing diagram**


_Table 115_ gives the list of Ethernet MAC signals for the RMII and _Figure 62_ shows the
corresponding timing diagram.


**Table 115. Dynamics characteristics: Ethernet MAC signals for RMII** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tsu(RXD)|Receive data setup time|2|-|-|ns|
|tih(RXD)|Receive data hold time|3|-|-|-|
|tsu(CRS)|Carrier sense setup time|2.5|-|-|-|
|tih(CRS)|Carrier sense hold time|2|-|-|-|
|td(TXEN)|Transmit enable valid delay time|4|4.5|7|7|
|td(TXD)|Transmit data valid delay time|7|7.5|11.5|11.5|



1. Guaranteed by characterization results.


**Figure 62. Ethernet RMII timing diagram**







_Table 116_ gives the list of Ethernet MAC signals for MII and _Figure 63_ shows the
corresponding timing diagram.


204/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Table 116. Dynamics characteristics: Ethernet MAC signals for MII** **[(1)]**



|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tsu(RXD)|Receive data setup time|2|-|-|ns|
|tih(RXD)|Receive data hold time|3|-|-|-|
|tsu(DV)|Data valid setup time|1.5|-|-|-|
|tih(DV)|Data valid hold time|1|-|-|-|
|tsu(ER)|Error setup time|1.5|-|-|-|
|tih(ER)|Error hold time|0.5|-|-|-|
|td(TXEN)|Transmit enable valid delay time|4.5|6.5|11|11|
|td(TXD)|Transmit data valid delay time|7|7.5|15|15|


1. Guaranteed by characterization results.

















**6.3.33** **JTAG/SWD interface characteristics**


Unless otherwise specified, the parameters given in _Table 117_ and _Table 118_ for JTAG/SWD
are derived from tests performed under the ambient temperature, f rcc_c_ck frequency and
V DD supply voltage summarized in _Table 24: General operating conditions_, with the
following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 0x10


      - Capacitive load C=30 pF


      - Measurement points are done at CMOS levels: 0.5V DD


Refer to _Section 6.3.15: I/O port characteristics_ for more details on the input/output
characteristics.


DS12110 Rev 10 205/357



320


**Electrical characteristics (rev Y)** **STM32H742xI/G STM32H743xI/G**


**Table 117. Dynamics JTAG characteristics** **[(1)]**

















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fpp|TCK clock<br>frequency|2.7 V <VDD< 3.6 V|-|-|37|MHz|
|1/tc(TCK)|1/tc(TCK)|1.62 V <VDD< 3.6 V|-|-|27.5|27.5|
|tisu(TMS)|TMS input<br>setup time|-|2|-|-|ns|
|tih(TMS)|TMS input<br>hold time|-|1|-|-|-|
|tisu(TDI)|TDI input<br>setup time|-|1.5|-|-|-|
|tih(TDI)|TDI input<br>hold time|-|1|-|-|-|
|tov (TDO)|TDO output<br>valid time|2.7 V <VDD< 3.6 V|-|8|13.5|13.5|
|tov (TDO)|TDO output<br>valid time|1.62 V <VDD< 3.6 V|-|8|18|18|
|toh(TDO)|TDO output<br>hold time|-|7|-|-|-|


1. Guaranteed by characterization results.


**Table 118. Dynamics SWD characteristics** **[(1)]**

















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fpp|SWCLK<br>clock<br>frequency|2.7 V <VDD< 3.6 V|-|-|71|MHz|
|1/tc(SWCLK)|1/tc(SWCLK)|1.62 V <VDD< 3.6 V|-|-|55.5|55.5|
|tisu(SWDIO)|SWDIO input<br>setup time|-|2.5|-|-|ns|
|tih(SWDIO)|SWDIO input<br>hold time|-|1|-|-|-|
|tov (SWDIO)|SWDIO<br>output valid<br>time|2.7 V <VDD< 3.6 V|-|8.5|14|14|
|tov (SWDIO)|SWDIO<br>output valid<br>time|1.62 V <VDD< 3.6 V|-|8.5|18|18|
|toh(SWDIO)|SWDIO<br>output hold<br>time|-|8|-|-|-|


1. Guaranteed by characterization results.


206/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev Y)**


**Figure 64. JTAG timing diagram**








|Col1|Col2|
|---|---|
|||
|||





**Figure 65. SWD timing diagram**











DS12110 Rev 10 207/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**

#### **7 Electrical characteristics (rev V)**

###### **7.1 Parameter conditions**


Unless otherwise specified, all voltages are referenced to V SS .


**7.1.1** **Minimum and maximum values**


Unless otherwise specified the minimum and maximum values are guaranteed in the worst
conditions of junction temperature, supply voltage and frequencies by tests in production on
100% of the devices with an junction temperature at T J = 25 °C and T J = T Jmax (given by the
selected temperature range).


Data based on characterization results, design simulation and/or technology characteristics
are indicated in the table footnotes. Based on characterization, the minimum and maximum
values refer to sample tests and represent the mean value plus or minus three times the
standard deviation (mean±3σ).


**7.1.2** **Typical values**


Unless otherwise specified, typical data are based on T J = 25 °C, V DD = 3.3 V (for the
1.7 V ≤ V DD ≤ 3.6 V voltage range). They are given only as design guidelines and are not
tested.


Typical ADC accuracy values are determined by characterization of a batch of samples from
a standard diffusion lot over the full temperature range, where 95% of the devices have an
error less than or equal to the value indicated (mean±2σ) .


**7.1.3** **Typical curves**


Unless otherwise specified, all typical curves are given only as design guidelines and are
not tested.


**7.1.4** **Loading capacitor**


The loading conditions used for pin parameter measurement are shown in _Figure 66_ .


**7.1.5** **Pin input voltage**


The input voltage measurement on a pin of the device is described in _Figure 67_ .







208/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.1.6** **Power supply scheme**


**Figure 68. Power supply scheme**
























|Col1|Col2|
|---|---|
||IOs|


|Col1|Core domain (V )<br>CORE|Col3|
|---|---|---|
||D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>D1 domain<br>(CPU, peripherals,<br>RAM)<br>Level shifter<br>Flash<br>D2 domain<br>(peripherals,<br>RAM)<br>Power<br>switch<br>Power<br>switch<br>IO<br>logic|D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>D1 domain<br>(CPU, peripherals,<br>RAM)<br>Level shifter<br>Flash<br>D2 domain<br>(peripherals,<br>RAM)<br>Power<br>switch<br>Power<br>switch<br>IO<br>logic|
||D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>D1 domain<br>(CPU, peripherals,<br>RAM)<br>Level shifter<br>Flash<br>D2 domain<br>(peripherals,<br>RAM)<br>Power<br>switch<br>Power<br>switch<br>IO<br>logic|D3 domain<br>(System<br>logic,<br>EXTI,<br>Peripherals,<br>RAM)<br>IO<br>logic|
||Level shifter|IO<br>logic|
||||












|Col1|BKUP<br>IOs|
|---|---|
|||














|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||



1. N corresponds to the number of VDD pins available on the package.



2. A tolerance of +/- 20% is acceptable on decoupling capacitors.


**Caution:** Each power supply pair (V DD /V SS, V DDA /V SSA ...) must be decoupled with filtering ceramic
capacitors as shown above. These capacitors must be placed as close as possible to, or
below, the appropriate pins on the underside of the PCB to ensure good operation of the


DS12110 Rev 10 209/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


device. It is not recommended to remove filtering capacitors to reduce PCB size or cost.
This might cause incorrect operation of the device.


**7.1.7** **Current consumption measurement**


**Figure 69. Current consumption measurement scheme**

###### **7.2 Absolute maximum ratings**


Stresses above the absolute maximum ratings listed in _Table 119: Voltage characteristics_,
_Table 120: Current characteristics_, and _Table 121: Thermal characteristics_ may cause
permanent damage to the device. These are stress ratings only and the functional operation
of the device at these conditions is not implied. Exposure to maximum rating conditions for
extended periods may affect device reliability. Device mission profile (application conditions)
is compliant with JEDEC JESD47 Qualification Standard, extended mission profiles are
available on demand.


**Table 119. Voltage characteristics** **[(1)]**







|Symbols|Ratings|Min|Max|Unit|
|---|---|---|---|---|
|VDDX- VSS|External main supply voltage (including VDD, <br>VDDLDO, VDDA, VDD33USB, VBAT)|−0.3|4.0|V|
|VIN<br>(2)|Input voltage on FT_xxx pins|VSS−0.3|Min(VDD, VDDA, <br>VDD33USB, VBAT) <br>+4.0(3)(4)|V|
|VIN<br>(2)|Input voltage on TT_xx pins|VSS-0.3|4.0|V|
|VIN<br>(2)|Input voltage on BOOT0 pin|VSS|9.0|V|
|VIN<br>(2)|Input voltage on any other pins|VSS-0.3|4.0|V|
||∆VDDX||Variations between different VDDX power pins<br>of the same domain|-|50|mV|
||VSSx-VSS||Variations between all the different ground pins|-|50|mV|


1. All main power (V DD, V DDA, V DD33USB, V BAT ) and ground (V SS, V SSA ) pins must always be connected to
the external power supply, in the permitted range.


2. V IN maximum must always be respected. Refer to _Table 156: I/O current injection susceptibility_ for the
maximum allowed injected current values.


210/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


3. This formula has to be applied on power supplies related to the IO structure described by the pin definition
table.


4. To sustain a voltage higher than 4V the internal pull-up/pull-down resistors must be disabled.


**Table 120. Current characteristics**
























|Symbols|Ratings|Max|Unit|
|---|---|---|---|
|ΣIVDD|Total current into sum of all VDD power lines (source)(1)|620|mA|
|ΣIVSS|Total current out of sum of all VSS ground lines (sink)(1)|620|620|
|IVDD|Maximum current into each VDD power pin (source)(1)|100|100|
|IVSS|Maximum current out of each VSS ground pin (sink)(1)|100|100|
|IIO|Output current sunk by any I/O and control pin, except Px_C|20|20|
|IIO|Output current sunk by Px_C pins|1|1|
|ΣI(PIN)|Total output current sunk by sum of all I/Os and control pins(2)|140|140|
|ΣI(PIN)|Total output current sourced by sum of all I/Os and control pins(2)|140|140|
|IINJ(PIN)<br>(3)(4)|Injected current on FT_xxx, TT_xx, RST and B pins except PA4,<br>PA5|−5/+0|−5/+0|
|IINJ(PIN)<br>(3)(4)|Injected current on PA4, PA5|−0/0|−0/0|
|ΣIINJ(PIN)|Total injected current (sum of all I/Os and control pins)(5)|±25|±25|



1. All main power (V DD, V DDA, V DD33USB ) and ground (V SS, V SSA ) pins must always be connected to the
external power supplies, in the permitted range.


2. This current consumption must be correctly distributed over all I/Os and control pins. The total output
current must not be sunk/sourced between two consecutive power supply pins referring to high pin count
QFP packages.


3. Positive injection is not possible on these I/Os and does not occur for input voltages lower than the
specified maximum value.


4. A positive injection is induced by V IN >V DD while a negative injection is induced by V IN <V SS . I INJ(PIN) must
never be exceeded. Refer also to _Table 119: Voltage characteristics_ for the maximum allowed input voltage
values.


5. When several inputs are submitted to a current injection, the maximum ∑I INJ(PIN) is the absolute sum of the
positive and negative injected currents (instantaneous values).


**Table 121. Thermal characteristics**

|Symbol|Ratings|Value|Unit|
|---|---|---|---|
|TSTG|Storage temperature range|−65 to +150|°C|
|TJ|Maximum junction temperature|125|125|



DS12110 Rev 10 211/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**

###### **7.3 Operating conditions**


**7.3.1** **General operating conditions**


**Table 122. General operating conditions**
























|Symbol|Parameter|Operating<br>conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD|Standard operating voltage|-|1.62(1)|-|3.6|V|
|VDDLDO|Supply voltage for the internal<br>regulator|VDDLDO≤ VDD|1.62(1)|-|3.6||
|VDD33USB|Standard operating voltage, USB<br>domain|USB used|3.0|-|3.6|V|
|VDD33USB|Standard operating voltage, USB<br>domain|USB not used|0|-|3.6|3.6|
|VDDA|Analog operating voltage|ADC or COMP used|1.62|-|3.6|3.6|
|VDDA|Analog operating voltage|DAC used|1.8|-|-|-|
|VDDA|Analog operating voltage|OPAMP used|2.0|-|-|-|
|VDDA|Analog operating voltage|VREFBUF used|1.8|-|-|-|
|VDDA|Analog operating voltage|ADC, DAC, OPAMP,<br>COMP, VREFBUF not<br>used|0|-|-|-|
|VIN|I/O Input voltage|TT_xx I/O|−0.3|-|VDD+0.3|VDD+0.3|
|VIN|I/O Input voltage|BOOT0|0|-|9|9|
|VIN|I/O Input voltage|All I/O except BOOT0<br>and TT_xx|−0.3|-|Min(VDD, VDDA, <br>VDD33USB) <br>+3.6V <<br>5.5V(2)(3)|Min(VDD, VDDA, <br>VDD33USB) <br>+3.6V <<br>5.5V(2)(3)|
|VCORE|Internal regulator ON (LDO)|VOS3 (max frequency<br>200 MHz)|0.95|1.0|1.05|V|
|VCORE|Internal regulator ON (LDO)|VOS2 (max frequency<br>300 MHz)|1.05|1.10|1.15|1.15|
|VCORE|Internal regulator ON (LDO)|VOS1 (max frequency<br>400 MHz)|1.15|1.20|1.26|1.26|
|VCORE|Internal regulator ON (LDO)|VOS0(4) (max<br>frequency 480 MHz(5))|1.26|1.35|1.40|1.40|
|VCORE|Regulator OFF: external VCORE <br>voltage must be supplied from external<br>regulator on two VCAP pins|VOS3 (max frequency<br>200 MHz)|0.98|1.03|1.08|1.08|
|VCORE|Regulator OFF: external VCORE <br>voltage must be supplied from external<br>regulator on two VCAP pins|VOS2 (max frequency<br>300 MHz)|1.08|1.13|1.17|1.17|
|VCORE|Regulator OFF: external VCORE <br>voltage must be supplied from external<br>regulator on two VCAP pins|VOS1 (max frequency<br>400 MHz)|1.17|1.23|1.37|1.37|
|VCORE|Regulator OFF: external VCORE <br>voltage must be supplied from external<br>regulator on two VCAP pins|VOS0 (max frequency<br>480 MHz(5))|1.37|1.38|1.40|1.40|



212/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 122. General operating conditions (continued)**











|Symbol|Parameter|Operating<br>conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fCPU|Arm® Cortex®-M7 clock frequency|VOS3|-|-|200|MHz|
|fCPU|Arm® Cortex®-M7 clock frequency|VOS2|-|-|300|300|
|fCPU|Arm® Cortex®-M7 clock frequency|VOS1|-|-|400|400|
|fCPU|Arm® Cortex®-M7 clock frequency|VOS0|-|-|480(5)|480(5)|
|fHCLK|AHB clock frequency|VOS3|-|-|100|100|
|fHCLK|AHB clock frequency|VOS2|-|-|150|150|
|fHCLK|AHB clock frequency|VOS1|-|-|200|200|
|fHCLK|AHB clock frequency|VOS0|-|-|240(5)|240(5)|
|fPCLK|APB clock frequency|VOS3|-|-|50(6)|50(6)|
|fPCLK|APB clock frequency|VOS2|-|-|75|75|
|fPCLK|APB clock frequency|VOS1|-|-|100|100|
|fPCLK|APB clock frequency|VOS0|-|-|120(5)|120(5)|
|TA|Ambient temperature for the suffix 6<br>version|Maximum power dissipation|Maximum power dissipation|–40|85|°C|
|TA|Ambient temperature for the suffix 6<br>version|Low-power dissipation(7)|Low-power dissipation(7)|–40|105|105|
|TA|Ambient temperature for the suffix 3<br>version|Maximum power dissipation|Maximum power dissipation|–40|125|125|
|TA|Ambient temperature for the suffix 3<br>version|Low-power dissipation(4)|Low-power dissipation(4)|–40|130|130|
|TJ|Junction temperature range|Suffix 6 version|Suffix 6 version|–40|125|°C|


1. When RESET is released functionality is guaranteed down to V BOR0 min


2. This formula has to be applied on power supplies related to the IO structure described by the pin definition table.


3. For operation with voltage higher than Min (V DD, V DDA, V DD33USB ) +0.3V, the internal Pull-up and Pull-Down resistors must
be disabled.


4. VOS0 is available only when the LDO regulator is ON.


5. T Jmax = 105 °C.


6. Maximum APB clock frequency when at least one peripheral is enabled.


7. In low-power dissipation state, T A can be extended to this range as long as T J does not exceed T Jmax (see _Section 8.10:_
_Thermal characteristics_ ).


**Table 123. Supply voltage and maximum frequency configuration**

|Power scale|V source<br>CORE|Max T (°C)<br>J|Max frequency (MHz)|Min V (V)<br>DDLDO|
|---|---|---|---|---|
|VOS0|LDO|105|480|1.7|
|VOS1|LDO|125|400|1.62|
|VOS2|LDO|125|300|1.62|
|VOS3|LDO|125|200|1.62|
|SVOS4|LDO|105|N/A|1.62|
|SVOS5|LDO|105|N/A|1.62|



DS12110 Rev 10 213/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**7.3.2** **VCAP external capacitor**


Stabilization for the main regulator is achieved by connecting an external capacitor C EXT to
the VCAP pin. C EXT is specified in _Table 124_ . Two external capacitors can be connected to
VCAP pins.


**Figure 70. External capacitor C** **EXT**


1. Legend: ESR is the equivalent series resistance.


**Table 124. VCAP operating conditions** **[(1)]**

|Symbol|Parameter|Conditions|
|---|---|---|
|CEXT|Capacitance of external capacitor|2.2 µF(2)|
|ESR|ESR of external capacitor|< 100 mΩ|



1. When bypassing the voltage regulator, the two 2.2 µF V CAP capacitors are not required and should be
replaced by two 100 nF decoupling capacitors.


2. This value corresponds to CEXT typical value. A variation of +/-20% is tolerated.


**7.3.3** **Operating conditions at power-up / power-down**


Subject to general operating conditions for T A .


**Table 125. Operating conditions at power-up / power-down (regulator ON)**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tVDD|VDD rise time rate|0|∞|µs/V|
|tVDD|VDD fall time rate|10|∞|∞|
|tVDDA|VDDA rise time rate|0|∞|∞|
|tVDDA|VDDA fall time rate|10|∞|∞|
|tVDDUSB|VDDUSB rise time rate|0|∞|∞|
|tVDDUSB|VDDUSB fall time rate|10|∞|∞|


214/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.4** **Embedded reset and power control block characteristics**


The parameters given in _Table 126_ are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in _Table 122: General_
_operating conditions_ .


**Table 126. Reset and power control block characteristics**



















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tRSTTEMPO<br>(1)|Reset temporization<br>after BOR0 released|-|-|377|-|µs|
|VBOR0/POR/PDR|Brown-out reset threshold 0<br>(VPOR/VPDR thresholds)|Rising edge(1)|1.62|1.67|1.71|V|
|VBOR0/POR/PDR|Brown-out reset threshold 0<br>(VPOR/VPDR thresholds)|Falling edge|1.58|1.62|1.68|1.68|
|VBOR1|Brown-out reset threshold 1|Rising edge|2.04|2.10|2.15|2.15|
|VBOR1|Brown-out reset threshold 1|Falling edge|1.95|2.00|2.06|2.06|
|VBOR2|Brown-out reset threshold 2|Rising edge|2.34|2.41|2.47|2.47|
|VBOR2|Brown-out reset threshold 2|Falling edge|2.25|2.31|2.37|2.37|
|VBOR3|Brown-out reset threshold 3|Rising edge|2.63|2.70|2.78|2.78|
|VBOR3|Brown-out reset threshold 3|Falling edge|2.54|2.61|2.68|2.68|
|VPVD0|Programmable Voltage<br>Detector threshold 0|Rising edge|1.90|1.96|2.01|2.01|
|VPVD0|Programmable Voltage<br>Detector threshold 0|Falling edge|1.81|1.86|1.91|1.91|
|VPVD1|Programmable Voltage<br>Detector threshold 1|Rising edge|2.05|2.10|2.16|2.16|
|VPVD1|Programmable Voltage<br>Detector threshold 1|Falling edge|1.96|2.01|2.06|2.06|
|VPVD2|Programmable Voltage<br>Detector threshold 2|Rising edge|2.19|2.26|2.32|2.32|
|VPVD2|Programmable Voltage<br>Detector threshold 2|Falling edge|2.10|2.15|2.21|2.21|
|VPVD3|Programmable Voltage<br>Detector threshold 3|Rising edge|2.35|2.41|2.47|2.47|
|VPVD3|Programmable Voltage<br>Detector threshold 3|Falling edge|2.25|2.31|2.37|2.37|
|VPVD4|Programmable Voltage<br>Detector threshold 4|Rising edge|2.49|2.56|2.62|2.62|
|VPVD4|Programmable Voltage<br>Detector threshold 4|Falling edge|2.39|2.45|2.51|2.51|
|VPVD5|Programmable Voltage<br>Detector threshold 5|Rising edge|2.64|2.71|2.78|2.78|
|VPVD5|Programmable Voltage<br>Detector threshold 5|Falling edge|2.55|2.61|2.68|2.68|
|VPVD6|Programmable Voltage<br>Detector threshold 6|Rising edge|2.78|2.86|2.94|2.94|
|VPVD6|Programmable Voltage<br>Detector threshold 6|Falling edge in Run mode|2.69|2.76|2.83|2.83|
|Vhyst_BOR_PVD|Hysteresis voltage of BOR<br>(unless BOR0) and PVD|Hysteresis in Run mode|-|100|-|mV|
|IDD_BOR_PVD<br>(1)|BOR(2)(unless BOR0) and<br>PVD consumption from VDD|-|-|-|0.630|µA|


DS12110 Rev 10 215/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 126. Reset and power control block characteristics (continued)**









|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VAVM_0|Analog voltage detector for<br>VDDA threshold 0|Rising edge|1.66|1.71|1.76|V|
|VAVM_0|Analog voltage detector for<br>VDDA threshold 0|Falling edge|1.56|1.61|1.66|1.66|
|VAVM_1|Analog voltage detector for<br>VDDA threshold 1|Rising edge|2.06|2.12|2.19|2.19|
|VAVM_1|Analog voltage detector for<br>VDDA threshold 1|Falling edge|1.96|2.02|2.08|2.08|
|VAVM_2|Analog voltage detector for<br>VDDA threshold 2|Rising edge|2.42|2.50|2.58|2.58|
|VAVM_2|Analog voltage detector for<br>VDDA threshold 2|Falling edge|2.35|2.42|2.49|2.49|
|VAVM_3|Analog voltage detector for<br>VDDA threshold 3|Rising edge|2.74|2.83|2.91|2.91|
|VAVM_3|Analog voltage detector for<br>VDDA threshold 3|Falling edge|2.64|2.72|2.80|2.80|
|Vhyst_VDDA|Hysteresis of VDDA voltage<br>detector|-|-|100|-|mV|
|IDD_PVM|PVM consumption from<br>VDD(1)|-|-|-|0.25|µA|
|IDD_VDDA|Voltage detector<br>consumption on VDDA<br>(1)|Resistor bridge|-|-|2.5|µA|


1. Guaranteed by design.


2. BOR0 is enabled in all modes and its consumption is therefore included in the supply current characteristics tables (refer to
_Section 7.3.6: Supply current characteristics_ ).


**7.3.5** **Embedded reference voltage**


The parameters given in _Table 127_ are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in _Table 122: General_
_operating conditions_ .


**Table 127. Embedded reference voltage**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VREFINT|Internal reference voltages|-40°C < TJ < 125 °C,<br>VDD = 3.3 V|1.180|1.216|1.255|V|
|tS_vrefint<br>(1)(2)|ADC sampling time when<br>reading the internal reference<br>voltage|-|4.3|-|-|µs|
|tS_vbat<br>(1)(2)|VBAT sampling time when<br>reading the internal VBAT<br>reference voltage|-|9|-|-|-|
|Irefbuf<br>(2)|Reference Buffer<br>consumption for ADC|VDDA=3.3 V|9|13.5|23|µA|
|ΔVREFINT<br>(2)|Internal reference voltage<br>spread over the temperature<br>range|-40°C < TJ < 125 °C|-|5|15|mV|
|Tcoeff<br>(2)|Average temperature<br>coefficient|Average temperature<br>coefficient|-|20|70|ppm/°C|
|VDDcoeff<br>(2)|Average Voltage coefficient|3.0V < VDD < 3.6V|-|10|1370|ppm/V|



216/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 127. Embedded reference voltage (continued)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VREFINT_DIV1|1/4 reference voltage|-|-|25|-|% <br>VREFINT|
|VREFINT_DIV2|1/2 reference voltage|-|-|50|-|-|
|VREFINT_DIV3|3/4 reference voltage|-|-|75|-|-|



1. The shortest sampling time for the application can be determined by multiple iterations.


2. Guaranteed by design.


**Table 128. Internal reference voltage calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|VREFIN_CAL|Raw data acquired at temperature of 30 °C, VDDA = 3.3 V|1FF1E860 - 1FF1E861|



**7.3.6** **Supply current characteristics**


The current consumption is a function of several parameters and factors such as the
operating voltage, ambient temperature, I/O pin loading, device software configuration,
operating frequencies, I/O pin switching rate, program location in memory and executed
binary code.


The current consumption is measured as described in _Figure 69: Current consumption_
_measurement scheme_ .


All the run-mode current consumption measurements given in this section are performed
with a CoreMark code.


**Typical and maximum current consumption**


The MCU is placed under the following conditions:


      - All I/O pins are in analog input mode.


      - All peripherals are disabled except when explicitly mentioned.


      - The flash memory access time is adjusted with the minimum wait states number,
depending on the f ACLK frequency (refer to the table “Number of wait states according to
CPU clock (f rcc_c_ck ) frequency and V CORE range” available in the reference manual).

      - When the peripherals are enabled, the AHB clock frequency is the CPU frequency
divided by 2 and the APB clock frequency is AHB clock frequency divided by 2.


The parameters given in the below tables are derived from tests performed under ambient
temperature and supply voltage conditions summarized in _Table 122: General operating_
_conditions_ .


DS12110 Rev 10 217/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 129. Typical and maximum current consumption in Run mode, code with data processing**
**running from ITCM, LDO regulator ON** **[(1)]**




















|Symbol|Parameter|Conditions|Col4|f<br>HCLK<br>(MHz)|Typ|Max(2)|Col8|Col9|Col10|Unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**fHCLK **<br>**(MHz)**|**Typ**|**Tj=25**<br>**°C**|**Tj=85**<br>**°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS0|480|148|226|307|390|-|mA|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS0|400|125|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS1|400|110|168|230|296|384|384|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS1|300|84|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS2|300|76|114|170|224|297|297|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS2|216|56|88|152|205|278|278|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS2|200|53|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|200|47|71|121|164|223|223|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|180|43|64|116|159|218|218|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|168|40|63|115|158|217|217|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|144|35|55|109|153|212|212|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|60|16|36|92|135|194|194|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|25|12|24|83|126|185|185|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS0|480|226|348|439|550|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS0|400|190|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS1|400|167|256|327|416|536|536|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS1|300|135|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS2|300|122|183|248|320|419|419|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS2|200|85|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS3|200|76|116|174|233|313|313|



1. Data are in DTCM for best computation performance, the cache has no influence on consumption in this case.


2. Guaranteed by characterization results, unless otherwise specified.


218/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 130. Typical and maximum current consumption in Run mode, code with data processing**
**running from flash memory, cache ON,**
**LDO regulator ON**














|Symbol|Parameter|Conditions|Col4|f<br>HCLK<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|Unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**fHCLK **<br>**(MHz)**|**Typ**|**Tj=25**<br>**°C**|**Tj=85**<br>**°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS0|480|110|222|304|388|-|mA|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS0|400|91|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS1|400|80|162|228|294|381|381|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS1|300|61.5|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS2|300|55|111|168|222|294|294|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS2|200|38.5|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|200|34.5|69|120|163|222|222|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS0|480|220|342|436|546|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS0|400|195|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS1|400|175|264|336|424|544|544|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS1|300|135|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS2|300|120|180|246|318|418|418|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS2|200|83|-|-|-|-|-|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS3|200|75|114|173|232|312|312|



1. Guaranteed by characterization results, unless otherwise specified.


**Table 131. Typical and maximum current consumption in Run mode, code with data processing**
**running from flash memory, cache OFF,**
**LDO regulator ON**














|Symbol|Parameter|Conditions|Col4|f<br>HCLK<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|Unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**fHCLK **<br>**(MHz)**|**Typ**|**Tj=25°C**|**Tj=85°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS0|480|87|157|259|342|453|mA|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS1|400|73|123|201|267|355|355|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS2|300|52|85|150|204|277|277|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>disabled|VOS3|200|34|54|109|152|212|212|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS0|480|168|276|390|504|658|658|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS1|400|135|224|308|397|519|519|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS2|300|100|154|228|301|401|401|
|IDD|Supply<br>current in<br>Run mode|All<br>peripherals<br>enabled|VOS3|200|70|103|167|226|307|307|



1. Guaranteed by characterization results, unless otherwise specified.


DS12110 Rev 10 219/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 132. Typical and maximum current consumption batch acquisition mode,**
**LDO regulator ON**


















|Symbol|Parameter|Conditions|Col4|f<br>HCLK<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|Unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**fHCLK **<br>**(MHz)**|**Typ**|**Tj=25°C**|** Tj=85°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD|Supply<br>current in<br>batch<br>acquisition<br>mode|D1<br>Standby,<br>D2<br>Standby,<br>D3 Run|VOS3|64|2.7|4.7|12.9|19.0|27.5|mA|
|IDD|Supply<br>current in<br>batch<br>acquisition<br>mode|D1<br>Standby,<br>D2<br>Standby,<br>D3 Run|VOS3|8|1.1|-|-|-|-|-|
|IDD|Supply<br>current in<br>batch<br>acquisition<br>mode|D1 Stop,<br>D2 Stop,<br>D3 Run|VOS3|64|5.4|18.4|83.7|132.6|202.4|202.4|
|IDD|Supply<br>current in<br>batch<br>acquisition<br>mode|D1 Stop,<br>D2 Stop,<br>D3 Run|VOS3|8|3.8|-|-|-|-|-|



1. Guaranteed by characterization results, unless otherwise specified.


**Table 133. Typical and maximum current consumption in Stop, LDO regulator ON**


















|Symbol|Parameter|Conditions|Col4|Typ|Max(1)|Col7|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**Typ**|**Tj=25°C**|**Tj=85°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD (Stop)|D1 Stop,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS5|1.27|6.3|42.5|72.0|-|mA|
|IDD (Stop)|D1 Stop,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS4|1.96|9.4|57.4|94.6|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS3|2.78|13.8|75.9|121.3|183.8|183.8|
|IDD (Stop)|D1 Stop,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>ON, no<br>IWDG|SVOS5|1.27|6.3|42.5|72.0|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>ON, no<br>IWDG|SVOS4|2.25|9.8|57.9|95.2|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>ON, no<br>IWDG|SVOS3|3.07|14.1|76.4|122.0|184.8|184.8|
|IDD (Stop)|D1 Stop,<br>D2 Standby,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS5|0.91|4.6|30.4|51.2|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Standby,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS4|1.42|6.8|41.1|67.3|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Standby,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS3|2.02|10.0|54.4|86.6|130.0|130.0|
|IDD (Stop)|D1 Stop,<br>D2 Standby,<br>D3 Stop|Flash<br>memory<br>ON, no<br>IWDG|SVOS5|0.91|4.6|30.4|51.2|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Standby,<br>D3 Stop|Flash<br>memory<br>ON, no<br>IWDG|SVOS4|1.70|7.2|41.5|67.9|-|-|
|IDD (Stop)|D1 Stop,<br>D2 Standby,<br>D3 Stop|Flash<br>memory<br>ON, no<br>IWDG|SVOS3|2.31|10.3|54.9|87.1|130.8|130.8|
|IDD (Stop)|D1 Standby,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS5|0.49|2.4|16.5|28.0|-|-|
|IDD (Stop)|D1 Standby,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS4|0.76|3.6|22.2|36.6|-|-|
|IDD (Stop)|D1 Standby,<br>D2 Stop,<br>D3 Stop|Flash<br>memory<br>OFF, no<br>IWDG|SVOS3|1.10|5.3|29.3|46.9|71.2|71.2|
|IDD (Stop)|D1 Standby,<br>D2 Standby,<br>D3 Stop|D1 Standby,<br>D2 Standby,<br>D3 Stop|SVOS5|0.15|0.7|4.3|7.3|-|-|
|IDD (Stop)|D1 Standby,<br>D2 Standby,<br>D3 Stop|D1 Standby,<br>D2 Standby,<br>D3 Stop|SVOS4|0.22|1.0|5.8|9.6|-|-|
|IDD (Stop)|D1 Standby,<br>D2 Standby,<br>D3 Stop|D1 Standby,<br>D2 Standby,<br>D3 Stop|SVOS3|0.35|1.5|7.8|12.3|18.6|18.6|



1. Guaranteed by characterization results, unless otherwise specified.


220/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 134. Typical and maximum current consumption in Sleep mode, LDO regulator**














|Symbol|Parameter|Conditions|Col4|f<br>HCLK<br>(MHz)|Typ|Max(1)|Col8|Col9|Col10|Unit|
|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**fHCLK **<br>**(MHz)**|**Typ**|**Tj=25**<br>**°C**|**Tj=85**<br>**°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS0|480|50.7|96.3|253.4|366.1|-|mA|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS0|400|43.4|87.8|245.5|357.9|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS1|400|35.3|66.5|181.3|265.8|379.6|379.6|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS1|300|27.9|-|-|-|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS2|300|24.6|47.3|139.1|207.3|300.4|300.4|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS2|200|18.8|-|-|-|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>disabled|VOS3|200|16.5|33.6|106.4|160.9|236.1|236.1|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS0|480|136.0|194.7|348.5|464.4|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS0|400|115.0|169.0|325.9|441.7|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS1|400|97.7|138.2|251.3|338.4|456.4|456.4|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS1|300|74.9|-|-|-|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS2|300|67.3|95.8|187.6|257.9|354.1|354.1|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS2|200|52.8|-|-|-|-|-|
|IDD (Sleep)|Supply<br>current in<br>Sleep mode|All<br>peripherals<br>enabled|VOS3|200|47.1|69.3|141.4|197.7|275.1|275.1|



1. Guaranteed by characterization results, unless otherwise specified.


**Table 135. Typical and maximum current consumption in Standby**
















|Symbol|Parameter|Conditions|Col4|Typ|Col6|Col7|Col8|Max(1)|Col10|Col11|Col12|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**1.62 V**|**2.4 V**|**3 V**|**3.3 V**|**3 V**|**3 V**|**3 V**|**3 V**|**3 V**|
|**Symbol**|**Parameter**|**Backup**<br>**SRAM**|**RTC**<br>**and**<br>**LSE**|**RTC**<br>**and**<br>**LSE**|**RTC**<br>**and**<br>**LSE**|**RTC**<br>**and**<br>**LSE**|**RTC**<br>**and**<br>**LSE**|**Tj=25**<br>**°C**|**Tj=85**<br>**°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|OFF|OFF|1,92|1,95|2,06|2,16|4|18|40|90|µA|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|ON|OFF|3,33|3,44|3,6|3,79|8.2|47|83|141|141|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|OFF|ON|2,43|2,57|2,77|2,95|-|-|-|-|-|
|IDD<br>(Standby)|Supply<br>current in<br>Standby<br>mode|ON|ON|3,82|4,05|4,31|4,55|-|-|-|-|-|



1. Guaranteed by characterization results, unless otherwise specified.


DS12110 Rev 10 221/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


















|Col1|Table 1|136. Typical and|Col4|maximum current consum|Col6|Col7|Col8|mption in VBAT mode|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Conditions**|**Conditions**|**Typ**|**Typ**|**Typ**|**Typ**|**Max(1) **|**Max(1) **|**Max(1) **|**Max(1) **|**Unit**|
|**Symbol**|**Parameter**|**Backup**<br>**SRAM**|**RTC**<br>**and**<br>**LSE**|**1.2 V**|**2 V**|**3 V**|**3.4 V**|**3 V**|**3 V**|**3 V**|**3 V**|**3 V**|
|**Symbol**|**Parameter**|**Backup**<br>**SRAM**|**RTC**<br>**and**<br>**LSE**|**1.2 V**|**2 V**|**3 V**|**3.4 V**|**Tj=25**<br>**°C**|**Tj=85**<br>**°C**|**Tj=105**<br>**°C**|**Tj=125**<br>**°C**|**Tj=125**<br>**°C**|
|IDD<br>(VBAT)|Supply<br>current in<br>VBAT mode|OFF|OFF|0,02|0,02|0,03|0,05|0,5|4,1|10|24|µA|
|IDD<br>(VBAT)|Supply<br>current in<br>VBAT mode|ON|OFF|1,33|1,45|1,58|1,7|4,4|22|48|87|87|
|IDD<br>(VBAT)|Supply<br>current in<br>VBAT mode|OFF|ON|0,46|0,57|0,75|0,87|-|-|-|-|-|
|IDD<br>(VBAT)|Supply<br>current in<br>VBAT mode|ON|ON|1,77|2|2,3|2,5|-|-|-|-|-|



1. Guaranteed by characterization results, unless otherwise specified.


**I/O system current consumption**


The current consumption of the I/O system has two components: static and dynamic.


**I/O static current consumption**


All the I/Os used as inputs with pull-up or pull-down generate a current consumption when
the pin is externally held low. The value of this current consumption can be simply computed
by using the pull-up/pull-down resistors values given in _Table 157: I/O static characteristics_ .


For the output pins, any internal or external pull-up or pull-down, and any external load must
also be considered to estimate the current consumption.


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


222/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**I/O dynamic current consumption**


In addition to the internal peripheral current consumption (see _Table 137: Peripheral current_
_consumption in Run mode_ ), the I/Os used by an application also contribute to the current
consumption. When an I/O pin switches, it uses the current from the MCU supply voltage to
supply the I/O pin circuitry and to charge/discharge the internal or external capacitive load
connected to the pin:


I = V × f × C
SW DDx SW L


where


I SW is the current sunk by a switching I/O to charge/discharge the capacitive load


V DDx is the MCU supply voltage


f SW is the I/O switching frequency


C L is the total capacitance seen by the I/O pin: C = C INT + C EXT


The test pin is configured in push-pull output mode and is toggled by software at a fixed
frequency.


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

– f rcc_c_ck = 480 MHz (Scale 0), f rcc_c_ck = 400 MHz (Scale 1), f rcc_c_ck = 300 MHz
(Scale 2), f rcc_c_ck = 200 MHz (Scale 3)

      - The ambient operating temperature is 25 °C and V DD =3.3 V.


DS12110 Rev 10 223/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 137. Peripheral current consumption in Run mode**

|Bus|Peripheral|VOS0|VOS1|VOS2|VOS3|Unit|
|---|---|---|---|---|---|---|
|AHB3|MDMA|4.6|3.8|3.4|3.2|µA/MHz|
|AHB3|DMA2D|2.9|2.4|2.1|1.9|1.9|
|AHB3|JPGDEC|4.1|3.7|3.4|3.1|3.1|
|AHB3|FLASH|17.0|15.0|14.0|12.0|12.0|
|AHB3|FMC registers|0.9|1.1|0.9|0.8|0.8|
|AHB3|FMC kernel|7.0|6.1|5.6|5.0|5.0|
|AHB3|QUADSPI registers|1.5|1.5|1.4|1.3|1.3|
|AHB3|QSPI kernel|1.0|0.9|0.8|0.7|0.7|
|AHB3|SDMMC1 registers|8.2|7.2|6.7|6.0|6.0|
|AHB3|SDMMC1 kernel|1.3|1.2|0.9|0.9|0.9|
|AHB3|DTCM1|7.9|6.8|6.0|5.3|5.3|
|AHB3|DTCM2|8.3|7.2|6.4|5.7|5.7|
|AHB3|ITCM|7.0|6.3|5.6|5.1|5.1|
|AHB3|D1SRAM1|13.0|11.0|9.9|8.7|8.7|
|AHB3|AHB3 bridge|35.0|32.0|29.0|26.0|26.0|
|AHB3|**Total AHB3**|**120**|**106**|**96**|**86**|**86**|
|AHB1|DMA1|54.0|48.0|41.0|37.0|37.0|
|AHB1|DMA2|55.0|49.0|42.0|37.0|37.0|
|AHB1|ADC12 registers|4.5|4.1|3.7|3.3|3.3|
|AHB1|ADC12 kernel|1.0|0.7|0.4|0.6|0.6|
|AHB1|ART accelerator|4.1|3.7|3.2|2.9|2.9|
|AHB1|ETH1MAC|17.0|15.0|14.0|12.0|12.0|
|AHB1|ETH1TX|0.1|0.1|0.1|0.1|0.1|
|AHB1|ETH1RX|0.1|0.1|0.1|0.1|0.1|
|AHB1|USB1 OTG registers|23.0|21.0|19.0|17.0|17.0|
|AHB1|USB1 OTG kernel|8.2|0.5|8.3|8.2|8.2|
|AHB1|USB1 ULPI|0.1|0.1|0.1|0.1|0.1|
|AHB1|USB2 OTG registers|21.0|19.0|17.0|15.0|15.0|
|AHB1|USB2 OTG kernel|8.5|0.4|8.6|8.3|8.3|
|AHB1|USB2 ULPI|23.0|19.0|20.0|19.0|19.0|
|AHB1|AHB1 bridge|0.1|0.1|0.1|0.1|0.1|
|AHB1|**Total AHB1**|**220**|**181**|**178**|**161**|**161**|



224/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 137. Peripheral current consumption in Run mode (continued)**





|Bus|Peripheral|VOS0|VOS1|VOS2|VOS3|Unit|
|---|---|---|---|---|---|---|
|AHB2|DCMI|2.1|1.9|1.8|1.6|µA/MHz|
|AHB2|RNG registers|1.7|2.0|1.3|1.2|1.2|
|AHB2|RNG kernel|11.0|0.1|9.7|9.4|9.4|
|AHB2|SDMMC2 registers|47.0|41.0|37.0|34.0|34.0|
|AHB2|SDMMC2 kernel|1.7|1.2|1.1|1.0|1.0|
|AHB2|D2SRAM1|5.7|4.9|4.4|3.9|3.9|
|AHB2|D2SRAM2|5.2|4.5|4.0|3.5|3.5|
|AHB2|D2SRAM3|4.1|3.6|3.2|2.8|2.8|
|AHB2|AHB2 bridge|0.1|0.1|0.1|0.1|0.1|
|AHB2|**Total AHB2**|**79**|**60**|**63**|**58**|**58**|
|AHB4|GPIOA|1.5|1.3|1.3|1.1|1.1|
|AHB4|GPIOB|1.2|1.0|1.0|0.9|0.9|
|AHB4|GPIOC|0.8|0.7|0.7|0.6|0.6|
|AHB4|GPIOD|1.1|1.0|1.0|0.9|0.9|
|AHB4|GPIOE|0.7|0.7|0.7|0.6|0.6|
|AHB4|GPIOF|0.8|0.8|0.7|0.6|0.6|
|AHB4|GPIOG|0.9|0.8|0.8|0.7|0.7|
|AHB4|GPIOH|1.1|1.0|1.0|0.9|0.9|
|AHB4|GPIOI|0.9|0.9|0.8|0.7|0.7|
|AHB4|GPIOJ|0.8|0.8|0.7|0.7|0.7|
|AHB4|GPIOK|0.7|0.8|0.7|0.6|0.6|
|AHB4|CRC|0.4|0.5|0.4|0.3|0.3|
|AHB4|BDMA|6.6|5.9|5.3|4.8|4.8|
|AHB4|ADC3 registers|1.7|1.5|1.2|1.2|1.2|
|AHB4|ADC3 kernel|0.4|0.3|0.5|0.2|0.2|
|AHB4|BKPRAM|2.3|1.9|1.7|1.5|1.5|
|AHB4|AHB4 bridge|0.1|0.1|0.1|0.1|0.1|
|AHB4|**Total AHB4**|**22**|**20**|**19**|**16**|**16**|
|APB3|WWDG1|0.7|0.5|0.5|0.2|µA/MHz|
|APB3|LCD-TFT|81.0|36.0|33.0|30.0|30.0|
|APB3|APB3 bridge|0.3|0.2|0.1|0.1|0.1|
|APB3|**Total APB3**|**87**|**41**|**38**|**34**|**34**|


DS12110 Rev 10 225/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 137. Peripheral current consumption in Run mode (continued)**








|Bus|Peripheral|VOS0|VOS1|VOS2|VOS3|Unit|
|---|---|---|---|---|---|---|
|APB1|TIM2|7.7|3.6|3.3|3.0|µA/MHz|
|APB1|TIM3|6.7|3.2|3.0|2.7|2.7|
|APB1|TIM4|6.3|3.1|2.8|2.5|2.5|
|APB1|TIM5|7.4|3.5|3.2|2.8|2.8|
|APB1|TIM6|1.4|0.7|0.8|0.6|0.6|
|APB1|TIM7|1.4|0.7|0.7|0.6|0.6|
|APB1|TIM12|3.2|1.5|1.5|1.3|1.3|
|APB1|TIM13|2.3|1.1|1.1|0.9|0.9|
|APB1|TIM14|2.1|1.1|1.1|0.9|0.9|
|APB1|LPTIM1 registers|0.7|0.5|0.8|0.7|0.7|
|APB1|LPTIM1 kernel|2.4|2.3|1.9|1.7|1.7|
|APB1|WWDG2|0.6|0.5|0.5|0.4|0.4|
|APB1|SPI2 registers|2.0|1.8|1.7|1.4|1.4|
|APB1|SPI2 kernel|0.8|0.6|0.5|0.6|0.6|
|APB1|SPI3 registers|1.8|1.6|1.6|1.3|1.3|
|APB1|SPI3 kernel|0.7|0.9|0.7|0.7|0.7|
|APB1|SPDIFRX1 registers|0.5|0.7|0.7|0.6|0.6|
|APB1|SPDIFRX1 kernel|3.5|2.8|2.4|2.2|2.2|
|APB1|USART2 registers|1.9|1.7|1.4|1.3|1.3|
|APB1|USART2 kernel|4.3|3.9|3.6|3.2|3.2|
|APB1|USART3 registers|1.9|1.7|1.4|1.3|1.3|
|APB1|USART3 kernel|4.4|3.9|3.5|3.2|3.2|
|APB1|UART4 registers|1.7|1.5|1.4|1.4|1.4|
|APB1|UART4 kernel|3.9|3.4|3.1|2.8|2.8|
|APB1|UART5 registers|1.6|1.4|1.4|1.3|1.3|
|APB1|UART5 kernel|3.8|3.4|3.0|2.7|2.7|
|APB1|I2C1 registers|1.1|0.8|0.9|0.8|0.8|
|APB1|I2C1 kernel|2.5|2.3|2.0|1.9|1.9|
|APB1|I2C2 registers|1.0|0.8|0.9|0.8|0.8|



226/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 137. Peripheral current consumption in Run mode (continued)**








|Bus|Peripheral|VOS0|VOS1|VOS2|VOS3|Unit|
|---|---|---|---|---|---|---|
|APB1<br>(continued)|I2C2 kernel|2.3|2.2|1.9|1.7|µA/MHz|
|APB1<br>(continued)|I2C3 registers|0.8|1.0|0.8|0.8|0.8|
|APB1<br>(continued)|I2C3 kernel|2.4|1.9|1.8|1.6|1.6|
|APB1<br>(continued)|HDMI-CEC registers|0.7|0.5|0.6|0.5|0.5|
|APB1<br>(continued)|HDMI-CEC kernel|0.1|0.1|3.2|0.1|0.1|
|APB1<br>(continued)|DAC12|3.6|1.3|1.2|1.0|1.0|
|APB1<br>(continued)|USART7 registers|1.8|1.8|1.6|1.4|1.4|
|APB1<br>(continued)|USART7 kernel|4.0|3.3|3.0|2.8|2.8|
|APB1<br>(continued)|USART8 registers|2.0|1.6|1.6|1.4|1.4|
|APB1<br>(continued)|USART8 kernel|3.9|3.4|3.1|2.8|2.8|
|APB1<br>(continued)|CRS|6.4|5.5|5.0|4.5|4.5|
|APB1<br>(continued)|SWPMI registers|2.7|2.4|2.3|1.9|1.9|
|APB1<br>(continued)|SWPMI kernel|0.1|0.1|0.1|0.1|0.1|
|APB1<br>(continued)|OPAMP|0.2|0.3|0.3|0.2|0.2|
|APB1<br>(continued)|MDIO|3.3|2.9|2.6|2.3|2.3|
|APB1<br>(continued)|FDCAN registers|19.0|17.0|15.0|13.0|13.0|
|APB1<br>(continued)|FDCAN kernel|9.1|7.9|6.9|6.4|6.4|
|APB1<br>(continued)|APB1 bridge|0.1|0.1|0.1|0.1|0.1|
|APB1<br>(continued)|**Total APB1**|**142**|**108**|**102**|**88**|**88**|
|APB2|TIM1|11.0|5.0|4.5|4.0|4.0|
|APB2|TIM8|10.0|4.7|4.3|3.8|3.8|
|APB2|USART1 registers|3.6|2.5|2.7|2.9|2.9|
|APB2|USART1 kernel|0.1|0.1|0.1|0.1|0.1|
|APB2|USART6 registers|4.5|3.0|3.1|3.4|3.4|
|APB2|USART6 kernel|0.1|0.1|0.1|0.1|0.1|
|APB2|SPI1 registers|2.0|1.7|1.6|1.4|1.4|
|APB2|SPI1 kernel|0.9|0.8|0.7|0.6|0.6|
|APB2|SPI4 registers|2.1|1.7|1.6|1.5|1.5|
|APB2|SPI4 kernel|0.6|0.5|0.5|0.3|0.3|
|APB2|TIM15|5.5|2.5|2.3|2.1|2.1|
|APB2|TIM16|4.1|2.0|1.8|1.7|1.7|
|APB2|TIM17|4.1|1.9|1.8|1.6|1.6|
|APB2|SPI5 registers|2.0|1.8|1.6|1.3|1.3|
|APB2|SPI5 kernel|0.5|0.4|0.4|0.5|0.5|
|APB2|SAI1 registers|1.3|1.1|1.1|1.0|1.0|



DS12110 Rev 10 227/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 137. Peripheral current consumption in Run mode (continued)**








|Bus|Peripheral|VOS0|VOS1|VOS2|VOS3|Unit|
|---|---|---|---|---|---|---|
|APB2<br>(continued)|SAI1 kernel|1.4|1.1|1.0|0.8|µA/MHz|
|APB2<br>(continued)|SAI2 registers|1.5|1.3|1.2|1.0|1.0|
|APB2<br>(continued)|SAI2 kernel|1.1|1.0|0.9|0.9|0.9|
|APB2<br>(continued)|SAI3 registers|1.6|1.3|1.1|1.0|1.0|
|APB2<br>(continued)|SAI3 kernel|1.1|1.2|1.1|0.9|0.9|
|APB2<br>(continued)|DFSDM1 registers|6.5|5.8|5.2|4.7|4.7|
|APB2<br>(continued)|DFSDM1 kernel|0.3|0.2|0.2|0.4|0.4|
|APB2<br>(continued)|HRTIM|84.0|39.0|35.0|32.0|32.0|
|APB2<br>(continued)|APB2 bridge|0.2|0.1|0.1|0.2|0.2|
|APB2<br>(continued)|**Total APB2**|**150**|**81**|**74**|**68**|**68**|
|APB4|SYSCFG|0.9|1.0|0.7|0.8|0.8|
|APB4|LPUART1 registers|1.1|1.3|1.0|0.8|0.8|
|APB4|LPUART1 kernel|2.9|2.2|2.2|2.1|2.1|
|APB4|SPI6 registers|1.8|1.6|1.4|1.3|1.3|
|APB4|SPI6 kernel|0.4|0.4|0.5|0.3|0.3|
|APB4|I2C4 registers|0.9|0.7|0.7|0.4|0.4|
|APB4|I2C4 kernel|2.2|2.1|1.9|1.8|1.8|
|APB4|LPTIM2 registers|0.8|0.6|0.7|0.5|0.5|
|APB4|LPTIM2 kernel|2.3|2.1|1.8|1.4|1.4|
|APB4|LPTIM3 registers|0.7|0.7|0.7|0.4|0.4|
|APB4|LPTIM3 kernel|2.1|1.7|1.6|1.5|1.5|
|APB4|LPTIM4 registers|0.8|0.4|0.6|0.4|0.4|
|APB4|LPTIM4 kernel|2.2|2.0|1.7|1.5|1.5|
|APB4|LPTIM5 registers|0.5|0.4|0.6|0.4|0.4|
|APB4|LPTIM5 kernel|2.0|1.8|1.5|1.2|1.2|
|APB4|COMP12|0.6|0.4|0.5|0.2|0.2|
|APB4|VREF|0.4|0.2|0.2|0.1|0.1|
|APB4|RTC|1.1|0.9|1.0|0.6|0.6|
|APB4|SAI4 registers|1.7|1.4|1.3|1.0|1.0|
|APB4|SAI4 kernel|2.0|2.0|1.8|1.6|1.6|
|APB4|APB4 bridge|0.1|0.1|0.1|0.1|0.1|
|APB4|**Total APB4**|**28**|**24.4**|**22.4**|**18.9**|**18.9**|



228/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.7** **Wakeup time from low-power modes**


The wakeup times given in _Table 138_ are measured starting from the wakeup event trigger
up to the first instruction executed by the CPU:


       - For Stop or Sleep modes: the wakeup event is WFE.


       - WKUP (PC1) pin is used to wakeup from Standby, Stop and Sleep modes.


All timings are derived from tests performed under ambient temperature and V DD =3.3 V.


**Table 138. Low-power mode wakeup timings**









|Symbol|Parameter|Conditions|Typ(1)|Max(1)|Unit|
|---|---|---|---|---|---|
|tWUSLEEP<br>(2)|Wakeup from Sleep|-|9|10|CPU<br>clock<br>cycles|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS3, HSI, flash memory in normal mode|4.4|5.6|µs|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS3, HSI, flash memory in low-power<br>mode|12|15|15|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS4, HSI, flash memory in normal mode|15|20|20|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS4, HSI, flash memory in low-power<br>mode|23|28|28|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS5, HSI, flash memory in normal mode|39|71|71|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS5, HSI, flash memory in low-power<br>mode|39|47|47|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS3, CSI, flash memory in normal mode|30|37|37|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS3, CSI, flash memory in low power<br>mode|36|50|50|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS4, CSI, flash memory in normal mode|38|48|48|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS4, CSI, flash memory in low-power<br>mode|47|61|61|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS5, CSI, flash memory in normal mode|68|75|75|
|tWUSTOP<br>**(2)**|Wakeup from Stop|VOS5, CSI, flash memory in low-power<br>mode|68|77|77|
|tWUSTOP_<br>KERON<br>**(2)**|Wakeup from Stop,<br>clock kept running|VOS3, HSI, flash memory in normal mode|2.6|3.4|3.4|
|tWUSTOP_<br>KERON<br>**(2)**|Wakeup from Stop,<br>clock kept running|VOS3, CSI, flash memory in normal mode|26|36|36|
|tWUSTDBY<br>**(2)**|Wakeup from Standby<br>mode|-|390|500|500|


1. Guaranteed by characterization results.


2. The wakeup times are measured from the wakeup event to the point in which the application code reads the first instruction.


DS12110 Rev 10 229/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**7.3.8** **External clock source characteristics**


**High-speed external user clock generated from an external source**


In bypass mode the HSE oscillator is switched off and the input pin is a standard I/O.


The external clock signal has to respect the _Table 157: I/O static characteristics_ . However,
the recommended clock input waveform is shown in _Figure 71_ .


**Table 139. High-speed external user clock characteristics** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|fHSE_ext|User external clock source frequency|4|25|50|MHz|
|VHSEH|Digital OSC_IN input high-level<br>voltage|0.7 VDD|-|VDD|V|
|VHSEL|Digital OSC_IN input low-level voltage|VSS|-|0.3 VDD|0.3 VDD|
|tW(HSE)|OSC_IN high or low time|7|-|-|ns|



1. Guaranteed by design.


**Figure 71. High-speed external clock source AC timing diagram**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||















230/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Low-speed external user clock generated from an external source**


In bypass mode the LSE oscillator is switched off and the input pin is a standard I/O. The
external clock signal has to respect the _Table 157: I/O static characteristics_ . However, the
recommended clock input waveform is shown in _Figure 72_ .


**Table 140. Low-speed external user clock characteristics** **[(1)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fLSE_ext|User external clock source frequency|-|-|32.768|1000|kHz|
|VLSEH|OSC32_IN input pin high level voltage|-|0.7 VDDIOx|-|VDDIOx|V|
|VLSEL|OSC32_IN input pin low level voltage|-|VSS|-|0.3 VDDIOx|0.3 VDDIOx|
|tw(LSEH)<br>tw(LSEL)|OSC32_IN high or low time|-|250|-|-|ns|



1. Guaranteed by design.


_Note:_ _For information on selecting the crystal, refer to the application note AN2867 “Oscillator_
_design guide for STM8AL/AF/S, STM32 MCUs and MPUs” available from the ST website_
_www.st.com._


**Figure 72. Low-speed external clock source AC timing diagram**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||











DS12110 Rev 10 231/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**High-speed external clock generated from a crystal/ceramic resonator**


The high-speed external (HSE) clock can be supplied with a 4 to 48 MHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
characterization results obtained with typical external components specified in _Table 141_ . In
the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).


**Table 141. 4-48 MHz HSE oscillator characteristics** **[(1)]**









|Symbol|Parameter|Operating<br>conditions(2)|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F|Oscillator frequency|-|4|-|48|MHz|
|RF|Feedback resistor|-|-|200|-|kΩ|
|IDD(HSE)|HSE current consumption|During startup(3)|-|-|4|mA|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10pF@4MHz|-|0.35|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 8 MHz|-|0.40|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 16 MHz|-|0.45|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 32 MHz|-|0.65|-|-|
|IDD(HSE)|HSE current consumption|VDD=3 V, Rm=30 Ω<br>CL=10 pF at 48 MHz|-|0.95|-|-|
|Gmcritmax|Maximum critical crystal gm|Startup|-|-|1.5|mA/V|
|tSU<br>(4)|Start-up time|VDD is stabilized|-|2|-|ms|


1. Guaranteed by design.


2. Resonator characteristics given by the crystal/ceramic resonator manufacturer.


3. This consumption level occurs during the first 2/3 of the t SU(HSE) startup time.

4. t SU(HSE) is the startup time measured from the moment it is enabled (by software) to a stabilized 8 MHz oscillation is
reached. This value is measured for a standard crystal resonator and it can vary significantly with the crystal manufacturer.


For C L1 and C L2, it is recommended to use high-quality external ceramic capacitors,
designed for high-frequency applications, and selected to match the requirements of the
crystal or resonator (see _Figure 73_ ). C L1 and C L2 are usually the same size. The crystal
manufacturer typically specifies a load capacitance which is the series combination of C L1
and C L2 . The PCB and MCU pin capacitance must be included (10 pF can be used as a
rough estimate of the combined pin and board capacitance) when sizing C L1 and C L2 .


_Note:_ _For information on selecting the crystal, refer to the application note AN2867 “Oscillator_
_design guide for STM8AF/AL/S, STM32 MCUs and MPUs” available from the ST website_
_www.st.com._


232/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 73. Typical application with an 8 MHz crystal**










|8 MHz<br>resonator|Col2|Col3|
|---|---|---|
|8 MHz<br>resonator|||


|Col1|Col2|Col3|
|---|---|---|
||RF|Bias<br>controlled<br>gain|
||||



1. R EXT value depends on the crystal characteristics.


**Low-speed external clock generated from a crystal/ceramic resonator**


The low-speed external (LSE) clock can be supplied with a 32.768 kHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
characterization results obtained with typical external components specified in _Table 142_ . In
the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).


**Table 142. Low-speed external user clock characteristics** **[(1)]**









|Symbol|Parameter|Operating conditions(2)|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F|Oscillator frequency|-|-|32.768|-|kHz|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 00,<br>Low drive capability|-|290|-|nA|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 01,<br>Medium Low drive capability|-|390|-|-|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 10,<br>Medium high drive capability|-|550|-|-|
|IDD|LSE current<br>consumption|LSEDRV[1:0] = 11,<br>High drive capability|-|900|-|-|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 00,<br>Low drive capability|-|-|0.5|µA/V|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 01,<br>Medium Low drive capability|-|-|0.75|0.75|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 10,<br>Medium high drive capability|-|-|1.7|1.7|
|Gmcritmax|Maximum critical crystal<br>gm|LSEDRV[1:0] = 11,<br>High drive capability|-|-|2.7|2.7|
|tSU<br>(3)|Startup time|VDD is stabilized|-|2|-|s|


1. Guaranteed by design.


2. Refer to the note and caution paragraphs below the table, and to the application note AN2867 “Oscillator design guide for
STM8AL/AF/S, STM32 MCUs and MPUs”.


3. t SU is the startup time measured from the moment it is enabled (by software) to a stabilized 32.768k Hz oscillation is
reached. This value is measured for a standard crystal resonator and it can vary significantly with the crystal manufacturer.


DS12110 Rev 10 233/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


_Note:_ _For information on selecting the crystal, refer to the application note AN2867 “Oscillator_
_design guide for STM8AL/AF/S, STM32 MCUs and MPUs” available from the ST website_
_www.st.com._


**Figure 74. Typical application with a 32.768 kHz crystal**










|Col1|Col2|Col3|
|---|---|---|
|32.768 kHz<br>resonator|||
|32.768 kHz<br>resonator|||


|Col1|Col2|Col3|
|---|---|---|
||RF|Bias<br>controlled<br>gain|
||||







_1._ _An external resistor is not required between OSC32_IN and OSC32_OUT and it is forbidden to add one._


**7.3.9** **Internal clock source characteristics**


The parameters given in _Table 143_ to _Table 146_ are derived from tests performed under
ambient temperature and V DD supply voltage conditions summarized in _Table 122: General_
_operating conditions_ .


**48 MHz high-speed internal RC oscillator (HSI48)**


**Table 143. HSI48 oscillator characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHSI48|HSI48 frequency|VDD=3.3 V,<br>TJ=30 °C|47.5(1)|48|48.5(1)|MHz|
|TRIM(2)|USER trimming step|-|-|0.175|-|%|
|USER TRIM<br>COVERAGE(3)|USER TRIMMING Coverage|± 32 steps|±4.79|±5.60|-|%|
|DuCy(HSI48)(2)|Duty Cycle|-|45|-|55|%|
|ACCHSI48_REL(3)(4)|Accuracy of the HSI48 oscillator over<br>temperature (factory calibrated)|TJ=-40 to 125 °C|–4.5|-|3.5|%|
|∆VDD(HSI48)(3)|HSI48 oscillator frequency drift with<br>VDD<br>(5)|VDD=3 to 3.6 V|-|0.025|0.05|%|
|∆VDD(HSI48)(3)|HSI48 oscillator frequency drift with<br>VDD<br>(5)|VDD=1.62 V to 3.6 V|-|0.05|0.1|0.1|
|tsu(HSI48)<br>(2)|HSI48 oscillator start-up time|-|-|2.1|4.0|µs|
|IDD(HSI48)<br>(2)|HSI48 oscillator power consumption|-|-|350|400|µA|
|NT jitter|Next transition jitter<br>Accumulated jitter on 28 cycles(6)|-|-|± 0.15|-|ns|
|PT jitter|Paired transition jitter<br>Accumulated jitter on 56 cycles(6)|-|-|± 0.25|-|ns|



1. Guaranteed by test in production.


2. Guaranteed by design.


3. Guaranteed by characterization.


234/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


4. ∆fHSI = ACCHSI48_REL + ∆ VDD .


5. These values are obtained by using the formula: (Freq(3.6V) - Freq(3.0V)) / Freq(3.0V) or (Freq(3.6V) - Freq(1.62V)) /
Freq(1.62V).


6. Jitter measurements are performed without clock source activated in parallel.


**64 MHz high-speed internal RC oscillator (HSI)**


**Table 144. HSI oscillator characteristics** **[(1)]**



















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fHSI|HSI frequency|VDD=3.3 V, TJ=30 °C|63.7(2)|64|64.3(2)|MHz|
|TRIM|HSI user trimming step|Trimming is not a multiple<br>of 32|-|0.24|0.32|%|
|TRIM|HSI user trimming step|Trimming is 128, 256 and<br>384|−5.2|−1.8|-|-|
|TRIM|HSI user trimming step|Trimming is 64, 192, 320<br>and 448|−1.4|−0.8|-|-|
|TRIM|HSI user trimming step|Other trimming are a<br>multiple of 32 (not<br>including multiple of 64<br>and 128)|−0.6|−0.25|-|-|
|DuCy(HSI)|Duty Cycle|-|45|-|55|%|
|ΔVDD (HSI)|HSI oscillator frequency drift over<br>VDD(reference is 3.3 V)|VDD=1.62 to 3.6 V|−0.12|-|0.03|%|
|ΔTEMP (HSI)|HSI oscillator frequency drift over<br>temperature (reference is 64 MHz)|TJ=-20 to 105 °C|−1(3)|-|1(3)|%|
|ΔTEMP (HSI)|HSI oscillator frequency drift over<br>temperature (reference is 64 MHz)|TJ=−40 to TJmax °C|−2(3)|-|1(3)|1(3)|
|tsu(HSI)|HSI oscillator start-up time|-|-|1.4|2|µs|
|tstab(HSI)|HSI oscillator stabilization time|at 1% of target frequency|-|4|8|µs|
|IDD(HSI)|HSI oscillator power consumption|-|-|300|400|µA|


1. Guaranteed by design unless otherwise specified.


2. Guaranteed by test in production.


3. Guaranteed by characterization.


**4 MHz low-power internal RC oscillator (CSI)**


**Table 145. CSI oscillator characteristics** **[(1)]**






|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fCSI|CSI frequency|VDD=3.3 V, TJ=30 °C|3.96(2)|4|4.04(2)|MHz|
|TRIM|Trimming step|-|-|0.35|-|%|
|DuCy(CSI)|Duty Cycle|-|45|-|55|%|
|∆TEMP (CSI)|CSI oscillator frequency drift over<br>temperature|TJ = 0 to 85 °C|-|−3.7(3)|4.5(3)|%|
|∆TEMP (CSI)|CSI oscillator frequency drift over<br>temperature|TJ = −40 to 125 °C|-|−11(3)|7.5(3)|7.5(3)|



DS12110 Rev 10 235/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 145. CSI oscillator characteristics** **[(1)]** **(continued)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|DVDD (CSI)|CSI oscillator frequency drift over<br>VDD|VDD= 1.62 to 3.6 V|-|−0.06|0.06|%|
|tsu(CSI)|CSI oscillator startup time|-|-|1|2|µs|
|tstab(CSI)|CSI oscillator stabilization time<br>(to reach ±3% of fCSI)|-|-|-|4|cycle|
|IDD(CSI)|CSI oscillator power consumption|-|-|23|30|µA|



1. Guaranteed by design.


2. Guaranteed by test in production.


3. Guaranteed by characterization.


**Low-speed internal (LSI) RC oscillator**


**Table 146. LSI oscillator characteristics**





















|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fLSI|LSI frequency|VDD = 3.3 V, TJ = 25 °C|31.4(1)|32|32.6(1)|kHz|
|fLSI|LSI frequency|TJ = –40 to 110 °C, VDD = 1.62 to<br>3.6 V|29.76(2)|-|33.6(2)|33.6(2)|
|fLSI|LSI frequency|TJ = –40 to 125 °C, VDD = 1.62 to<br>3.6 V|29.4|-|33.6|33.6|
|tsu(LSI)<br>(3)|LSI oscillator<br>startup time|-|-|80|130|µs|
|tstab(LSI)<br>(3)|LSI oscillator<br>stabilization<br>time (5% of<br>final value)|-|-|120|170|170|
|IDD(LSI)<br>(3)|LSI oscillator<br>power<br>consumption|-|-|130|280|nA|


1. Guaranteed by test in production.


2. Guaranteed by characterization results.


3. Guaranteed by design.


236/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.10** **PLL characteristics**


The parameters given in _Table 147_ are derived from tests performed under temperature and
V DD supply voltage conditions summarized in _Table 122: General operating conditions_ .


**Table 147. PLL characteristics (wide VCO frequency range)** **[(1)]**





















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|fPLL_IN|PLL input clock|-|-|2|-|16|MHz|
|fPLL_IN|PLL input clock duty cycle|-|-|10|-|90|%|
|fPLL_P_OUT|PLL multiplier output clock P|VOS0|VOS0|1.5|-|480(2)|MHz|
|fPLL_P_OUT|PLL multiplier output clock P|VOS1|VOS1|1.5|-|400(2)|400(2)|
|fPLL_P_OUT|PLL multiplier output clock P|VOS2|VOS2|1.5|-|300(2)|300(2)|
|fPLL_P_OUT|PLL multiplier output clock P|VOS3|VOS3|1.5|-|200(2)|200(2)|
|fVCO_OUT|PLL VCO output|-|-|192|-|960|960|
|tLOCK|PLL lock time|Normal mode|Normal mode|-|50(3)|150(3)|µs|
|tLOCK|PLL lock time|Sigma-delta mode<br>(CKIN≥ 8 MHz)|Sigma-delta mode<br>(CKIN≥ 8 MHz)|-|58(3)|166(3)|166(3)|
|Jitter|Cycle-to-cycle jitter(4)|-|VCO =<br>192 MHz|-|134|-|±ps|
|Jitter|Cycle-to-cycle jitter(4)|-|VCO =<br>200 MHz|-|134|-|-|
|Jitter|Cycle-to-cycle jitter(4)|-|VCO =<br>400 MHz|-|76|-|-|
|Jitter|Cycle-to-cycle jitter(4)|-|VCO =<br>800 MHz|-|39|-|-|
|Jitter|Long term jitter|Normal mode|VCO =<br>800 MHz|-|±0.7|-|%|
|Jitter|Long term jitter|Sigma-delta<br>mode (CKIN =<br>16 MHz)|VCO =<br>800 MHz|-|±0.8|-|-|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>836 MHz|VDDA|-|590|1500|µA|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>836 MHz|VCORE|-|720|-|-|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>192 MHz|VDDA|-|180|600|600|
|IDD(PLL)<br>(3)|PLL power consumption on VDD|VCO freq =<br>192 MHz|VCORE|-|280|-|-|


1. Guaranteed by design unless otherwise specified.









2. This value must be limited to the maximum frequency due to the product limitation (480 MHz for VOS0, 400 MHz for VOS1,
300 MHz for VOS2, 200 MHz for VOS3).


3. Guaranteed by characterization results.


4. Integer mode only.


DS12110 Rev 10 237/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 148. PLL characteristics (medium VCO frequency range)** **[(1)]**























|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|fPLL_IN|PLL input clock|-|-|1|-|2|MHz|
|fPLL_IN|PLL input clock duty cycle|-|-|10|-|90|%|
|fPLL_OUT|PLL multiplier output clock P, Q,<br>R|VOS1|VOS1|1.17|-|210|MHz|
|fPLL_OUT|PLL multiplier output clock P, Q,<br>R|VOS2|VOS2|1.17|-|210|210|
|fPLL_OUT|PLL multiplier output clock P, Q,<br>R|VOS3|VOS3|1.17|-|200|200|
|fVCO_OUT|PLL VCO output|-|-|150|-|420|420|
|tLOCK|PLL lock time|Normal mode|Normal mode|-|60(2)|100(2)|µs|
|tLOCK|PLL lock time|Sigma-delta mode|Sigma-delta mode|forbidden|forbidden|forbidden|forbidden|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>150 MHz|-|145|-|±ps|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>300 MHz|-|91|-|-|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>400 MHz|-|64|-|-|
|Jitter|Cycle-to-cycle jitter(3)|-|VCO =<br>420 MHz|-|63|-|-|
|Jitter|Period jitter|fPLL_OUT =<br>50 MHz|VCO =<br>150 MHz|-|55|-|±-ps|
|Jitter|Period jitter|fPLL_OUT =<br>50 MHz|VCO =<br>400 MHz|-|30|-|-|
|Jitter|Long term jitter|Normal mode|VCO =<br>400 MHz|-|±0.3|-|%|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>420MHz|VDD|-|440|1150|µA|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>420MHz|VCORE|-|530|-|-|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>150MHz|VDD|-|180|500|500|
|I(PLL)(2)|PLL power consumption on VDD|VCO freq =<br>150MHz|VCORE|-|200|-|-|


1. Guaranteed by design unless otherwise specified.


2. Guaranteed by characterization results.


3. Integer mode only.





238/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.11** **Memory characteristics**


**Flash memory**


The characteristics are given at T J = –40 to 125 °C unless otherwise specified.


The devices are shipped to customers with the flash memory erased.


**Table 149. Flash memory characteristics**





|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|IDD|Supply current|Write / Erase 8-bit mode|-|6.5|-|mA|
|IDD|Supply current|Write / Erase 16-bit mode|-|11.5|-|-|
|IDD|Supply current|Write / Erase 32-bit mode|-|20|-|-|
|IDD|Supply current|Write / Erase 64-bit mode|-|35|-|-|


**Table 150. Flash memory** **programming**





|Symbol|Parameter|Conditions|Min(1)|Typ|Max(1)|Unit|
|---|---|---|---|---|---|---|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 8|-|290|580(2)|µs|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 16|-|180|360|360|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 32|-|130|260|260|
|tprog|Word (266 bits) programming<br>time|Program/erase parallelism x 64|-|100|200|200|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 8|-|2|4|s|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 16|-|1.8|3.6|3.6|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 32|-|1.1|2.2|2.2|
|tERASE128KB|Sector (128 KB) erase time|Program/erase parallelism x 64|-|1|2|2|
|tME|Mass erase time|Program/erase parallelism x 8|-|13|26|26|
|tME|Mass erase time|Program/erase parallelism x 16|-|8|16|16|
|tME|Mass erase time|Program/erase parallelism x 32|-|6|12|12|
|tME|Mass erase time|Program/erase parallelism x 64|-|5|10|10|
|Vprog|Programming voltage|Program parallelism x 8|1.62|-|3.6|V|
|Vprog|Programming voltage|Program parallelism x 16|Program parallelism x 16|Program parallelism x 16|Program parallelism x 16|Program parallelism x 16|
|Vprog|Programming voltage|Program parallelism x 32|Program parallelism x 32|Program parallelism x 32|Program parallelism x 32|Program parallelism x 32|
|Vprog|Programming voltage|Program parallelism x 64|1.8|-|3.6|3.6|


1. Guaranteed by characterization results.





2. The maximum programming time is measured after 10K erase operations.


DS12110 Rev 10 239/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 151. Flash memory endurance and data retention**

|Symbol|Parameter|Conditions|Value|Unit|
|---|---|---|---|---|
|**Symbol**|**Parameter**|** Conditions**|**Min(1)**|**Min(1)**|
|NEND|Endurance|TJ = –40 to +125 °C (6 suffix versions)|10|kcycles|
|tRET|Data retention|1 kcycle at TA = 85 °C|30|Years|
|tRET|Data retention|10 kcycles at TA = 55 °C|20|20|



1. Guaranteed by characterization results.


**7.3.12** **EMC characteristics**


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


The test results are given in _Table 152_ . They are based on the EMS levels and classes
defined in application note AN1709.


**Table 152. EMS characteristics**








|Symbol|Parameter|Conditions|Level/<br>Class|
|---|---|---|---|
|VFESD|Voltage limits to be applied on any I/O pin to induce<br>a functional disturbance|VDD= 3.3 V, TA = +25 °C,<br>UFBGA240, frcc_c_ck =<br>400 MHz, conforms to<br>IEC 61000-4-2|3B|
|VFTB|Fast transient voltage burst limits to be applied<br>through 100 pF on VDD and VSSpins to induce a<br>functional disturbance|Fast transient voltage burst limits to be applied<br>through 100 pF on VDD and VSSpins to induce a<br>functional disturbance|5A|



As a consequence, it is recommended to add a serial resistor (1 kΏ) located as close as
possible to the MCU to the pins exposed to noise (connected to tracks longer than 50 mm
on PCB).


240/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Designing hardened software to avoid noise problems**


EMC characterization and optimization are performed at component level with a typical
application environment and simplified MCU software. It should be noted that good EMC
performance is highly dependent on the user application and the software in particular.


Therefore it is recommended that the user applies EMC software optimization and
prequalification tests in relation with the EMC level requested for his application.


**Software recommendations**


The software flowchart must include the management of runaway conditions such as:


      - Corrupted program counter


      - Unexpected reset


      - Critical Data corruption (control registers...)


**Prequalification trials**


Most of the common failures (unexpected reset and program counter corruption) can be
reproduced by manually forcing a low state on the NRST pin or the Oscillator pins for 1
second.


To complete these trials, ESD stress can be applied directly on the device, over the range of
specification values. When unexpected behavior is detected, the software can be hardened
to prevent unrecoverable errors occurring (see application note AN1015).


**Electromagnetic Interference (EMI)**


The electromagnetic field emitted by the device is monitored while a simple application,
executing EEMBC code, is running. This emission test is compliant with SAE IEC61967-2
standard which specifies the test board and the pin loading.


**Table 153. EMI characteristics for f** **HSE** **= 8 MHz and f** **CPU** **= 400 MHz**







|Symbol|Parameter|Conditions|Monitored<br>frequency band|Value|Unit|
|---|---|---|---|---|---|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240<br>package, compliant with IEC61967-2|0.1 MHz to 30 MHz|11|dBµV|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240<br>package, compliant with IEC61967-2|30 MHz to 130 MHz|6|6|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240<br>package, compliant with IEC61967-2|130 MHz to 1 GHz|12|12|
|SEMI|Peak(1)|VDD= 3.6 V, TA = 25 °C, UFBGA240<br>package, compliant with IEC61967-2|1 GHz to 2 GHz|7|7|
|SEMI|Level(2)|Level(2)|0.1 MHz to 2 GHz|2.5|-|


1. Refer to AN1709 “EMI radiated test” chapter.


2. Refer to AN1709 “EMI level classification” chapter.


DS12110 Rev 10 241/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**7.3.13** **Absolute maximum ratings (electrical sensitivity)**


Based on three different tests (ESD, LU) using specific measurement methods, the device is
stressed in order to determine its performance in terms of electrical sensitivity.


**Electrostatic discharge (ESD)**


Electrostatic discharges (a positive then a negative pulse) are applied to the pins of each
sample according to each pin combination. This test conforms to the ANSI/ESDA/JEDEC
JS-001 and ANSI/ESDA/JEDEC JS-002 standards.


**Table 154. ESD absolute maximum ratings**



|Symbol|Ratings|Conditions|Packages|Class|Maximum<br>value(1)|Unit|
|---|---|---|---|---|---|---|
|VESD(HBM)|Electrostatic discharge<br>voltage (human body<br>model)|TA = +25 °C conforming to<br>ANSI/ESDA/JEDEC JS-<br>001|All|1C|1000|V|
|VESD(CDM)|Electrostatic discharge<br>voltage (charge device<br>model)|TA = +25 °C conforming to<br>ANSI/ESDA/JEDEC JS-<br>002|All|C1|250|250|


1. Guaranteed by characterization results.


**Static latchup**







Two complementary static tests are required on six parts to assess the latchup
performance:


       - A supply overvoltage is applied to each power supply pin


       - A current injection is applied to each input, output and configurable I/O pin


These tests are compliant with JESD78 IC latchup standard.


**Table 155. Electrical sensitivities**

|Symbol|Parameter|Conditions|Class|
|---|---|---|---|
|LU|Static latchup class|TA = +25 °C conforming to JESD78|II level A|



242/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.14** **I/O current injection characteristics**


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


**Table 156. I/O current injection susceptibility** **[(1)]**










|Symbol|Description|Functional susceptibility|Col4|Unit|
|---|---|---|---|---|
|**Symbol**|**Description**|**Negative**<br>**injection**|**Positive**<br>**injection**|**Positive**<br>**injection**|
|IINJ|PA7, PC5, PG1, PB14, PJ7, PA11, PA12, PA13, PA14, PA15,<br>PJ12, PB4|5|0|mA|
|IINJ|PA2, PH2, PH3, PE8, PA6, PA7, PC4, PE7, PE10, PE11|0|NA|NA|
|IINJ|PA0, PA_C, PA1, PA1_C, PC2, PC2_C, PC3, PC3_C, PA4,<br>PA5, PH4, PH5, BOOT0|0|0|0|
|IINJ|All other I/Os|5|NA|NA|



1. Guaranteed by characterization .



DS12110 Rev 10 243/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**7.3.15** **I/O port characteristics**


**General input/output characteristics**


Unless otherwise specified, the parameters given in _Table 157: I/O static characteristics_ are
derived from tests performed under the conditions summarized in _Table 122: General_
_operating conditions_ . All I/Os are CMOS and TTL compliant (except for BOOT0).


For information on GPIO configuration, refer to the application note AN4899 “STM32 GPIO
configuration for hardware settings and low-power consumption” available from the ST
website www.st.com.


**Table 157. I/O static characteristics**





























|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VIL|I/O input low level voltage except<br>BOOT0|1.62 V<VDDIOx<3.6 V|-|-|0.3VDD<br>(1)|V|
|VIL|I/O input low level voltage except<br>BOOT0|I/O input low level voltage except<br>BOOT0|-|-|0.4VDD−0.<br>1(2)|0.4VDD−0.<br>1(2)|
|VIL|BOOT0 I/O input low level voltage|BOOT0 I/O input low level voltage|-|-|0.19VDD+<br>0.1(2)|0.19VDD+<br>0.1(2)|
|VIH|I/O input high level voltage except<br>BOOT0|1.62 V<VDDIOx<3.6 V|0.7VDD<br>(1)|-|-|V|
|VIH|I/O input high level voltage except<br>BOOT0(3)|I/O input high level voltage except<br>BOOT0(3)|0.47VDD+0.<br>25(2)|-|-|-|
|VIH|BOOT0 I/O input high level<br>voltage(3)|BOOT0 I/O input high level<br>voltage(3)|0.17VDD+0.<br>6(2)|-|-|-|
|VHYS<br>(2)|TT_xx, FT_xxx and NRST I/O<br>input hysteresis|1.62 V< VDDIOx <3.6 V|-|250|-|mV|
|VHYS<br>(2)|BOOT0 I/O input hysteresis|BOOT0 I/O input hysteresis|-|200|-|-|
|Ilkg<br>(4)|FT_xx Input leakage current(2)|0< VIN≤ Max(VDDXXX)(9)|-|-|+/-250|nA|
|Ilkg<br>(4)|FT_xx Input leakage current(2)|Max(VDDXXX) < VIN≤ 5.5 V<br>(5)(6)(9)|-|-|1500|1500|
|Ilkg<br>(4)|FT_u IO|0< VIN≤ Max(VDDXXX)(9)|-|-|+/- 350|+/- 350|
|Ilkg<br>(4)|FT_u IO|Max(VDDXXX) < VIN≤ 5.5 V<br>(5)(6)(9)|-|-|5000(7)|5000(7)|
|Ilkg<br>(4)|TT_xx Input leakage current|0< VIN≤ Max(VDDXXX) (9)|-|-|+/-250|+/-250|
|Ilkg<br>(4)|VPP (BOOT0 alternate function)|0< VIN≤ VDDIOX|-|-|15|15|
|Ilkg<br>(4)|VPP (BOOT0 alternate function)|VDDIOX < VIN≤ 9 V|||35|35|
|RPU|Weak pull-up equivalent<br>resistor(8)|VIN=VSS|30|40|50|kΩ|
|RPD|Weak pull-down equivalent<br>resistor(8)|VIN=VDD<br>(9)|30|40|50|50|
|CIO|I/O pin capacitance|-|-|5|-|pF|


1. Compliant with CMOS requirements.


2. Guaranteed by design.


244/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


3. V DDIOx represents V DDIO1, V DDIO2 or V DDIO3 . V DDIOx = V DD .


4. This parameter represents the pad leakage of the I/O itself. The total product pad leakage is provided by the following
formula: I Total_Ikg_max = 10 μA + [number of I/Os where V IN is applied on the pad] ₓ I lkg(Max) .


5. All FT_xx IO except FT_lu, FT_u and PC3.


6. V IN must be less than Max(VDDXXX) + 3.6 V.


7. To sustain a voltage higher than MIN(V DD, V DDA, V DD33USB ) +0.3 V, the internal pull-up and pull-down resistors must be
disabled.


8. The pull-up and pull-down resistors are designed with a true resistance in series with a switchable PMOS/NMOS. This
PMOS/NMOS contribution to the series resistance is minimal (~10% order).


9. Max(VDDXXX) is the maximum value of all the I/O supplies.


All I/Os are CMOS and TTL compliant (no software configuration required). Their
characteristics cover more than the strict CMOS-technology or TTL parameters. The
coverage of these requirements for FT I/Os is shown in _Figure 75_ .


**Figure 75. V** **IL** **/V** **IH** **for all I/Os except BOOT0**







|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||||||.7VDD||TLL re|quirement:|VIHmin = 2 V|
||||CMOS req<br>|uirement: V<br> on simu|IHmin=0<br>lation VIHmin|=0.47VDD+0|.25|||
||||Ba|sed<br>|n simulation|.3<br><br> VILmax=0.4V|VDD <br><br>DD-0.1|||
|||||CMOS<br>Based|requiremen<br>|t: VILmax=0<br>||||
|||||CMOS<br>Based|requiremen<br>||TLL req<br>|uirement: VI|Lmin = 0.8 V|
|||||||||||


**Output driving current**





The GPIOs (general purpose input/outputs) can sink or source up to ± 8 mA, and sink or
source up to ± 20 mA (with a relaxed V OL /V OH ).


In the user application, the number of I/O pins which can drive current must be limited to
respect the absolute maximum rating specified in _Section 7.2_ . In particular:


- The sum of the currents sourced by all the I/Os on V DD, plus the maximum Run
consumption of the MCU sourced on V DD, cannot exceed the absolute maximum rating
ΣI VDD (see _Table 120_ ).


- The sum of the currents sunk by all the I/Os on V SS plus the maximum Run
consumption of the MCU sunk on V SS cannot exceed the absolute maximum rating
ΣI VSS (see _Table 120_ ).


DS12110 Rev 10 245/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Output voltage levels**


Unless otherwise specified, the parameters given in _Table 158: Output voltage_
_characteristics for all I/Os except PC13, PC14, PC15 and PI8_ and _Table 159: Output voltage_
_characteristics for PC13, PC14, PC15 and PI8_ are derived from tests performed under
ambient temperature and V DD supply voltage conditions summarized in _Table 122: General_
_operating conditions_ . All I/Os are CMOS and TTL compliant.


**Table 158. Output voltage characteristics for all I/Os except PC13, PC14, PC15 and PI8** **[(1)]**










|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|VOL|Output low level voltage|CMOS port(2)<br>IIO=8 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|V|
|VOH|Output high level voltage|CMOS port(2)<br>IIO=-8 mA<br>2.7 V≤ VDD ≤3.6 V|VDD−0.4|-|-|
|VOL<br>(3)|Output low level voltage|TTL port(2)<br>IIO=8 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH<br>(3)|Output high level voltage|TTL port(2)<br>IIO=-8 mA<br>2.7 V≤ VDD ≤3.6 V|2.4|-|-|
|VOL<br>(3)|Output low level voltage|IIO=20 mA<br>2.7 V≤ VDD ≤3.6 V|-|1.3|1.3|
|VOH<br>(3)|Output high level voltage|IIO=-20 mA<br>2.7 V≤ VDD ≤3.6 V|VDD−1.3|-|-|
|VOL<br>(3)|Output low level voltage|IIO=4 mA<br>1.62 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH (3)|Output high level voltage|IIO=-4 mA<br>1.62 V≤VDD<3.6 V|VDD−-0.4|-|-|
|VOLFM+<br>(3)|Output low level voltage for an FTf<br>I/O pin in FM+ mode|IIO= 20 mA<br>2.3 V≤ VDD≤3.6 V|-|0.4|0.4|
|VOLFM+<br>(3)|Output low level voltage for an FTf<br>I/O pin in FM+ mode|IIO= 10 mA<br>1.62 V≤ VDD ≤3.6 V|-|0.4|0.4|



1. The IIO current sourced or sunk by the device must always respect the absolute maximum rating specified in _Table 119:_
_Voltage characteristics_, and the sum of the currents sourced or sunk by all the I/Os (I/O ports and control pins) must always
respect the absolute maximum ratings ΣIIO.


2. TTL and CMOS outputs are compatible with JEDEC standards JESD36 and JESD52.


3. Guaranteed by design.


246/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 159. Output voltage characteristics for PC13, PC14, PC15 and PI8** **(1)**







|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|VOL|Output low level voltage|CMOS port(2)<br>IIO=3 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|V|
|VOH|Output high level voltage|CMOS port(2)<br>IIO=-3 mA<br>2.7 V≤ VDD ≤3.6 V|VDD−0.4|-|-|
|VOL<br>(3)|Output low level voltage|TTL port(2)<br>IIO=3 mA<br>2.7 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH<br>(2)|Output high level voltage|TTL port(2)<br>IIO=-3 mA<br>2.7 V≤ VDD ≤3.6 V|2.4|-|-|
|VOL<br>(2)|Output low level voltage|IIO=1.5 mA<br>1.62 V≤ VDD ≤3.6 V|-|0.4|0.4|
|VOH<br>(2)|Output high level voltage|IIO=-1.5 mA<br>1.62 V≤ VDD ≤3.6 V|VDD−0.4|-|-|


1. The IIO current sourced or sunk by the device must always respect the absolute maximum rating specified in _Table 119:_
_Voltage characteristics_, and the sum of the currents sourced or sunk by all the I/Os (I/O ports and control pins) must always
respect the absolute maximum ratings ΣIIO.


2. TTL and CMOS outputs are compatible with JEDEC standards JESD36 and JESD52.


3. Guaranteed by design.


DS12110 Rev 10 247/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Output buffer timing characteristics (HSLV option disabled)**


The HSLV bit of SYSCFG_CCCSR register can be used to optimize the I/O speed when the
product voltage is below 2.7 V.


**Table 160. Output timing characteristics (HSLV OFF)** **[(1)(2)]**










|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|00|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|12|MHz|
|00|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|3|3|
|00|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V|-|12|12|
|00|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|3|3|
|00|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V|-|16|16|
|00|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|4|4|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|16.6|ns|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|33.3|33.3|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V|-|13.3|13.3|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|25|25|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V|-|10|10|
|00|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|20|20|
|01|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|60|MHz|
|01|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|15|15|
|01|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V|-|80|80|
|01|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|15|15|
|01|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V|-|110|110|
|01|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|20|20|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤ VDD≤3.6 V|-|5.2|ns|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|10|10|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V|-|4.2|4.2|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|7.5|7.5|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V|-|2.8|2.8|
|01|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|5.2|5.2|



248/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 160. Output timing characteristics (HSLV OFF)** **[(1)(2)]** **(continued)**










|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|10|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|85|MHz|
|10|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|35|35|
|10|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|110|110|
|10|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|40|40|
|10|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|166|166|
|10|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|85|85|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|3.8|ns|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|6.9|6.9|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|2.8|2.8|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|5.2|5.2|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|1.8|1.8|
|10|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 Vv|-|3.3|3.3|
|11|Fmax<br>(3)|Maximum frequency|C=50 pF, 2.7 V≤VDD≤3.6 Vv|-|100|MHz|
|11|Fmax<br>(3)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|50|50|
|11|Fmax<br>(3)|Maximum frequency|C=30 pF, 2.7 V≤VDD≤3.6 Vv|-|133|133|
|11|Fmax<br>(3)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|66|66|
|11|Fmax<br>(3)|Maximum frequency|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|220|220|
|11|Fmax<br>(3)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|100|100|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 2.7 V≤VDD≤3.6 V(5)|-|3.3|ns|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(5)|-|6.6|6.6|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 2.7 V≤VDD≤3.6 V(5)|-|2.4|2.4|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(5)|-|4.5|4.5|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 2.7 V≤VDD≤3.6 V(5)|-|1.5|1.5|
|11|tr/tf<br>(4)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(5)|-|2.7|2.7|



1. Guaranteed by design.


2. The frequency of the GPIOs that can be supplied in V BAT mode (PC13, PC14, PC15 and PI8) is limited to 2 MHz


3. The maximum frequency is defined with the following conditions:
(t r +t f ) ≤ 2/3 T
Skew ≤ 1/20 T
45%<Duty cycle<55%


4. The fall and rise times are defined between 90% and 10% and between 10% and 90% of the output waveform, respectively.


5. Compensation system enabled.


DS12110 Rev 10 249/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Output buffer timing characteristics (HSLV option enabled)**


**Table 161. Output timing characteristics (HSLV ON)** **[(1)]**








|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|00|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|10|MHz|
|00|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|10|10|
|00|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|10|10|
|00|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|11|ns|
|00|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|9|9|
|00|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|6.6|6.6|
|01|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V|-|50|MHz|
|01|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V|-|58|58|
|01|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V|-|66|66|
|01|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V|-|6.6|ns|
|01|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V|-|4.8|4.8|
|01|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V|-|3|3|
|10|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|55|MHz|
|10|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|80|80|
|10|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|133|133|
|10|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|5.8|ns|
|10|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|4|4|
|10|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|2.4|2.4|
|11|Fmax<br>(2)|Maximum frequency|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|60|MHz|
|11|Fmax<br>(2)|Maximum frequency|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|90|90|
|11|Fmax<br>(2)|Maximum frequency|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|175|175|
|11|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=50 pF, 1.62 V≤VDD≤2.7 V(4)|-|5.3|ns|
|11|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=30 pF, 1.62 V≤VDD≤2.7 V(4)|-|3.6|3.6|
|11|tr/tf<br>(3)|Output high to low level<br>fall time and output low<br>to high level rise time|C=10 pF, 1.62 V≤VDD≤2.7 V(4)|-|1.9|1.9|



1. Guaranteed by design.


2. The maximum frequency is defined with the following conditions:
(t r +t f ) ≤ 2/3 T
Skew ≤ 1/20 T
45%<Duty cycle<55%


3. The fall and rise times are defined between 90% and 10% and between 10% and 90% of the output waveform, respectively.


4. Compensation system enabled.


250/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.16** **NRST pin characteristics**


The NRST pin input driver uses CMOS technology. It is connected to a permanent pull-up
resistor, R PU (see _Table 157: I/O static characteristics_ ).


Unless otherwise specified, the parameters given in _Table 162_ are derived from tests
performed under the ambient temperature and V DD supply voltage conditions summarized
in _Table 122: General operating conditions_ .


**Table 162. NRST pin characteristics**












|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|RPU<br>(2)|Weak pull-up equivalent<br>resistor(1)|VIN= VSS|30|40|50|㏀|
|VF(NRST)<br>(2)|NRST Input filtered pulse|1.71 V < VDD < 3.6 V|-|-|50|ns|
|VNF(NRST)<br>(2)|NRST Input not filtered pulse|1.71 V < VDD < 3.6 V|300|-|-|-|
|VNF(NRST)<br>(2)|NRST Input not filtered pulse|1.62 V < VDD < 3.6 V|1000|-|-|-|



1. The pull-up is designed with a true resistance in series with a switchable PMOS. This PMOS contribution
to the series resistance must be minimum (~10% order) .


2. Guaranteed by design.


**Figure 76. Recommended NRST pin protection**













1. The reset network protects the device against parasitic resets.


2. The user must ensure that the level on the NRST pin can go below the V IL(NRST) max level specified in
_Table 157_ . Otherwise the reset is not taken into account by the device.


**7.3.17** **FMC characteristics**


Unless otherwise specified, the parameters given in _Table 163_ to _Table 176_ for the FMC
interface are derived from tests performed under the ambient temperature, f HCLK frequency
and V DD supply voltage conditions summarized in _Table 122: General operating conditions_,
with the following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.


      - HSLV activated when V DD ≤ 2.7 V


      - VOS level set to VOS1.


DS12110 Rev 10 251/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics.


**Asynchronous waveforms and timings**


_Figure 77_ through _Figure 79_ represent asynchronous waveforms and _Table 163_ through
_Table 170_ provide the corresponding timings. The results shown in these tables are
obtained with the following FMC configuration:


      - AddressSetupTime = 0x1


      - AddressHoldTime = 0x1


      - DataSetupTime = 0x1 (except for asynchronous NWAIT mode, DataSetupTime = 0x5)


      - BusTurnAroundDuration = 0x0


      - Capacitive load C L = 30 pF


In all timing tables, the T KERCK is the f mc_ker_ck clock period.


**Figure 77. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms**



|tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|w(NOE)<br>t|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||
|w(NOE)<br>t|Address|||


1. Mode 2/B, C and D only. In Mode 1, FMC_NADV is not used.


252/357 DS12110 Rev 10












**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 163. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|3Tfmc_ker_ck–1|3Tfmc_ker_ck+1|ns|
|tv(NOE_NE)|FMC_NEx low to FMC_NOE low|0|0.5|0.5|
|tw(NOE)|FMC_NOE low time|2Tfmc_ker_ck–1|2Tfmc_ker_ck+1|2Tfmc_ker_ck+1|
|th(NE_NOE)|FMC_NOE high to FMC_NE high<br>hold time|0|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|0.5|0.5|
|th(A_NOE)|Address hold time after<br>FMC_NOE high|0|-|-|
|tsu(Data_NE)|Data to FMC_NEx high setup<br>time|11|-|-|
|tsu(Data_NOE)|Data to FMC_NOEx high setup<br>time|11|-|-|
|th(Data_NOE)|Data hold time after FMC_NOE<br>high|0|-|-|
|th(Data_NE)|Data hold time after FMC_NEx<br>high|0|-|-|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|-|0|0|
|tw(NADV)|FMC_NADV low time|-|Tfmc_ker_ck+1|Tfmc_ker_ck+1|


1. Guaranteed by characterization results.


**Table 164. Asynchronous non-multiplexed SRAM/PSRAM/NOR read-NWAIT**
**timings** **[(1)(2)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|7Tfmc_ker_ck+1|7Tfmc_ker_ck+1|ns|
|tw(NOE)|FMC_NOE low time|5Tfmc_ker_ck–1|5Tfmc_ker_ck +1|5Tfmc_ker_ck +1|
|tw(NWAIT)|FMC_NWAIT low time|Tfmc_ker_ck– 0.5|-|-|
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx<br>high|4Tfmc_ker_ck +11|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after<br>FMC_NWAIT invalid|3Tfmc_ker_ck+11.5|-|-|


1. Guaranteed by characterization results.


2. N WAIT pulse width is equal to 1 AHB cycle.





DS12110 Rev 10 253/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 78. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms**























1. Mode 2/B, C and D only. In Mode 1, FMC_NADV is not used.


254/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 165. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|3Tfmc_ker_ck–1|3Tfmc_ker_ck|ns|
|tv(NWE_NE)|FMC_NEx low to FMC_NWE low|Tfmc_ker_ck|Tfmc_ker_ck+1|Tfmc_ker_ck+1|
|tw(NWE)|FMC_NWE low time|Tfmc_ker_ck–0.5|Tfmc_ker_ck+0.5|Tfmc_ker_ck+0.5|
|th(NE_NWE)|FMC_NWE high to FMC_NE high<br>hold time|Tfmc_ker_ck|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|2|2|
|th(A_NWE)|Address hold time after FMC_NWE<br>high|Tfmc_ker_ck–0.5|-|-|
|tv(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5|0.5|
|th(BL_NWE)|FMC_BL hold time after FMC_NWE<br>high|Tfmc_ker_ck–0.5|-|-|
|tv(Data_NE)|Data to FMC_NEx low to Data valid|-|Tfmc_ker_ck+ 2.5|Tfmc_ker_ck+ 2.5|
|th(Data_NWE)|Data hold time after FMC_NWE high|Tfmc_ker_ck+0.5|-|-|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|-|0|0|
|tw(NADV)|FMC_NADV low time|-|Tfmc_ker_ck+ 1|Tfmc_ker_ck+ 1|


1. Guaranteed by characterization results.


**Table 166. Asynchronous non-multiplexed SRAM/PSRAM/NOR write-NWAIT**
**timings** **[(1)(2)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|8Tfmc_ker_ck–1|8Tfmc_ker_ck+1|ns|
|tw(NWE)|FMC_NWE low time|6Tfmc_ker_ck–1.5|6Tfmc_ker_ck+0.5|6Tfmc_ker_ck+0.5|
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx<br>high|5Tfmc_ker_ck+13|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after<br>FMC_NWAIT invalid|4Tfmc_ker_ck+13|-|-|


1. Guaranteed by characterization results.


2. N WAIT pulse width is equal to 1 AHB cycle.





DS12110 Rev 10 255/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 79. Asynchronous multiplexed PSRAM/NOR read waveforms**






|tv(NOE_NE) th(NE_NOE)<br>tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||
|tw(NOE)<br>tv(NOE_NE)<br>th(NE_NOE)|Address|||





















256/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 167. Asynchronous multiplexed PSRAM/NOR read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|4Tfmc_ker_ck–1|4Tfmc_ker_ck+1|ns|
|tv(NOE_NE)|FMC_NEx low to FMC_NOE low|2Tfmc_ker_ck|2Tfmc_ker_ck<br>+0.5|2Tfmc_ker_ck<br>+0.5|
|ttw(NOE)|FMC_NOE low time|Tfmc_ker_ck–1|Tfmc_ker_ck+1|Tfmc_ker_ck+1|
|th(NE_NOE)|FMC_NOE high to FMC_NE high hold<br>time|0|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|0.5|0.5|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|0|0.5|0.5|
|tw(NADV)|FMC_NADV low time|Tfmc_ker_ck–0.5|Tfmc_ker_ck+1|Tfmc_ker_ck+1|
|th(AD_NADV)|FMC_AD(address) valid hold time<br>after FMC_NADV high)|Tfmc_ker_ck+0.5|-|-|
|th(A_NOE)|Address hold time after FMC_NOE<br>high|Tfmc_ker_ck–0.5|-|-|
|tsu(Data_NE)|Data to FMC_NEx high setup time|11|-|-|
|tsu(Data_NOE)|Data to FMC_NOE high setup time|11|-|-|
|th(Data_NE)|Data hold time after FMC_NEx high|0|-|-|
|th(Data_NOE)|Data hold time after FMC_NOE high|0|-|-|


1. Guaranteed by characterization results.


**Table 168. Asynchronous multiplexed PSRAM/NOR read-NWAIT timings** **[(1)(2)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|8Tfmc_ker_ck–1|8Tfmc_ker_ck|ns|
|tw(NOE)|FMC_NWE low time|5Tfmc_ker_ck–1.5|5Tfmc_ker_ck+0.5|5Tfmc_ker_ck+0.5|
|tsu(NWAIT_NE)|FMC_NWAIT valid before<br>FMC_NEx high|4Tfmc_ker_ck+11|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after<br>FMC_NWAIT invalid|3Tfmc_ker_ck+11.5|-|-|


1. Guaranteed by characterization results.


2. N WAIT pulse width is equal to 1 AHB cycle.





DS12110 Rev 10 257/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 169. Asynchronous multiplexed PSRAM/NOR write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|4Tfmc_ker_ck–1|4Tfmc_ker_ck|ns|
|tv(NWE_NE)|FMC_NEx low to FMC_NWE low|Tfmc_ker_ck–1|Tfmc_ker_ck+0.5|Tfmc_ker_ck+0.5|
|tw(NWE)|FMC_NWE low time|2Tfmc_ker_ck–0.5|2Tfmc_ker_ck+0.5|2Tfmc_ker_ck+0.5|
|th(NE_NWE)|FMC_NWE high to FMC_NE high hold<br>time|Tfmc_ker_ck–0.5|-|-|
|tv(A_NE)|FMC_NEx low to FMC_A valid|-|0|0|
|tv(NADV_NE)|FMC_NEx low to FMC_NADV low|0|0.5|0.5|
|tw(NADV)|FMC_NADV low time|Tfmc_ker_ck|Tfmc_ker_ck+ 1|Tfmc_ker_ck+ 1|
|th(AD_NADV)|FMC_AD(adress) valid hold time after<br>FMC_NADV high)|Tfmc_ker_ck+0.5|-|-|
|th(A_NWE)|Address hold time after FMC_NWE<br>high|Tfmc_ker_ck+0.5|-|-|
|th(BL_NWE)|FMC_BL hold time after FMC_NWE<br>high|Tfmc_ker_ck– 0.5|-|-|
|tv(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5|0.5|
|tv(Data_NADV)|FMC_NADV high to Data valid|-|Tfmc_ker_ck+2|Tfmc_ker_ck+2|
|th(Data_NWE)|Data hold time after FMC_NWE high|Tfmc_ker_ck+0.5|-|-|


1. Guaranteed by characterization results.


**Table 170. Asynchronous multiplexed PSRAM/NOR write-NWAIT timings** **[(1)(2)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NE)|FMC_NE low time|9Tfmc_ker_ck–1|9Tfmc_ker_ck|ns|
|tw(NWE)|FMC_NWE low time|7Tfmc_ker_ck–0.5|7Tfmc_ker_ck+0.5|7Tfmc_ker_ck+0.5|
|tsu(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx<br>high|5Tfmc_ker_ck+11|-|-|
|th(NE_NWAIT)|FMC_NEx hold time after<br>FMC_NWAIT invalid|4Tfmc_ker_ck+11.5|-|-|


1. Guaranteed by characterization results.


2. N WAIT pulse width is equal to 1 AHB cycle.


**Synchronous waveforms and timings**


_Figure 80_ through _Figure 83_ represent synchronous waveforms and _Table 171_ through
_Table 174_ provide the corresponding timings. The results shown in these tables are
obtained with the following FMC configuration:


      - BurstAccessMode = FMC_BurstAccessMode_Enable


      - MemoryType = FMC_MemoryType_CRAM


      - WriteBurst = FMC_WriteBurst_Enable


      - CLKDivision = 1


      - DataLatency = 1 for NOR flash; DataLatency = 0 for PSRAM


258/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


In all the timing tables, the T fmc_ker_ck is the f mc_ker_ck clock period, with the following
FMC_CLK maximum values:


      - For 2.7 V<V DD <3.6 V, FMC_CLK = 125 MHz at 20 pF


      - For 1.8 V<V DD <1.9 V, FMC_CLK = 100 MHz at 20 pF


      - For 1.62 V<V DD <1.8 V, FMC_CLK = 100 MHz at 15 pF


**Figure 80. Synchronous multiplexed NOR/PSRAM read timings**

























|td(CL<br>td(CL|Da<br>KL-NExL)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|td(CL<br>td(CL|Da<br>KL-NExL)|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|
|td(CL<br>td(CL|KL-AV)<br>td(CL|KL-NADVH)|||||
|td(CL<br>td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)|KH-AIV)|
|td(CL<br>td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)||
|td(CL<br>td(CL|||||||
|td(CL<br>td(CL|||OEL)|td(CLKH|-NOEH)|-NOEH)|
|AD<br>td(CLK|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|
|AD<br>td(CLK|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|L-ADIV~~)~~<br>tsu(A|2<br>th(CL<br>ITV)|2<br>th(CL<br>ITV)|
|AD<br>td(CLK|L-ADIV~~)~~<br>tsu(A||||||
|AD<br>td(CLK|[15:0]||||||
|AD<br>td(CLK|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|
||||||||
||||||||
||||||||


|Col1|LKH)|
|---|---|
|TV-C|TV-C|
|||


DS12110 Rev 10 259/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 171. Synchronous multiplexed NOR/PSRAM read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FMC_CLK period|2Tfmc_ker_ck–1|-|ns|
|td(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|1|1|
|td(CLKH_NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)|Tfmc_ker_ck+0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|1|1|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)|-|2.5|2.5|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid<br>(x=16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NOEL)|FMC_CLK low to FMC_NOE low|-|1.5|1.5|
|td(CLKH-NOEH)|FMC_CLK high to FMC_NOE high|Tfmc_ker_ck–0.5|-|-|
|td(CLKL-ADV)|FMC_CLK low to FMC_AD[15:0] valid|-|3|3|
|td(CLKL-ADIV)|FMC_CLK low to FMC_AD[15:0] invalid|0|-|-|
|tsu(ADV-CLKH)|FMC_A/D[15:0] valid data before FMC_CLK<br>high|3|-|-|
|th(CLKH-ADV)|FMC_A/D[15:0] valid data after FMC_CLK<br>high|0|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|3|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|1|-|-|


1. Guaranteed by characterization results.


260/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 81. Synchronous multiplexed PSRAM write timings**























|td(CL<br>td(CL<br>td(CL<br>td(CLK<br>AD|Da<br>KL-NExL)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|Da<br>KL-NExL)|Da<br>KL-NExL)|Da<br>KL-NExL)|Da<br>KL-NExL)|Da<br>KL-NExL)|CLK|CLK|CLK|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|Da<br>KL-NExL)|ta latency|= 0|= 0|= 0|= 0|= 0|= 0|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-AV)<br>td(CL|KL-NADVH|)|)|||||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-AV)<br>td(CL||||t|d(CL|KH-AIV)|KH-AIV)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|||||||||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||td(C|LKH|-NWEH)|-NWEH)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||td(C|LKH|-NWEH)||
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||d(CLKL-Data~~)~~|LKH<br>-NW|D2<br>-NBLH)<br>AITV)|D2<br>-NBLH)<br>AITV)|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||D1|D1|D1|D1|
|AD<br>td(CL<br>td(CL<br>td(CL<br>td(CLK|KL-NWEL)||||td(C<br>th(CLKH|td(C<br>th(CLKH|td(C<br>th(CLKH|td(C<br>th(CLKH|
||||||||||
||||||||||


DS12110 Rev 10 261/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 172. Synchronous multiplexed PSRAM write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FMC_CLK period, VDD = 2.7 to 3.6 V|2Tfmc_ker_ck–1<br>1|-|Ns|
|td(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x =0..2)|-|1|1|
|td(CLKH-NExH)|FMC_CLK high to FMC_NEx high<br>(x = 0…2)|Tfmc_ker_ck+0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|1.5|1.5|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid<br>(x =16…25)|-|2|2|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid<br>(x =16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NWEL)|FMC_CLK low to FMC_NWE low|-|1.5|1.5|
|t(CLKH-NWEH)|FMC_CLK high to FMC_NWE high|Tfmc_ker_ck+0.5|-|-|
|td(CLKL-ADV)|FMC_CLK low to to FMC_AD[15:0] valid|-|2.5|2.5|
|td(CLKL-ADIV)|FMC_CLK low to FMC_AD[15:0] invalid|0|-|-|
|td(CLKL-DATA)|FMC_A/D[15:0] valid data after FMC_CLK<br>low|-|2.5|2.5|
|td(CLKL-NBLL)|FMC_CLK low to FMC_NBL low|-|2|2|
|td(CLKH-NBLH)|FMC_CLK high to FMC_NBL high|Tfmc_ker_ck+0.5|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|2|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|2|-|-|


1. Guaranteed by characterization results.


262/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 82. Synchronous non-multiplexed NOR/PSRAM read timings**





|td(CL|Da|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|td(CL|Da|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|ta latency = 0|
|td(CL|KL-AV)<br>td(CL|KL-NADVH)|||||
|td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)|KH-AIV)|
|td(CL|KL-AV)<br>td(CL|||td(CL|KH-AIV)||
|td(CL|||||||
|td(CL|||OEL)|td(CLK|H-NOEH~~)~~|H-NOEH~~)~~|
|td(CL|||OEL)|td(CLK|H-NOEH~~)~~||
||tsu(|tsu(|tsu(|tsu(|tsu(|tsu(|
||tsu(|tsu(|tsu(|tsu(|2<br>th(CL<br>ITV)|2<br>th(CL<br>ITV)|
||tsu(NW|tsu(NW|tsu(NW|tsu(NW|tsu(NW|tsu(NW|
||||||||
||||||||
||||||||


|Col1|CLKH)|
|---|---|
|ITV-|ITV-|
|||


DS12110 Rev 10 263/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 173. Synchronous non-multiplexed NOR/PSRAM read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(CLK)|FMC_CLK period|2Tfmc_ker_ck–1|-|ns|
|t(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|1|1|
|td(CLKH-NExH)|FMC_CLK high to FMC_NEx high<br>(x= 0…2)|2Tfmc_ker_ck+0.5|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|0.5|0.5|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|0|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid<br>(x=16…25)|-|2|2|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid<br>(x=16…25)|2Tfmc_ker_ck|-|-|
|td(CLKL-NOEL)|FMC_CLK low to FMC_NOE low|-|1.5|1.5|
|td(CLKH-NOEH)|FMC_CLK high to FMC_NOE high|2Tfmc_ker_ck-0.5|-|-|
|tsu(DV-CLKH)|FMC_D[15:0] valid data before FMC_CLK<br>high|3|-|-|
|th(CLKH-DV)|FMC_D[15:0] valid data after FMC_CLK<br>high|0|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|3|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|1|-|-|


1. Guaranteed by characterization results.


264/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 83. Synchronous non-multiplexed PSRAM write timings**














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|td(CL<br>td(CL|Da|Da|Da|Da|Da|Da|Da|
|td(CL<br>td(CL|Da|ta latency =|0|0|0|0|0|
|td(CL<br>td(CL|KL-AV)<br>td(CL|KL-NADVH|)|||||
|td(CL<br>td(CL|KL-AV)<br>td(CL|||t|d(CLKH-A|IV)|IV)|
|td(CL<br>td(CL|KL-AV)<br>td(CL|||t|d(CLKH-A|IV)||
|td(CL<br>td(CL||||||||
|td(CL<br>td(CL|KL-NWEL)|||td(C|LKH-NWE|H)|H)|
|td(CL<br>td(CL|KL-NWEL)|||td(C|LKH-NWE|H)||
|td(CL<br>td(CL|td(CL|KL-Data~~)~~|KL-Data~~)~~||D2<br>td(CLK<br>-NWAITV)<br>CLKH-NB|L-Da<br>LH~~)~~|L-Da<br>LH~~)~~|
|td(CL<br>td(CL|td(CL|KL-Data~~)~~|KL-Data~~)~~|D1|D1|D1|D1|
|||||||||
|||||||||
||tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|tsu(NWA|



DS12110 Rev 10 265/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 174. Synchronous non-multiplexed PSRAM write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t(CLK)|FMC_CLK period|2Tfmc_ker_ck–1|-|ns|
|td(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)|-|2|2|
|t(CLKH-NExH)|FMC_CLK high to FMC_NEx high<br>(x= 0…2)|Tfmc_ker_ck**+0.5**|-|-|
|td(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|-|0.5|0.5|
|td(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|**0**|-|-|
|td(CLKL-AV)|FMC_CLK low to FMC_Ax valid<br>(x=16…25)|-|2.|2.|
|td(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid<br>(x=16…25)|Tfmc_ker_ck|-|-|
|td(CLKL-NWEL)|FMC_CLK low to FMC_NWE low|-|1.5|1.5|
|td(CLKH-NWEH)|FMC_CLK high to FMC_NWE high|Tfmc_ker_ck+1|-|-|
|td(CLKL-Data)|FMC_D[15:0] valid data after FMC_CLK<br>low|-|3.5|3.5|
|td(CLKL-NBLL)|FMC_CLK low to FMC_NBL low|-|2|2|
|td(CLKH-NBLH)|FMC_CLK high to FMC_NBL high|Tfmc_ker_ck+1|-|-|
|tsu(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high|2|-|-|
|th(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high|2|-|-|


1. Guaranteed by characterization results.


266/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**NAND controller waveforms and timings**


_Figure 84_ through _Figure 87_ represent synchronous waveforms, and _Table 175_ and
_Table 176_ provide the corresponding timings. The results shown in this table are obtained
with the following FMC configuration:


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


      - Capacitive load C L = 30 pF


In all timing tables, the T fmc_ker_ck is the fmc_ker_ck clock period.


**Figure 84. NAND controller waveforms for read access**


DS12110 Rev 10 267/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 85. NAND controller waveforms for write access**


**Figure 86. NAND controller waveforms for common memory read access**


268/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 87. NAND controller waveforms for common memory write access**







**Table 175. Switching characteristics for NAND flash read cycles** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(N0E)|FMC_NOE low width|4Tfmc_ker_ck– 0.5|4Tfmc_ker_ck+0.5|ns|
|tsu(D-NOE)|FMC_D[15-0] valid data before<br>FMC_NOE high|8|-|-|
|th(NOE-D)|FMC_D[15-0] valid data after<br>FMC_NOE high|0|-|-|
|td(ALE-NOE)|FMC_ALE valid before FMC_NOE low|-|3Tfmc_ker_ck +1|3Tfmc_ker_ck +1|
|th(NOE-ALE)|FMC_NWE high to FMC_ALE invalid|4Tfmc_ker_ck–2|-|-|


1. Guaranteed by characterization results.


**Table 176. Switching characteristics for NAND flash write cycles** **[(1)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(NWE)|FMC_NWE low width|4Tfmc_ker_ck– 0.5|4Tfmc_ker_ck+0.5|ns|
|tv(NWE-D)|FMC_NWE low to FMC_D[15-0]<br>valid|0|-|-|
|th(NWE-D)|FMC_NWE high to FMC_D[15-0]<br>invalid|2Tfmc_ker_ck– 0.5|-|-|
|td(D-NWE)|FMC_D[15-0] valid before<br>FMC_NWE high|5Tfmc_ker_ck– 1|-|-|
|td(ALE-NWE)|FMC_ALE valid before FMC_NWE<br>low|-|3Tfmc_ker_ck+0.5|3Tfmc_ker_ck+0.5|
|th(NWE-ALE)|FMC_NWE high to FMC_ALE<br>invalid|2Tfmc_ker_ck– 1|-|-|


1. Guaranteed by characterization results.





DS12110 Rev 10 269/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**SDRAM waveforms and timings**


In all timing tables, the TKERCK is the fmc_ker_ck clock period, with the following
FMC_SDCLK maximum values:


      - For 2.7 V<V DD <3.6 V: FMC_SDCLK =110 MHz at 20 pF


      - For 1.8 V<V DD <1.9 V: FMC_SDCLK =100 MHz at 20 pF


      - For 1.62 V< DD <1.8 V, FMC_SDCLK =100 MHz at 15 pF


**Figure 88. SDRAM read access waveforms (CL = 1)**












|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|||Coln|Coln|Coln|
||||||
||||||
|L_NRAS)|||||
|L_NCAS)|||||
|L_NCAS)|||||
||||||



270/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 177. SDRAM read timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck– 1|2Tfmc_ker_ck<br>+0.5|ns|
|tsu(SDCLKH _Data)|Data input setup time|3|-|-|
|th(SDCLKH_Data)|Data input hold time|0|-|-|
|td(SDCLKL_Add)|Address valid time|-|1.5|1.5|
|td(SDCLKL- SDNE)|Chip select valid time|-|1.5|1.5|
|th(SDCLKL_SDNE)|Chip select hold time|0.5|-|-|
|td(SDCLKL_SDNRAS)|SDNRAS valid time|-|1|1|
|th(SDCLKL_SDNRAS)|SDNRAS hold time|0.5|-|-|
|td(SDCLKL_SDNCAS)|SDNCAS valid time|-|0.5|0.5|
|th(SDCLKL_SDNCAS)|SDNCAS hold time|0|-|-|


1. Guaranteed by characterization results.


**Table 178. LPSDR SDRAM read timings** **[(1)]**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tW(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck– 1|2Tfmc_ker_ck+0.5|ns|
|tsu(SDCLKH_Data)|Data input setup time|3|-|-|
|th(SDCLKH_Data)|Data input hold time|0.5|-|-|
|td(SDCLKL_Add)|Address valid time|-|2.5|2.5|
|td(SDCLKL_SDNE)|Chip select valid time|-|2.5|2.5|
|th(SDCLKL_SDNE)|Chip select hold time|0|-|-|
|td(SDCLKL_SDNRAS|SDNRAS valid time|-|0.5|0.5|
|th(SDCLKL_SDNRAS)|SDNRAS hold time|0|-|-|
|td(SDCLKL_SDNCAS)|SDNCAS valid time|-|1.5|1.5|
|th(SDCLKL_SDNCAS)|SDNCAS hold time|0|-|-|


1. Guaranteed by characterization results.





DS12110 Rev 10 271/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 89. SDRAM write access waveforms**














|DCLK<br>DCLK|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||Col2|Col2|Col2|Coln|Coln|Coln|
|||th(S|th(S|th(S||||
|E)|E)|E)|E)|E)|E)|E)|E)|
|E)|E)|E)|E)|E)|E)|||
|DCLK|DCLK|L_NR|AS)|||||
|DCLK|DCLK|L_NC|AS)|||||
|DCLK|DCLK|L_NC|AS)|||||
|DCLK|DCLK|L_N|WE)|||||
|DCLK|DCLK|L_N|WE)|||||
|DCLK|DCLK|||||||
|DCLK|D|ata2|ata2|ata2|atan|atan|atan|



**Table 179. SDRAM Write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck– 1|2Tfmc_ker_ck+0.5|ns|
|td(SDCLKL _Data)|Data output valid time|-|1|1|
|th(SDCLKL _Data)|Data output hold time|0|-|-|
|td(SDCLKL_Add)|Address valid time|-|1.5|1.5|
|td(SDCLKL_SDNWE)|SDNWE valid time|-|1.5|1.5|
|th(SDCLKL_SDNWE)|SDNWE hold time|0.5|-|-|
|td(SDCLKL_ SDNE)|Chip select valid time|-|1.5|1.5|
|th(SDCLKL-_SDNE)|Chip select hold time|0.5|-|-|
|td(SDCLKL_SDNRAS)|SDNRAS valid time|-|1|1|
|th(SDCLKL_SDNRAS)|SDNRAS hold time|0.5|-|-|
|td(SDCLKL_SDNCAS)|SDNCAS valid time|-|1|1|
|td(SDCLKL_SDNCAS)|SDNCAS hold time|0.5|-|-|


1. Guaranteed by characterization results.


272/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 180. LPSDR SDRAM Write timings** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tw(SDCLK)|FMC_SDCLK period|2Tfmc_ker_ck– 1|2Tfmc_ker_ck+0.5|ns|
|td(SDCLKL _Data)|Data output valid time|-|2.5|2.5|
|th(SDCLKL _Data)|Data output hold time|0|-|-|
|td(SDCLKL_Add)|Address valid time|-|2.5|2.5|
|td(SDCLKL-SDNWE)|SDNWE valid time|-|2.5|2.5|
|th(SDCLKL-SDNWE)|SDNWE hold time|0|-|-|
|td(SDCLKL- SDNE)|Chip select valid time|-|3|3|
|th(SDCLKL- SDNE)|Chip select hold time|0|-|-|
|td(SDCLKL-SDNRAS)|SDNRAS valid time|-|1.5|1.5|
|th(SDCLKL-SDNRAS)|SDNRAS hold time|0|-|-|
|td(SDCLKL-SDNCAS)|SDNCAS valid time|-|1.5|1.5|
|td(SDCLKL-SDNCAS)|SDNCAS hold time|0|-|-|


1. Guaranteed by characterization results.


**7.3.18** **Quad-SPI interface characteristics**





Unless otherwise specified, the parameters given in _Table 181_ and _Table 182_ for QUADSPI
are derived from tests performed under the ambient temperature, f AHB frequency and V DD
supply voltage conditions summarized in _Table 122: General operating conditions_, with the
following configuration:


- Output speed is set to OSPEEDRy[1:0] = 11


- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.


- HSLV activated when V DD ≤ 2.7 V


- VOS level set to VOS1


Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics.


The following table summarizes the parameters measured in SDR mode.


DS12110 Rev 10 273/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 181. QUADSPI characteristics in SDR mode** **[(1)]**





























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fck11/TCK|QUADSPI clock<br>frequency|2.7<VDD<3.6 V<br>CL = 20 pF|-|-|133|MHz|
|Fck11/TCK|QUADSPI clock<br>frequency|1.62<VDD<3.6 V<br>CL = 15 pF|-|-|100|100|
|tw(CKH)|QUADSPI clock high<br>and low time Even<br>division|PRESCALER[7:0] =<br>n = 0,1,3,5...|TCK/2–0.5|-|TCK/2|ns|
|tw(CKL)|tw(CKL)|tw(CKL)|TCK/2|-|TCK/2+0.5|TCK/2+0.5|
|tw(CKH)|QUADSPI clock high<br>and low time Odd<br>division|PRESCALER[7:0] =<br>n = 2,4,6,8...|(n/2)*TCK/(n+1)-0.5|-|(n/2)*TCK/ (n+1)|(n/2)*TCK/ (n+1)|
|tw(CKL)|tw(CKL)|tw(CKL)|(n/2+1)*TCK/(n+1)|-|(n/2+1)*TCK/ <br>(n+1)+0.5|(n/2+1)*TCK/ <br>(n+1)+0.5|
|ts(IN)|Data input setup time|2.7<VDD<3.6 V|2|-|-|-|
|ts(IN)|Data input setup time|1.62<VDD<3.6 V|2|-|-|-|
|th(IN)|Data input hold time|2.7<VDD<3.6 V|1|-|-|-|
|th(IN)|Data input hold time|1.62<VDD<3.6 V|2.5|-|-|-|
|tv(OUT)|Data output valid time|-|-|1|2|2|
|th(OUT)|Data output hold time|-|0|-|-|-|


1. Guaranteed by characterization results.


The following table summarizes the parameters measured in DDR mode.


274/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 182. QUADSPI characteristics in DDR mode** **[(1)]**

























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fck11/TCK|QUADSPI clock frequency|2.7<VDD<3.6 V<br>CL = 20 pF|-|-|100|MHz|
|Fck11/TCK|QUADSPI clock frequency|1.62<VDD<3.6 V<br>CL = 15 pF|-|-|100|100|
|tw(CKH)|QUADSPI clock high and<br>low time Even division|PRESCALER[7:0] =<br>n = 0,1,3,5...|TCK/2–0.5|-|TCK/2|ns|
|tw(CKL)|tw(CKL)|tw(CKL)|TCK/2|-|TCK/2+0.5|TCK/2+0.5|
|tw(CKH)|QUADSPI clock high and<br>low time Odd division|PRESCALER[7:0] =<br>n = 2,4,6,8...|(n/2)*TCK/<br>(n+1)-0.5|-|(n/2)*TCK/ <br>(n+1)|(n/2)*TCK/ <br>(n+1)|
|tw(CKL)|tw(CKL)|tw(CKL)|(n/2+1)*TCK/<br>(n+1)|-|(n/2+1)*TCK /<br>(n+1)+0.5|(n/2+1)*TCK /<br>(n+1)+0.5|
|tsr(IN), tsf(IN)|Data input setup time|2.7<VDD<3.6 V|2.5|-|-|-|
|tsr(IN), tsf(IN)|Data input setup time|1.62<VDD<3.6 V|1.5|-|-|-|
|thr(IN),thf(IN)|Data input hold time|2.7<VDD<3.6 V|1|-|-|-|
|thr(IN),thf(IN)|Data input hold time|1.62<VDD<3.6 V|2.5||||
|tvr(OUT), <br>tvf(OUT)|Data output valid time|DHHC=0|-|5|6|6|
|tvr(OUT), <br>tvf(OUT)|Data output valid time|DHHC=1<br>PRESCALER[7:0] =<br>1,2…|-|TCK/4+1|TCK/4+2|TCK/4+2|
|thr(OUT), <br>thf(OUT)|Data output hold time|DHHC=0|3|-|-|-|
|thr(OUT), <br>thf(OUT)|Data output hold time|DHHC=1<br>PRESCALER[7:0]=1<br>,2…|TCK/4|-|-|-|


1. Guaranteed by characterization results.





**Figure 90. QUADSPI timing diagram - SDR mode**








|Col1|h(OU|
|---|---|
|||
|D0||




|ts(IN)|th(IN)|
|---|---|
|||
||D1|





DS12110 Rev 10 275/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 91. Quad-SPI timing diagram - DDR mode**












|Col1|r(OU|
|---|---|
|||
|IO0||


|Col1|Col2|f(OU|
|---|---|---|
||||
|IO2|IO3||










|Col1|Col2|Col3|Col4|
|---|---|---|---|
|IO0||I|O1|


|Col1|Col2|Col3|Col4|
|---|---|---|---|
|IO3||IO|4|





**7.3.19** **Delay block (DLYB) characteristics**


Unless otherwise specified, the parameters given in _Table 183_ for Delay Block are derived
from tests performed under the ambient temperature, f rcc_c_ck frequency and VDD supply
voltage summarized in _Table 122: General operating conditions_, with the following
configuration:


**Table 183. Delay Block characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tinit|Initial delay|-|1400|2200|2400|ps|
|t∆|Unit Delay|-|35|40|45|-|



**7.3.20** **16-bit ADC characteristics**


Unless otherwise specified, the parameters given in _Table 184_ are derived from tests
performed under the ambient temperature, f PCLK2 frequency and V DDA supply voltage
conditions summarized in _Table 122: General operating conditions_ .


**Table 184. ADC characteristics** **[(1)(2)]**



|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply<br>voltage for ADC<br>ON|-|-|1.62|-|3.6|V|
|VREF+|Positive reference<br>voltage|-|-|1.62|-|VDDA|V|
|VREF-|Negative<br>reference voltage|-|-|VSSA|VSSA|VSSA|V|
|fADC|ADC clock<br>frequency|1.62 V ≤ VDDA ≤ 3.6 V|BOOST = 11|0.12|-|50|MHz|
|fADC|ADC clock<br>frequency|1.62 V ≤ VDDA ≤ 3.6 V|BOOST = 10|0.12|-|25|25|
|fADC|ADC clock<br>frequency|1.62 V ≤ VDDA ≤ 3.6 V|BOOST = 01|0.12|-|12.5|12.5|
|fADC|ADC clock<br>frequency|1.62 V ≤ VDDA ≤ 3.6 V|BOOST = 00|-|-|6.25|6.25|


276/357 DS12110 Rev 10




**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 184. ADC characteristics** **[(1)(2)]** **(continued)**





































|Symbol|Parameter|Conditions|Col4|Col5|Col6|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|---|---|
|fs<br>(3)|Sampling rate for<br>Direct channels(4)|Resolution = 16 bits,<br>VDDA>2.5 V|TJ = 90 °C|fADC=36 MHz|SMP = 1.5|-|-|3.60|MSps|
|fs<br>(3)|Sampling rate for<br>Direct channels(4)|Resolution = 16 bits|Resolution = 16 bits|fADC=37 MHz|SMP = 2.5|-|-|3.35|3.35|
|fs<br>(3)|Sampling rate for<br>Direct channels(4)|Resolution = 14 bits|TJ = 125 °C|fADC = 50 MHz|SMP = 2.5|-|-|5.00|5.00|
|fs<br>(3)|Sampling rate for<br>Direct channels(4)|Resolution = 12 bits|Resolution = 12 bits|fADC = 50 MHz|SMP = 2.5|-|-|5.50|5.50|
|fs<br>(3)|Sampling rate for<br>Direct channels(4)|Resolution = 10 bits|Resolution = 10 bits|fADC = 50 MHz|SMP = 1.5|-|-|7.10|7.10|
|fs<br>(3)|Sampling rate for<br>Direct channels(4)|Resolution = 8 bits|Resolution = 8 bits|fADC = 50 MHz|SMP = 1.5|-|-|8.30|8.30|
|fs<br>(3)|Sampling rate for<br>Fast channels|Resolution = 16 bits,<br>VDDA>2.5 V|TJ = 90 °C|fADC=32 MHz|SMP = 2.5|-|-|2.90|2.90|
|fs<br>(3)|Sampling rate for<br>Fast channels|Resolution = 16 bits|Resolution = 16 bits|fADC=31 MHz|SMP = 2.5|-|-|2.80|2.80|
|fs<br>(3)|Sampling rate for<br>Fast channels|Resolution = 14 bits|TJ = 125 °C|fADC = 33 MHz|SMP = 2.5|-|-|3.30|3.30|
|fs<br>(3)|Sampling rate for<br>Fast channels|Resolution = 12 bits|Resolution = 12 bits|fADC = 39 MHz|SMP = 2.5|-|-|4.30|4.30|
|fs<br>(3)|Sampling rate for<br>Fast channels|Resolution = 10 bits|Resolution = 10 bits|fADC = 48 MHz|SMP = 2.5|-|-|6.00|6.00|
|fs<br>(3)|Sampling rate for<br>Fast channels|Resolution = 8 bits|Resolution = 8 bits|fADC = 50 MHz|SMP = 2.5|-|-|7.10|7.10|
|fs<br>(3)|Sampling rate for<br>Slow channels|Resolution = 16 bits|TJ = 90 °C|fADC= 10 MHz|SMP = 1.5|-|-|1.00|1.00|
|fs<br>(3)|Sampling rate for<br>Slow channels|resolution = 14 bits|TJ = 125 °C|TJ = 125 °C|TJ = 125 °C|-|-|-|-|
|fs<br>(3)|Sampling rate for<br>Slow channels|resolution = 12 bits|resolution = 12 bits|resolution = 12 bits|resolution = 12 bits|-|-|-|-|
|fs<br>(3)|Sampling rate for<br>Slow channels|resolution = 10 bits|resolution = 10 bits|resolution = 10 bits|resolution = 10 bits|-|-|-|-|
|fs<br>(3)|Sampling rate for<br>Slow channels|resolution = 8 bits|resolution = 8 bits|resolution = 8 bits|resolution = 8 bits|-|-|-|-|
|tTRIG|External trigger<br>period|Resolution = 16 bits|Resolution = 16 bits|-|-|-|-|10|1/<br>fADC|
|VAIN<br>(5)|Conversion<br>voltage range|-|-|-|-|0|-|VREF+|V|
|VCMIV|Common mode<br>input voltage|-|-|-|-|VREF/2<br>− 10%|VREF/<br>2|VREF/2<br>+ 10%|V|
|RAIN<br>(6)|External input<br>impedance|Resolution = 16 bits, TJ = 125 °C|Resolution = 16 bits, TJ = 125 °C|-|-|-|-|170|Ω|
|RAIN<br>(6)|External input<br>impedance|Resolution = 14 bits, TJ = 125 °C|Resolution = 14 bits, TJ = 125 °C|-|-|-|-|435|435|
|RAIN<br>(6)|External input<br>impedance|Resolution = 12 bits, TJ =125 °C|Resolution = 12 bits, TJ =125 °C|-|-|-|-|1150|1150|
|RAIN<br>(6)|External input<br>impedance|Resolution = 10 bits, TJ = 125 °C|Resolution = 10 bits, TJ = 125 °C|-|-|-|-|5650|5650|
|RAIN<br>(6)|External input<br>impedance|Resolution = 8 bits, TJ = 125 °C|Resolution = 8 bits, TJ = 125 °C|-|-|-|-|26500|26500|
|CADC|Internal sample<br>and hold<br>capacitor|-|-|-|-|-|4|-|pF|
|tADCVREG<br>_STUP|ADC LDO startup<br>time|-|-|-|-|-|5|10|us|
|tSTAB|ADC Power-up<br>time|LDO already started|LDO already started|-|-|1|-|-|conver<br>sion<br>cycle|
|tCAL|Offset and<br>linearity<br>calibration time|-|-|-|-|165010|-|-|1/fADC|
|tOFF_<br>CAL|Offset calibration<br>time|-|-|-|-|1280|-|-|1/fADC|


DS12110 Rev 10 277/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 184. ADC characteristics** **[(1)(2)]** **(continued)**









|Symbol|Parameter|Conditions|Col4|Col5|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|---|
|tLATR|Trigger<br>conversion<br>latency regular<br>and injected<br>channels without<br>conversion abort|CKMODE = 00|-|-|1.5|2|2.5|1/fADC|
|tLATR|Trigger<br>conversion<br>latency regular<br>and injected<br>channels without<br>conversion abort|CKMODE = 01|-|-|-|-|2.5|2.5|
|tLATR|Trigger<br>conversion<br>latency regular<br>and injected<br>channels without<br>conversion abort|CKMODE = 10|-|-|-|-|2.5|2.5|
|tLATR|Trigger<br>conversion<br>latency regular<br>and injected<br>channels without<br>conversion abort|CKMODE = 11|-|-|-|-|2.25|2.25|
|tLATRINJ|Trigger<br>conversion<br>latency regular<br>injected channels<br>aborting a regular<br>conversion|CKMODE = 00|-|-|2.5|3|3.5|1/fADC|
|tLATRINJ|Trigger<br>conversion<br>latency regular<br>injected channels<br>aborting a regular<br>conversion|CKMODE = 01|-|-|-|-|3.5|3.5|
|tLATRINJ|Trigger<br>conversion<br>latency regular<br>injected channels<br>aborting a regular<br>conversion|CKMODE = 10|-|-|-|-|3.5|3.5|
|tLATRINJ|Trigger<br>conversion<br>latency regular<br>injected channels<br>aborting a regular<br>conversion|CKMODE = 11|-|-|-|-|3.25|3.25|
|tS|Sampling time|-|-|-|1.5|-|810.5|1/fADC|
|tCONV|Total conversion<br>time (including<br>sampling time)|Resolution = N bits|-|-|ts + 0.5<br>+ N/2|-|-|1/fADC|


278/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 184. ADC characteristics** **[(1)(2)]** **(continued)**











|Symbol|Parameter|Conditions|Col4|Col5|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|---|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA,<br>BOOST=11,<br>Differential mode|Resolution = 16 bits, fADC=25 MHz|-|-|-|1440|-|µA|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA,<br>BOOST=11,<br>Differential mode|Resolution = 14 bits, fADC=30 MHz|-|-|-|1350|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA,<br>BOOST=11,<br>Differential mode|Resolution = 12 bits, fADC=40 MHz|-|-|-|990|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=10,<br>Differential mode<br>fADC=25 MHz|Resolution = 16 bits|-|-|-|1080|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=10,<br>Differential mode<br>fADC=25 MHz|Resolution = 14 bits|-|-|-|810|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=10,<br>Differential mode<br>fADC=25 MHz|Resolution = 12 bits|-|-|-|585|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=01,<br>Differential mode<br>fADC=12.5 MHz|Resolution = 16 bits|-|-|-|630|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=01,<br>Differential mode<br>fADC=12.5 MHz|Resolution = 14 bits|-|-|-|432|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=01,<br>Differential mode<br>fADC=12.5 MHz|Resolution = 12 bits|-|-|-|315|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=00,<br>Differential mode<br>fADC=6.25 MHz|Resolution = 16 bits|-|-|-|360|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=00,<br>Differential mode<br>fADC=6.25 MHz|Resolution = 14 bits|-|-|-|270|-|-|
|IDDA_D<br>(ADC)|ADC consumption<br>on VDDA<br>BOOST=00,<br>Differential mode<br>fADC=6.25 MHz|Resolution = 12 bits|-|-|-|225|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=11,<br>Single-ended<br>mode|Resolution = 16 bits, fADC=25 MHz|-|-|-|720|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=11,<br>Single-ended<br>mode|Resolution = 14 bits, fADC=30 MHz|-|-|-|675|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=11,<br>Single-ended<br>mode|Resolution = 12 bits, fADC=40 MHz|-|-|-|495|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=10,<br>Singl-ended mode<br>fADC=25 MHz|Resolution = 16 bits|-|-|-|540|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=10,<br>Singl-ended mode<br>fADC=25 MHz|Resolution = 14 bits|-|-|-|405|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=10,<br>Singl-ended mode<br>fADC=25 MHz|Resolution = 12 bits|-|-|-|292.5|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=01,<br>Single-ended<br>mode<br>fADC=12.5 MHz|Resolution = 16 bits|-|-|-|315|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=01,<br>Single-ended<br>mode<br>fADC=12.5 MHz|Resolution = 14 bits|-|-|-|216|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=01,<br>Single-ended<br>mode<br>fADC=12.5 MHz|Resolution = 12 bits|-|-|-|157.5|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=00,<br>Single-ended<br>mode<br>fADC=6.25 MHz|Resolution = 16 bits|-|-|-|180|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=00,<br>Single-ended<br>mode<br>fADC=6.25 MHz|Resolution = 14 bits|-|-|-|135|-|-|
|IDDA_SE(<br>ADC)|ADC consumption<br>on VDDA<br>BOOST=00,<br>Single-ended<br>mode<br>fADC=6.25 MHz|Resolution = 12 bits|-|-|-|112.5|-|-|
|IDD<br>(ADC)|ADC consumption<br>on VDD|fADC=50 MHz|-|-|-|400|-|-|
|IDD<br>(ADC)|ADC consumption<br>on VDD|fADC=25 MHz|-|-|-|220|-|-|
|IDD<br>(ADC)|ADC consumption<br>on VDD|fADC=12.5 MHz|-|-|-|180|-|-|
|IDD<br>(ADC)|ADC consumption<br>on VDD|fADC=6.25 MHz|-|-|-|120|-|-|
|IDD<br>(ADC)|ADC consumption<br>on VDD|fADC=3.125 MHz|-|-|-|80|-|-|


1. Guaranteed by design.



2. The voltage booster on ADC switches must be used for VDDA < 2.4 V (embedded I/O switches).


3. These values are valid for UFBGA169 and one ADC. Refer to _Getting started with the STM32H7 Series MCU 16-bit ADC_
_(_ AN5354) for values of other packages and multiple ADCs operation.


4. Direct channels are connected to analog I/Os (PA0_C, PA1_C, PC2_C and PC3_C) to optimize ADC performance.


5. Depending on the package, V REF+ can be internally connected to V DDA and V REF- to V SSA .


6. The tolerance is 10 LSBs for 16-bit resolution, 4 LSBs for 14-bit resolution, and 2 LSBs for 12-bit, 10-bit and 8-bit resolutions.


DS12110 Rev 10 279/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 185. Minimum sampling time vs R** **AIN(1)(2)**












|Resolution|RAIN (Ω)|Minimum sampling time (s)|Col4|Col5|
|---|---|---|---|---|
|**Resolution**|**RAIN (Ω)**|**Direct**<br>**channels(3)**|**Fast channels(4)**|**Slow channels(5)**|
|16 bits|47|7.37E-08|1.14E-07|1.72E-07|
|14 bits|47|6.29E-08|9.74E-08|1.55E-07|
|14 bits|68|6.84E-08|1.02E-07|1.58E-07|
|14 bits|100|7.80E-08|1.12E-07|1.62E-07|
|14 bits|150|9.86E-08|1.32E-07|1.80E-07|
|14 bits|220|1.32E-07|1.61E-07|2.01E-07|
|12 bits|47|5.32E-08|8.00E-08|1.29E-07|
|12 bits|68|5.74E-08|8.50E-08|1.32E-07|
|12 bits|100|6.58E-08|9.31E-08|1.40E-07|
|12 bits|150|8.37E-08|1.10E-07|1.51E-07|
|12 bits|220|1.11E-07|1.34E-07|1.73E-07|
|12 bits|330|1.56E-07|1.78E-07|2.14E-07|
|12 bits|470|2.16E-07|2.39E-07|2.68E-07|
|12 bits|680|3.01E-07|3.29E-07|3.54E-07|
|10 bits|47|4.34E-08|6.51E-08|1.08E-07|
|10 bits|68|4.68E-08|6.89E-08|1.11E-07|
|10 bits|100|5.35E-08|7.55E-08|1.16E-07|
|10 bits|150|6.68E-08|8.77E-08|1.26E-07|
|10 bits|220|8.80E-08|1.08E-07|1.40E-07|
|10 bits|330|1.24E-07|1.43E-07|1.71E-07|
|10 bits|470|1.69E-07|1.89E-07|2.13E-07|
|10 bits|680|2.38E-07|2.60E-07|2.80E-07|
|10 bits|1000|3.45E-07|3.66E-07|3.84E-07|
|10 bits|1500|5.15E-07|5.35E-07|5.48E-07|
|10 bits|2200|7.42E-07|7.75E-07|7.78E-07|
|10 bits|3300|1.10E-06|1.14E-06|1.14E-06|



280/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 185. Minimum sampling time vs R** **AIN(1)(2)** **(continued)**







|Resolution|RAIN (Ω)|Minimum sampling time (s)|Col4|Col5|
|---|---|---|---|---|
|**Resolution**|**RAIN (Ω)**|**Direct**<br>**channels(3)**|**Fast channels(4)**|**Slow channels(5)**|
|8 bits|47|3.32E-08|5.10E-08|8.61E-08|
|8 bits|68|3.59E-08|5.35E-08|8.83E-08|
|8 bits|100|4.10E-08|5.83E-08|9.22E-08|
|8 bits|150|5.06E-08|6.76E-08|9.95E-08|
|8 bits|220|6.61E-08|8.22E-08|1.11E-07|
|8 bits|330|9.17E-08|1.08E-07|1.32E-07|
|8 bits|470|1.24E-07|1.40E-07|1.63E-07|
|8 bits|680|1.74E-07|1.91E-07|2.12E-07|
|8 bits|1000|2.53E-07|2.70E-07|2.85E-07|
|8 bits|1500|3.73E-07|3.93E-07|4.05E-07|
|8 bits|2200|5.39E-07|5.67E-07|5.75E-07|
|8 bits|3300|8.02E-07|8.36E-07|8.38E-07|
|8 bits|4700|1.13E-06|1.18E-06|1.18E-06|
|8 bits|6800|1.62E-06|1.69E-06|1.68E-06|
|8 bits|10000|2.36E-06|2.47E-06|2.45E-06|
|8 bits|15000|3.50E-06|3.69E-06|3.65E-06|


1. Guaranteed by design.





2. Data valid at up to 125 °C, with a 47 pF PCB capacitor, and V DDA =1.6 V.


3. Direct channels are connected to analog I/Os (PA0_C, PA1_C, PC2_C and PC3_C) to optimize ADC performance.


4. Fast channels cor respond to PF3, PF5, PF7, PF9, PA6, PC4, PB1, PF11 and PF13.


5. Slow channels correspond to all ADC inputs except for the Direct and Fast channels.


DS12110 Rev 10 281/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 186. ADC accuracy** **[(1)(2)]**





































|Symbol|Parameter|Conditions(3)|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|ET|Total undadjusted error|Direct<br>channel|Single ended|-|+10/–20|-|LSB|
|ET|Total undadjusted error|Direct<br>channel|Differential|-|±15|-|-|
|ET|Total undadjusted error|Fast channel|Single ended|-|+10/–20|-|-|
|ET|Total undadjusted error|Fast channel|Differential|-|±15|-|-|
|ET|Total undadjusted error|Slow<br>channel|Single ended|-|±10|-|-|
|ET|Total undadjusted error|Slow<br>channel|Differential|-|±10|-|-|
|EO|Offset error|-|-|-|±10|-|-|
|EG|Gain error|-|-|-|±15|-|-|
|ED|Differential linearity error|Single ended|Single ended|-|+3/–1|-|-|
|ED|Differential linearity error|Differential|Differential|-|+4.5/–1|-|-|
|EL|Integral linearity error|Direct<br>channel|Single ended|-|±11|-|-|
|EL|Integral linearity error|Direct<br>channel|Differential|-|±7|-|-|
|EL|Integral linearity error|Fast channel|Single ended|-|±13|-|-|
|EL|Integral linearity error|Fast channel|Differential|-|±7|-|-|
|EL|Integral linearity error|Slow<br>channel|Single ended|-|±10|-|-|
|EL|Integral linearity error|Slow<br>channel|Differential|-|±6|-|-|
|ENOB|Effective number of bits|Single ended|Single ended|-|12.2|-|Bits|
|ENOB|Effective number of bits|Differential|Differential|-|13.2|-|-|
|SINAD|Signal-to-noise and<br>distortion ratio|Single ended|Single ended|-|75.2|-|dB|
|SINAD|Signal-to-noise and<br>distortion ratio|Differential|Differential|-|81.2|-|-|
|SNR|Signal-to-noise ratio|Single ended|Single ended|-|77.0|-|-|
|SNR|Signal-to-noise ratio|Differential|Differential|-|81.0|-|-|
|THD|Total harmonic distortion|Single ended|Single ended|-|87|-|-|
|THD|Total harmonic distortion|Differential|Differential|-|90|-|-|


1. Data guaranteed by characterization for BGA packages. The values for LQFP packages might differ.


2. ADC DC accuracy values are measured after internal calibration.


3. ADC clock frequency = 25 MHz, ADC resolution = 16 bits, V DDA =V REF+ =3.3 V and BOOST=11.





Note: ADC accuracy vs. negative injection current: injecting a negative current on any analog
input pins should be avoided as this significantly reduces the accuracy of the conversion
being performed on another analog input. It is recommended to add a Schottky diode (pin to
ground) to analog pins which may potentially inject negative currents.


Any positive injection current within the limits specified for I INJ(PIN) and ΣI INJ(PIN) in
_Section 7.3.14_ does not affect the ADC accuracy.


282/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 92. ADC accuracy characteristics**





























**Figure 93. Typical connection diagram when using the ADC with FT/TT pins**
**featuring analog switch function**

























1. Refer to _Section 7.3.20: 16-bit ADC characteristics_ for the values of R AIN and C ADC .


2. C parasitic represents the capacitance of the PCB (dependent on soldering and PCB layout quality) plus the
pad capacitance (refer to _Table 157: I/O static characteristics_ for the value of the pad capacitance). A high
C parasitic value downgrades conversion accuracy. To remedy this, f ADC should be reduced.


3. Refer to _Table 157: I/O static characteristics_ for the value of I .
lkg


4. Refer to _Figure 68: Power supply scheme_ .


DS12110 Rev 10 283/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**General PCB design guidelines**


Power supply decoupling should be performed as shown in _Figure 94_ or _Figure 95_,
depending on whether V REF+ is connected to V DDA or not. The 100 nF capacitors should be
ceramic (good quality). They should be placed them as close as possible to the chip.


**Figure 94. Power supply and reference decoupling** **(V** **REF+** **not connected to** **V** **DDA** **)**











1. V REF+ input is available on all package whereas the V REF– s available only on UFBGA176+25 and
TFBGA240+25. When V REF- is not available, it is internally connected to V DDA and V SSA .


**Figure 95. Power supply and reference decoupling** **(V** **REF+** **connected to** **V** **DDA** **)**









1. V REF+ input is available on all package whereas the V REF– s available only on UFBGA176+25 and
TFBGA240+25. When V REF- is not available, it is internally connected to V DDA and V SSA .


284/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.21** **DAC characteristics**


**Table 187. DAC characteristics** **[(1)(2)]**

































|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|-|-|1.8|3.3|3.6|V|
|VREF+|Positive reference voltage|-|-|1.80|-|VDDA|VDDA|
|VREF-|Negative reference<br>voltage|-|-|-|VSSA|-|-|
|RL|Resistive Load|DAC output buffer<br>ON|connected<br>to VSSA|5|-|-|kΩ|
|RL|Resistive Load|DAC output buffer<br>ON|connected<br>to VDDA|25|-|-|-|
|RO|Output Impedance|DAC output buffer OFF|DAC output buffer OFF|10.3|13|16|16|
|RBON|Output impedance<br>sample and hold mode,<br>output buffer ON|DAC output buffer<br>ON|VDD =<br>2.7 V|-|-|1.6|kΩ|
|RBON|Output impedance<br>sample and hold mode,<br>output buffer ON|DAC output buffer<br>ON|VDD =<br>2.0 V|-|-|2.6|2.6|
|RBOFF|Output impedance<br>sample and hold mode,<br>output buffer OFF|DAC output buffer<br>OFF|VDD =<br>2.7 V|-|-|17.8|kΩ|
|RBOFF|Output impedance<br>sample and hold mode,<br>output buffer OFF|DAC output buffer<br>OFF|VDD =<br>2.0 V|-|-|18.7|18.7|
|CL|Capacitive Load|DAC output buffer OFF|DAC output buffer OFF|-|-|50|pF|
|CSH|CSH|Sample and Hold mode|Sample and Hold mode|-|0.1|1|µF|
|VDAC_OUT|Voltage on DAC_OUT<br>output|DAC output buffer ON|DAC output buffer ON|0.2|-|VREF+ <br>−0.2|V|
|VDAC_OUT|Voltage on DAC_OUT<br>output|DAC output buffer OFF|DAC output buffer OFF|0|-|VREF+|VREF+|
|tSETTLING|Settling time (full scale:<br>for a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC<br>output buffer ON,<br>CL ≤ 50 pF,<br>RL ≥ 5㏀|±0.5 LSB|-|2.05|-|µs|
|tSETTLING|Settling time (full scale:<br>for a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC<br>output buffer ON,<br>CL ≤ 50 pF,<br>RL ≥ 5㏀|±1 LSB|-|1.97|-|-|
|tSETTLING|Settling time (full scale:<br>for a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC<br>output buffer ON,<br>CL ≤ 50 pF,<br>RL ≥ 5㏀|±2 LSB|-|1.67|-|-|
|tSETTLING|Settling time (full scale:<br>for a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC<br>output buffer ON,<br>CL ≤ 50 pF,<br>RL ≥ 5㏀|±4 LSB|-|1.66|-|-|
|tSETTLING|Settling time (full scale:<br>for a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC<br>output buffer ON,<br>CL ≤ 50 pF,<br>RL ≥ 5㏀|±8 LSB|-|1.65|-|-|
|tSETTLING|Settling time (full scale:<br>for a 12-bit code transition<br>between the lowest and<br>the highest input codes<br>when DAC_OUT reaches<br>the final value of ±0.5LSB,<br>±1LSB, ±2LSB, ±4LSB,<br>±8LSB)|Normal mode, DAC output buffer<br>OFF, ±1LSB CL=10 pF|Normal mode, DAC output buffer<br>OFF, ±1LSB CL=10 pF|-|1.7|2|2|
|tWAKEUP<br>(3)|Wakeup time from off<br>state (setting the ENx bit<br>in the DAC Control<br>register) until the final<br>value of ±1LSB is reached|Normal mode, DAC output buffer<br>ON, CL ≤ 50 pF, RL = 5㏀|Normal mode, DAC output buffer<br>ON, CL ≤ 50 pF, RL = 5㏀|-|5|7.5|µs|
|tWAKEUP<br>(3)|Wakeup time from off<br>state (setting the ENx bit<br>in the DAC Control<br>register) until the final<br>value of ±1LSB is reached|Normal mode, DAC output buffer<br>OFF, CL ≤ 10 pF|Normal mode, DAC output buffer<br>OFF, CL ≤ 10 pF|-|2|5|5|
|PSRR|DC VDDA supply rejection<br>ratio|Normal mode, DAC output buffer<br>ON, CL ≤ 50 pF, RL = 5㏀|Normal mode, DAC output buffer<br>ON, CL ≤ 50 pF, RL = 5㏀|-|−80|−28|dB|


DS12110 Rev 10 285/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 187. DAC characteristics** **[(1)(2)]** **(continued)**











































|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|tSAMP|Sampling time in Sample<br>and Hold mode<br>CL=100 nF<br>(code transition between<br>the lowest input code and<br>the highest input code<br>when DAC_OUT reaches<br>the ±1LSB final value)|MODE<2:0>_V12=100/101<br>(BUFFER ON)|MODE<2:0>_V12=100/101<br>(BUFFER ON)|-|0.7|2.6|ms|
|tSAMP|Sampling time in Sample<br>and Hold mode<br>CL=100 nF<br>(code transition between<br>the lowest input code and<br>the highest input code<br>when DAC_OUT reaches<br>the ±1LSB final value)|MODE<2:0>_V12=110<br>(BUFFER OFF)|MODE<2:0>_V12=110<br>(BUFFER OFF)|-|11.5|18.7|18.7|
|tSAMP|Sampling time in Sample<br>and Hold mode<br>CL=100 nF<br>(code transition between<br>the lowest input code and<br>the highest input code<br>when DAC_OUT reaches<br>the ±1LSB final value)|MODE<2:0>_V12=111<br>(INTERNAL BUFFER OFF)|MODE<2:0>_V12=111<br>(INTERNAL BUFFER OFF)|-|0.3|0.6|µs|
|CIint|Internal sample and hold<br>capacitor|-|-|1.8|2.2|2.6|pF|
|tTRIM|Middle code offset trim<br>time|Minimum time to verify the each<br>code|Minimum time to verify the each<br>code|50|-|-|µs|
|Voffset|Middle code offset for 1<br>trim code step|VREF+ = 3.6 V|VREF+ = 3.6 V|-|850|-|µV|
|Voffset|Middle code offset for 1<br>trim code step|VREF+ = 1.8 V|VREF+ = 1.8 V|-|425|-|-|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|DAC output buffer<br>ON|No load,<br>middle<br>code<br>(0x800)|-|360|-|µA|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|DAC output buffer<br>ON|No load,<br>worst code<br>(0xF1C)|-|490|-|-|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|DAC output buffer<br>OFF|No load,<br>middle/wor<br>st code<br>(0x800)|-|20|-|-|
|IDDA(DAC)|DAC quiescent<br>consumption from VDDA|Sample and Hold mode,<br>CSH=100 nF|Sample and Hold mode,<br>CSH=100 nF|-|360*TON/<br>(TON+TOFF)<br>(4)|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|DAC output buffer<br>ON|No load,<br>middle<br>code<br>(0x800)|-|170|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|DAC output buffer<br>ON|No load,<br>worst code<br>(0xF1C)|-|170|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|DAC output buffer<br>OFF|No load,<br>middle/wor<br>st code<br>(0x800)|-|160|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|Sample and Hold mode, Buffer<br>ON, CSH=100 nF (worst code)|Sample and Hold mode, Buffer<br>ON, CSH=100 nF (worst code)|-|170*TON/<br>(TON+TOFF)<br>(4)|-|-|
|IDDV(DAC)|DAC consumption from<br>VREF+|Sample and Hold mode, Buffer<br>OFF, CSH=100 nF (worst code)|Sample and Hold mode, Buffer<br>OFF, CSH=100 nF (worst code)|-|160*TON/<br>(TON+TOFF)<br>(4)|-|-|


1. Guaranteed by design unless otherwise specified.


286/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


2. TBD stands for “to be defined”.


3. In buffered mode, the output can overshoot above the final value for low input code (starting from the minimum value).


4. T ON is the refresh phase duration, while T OFF is the hold phase duration. Refer to the product reference manual for more
details.


**Table 188. DAC accuracy** **[(1)]**















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|DNL|Differential non<br>linearity(2)|DAC output buffer ON|DAC output buffer ON|−2|-|2|LSB|
|DNL|Differential non<br>linearity(2)|DAC output buffer OFF|DAC output buffer OFF|−2|-|2|2|
|-|Monotonicity|10 bits|10 bits|-|-|-|-|
|INL|Integral non linearity(3)|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀|−4|-|4|LSB|
|INL|Integral non linearity(3)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|−4|-|4|4|
|Offset|Offset error at code<br>0x800(3)|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 3.6 V|-|-|±15|LSB|
|Offset|Offset error at code<br>0x800(3)|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 1.8 V|-|-|±30|±30|
|Offset|Offset error at code<br>0x800(3)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±8|±8|
|Offset1|Offset error at code<br>0x001(4)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±5|LSB|
|OffsetCal|Offset error at code<br>0x800 after factory<br>calibration|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 3.6 V|-|-|±6|LSB|
|OffsetCal|Offset error at code<br>0x800 after factory<br>calibration|DAC output<br>buffer ON,<br>CL ≤50 pF,<br>RL ≥5 ㏀|VREF+ = 1.8 V|-|-|±7|±7|
|Gain|Gain error(5)|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀|-|-|±1|%|
|Gain|Gain error(5)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL|-|-|±1|±1|
|SNR|Signal-to-noise ratio(6)|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz, BW = 500 KHz|DAC output buffer ON,CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz, BW = 500 KHz|-|67.8|-|dB|
|SNR|Signal-to-noise ratio(6)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL,1 kHz, BW =<br>500 KHz|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL,1 kHz, BW =<br>500 KHz|-|67.8|-|-|
|THD|Total harmonic<br>distortion(6)|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz|-|−78.6|-|dB|
|THD|Total harmonic<br>distortion(6)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL, 1 kHz|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL, 1 kHz|-|−78.6|-|-|
|SINAD|Signal-to-noise and<br>distortion ratio(6)|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz|DAC output buffer ON, CL ≤50 pF,<br>RL ≥5 ㏀, 1 kHz|-|67.5|-|dB|
|SINAD|Signal-to-noise and<br>distortion ratio(6)|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL, 1 kHz|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL, 1 kHz|-|67.5|-|-|


DS12110 Rev 10 287/357







320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 188. DAC accuracy** **[(1)]** **(continued)**



|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|ENOB|Effective number of<br>bits|DAC output buffer ON,<br>CL ≤50 pF, RL ≥5 ㏀, 1 kHz|-|10.9|-|bits|
|ENOB|Effective number of<br>bits|DAC output buffer OFF,<br>CL ≤ 50 pF, no RL, 1 kHz|-|10.9|-|-|


1. Guaranteed by characterization.





2. Difference between two consecutive codes minus 1 LSB.


3. Difference between the value measured at Code i and the value measured at Code i on a line drawn between Code 0 and
last Code 4095.


4. Difference between the value measured at Code (0x001) and the ideal value.


5. Difference between the ideal slope of the transfer function and the measured slope computed from code 0x000 and 0xFFF
when the buffer is OFF, and from code giving 0.2 V and (V REF+   - 0.2 V) when the buffer is ON.


6. Signal is −0.5dBFS with F sampling =1 MHz.


**Figure 96. 12-bit buffered /non-buffered DAC**











1. The DAC integrates an output buffer that can be used to reduce the output impedance and to drive external loads directly
without the use of an external operational amplifier. The buffer can be bypassed by configuring the BOFFx bit in the
DAC_CR register.


288/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.22** **Voltage reference buffer characteristics**


**Table 189. VREFBUF characteristics** **[(1)]**





















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 000|2.8|3.3|3.6|V|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 001|2.4|-|3.6|3.6|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 010|2.1|-|3.6|3.6|
|VDDA|Analog supply voltage|Normal mode|VSCALE = 011|1.8|-|3.6|3.6|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 000|1.62|-|2.80|2.80|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 001|1.62|-|2.40|2.40|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 010|1.62|-|2.10|2.10|
|VDDA|Analog supply voltage|Degraded mode|VSCALE = 011|1.62|-|1.80|1.80|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Normal mode|VSCALE = 000|2.498|2.5|2.5035|2.5035|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Normal mode|VSCALE = 001|2.046|2.049|2.052|2.052|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Normal mode|VSCALE = 010|1.801|1.804|1.806|1.806|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Normal mode|VSCALE = 011|1.4995|1.5015|1.504|1.504|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Degraded mode(2)|VSCALE = 000|VDDA−<br>150 mV|-|VDDA|VDDA|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Degraded mode(2)|VSCALE = 001|VDDA−<br>150 mV|-|VDDA|VDDA|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Degraded mode(2)|VSCALE = 010|VDDA−<br>150 mV|-|VDDA|VDDA|
|VREFBUF<br>_OUT|Voltage Reference<br>Buffer Output, at 30 °C,<br>Iload= 100 µA|Degraded mode(2)|VSCALE = 011|VDDA−<br>150 mV|-|VDDA|VDDA|
|TRIM|Trim step resolution|-|-|-|±0.05|±0.1|%|
|CL|Load capacitor|-|-|0.5|1|1.50|uF|
|esr|Equivalent Serial<br>Resistor of CL|-|-|-|-|2|Ω|
|Iload|Static load current|-|-|-|-|4|mA|
|Iline_reg|Line regulation|2.8 V ≤ VDDA ≤ 3.6 V|Iload = 500 µA|-|200|-|ppm/V|
|Iline_reg|Line regulation|2.8 V ≤ VDDA ≤ 3.6 V|Iload = 4 mA|-|100|-|-|
|Iload_reg|Load regulation|500 µA ≤ ILOAD ≤ 4 mA|Normal Mode|-|50|-|ppm/<br>mA|
|Tcoeff|Temperature coefficient|−40 °C < TJ < +125 °C|−40 °C < TJ < +125 °C|-|-|Tcoeff <br>VREFINT <br>+ 100|ppm/<br>°C|
|PSRR|Power supply rejection|DC|-|-|60|-|dB|
|PSRR|Power supply rejection|100KHz|-|-|40|-|-|


DS12110 Rev 10 289/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 189. VREFBUF characteristics** **[(1)]** **(continued)**














|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|tSTART|Start-up time|CL=0.5 µF|-|-|300|-|µs|
|tSTART|Start-up time|CL=1 µF|-|-|500|-|-|
|tSTART|Start-up time|CL=1.5 µF|-|-|650|-|-|
|IINRUSH|Control of maximum<br>DC current drive on<br>VREFBUF_OUT during<br>startup phase(3)|-|-|-|8|-|mA|
|IDDA(VRE<br>FBUF)|VREFBUF<br>consumption from<br>VDDA|ILOAD = 0 µA|-|-|15|25|µA|
|IDDA(VRE<br>FBUF)|VREFBUF<br>consumption from<br>VDDA|ILOAD = 500 µA|-|-|16|30|30|
|IDDA(VRE<br>FBUF)|VREFBUF<br>consumption from<br>VDDA|ILOAD = 4 mA|-|-|32|50|50|



1. Guaranteed by design.


2. In degraded mode, the voltage reference buffer cannot accurately maintain the output voltage (V DDA −drop voltage).


3. To properly control VREFBUF I INRUSH current during the startup phase and the change of scaling, V DDA voltage should be in
the range of 1.8 V-3.6 V, 2.1 V-3.6 V, 2.4 V-3.6 V and 2.8 V-3.6 V for VSCALE = 011, 010, 001 and 000, respectively.


**7.3.23** **Temperature sensor characteristics**


**Table 190. Temperature sensor characteristics**







|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|TL<br>(1)|VSENSE linearity with temperature|-|-|±3|°C|
|Avg_Slope(2)|Average slope|-|2|-|mV/°C|
|V30<br>(3)|Voltage at 30°C ± 5 °C|-|0.62|-|V|
|tstart_run|Startup time in Run mode (buffer startup)|-|-|25.2|µs|
|tS_temp<br>(1)|ADC sampling time when reading the temperature|9|-|-|-|
|Isens<br>(1)|Sensor consumption|-|0.18|0.31|µA|
|Isensbuf<br>(1)|Sensor buffer consumption|-|3.8|6.5|6.5|


1. Guaranteed by design.


2. Guaranteed by characterization.


3. Measured at V DDA = 3.3 V ± 10 mV. The V 30 ADC conversion result is stored in the TS_CAL1
byte.


**Table 191. Temperature sensor calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|TS_CAL1|Temperature sensor raw data acquired value at<br>30 °C, VDDA = 3.3 V|0x1FF1 E820 -0x1FF1 E821|
|TS_CAL2|Temperature sensor raw data acquired value at<br>130 °C, VDDA = 3.3 V|0x1FF1 E840 - 0x1FF1 E841|



290/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.24** **Temperature and V** **BAT** **monitoring**


**Table 192. V** **BAT** **monitoring characteristics**







|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|R|Resistor bridge for VBAT|-|26|-|KΩ|
|Q|Ratio on VBAT measurement|-|4|-|-|
|Er(1)|Error on Q|–10|-|+10|%|
|tS_vbat<br>(1)|ADC sampling time when reading VBATinput|9|-|-|µs|
|VBAThigh|High supply monitoring|-|3.55|-|V|
|VBATlow|Low supply monitoring|-|1.36|-|-|


1. Guaranteed by design.


**Table 193. V** **BAT** **charging characteristics**

|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|RBC|Battery charging resistor|VBRS in PWR_CR3= 0|-|5|-|KΩ|
|RBC|Battery charging resistor|VBRS in PWR_CR3= 1|-|1.5|-|-|



**Table 194. Temperature monitoring characteristics**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|TEMPhigh|High temperature monitoring|-|117|-|°C|
|TEMPlow|Low temperature monitoring|-|**–**25|-|-|



**7.3.25** **Voltage booster for analog switch**


**Table 195. Voltage booster for analog switch characteristics** **[(1)]**

|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD|Supply voltage|-|1.62|2.6|3.6|V|
|tSU(BOOST)|Booster startup time|-|-|-|50|µs|
|IDD(BOOST)|Booster consumption|1.62 V ≤ VDD ≤ 2.7 V|-|-|125|µA|
|IDD(BOOST)|Booster consumption|2.7 V < VDD < 3.6 V|-|-|250|250|



1. Guaranteed by characterization results.


DS12110 Rev 10 291/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**7.3.26** **Comparator characteristics**


**Table 196. COMP characteristics** **[(1)]**






















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage|-|-|1.62|3.3|3.6|V|
|VIN|Comparator input voltage<br>range|-|-|0|-|VDDA|VDDA|
|VBG|Scaler input voltage|-|-|(2)|(2)|(2)|(2)|
|VSC|Scaler offset voltage|-|-|-|±5|±10|mV|
|IDDA(SCALER)|Scaler static consumption<br>from VDDA|BRG_EN=0 (bridge disable)|BRG_EN=0 (bridge disable)|-|0.2|0.3|µA|
|IDDA(SCALER)|Scaler static consumption<br>from VDDA|BRG_EN=1 (bridge enable)|BRG_EN=1 (bridge enable)|-|0.8|1|1|
|tSTART_SCALER|Scaler startup time|-|-|-|140|250|µs|
|tSTART|Comparator startup time to<br>reach propagation delay<br>specification|High-speed mode|High-speed mode|-|2|5|µs|
|tSTART|Comparator startup time to<br>reach propagation delay<br>specification|Medium mode|Medium mode|-|5|20|20|
|tSTART|Comparator startup time to<br>reach propagation delay<br>specification|Ultra-low-power mode|Ultra-low-power mode|-|15|80|80|
|tD<br>(3)|Propagation delay for<br>200 mV step with 100 mV<br>overdrive|High-speed mode|High-speed mode|-|50|80|ns|
|tD<br>(3)|Propagation delay for<br>200 mV step with 100 mV<br>overdrive|Medium mode|Medium mode|-|0.5|1.2|µs|
|tD<br>(3)|Propagation delay for<br>200 mV step with 100 mV<br>overdrive|Ultra-low-power mode|Ultra-low-power mode|-|2.5|7|7|
|tD<br>(3)|Propagation delay for step<br>> 200 mV with 100 mV<br>overdrive only on positive<br>inputs|High-speed mode|High-speed mode|-|50|120|ns|
|tD<br>(3)|Propagation delay for step<br>> 200 mV with 100 mV<br>overdrive only on positive<br>inputs|Medium mode|Medium mode|-|0.5|1.2|µs|
|tD<br>(3)|Propagation delay for step<br>> 200 mV with 100 mV<br>overdrive only on positive<br>inputs|Ultra-low-power mode|Ultra-low-power mode|-|2.5|7|7|
|Voffset|Comparator offset error|Full common mode range|Full common mode range|-|±5|±20|mV|
|Vhys|Comparator hysteresis|No hysteresis|No hysteresis|-|0|-|mV|
|Vhys|Comparator hysteresis|Low hysteresis|Low hysteresis|5|10|22|22|
|Vhys|Comparator hysteresis|Medium hysteresis|Medium hysteresis|8|20|37|37|
|Vhys|Comparator hysteresis|High hysteresis|High hysteresis|16|30|52|52|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Ultra-low-<br>power mode|Static|-|400|600|nA|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Ultra-low-<br>power mode|With 50 kHz<br>±100 mV overdrive<br>square signal|-|800|-|-|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Medium mode|Static|-|5|7|µA|
|IDDA(COMP)|Comparator consumption<br>from VDDA|Medium mode|With 50 kHz<br>±100 mV overdrive<br>square signal|-|6|-|-|
|IDDA(COMP)|Comparator consumption<br>from VDDA|High-speed<br>mode|Static|-|70|100|100|
|IDDA(COMP)|Comparator consumption<br>from VDDA|High-speed<br>mode|With 50 kHz<br>±100 mV overdrive<br>square signal|-|75|-|-|



1. Guaranteed by design, unless otherwise specified.


2. Refer to _Table 127: Embedded reference voltage_ .


292/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


3. Guaranteed by characterization results.


**7.3.27** **Operational amplifier characteristics**


**Table 197. Operational amplifier characteristics**



































|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDDA|Analog supply voltage<br>Range|-|2|3.3|3.6|V|
|CMIR|Common Mode Input<br>Range|-|0|-|VDDA|VDDA|
|VIOFFSET|Input offset voltage|25°C, no load on output|-|-|±1.5|mV|
|VIOFFSET|Input offset voltage|All voltages and<br>temperature, no load|-|-|±2.5|±2.5|
|ΔVIOFFSET|Input offset voltage drift|-|-|±3.0|-|μV/°C|
|TRIMOFFSETP<br>TRIMLPOFFSETP|Offset trim step at low<br>common input voltage<br>(0.1*VDDA)|-|-|1.1|1.5|mV|
|TRIMOFFSETN<br>TRIMLPOFFSETN|Offset trim step at high<br>common input voltage<br>(0.9*VDDA)|-|-|1.1|1.5|1.5|
|ILOAD|Drive current|-|-|-|500|μA|
|ILOAD_PGA|Drive current in PGA mode|-|-|-|270|270|
|CLOAD|Capacitive load|-|-|-|50|pF|
|CMRR|Common mode rejection<br>ratio|-|-|80|-|dB|
|PSRR|Power supply rejection<br>ratio|CLOAD ≤ 50pf /<br>RLOAD ≥ 4 kΩ(1) at 1 kHz,<br>Vcom=VDDA/2|50|66|-|dB|
|GBW|Gain bandwidth for high<br>supply range|200 mV ≤ Output dynamic<br>range ≤ VDDA - 200 mV|4|7.3|12.3|MHz|
|SR|Slew rate (from 10% and<br>90% of output voltage)|Normal mode|-|3|-|V/µs|
|SR|Slew rate (from 10% and<br>90% of output voltage)|High-speed mode|-|30|-|-|
|AO|Open loop gain|200 mV ≤ Output dynamic<br>range ≤ VDDA - 200 mV|59|90|129|dB|
|φm|Phase margin|-|-|55|-|°|
|GM|Gain margin|-|-|12|-|dB|
|VOHSAT|High saturation voltage|Iload=max or RLOAD=min,<br>Input at VDDA|VDDA <br>−100 mV|-|-|mV|
|VOLSAT|Low saturation voltage|Iload=max or RLOAD=min,<br>Input at 0 V|-|-|100|100|


DS12110 Rev 10 293/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 197. Operational amplifier characteristics (continued)**



















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|tWAKEUP|Wake up time from OFF<br>state|Normal<br>mode|CLOAD ≤ 50pf,<br>RLOAD ≥ 4 kΩ,<br>follower<br>configuration|-|0.8|3.2|µs|
|tWAKEUP|Wake up time from OFF<br>state|High<br>speed<br>mode|CLOAD ≤ 50pf,<br>RLOAD ≥ 4 kΩ,<br>follower<br>configuration|-|0.9|2.8|2.8|
|PGA gain|Non inverting gain error<br>value|PGA gain = 2|PGA gain = 2|−1|-|1|%|
|PGA gain|Non inverting gain error<br>value|PGA gain = 4|PGA gain = 4|−2|-|2|2|
|PGA gain|Non inverting gain error<br>value|PGA gain = 8|PGA gain = 8|−2.5|-|2.5|2.5|
|PGA gain|Non inverting gain error<br>value|PGA gain = 16|PGA gain = 16|−3|-|3|3|
|PGA gain|Inverting gain error value|PGA gain = 2|PGA gain = 2|−1|-|1|1|
|PGA gain|Inverting gain error value|PGA gain = 4|PGA gain = 4|−1|-|1|1|
|PGA gain|Inverting gain error value|PGA gain = 8|PGA gain = 8|−2|-|2|2|
|PGA gain|Inverting gain error value|PGA gain = 16|PGA gain = 16|−3|-|3|3|
|PGA gain|External non-inverting gain<br>error value|PGA gain = 2|PGA gain = 2|−1|-|1|1|
|PGA gain|External non-inverting gain<br>error value|PGA gain = 4|PGA gain = 4|−3|-|3|3|
|PGA gain|External non-inverting gain<br>error value|PGA gain = 8|PGA gain = 8|−3.5|-|3.5|3.5|
|PGA gain|External non-inverting gain<br>error value|PGA gain = 16|PGA gain = 16|−4|-|4|4|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(2)|PGA Gain=2|PGA Gain=2|-|10/10|-|kΩ/<br>kΩ|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(2)|PGA Gain=4|PGA Gain=4|-|30/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(2)|PGA Gain=8|PGA Gain=8|-|70/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in non-inverting<br>PGA mode(2)|PGA Gain=16|PGA Gain=16|-|150/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(2)|PGA Gain = -1|PGA Gain = -1|-|10/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(2)|PGA Gain = -3|PGA Gain = -3|-|30/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(2)|PGA Gain = -7|PGA Gain = -7|-|70/10|-|-|
|Rnetwork|R2/R1 internal resistance<br>values in inverting PGA<br>mode(2)|PGA Gain = -15|PGA Gain = -15|-|150/10|-|-|
|Delta R|Resistance variation (R1<br>or R2)|-|-|−15|-|15|%|


294/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 197. Operational amplifier characteristics (continued)**
















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=2|Gain=2|-|GBW/2|-|MHz|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=4|Gain=4|-|GBW/4|-|-|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=8|Gain=8|-|GBW/8|-|-|
|PGA BW|PGA bandwidth for<br>different non inverting gain|Gain=16|Gain=16|-|GBW/16|-|-|
|PGA BW|PGA bandwidth for<br>different inverting gain|Gain = -1|Gain = -1|-|5.00|-|MHz|
|PGA BW|PGA bandwidth for<br>different inverting gain|Gain = -3|Gain = -3|-|3.00|-|-|
|PGA BW|PGA bandwidth for<br>different inverting gain|Gain = -7|Gain = -7|-|1.50|-|-|
|PGA BW|PGA bandwidth for<br>different inverting gain|Gain = -15|Gain = -15|-|0.80|-|-|
|en|Voltage noise density|at<br>1 KHz|output loaded<br>with 4 kΩ|-|140|-|nV/√<br>Hz|
|en|Voltage noise density|at<br>10 KHz|at<br>10 KHz|-|55|-|-|
|IDDA(OPAMP)|OPAMP consumption from<br>VDDA|Normal<br>mode|no Load,<br>quiescent mode,<br>follower|-|570|1000|µA|
|IDDA(OPAMP)|OPAMP consumption from<br>VDDA|High-<br>speed<br>mode|High-<br>speed<br>mode|-|610|1200|1200|



1. R LOAD is the resistive load connected to VSSA or to VDDA.


2. R2 is the internal resistance between the OPAMP output and th OPAMP inverting input. R1 is the internal resistance
between the OPAMP inverting input and ground. PGA gain = 1 + R2/R1.


**7.3.28** **Digital filter for Sigma-Delta Modulators (DFSDM) characteristics**


Unless otherwise specified, the parameters given in _Table 198_ for DFSDM are derived from
tests performed under the ambient temperature, fPCLKx frequency and supply voltage
conditions summarized in _Table 122: General operating conditions_ .


       - Output speed is set to OSPEEDRy[1:0] = 10


       - Capacitive load C L = 30 pF


       - Measurement points are done at CMOS levels: 0.5V DD

       - VOS level set to VOS1


Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (DìFSDM_CKINx, DFSDM_DATINx, DFSDM_CKOUT for DFSDM).


DS12110 Rev 10 295/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 198. DFSDM measured timing - 1.62-3.6 V**


























|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|fDFSDMCLK|DFSDM<br>clock|1.62 < VDD < 3.6 V|1.62 < VDD < 3.6 V|-|-|250|MHz|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|-|-|20|20|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>2.7 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>2.7 < VDD < 3.6 V|-|-|20|20|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode (SPICKSEL[1:0]¹0),<br>1.62 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode (SPICKSEL[1:0]¹0),<br>1.62 < VDD < 3.6 V|-|-|20|20|
|fCKIN<br>(1/TCKIN)|Input clock<br>frequency|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode (SPICKSEL[1:0]¹0),<br>2.7 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>Internal clock mode (SPICKSEL[1:0]¹0),<br>2.7 < VDD < 3.6 V|-|-|20|20|
|fCKOUT|Output clock<br>frequency|1.62 < VDD < 3.6 V|1.62 < VDD < 3.6 V|-|-|20|20|
|DuCyCK<br>OUT|Output clock<br>frequency<br>duty cycle|1.62 < VDD < 3.6 V|Even division,<br>CKOUTDIV[7:0] =<br> 1, 3, 5...|45|50|55|%|
|DuCyCK<br>OUT|Output clock<br>frequency<br>duty cycle|1.62 < VDD < 3.6 V|Odd division,<br>CKOUTDIV[7:0] =<br> 2, 4, 6...|(((n/2+1)/(n+1))<br>*100)–5|(((n/2+1)/(n+1))<br>*100)|(((n/2+1)/(n+1))<br>*100)+5|(((n/2+1)/(n+1))<br>*100)+5|
|twh(CKIN)<br>twl(CKIN)|Input clock<br>high and low<br>time|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|TCKIN/2-0.5|TCKIN/2|-|ns|
|tsu|Data input<br>setup time|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|1.5|-|-|-|
|th|Data input<br>hold time|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|SPI mode (SITP[1:0]=0,1),<br>External clock mode (SPICKSEL[1:0]=0),<br>1.62 < VDD < 3.6 V|0.5|-|-|-|
|TManchester|Manchester<br>data period<br>(recovered<br>clock period)|Manchester mode (SITP[1:0]=2,3),<br>Internal clock mode (SPICKSEL[1:0]¹0),<br>1.62 < VDD < 3.6 V|Manchester mode (SITP[1:0]=2,3),<br>Internal clock mode (SPICKSEL[1:0]¹0),<br>1.62 < VDD < 3.6 V|(CKOUTDIV+1)<br>* TDFSDMCLK|-|(2*CKOUTDIV)<br>* TDFSDMCLK|(2*CKOUTDIV)<br>* TDFSDMCLK|



296/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 97. Channel transceiver timing diagrams**



















DS12110 Rev 10 297/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**7.3.29** **Camera interface (DCMI) timing specifications**


Unless otherwise specified, the parameters given in _Table 199_ for DCMI are derived from
tests performed under the ambient temperature, f HCLK frequency and VDD supply voltage
summarized in _Table 122: General operating conditions_, with the following configuration:


      - DCMI_PIXCLK polarity: falling


      - DCMI_VSYNC and DCMI_HSYNC polarity: high


      - Data formats: 14 bits


      - Capacitive load C L =30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - VOS level set to VOS1


**Table 199. DCMI characteristics** **[(1)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|-|Frequency ratio DCMI_PIXCLK/fHCLK|-|0.4|-|
|DCMI_PIXCLK|Pixel Clock input|-|80|MHz|
|Dpixel|Pixel Clock input duty cycle|30|70|%|
|tsu(DATA)|Data input setup time|3|-|-|
|th(DATA)|Data hold time|1|-|-|
|tsu(HSYNC),<br>tsu(VSYNC)|DCMI_HSYNC/ DCMI_VSYNC input setup time|2|-|ns|
|th(HSYNC),<br>th(VSYNC)|DCMI_HSYNC/ DCMI_VSYNC input hold time|1|-|-|



1. Guaranteed by characterization results.


**Figure 98. DCMI timing diagram**








|Col1|Col2|
|---|---|
||tsu(VSY|
|||





298/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.30** **LCD-TFT controller (LTDC) characteristics**


Unless otherwise specified, the parameters given in _Table 200_ for LCD-TFT are derived
from tests performed under the ambient temperature, f HCLK frequency and VDD supply
voltage summarized in _Table 122: General operating conditions_, with the following
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


      - VOS level set to VOS1


**Table 200. LTDC characteristics** **[(1)]**




















|Symbol|Parameter|Col3|Col4|Min|Max|Unit|
|---|---|---|---|---|---|---|
|fCLK|LTDC clock<br>output<br>frequency|2.7<VDD<3.6 V<br>20pF|2.7<VDD<3.6 V<br>20pF|-|150|MHz|
|fCLK|LTDC clock<br>output<br>frequency|2.7<VDD<3.6 V|2.7<VDD<3.6 V|2.7<VDD<3.6 V|133|133|
|fCLK|LTDC clock<br>output<br>frequency|1.62<VDD<3.6 V|1.62<VDD<3.6 V|1.62<VDD<3.6 V|90|90|
|DCLK|LTDC clock output duty cycle|LTDC clock output duty cycle|LTDC clock output duty cycle|45|55|%|
|tw(CLKH),<br>tw(CLKL)|Clock High time, low time|Clock High time, low time|Clock High time, low time|tw(CLK)//2-0.5|tw(CLK)//2+0.5|-|
|tv(DATA)|Data output valid time|Data output valid time|2.7<VDD<3.6 V|-|0.5|0.5|
|th(DATA)|th(DATA)|th(DATA)|1.62<VDD<3.6 V|1.62<VDD<3.6 V|5|5|
|tv(DATA)|Data output hold time|Data output hold time|Data output hold time|0|-|-|
|tv(HSYNC),<br>tv(VSYNC),<br>tv(DE)|HSYNC/VSYNC/DE output<br>valid time|HSYNC/VSYNC/DE output<br>valid time|2.7<VDD<3.6 V|-|0.5|-|
|tv(HSYNC),<br>tv(VSYNC),<br>tv(DE)|HSYNC/VSYNC/DE output<br>valid time|HSYNC/VSYNC/DE output<br>valid time|1.62<VDD<3.6 V|-|5|5|
|th(HSYNC),<br>th(VSYNC),<br>th(DE)|HSYNC/VSYNC/DE output hold time|HSYNC/VSYNC/DE output hold time|HSYNC/VSYNC/DE output hold time|0|-|-|



1. Guaranteed by characterization results.



DS12110 Rev 10 299/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 99. LCD-TFT horizontal timing diagram**








|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||tv(DE)|||t|v(HSYNC)|
||tv(DE)|||th(DE)|th(DE)|
||tv(D|tv(D|tv(D|tv(D|tv(D|
|||||||







**Figure 100. LCD-TFT vertical timing diagram**















300/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**7.3.31** **Timer characteristics**


The parameters given in _Table 201_ are guaranteed by design.


Refer to _Section 7.3.15: I/O port characteristics_ for details on the input/output alternate
function characteristics (output compare, input capture, external clock, PWM output).


**Table 201. TIMx characteristics** **[(1)(2)]**











|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|tres(TIM)|Timer resolution time|AHB/APBx prescaler=1<br>or 2 or 4, fTIMxCLK =<br>240 MHz|1|-|tTIMxCLK|
|tres(TIM)|Timer resolution time|AHB/APBx<br>prescaler>4, fTIMxCLK =<br>120 MHz|1|-|tTIMxCLK|
|fEXT|Timer external clock<br>frequency on CH1 to CH4|fTIMxCLK = 240 MHz|0|fTIMxCLK/2|MHz|
|ResTIM|Timer resolution|Timer resolution|-|16/32|bit|
|tMAX_COUNT|Maximum possible count<br>with 32-bit counter|-|-|65536 ×<br>65536|tTIMxCLK|


1. TIMx is used as a general term to refer to the TIM1 to TIM17 timers.


2. Guaranteed by design.


3. The maximum timer frequency on APB1 or APB2 is up to 240 MHz, by setting the TIMPRE bit in the
RCC_CFGR register, if APBx prescaler is 1 or 2 or 4, then TIMxCLK = rcc_hclk1, otherwise TIMxCLK = 4x
F rcc_pclkx_d2 .


**7.3.32** **Communication interfaces**


**I** **[2]** **C interface characteristics**


The I [2] C interface meets the timings requirements of the I 2 C-bus specification and user
manual revision 03 for:


      - Standard-mode (Sm): with a bit rate up to 100 kbit/s


      - Fast-mode (Fm): with a bit rate up to 400 kbit/s


      - Fast-mode Plus (Fm+): with a bit rate up to 1 Mbit/s.


The I [2] C timings requirements are guaranteed by design when the I [2] C peripheral is properly
configured (refer to RM0399 reference manual) and when the i2c_ker_ck frequency is
greater than the minimum shown in the table below:


DS12110 Rev 10 301/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 202. Minimum i2c_ker_ck frequency in all I** **[2]** **C modes**






|Symbol|Parameter|Condition|Col4|Min|Unit|
|---|---|---|---|---|---|
|f(I2CCLK)|I2CCLK<br>frequency|Standard-mode|-|2|MHz|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode|Analog Filtre ON<br>DNF=0|8|8|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode|Analog Filtre OFF<br>DNF=1|9|9|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode Plus|Analog Filtre ON<br>DNF=0|17|17|
|f(I2CCLK)|I2CCLK<br>frequency|Fast-mode Plus|Analog Filtre OFF<br>DNF=1|16|-|



The SDA and SCL I/O requirements are met with the following restrictions:


- The SDA and SCL I/O pins are not “true” open-drain. When configured as open-drain,
the PMOS connected between the I/O pin and V DDIOx is disabled, but still present.


- The 20 mA output drive requirement in Fast-mode Plus is not supported. This limits the
maximum load C Load supported in Fm+, which is given by these formulas:

t r(SDA/SCL) =0.8473xR P xC Load
R P(min) = (V DD -V OL(max) )/I OL(max)
Where R P is the I2C lines pull-up. Refer to _Section 7.3.15: I/O port characteristics_ for
the I [2] C I/Os characteristics.


All I [2] C SDA and SCL I/Os embed an analog filter. Refer to the table below for the analog fil
ter characteristics:


**Table 203. I** **[2]** **C analog filter characteristics** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|tAF|Maximum pulse width of spikes<br>that are suppressed by analog<br>filter|50(2)|80(3)|ns|


1. Guaranteed by characterization results.


2. Spikes with widths below t AF(min) are filtered.

3. Spikes with widths above t AF(max) are not filtered.


**USART interface characteristics**







Unless otherwise specified, the parameters given in _Table 204_ for USART are derived from
tests performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
conditions summarized in _Table 122: General operating conditions_, with the following
configuration:


      - Output speed is set to OSPEEDRy[1:0] = 10


      - Capacitive load C L = 30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.


      - VOS level set to VOS1


302/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (NSS, CK, TX, RX for USART).



**Table 204. USART characteristics** **[(1)]**












|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fCK|USART clock frequency|Master mode|-|-|12.5|MHz|
|fCK|USART clock frequency|Slave mode|Slave mode|Slave mode|25|25|
|tsu(NSS)|NSS setup time|Slave mode|tker+1|-|-|-|
|th(NSS)|NSS hold time|Slave mode|2|-|-|-|
|tw(SCKH), <br>tw(SCKL)|CK high and low time|Master mode|1/fCK/2-2|1/fCK/2|1/fCK/2+2|1/fCK/2+2|
|tsu(RX)|Data input setup time|Master mode|tker+6|-|-|ns|
|tsu(RX)|Data input setup time|Slave mode|1.5|-|-|-|
|th(RX)|Data input hold time|Master mode|0|-|-|-|
|th(RX)|Data input hold time|Slave mode|1.5|-|-|-|
|tv(TX)|Data output valid time|Slave mode|-|12|20|20|
|tv(TX)|Data output valid time|Master mode|-|0.5|1|1|
|th(TX)|Data output hold time|Slave mode|9|-|-|-|
|th(TX)|Data output hold time|Master mode|0|-|-|-|



1. Guaranteed by characterization results.


**Figure 101. USART timing diagram in Master mode**










|Col1|Col2|Col3|
|---|---|---|
||tw(SCKH)<br>tw(SCKL)|tw(SCKH)<br>tw(SCKL)|
||MSB IN||













1. Measurement points are done at 0.5V DD and with external C L = 30 pF.


DS12110 Rev 10 303/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 102. USART timing diagram in Slave mode**































**SPI interface characteristics**


Unless otherwise specified, the parameters given in _Table 205_ for SPI are derived from tests
performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
conditions summarized in _Table 122: General operating conditions_, with the following
configuration:


      - Output speed is set to OSPEEDRy[1:0] = 11


      - Capacitive load C L = 30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.


      - HSLV activated when VDD ≤ 2.7 V


      - VOS level set to VOS1


Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (NSS, SCK, MOSI, MISO for SPI).


304/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 205. SPI dynamic characteristics** **[(1)]**



























|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fSCK|SPI clock frequency|Master mode<br>1.62<VDD<3.6 V<br>SPI1, 2, 3|-|-|80|MHz|
|fSCK|SPI clock frequency|Master mode<br>2.7<VDD<3.6 V<br>SPI1, 2, 3|Master mode<br>2.7<VDD<3.6 V<br>SPI1, 2, 3|Master mode<br>2.7<VDD<3.6 V<br>SPI1, 2, 3|100|100|
|fSCK|SPI clock frequency|Master mode<br>1.62<VDD<3.6 V<br>SPI4, 5, 6|Master mode<br>1.62<VDD<3.6 V<br>SPI4, 5, 6|Master mode<br>1.62<VDD<3.6 V<br>SPI4, 5, 6|50|50|
|fSCK|SPI clock frequency|Slave receiver mode<br>1.62<VDD<3.6 V|Slave receiver mode<br>1.62<VDD<3.6 V|Slave receiver mode<br>1.62<VDD<3.6 V|100|100|
|fSCK|SPI clock frequency|Slave mode transmitter/full duplex<br>2.7<VDD<3.6 V|Slave mode transmitter/full duplex<br>2.7<VDD<3.6 V|Slave mode transmitter/full duplex<br>2.7<VDD<3.6 V|31|31|
|fSCK|SPI clock frequency|Slave mode transmitter/full duplex<br>1.62 <VDD<3.6 V|Slave mode transmitter/full duplex<br>1.62 <VDD<3.6 V|Slave mode transmitter/full duplex<br>1.62 <VDD<3.6 V|29|29|
|tsu(NSS)|NSS setup time|Slave mode|2|-|-|-|
|th(NSS)|NSS hold time|Slave mode|1|-|-|-|
|tw(SCKH), <br>tw(SCKL)|SCK high and low time|Master mode|TPCLK-2|TPCLK|TPCLK+2|TPCLK+2|
|tsu(MI)|Data input setup time|Master mode|2|-|-|ns|
|tsu(SI)|tsu(SI)|Slave mode|1|-|-|-|
|th(MI)|Data input hold time|Master mode|3|-|-|-|
|th(SI)|th(SI)|Slave mode|2|-|-|-|
|ta(SO)|Data output access time|Slave mode|9|13|27|27|
|tdis(SO)|Data output disable time|Slave mode|0|1|5|5|
|tv(SO)|Data output valid time|Slave mode<br>2.7<VDD<3.6 V|-|12.5|16|16|
|tv(SO)|Data output valid time|Slave mode<br>1.62<VDD<3.6 V|-|12.5|17|17|
|tv(MO)|tv(MO)|Master mode|-|1|3|3|
|th(SO)|Data output hold time|Slave mode<br>1.62<VDD<3.6 V|10|-|-|-|
|th(MO)|th(MO)|Master mode|0|-|-|-|


1. Guaranteed by characterization results.


DS12110 Rev 10 305/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 103. SPI timing diagram - slave mode and CPHA = 0**































**Figure 104. SPI timing diagram - slave mode and CPHA = 1** **[(1)]**























1. Measurement points are done at 0.5V DD and with external C L = 30 pF.


306/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 105. SPI timing diagram - master mode** **[(1)]**












|Col1|tw(SCKH)<br>tw(SCKL)|Col3|
|---|---|---|
||MSB IN||







|BIT1 OUT|Col2|
|---|---|
|BIT1 OUT||


1. Measurement points are done at 0.5V DD and with external C L = 30 pF.


**I** **[2]** **S Interface characteristics**





Unless otherwise specified, the parameters given in _Table 206_ for I [2] S are derived from tests
performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
conditions summarized in _Table 122: General operating conditions_, with the following
configuration:


- Output speed is set to OSPEEDRy[1:0] = 10


- Capacitive load C L = 30 pF


- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.


- HSLV activated when VDD ≤ 2.7 V


- VOS level set to VOS1


Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output alternate
function characteristics (CK,SD,WS).


DS12110 Rev 10 307/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 206. I** **[2]** **S dynamic characteristics** **[(1)]**

















|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|fMCK|I2S main clock output|-|256x8K|256FS|MHz|
|fCK|I2S clock frequency|Master data|-|64FS|MHz|
|fCK|I2S clock frequency|Slave data|-|64FS|64FS|
|tv(WS)|WS valid time|Master mode|-|3|ns|
|th(WS)|WS hold time|Master mode|0|-|-|
|tsu(WS)|WS setup time|Slave mode|1|-|-|
|th(WS)|WS hold time|Slave mode|1|-|-|
|tsu(SD_MR)|Data input setup time|Master receiver|1|-|-|
|tsu(SD_SR)|tsu(SD_SR)|Slave receiver|1|-|-|
|th(SD_MR)|Data input hold time|Master receiver|4|-|-|
|th(SD_SR)|th(SD_SR)|Slave receiver|2|-|-|
|tv(SD_ST)|Data output valid time|Slave transmitter (after enable<br>edge)|-|17|17|
|tv(SD_MT)|tv(SD_MT)|Master transmitter (after<br>enable edge)|-|3|3|
|th(SD_ST)|Data output hold time|Slave transmitter (after enable<br>edge)|9|-|-|
|th(SD_MT)|th(SD_MT)|Master transmitter (after<br>enable edge)|0|-|-|


1. Guaranteed by characterization results.


**Figure 106. I** **[2]** **S slave timing diagram (Philips protocol)** **[(1)]**


1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.


308/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 107. I** **[2]** **S master timing diagram (Philips protocol)** **[(1)]**


1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.


**SAI characteristics**


Unless otherwise specified, the parameters given in _Table 207_ for SAI are derived from tests
performed under the ambient temperature, f PCLKx frequency and VDD supply voltage
conditions summarized in _Table 122: General operating conditions_, with the following
configuration:


      - Output speed is set to OSPEEDRy[1:0] = 10


      - Capacitive load C L = 30 pF


      - IO Compensation cell activated.


      - Measurement points are done at CMOS levels: 0.5VDD


      - VOS level set to VOS1.

Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output

alternate function characteristics (SCK,SD,WS).


**Table 207. SAI characteristics** **[(1)]**

|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|fMCK|SAI Main clock output|-|256x8K|256xFS|MHz|
|fCK|SAI clock<br>frequency(2)|Master Data: 32 bits|-|128xFS<br>(3)|128xFS<br>(3)|
|fCK|SAI clock<br>frequency(2)|Slave Data: 32 bits|-|128xFS<br>(3)|128xFS<br>(3)|



DS12110 Rev 10 309/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 207. SAI characteristics** **[(1)]** **(continued)**





















|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|tv(FS)|FS valid time|Master mode<br>2.7≤VDD≤3.6|-|13|ns|
|tv(FS)|FS valid time|Master mode<br>1.62≤VDD≤3.6|-|20|20|
|tsu(FS)|FS hold time|Master mode|8|-|-|
|th(FS)|FS setup time|Slave mode|1|-|-|
|th(FS)|FS hold time|Slave mode|1|-|-|
|tsu(SD_A_MR)|Data input setup time|Master receiver|0.5|-|-|
|tsu(SD_B_SR)|tsu(SD_B_SR)|Slave receiver|1|-|-|
|th(SD_A_MR)|Data input hold time|Master receiver|3.5|-|-|
|th(SD_B_SR)|th(SD_B_SR)|Slave receiver|2|-|-|
|tv(SD_B_ST)|Data output valid time|Slave transmitter (after enable<br>edge)<br>2.7≤VDD≤3.6|-|14|14|
|tv(SD_B_ST)|Data output valid time|Slave transmitter (after enable<br>edge)<br>1.62≤VDD≤3.6|-|20|20|
|th(SD_B_ST)|Data output hold time|Slave transmitter (after enable<br>edge)|9|-|-|
|tv(SD_A_MT)|Data output valid time|Master transmitter (after enable<br>edge)<br>2.7≤VDD≤3.6|-|12|12|
|tv(SD_A_MT)|Data output valid time|Master transmitter (after enable<br>edge)<br>1.62≤VDD≤3.6|-|19|19|
|th(SD_A_MT)|Data output hold time|Master transmitter (after enable<br>edge)|7.5|-|-|


1. Guaranteed by characterization results.


2. APB clock frequency must be at least twice SAI clock frequency.


3. With F S =192 kHz.


310/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 108. SAI master timing waveforms**



















**Figure 109. SAI slave timing waveforms**























**MDIO characteristics**


**Table 208. MDIO Slave timing** **parameters**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|FMDC|Management Data Clock|-|-|30|MHz|
|td(MDIO)|Management Data Iput/output output valid time|8|10|19|ns|
|tsu(MDIO)|Management Data Iput/output setup time|1|-|-|-|
|th(MDIO)|Management Data Iput/output hold time|1|-|-|-|



DS12110 Rev 10 311/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 110. MDIO Slave timing diagram**









**SD/SDIO MMC card host interface (SDMMC) characteristics**


Unless otherwise specified, the parameters given in _Table 209_ and _Table 210_ for SDIO are
derived from tests performed under the ambient temperature, f PCLKx frequency and VDD
supply voltage summarized in _Table 122: General operating conditions_, with the following
configuration:


      - Output speed is set to OSPEEDRy[1:0] = 0x11


      - Capacitive load C L =30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.


      - HSLV activated when V DD ≤ 2.7 V


      - VOS level set to VOS1

Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output

characteristics.


**Table 209. Dynamics characteristics: SD / MMC characteristics, V** **DD** **= 2.7 to 3.6 V** **[(1)(2)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPP|Clock frequency in data transfer mode|-|0|-|133|MHz|
|-|SDIO_CK/fPCLK2 frequency ratio|-|-|-|8/3|-|
|tW(CKL)|Clock low time|fPP =52MHz|8.5|9.5|-|ns|
|tW(CKH)|Clock high time|fPP =52MHz|8.5|9.5|-|-|
|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|**CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR(3)/DDR(3) mode**|
|tISU|Input setup time HS|-|2.5|-|-|ns|
|tIH|Input hold time HS|-|0.5|-|-|-|
|tIDW<br>(4)|Input valid window (variable window)|-|3|-|-|-|
|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|**CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR(3) mode**|
|tOV|Output valid time HS|-|-|3.5|5|ns|
|tOH|Output hold time HS|-|3|-|-|-|



312/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 209. Dynamics characteristics: SD / MMC characteristics, V** **DD** **= 2.7 to 3.6 V** **[(1)(2)]** **(continued)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|**CMD, D inputs (referenced to CK) in SD default mode**|
|tISUD|Input setup time SD|-|2.5|-|-|ns|
|tIHD|Input hold time SD|-|0.5|-|-|-|
|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|**CMD, D outputs (referenced to CK) in SD default mode**|
|tOVD|Output valid default time SD|-|-|0.5|2|ns|
|tOHD|Output hold default time SD|-|0|-|-|-|



1. Guaranteed by characterization results.


2. Above 100 MHz, C L = 20 pF.


3. An external voltage converter is required to support SD 1.8 V.


4. The minimum window of time where the data needs to be stable for proper sampling in tuning mode.


**Table 210. Dynamics characteristics: eMMC characteristics VDD = 1.71V to 1.9V** **[(1)(2)]**







|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|fPP|Clock frequency in data transfer<br>mode|-|0|-|120|MHz|
|-|SDIO_CK/fPCLK2 frequency ratio|-|-|-|8/3|-|
|tW(CKL)|Clock low time|fPP =52 MHz|8.5|9.5|-|ns|
|tW(CKH)|Clock high time|fPP =52 MHz|8.5|9.5|-|-|
|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|**CMD, D inputs (referenced to CK) in eMMC mode**|
|tISU|Input setup time HS|-|2|-|-|ns|
|tIH|Input hold time HS|-|1.5|-|-|-|
|tIDW<br>(3)|Input valid window (variable<br>window)|-|3.5|-|-|-|
|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|**CMD, D outputs (referenced to CK) in eMMC mode**|
|tOVD|Output valid time HS|-|-|5|7|ns|
|tOHD|Output hold time HS|-|3|-|-|-|


1. Guaranteed by characterization results.


2. C L = 20 pF.


3. The minimum window of time where the data needs to be stable for proper sampling in tuning mode.


DS12110 Rev 10 313/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 111. SDIO high-speed mode**


**Figure 112. SD default mode**


**Figure 113. DDR mode**




















|Col1|Col2|
|---|---|
|IO|1|


|Col1|Col2|thr(IN)|
|---|---|---|
||||
|IO3|I|O4|





314/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**USB OTG_FS characteristics**


The USB interface is fully compliant with the USB specification version 2.0 and is USB-IF
certified (for Full-speed device operation).


**Table 211. USB OTG_FS electrical characteristics**












|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD33USB|USB transceiver operating<br>voltage|-|3.0(1)|-|3.6|V|
|RPUI|Embedded USB_DP pull-up<br>value during idle|-|900|1250|1600|Ω|
|RPUR|Embedded USB_DP pull-up<br>value during reception|-|1400|2300|3200|3200|
|ZDRV|Output driver impedance(2)|Driver high<br>and low|28|36|44|44|



1. The USB functionality is ensured down to 2.7 V but not the full USB electrical characteristics which are
degraded in the 2.7 to 3.0 V voltage range.


2. No external termination series resistors are required on USB_DP (D+) and USB_DM (D-); the matching
impedance is already included in the embedded driver.


**USB OTG_HS characteristics**


Unless otherwise specified, the parameters given in _Table 212_ for ULPI are derived from
tests performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
summarized in _Table 122: General operating conditions_, with the following configuration:


- Output speed is set to OSPEEDRy[1:0] = 11


- Capacitive load C L =20 pF


- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.


- VOS level set to VOS1

Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output

characteristics.


**Table 212. Dynamics characteristics: USB ULPI** **[(1)]**














|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|tSC|Control in (ULPI_DIR, ULPI_NXT) setup<br>time|-|2.5|-|-|ns|
|tSC|Control in (ULPI_DIR, ULPI_NXT) setup<br>time|-|4.5(2)|-|-|-|
|tHC|Control in (ULPI_DIR, ULPI_NXT) hold<br>time|-|2|-|-|-|
|tSD|Data in setup time|-|2.5|-|-|-|
|tHD|Data in hold time|-|0|-|-|-|
|tDC/tDD|Control/Datal output delay|2.7<VDD<3.6 V<br>CL=20 pF|-|9|9.5|9.5|
|tDC/tDD|Control/Datal output delay|1.71<VDD<3.6 V<br>CL=15 pF|-|9|14|14|



DS12110 Rev 10 315/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


1. Guaranteed by characterization results.


2. When using PC2_C/PC3_C.


**Figure 114. ULPI timing diagram**













**Ethernet interface characteristics**


Unless otherwise specified, the parameters given in _Table 213_, _Table 214_ and _Table 215_ for
SMI, RMII and MII are derived from tests performed under the ambient temperature,
f rcc_c_ck frequency and V DD supply voltage conditions summarized in _Table 122: General_
_operating conditions_, with the following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 10


      - Capacitive load C L =20 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.


      - HSLV activated when VDD ≤ 2.7 V


      - VOS level set to VOS1

Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output

characteristics:


**Table 213. Dynamics characteristics: Ethernet MAC signals for SMI** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tMDC|MDC cycle time( 2.5 MHz)|400|400|403|ns|
|Td(MDIO)|Write data valid time|0.5|1.5|4|4|
|tsu(MDIO)|Read data setup time|12.5|-|-|-|
|th(MDIO)|Read data hold time|0|-|-|-|



1. Guaranteed by characterization results.


316/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Figure 115. Ethernet SMI timing diagram**


**Table 214. Dynamics characteristics: Ethernet MAC signals for RMII** **[(1)]**



|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tsu(RXD)|Receive data setup time|2|-|-|ns|
|tih(RXD)|Receive data hold time|2|-|-|-|
|tsu(CRS)|Carrier sense setup time|1.5|-|-|-|
|tih(CRS)|Carrier sense hold time|1.5|-|-|-|
|td(TXEN)|Transmit enable valid delay time|7|8|9.5|9.5|
|td(TXD)|Transmit data valid delay time|8|9|11|11|


1. Guaranteed by characterization results.


**Figure 116. Ethernet RMII timing diagram**











DS12110 Rev 10 317/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Table 215. Dynamics characteristics: Ethernet MAC signals for MII** **[(1)]**



|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|tsu(RXD)|Receive data setup time|2|-|-|ns|
|tih(RXD)|Receive data hold time|2|-|-|-|
|tsu(DV)|Data valid setup time|1.5|-|-|-|
|tih(DV)|Data valid hold time|1.5|-|-|-|
|tsu(ER)|Error setup time|1.5|-|-|-|
|tih(ER)|Error hold time|0.5|-|-|-|
|td(TXEN)|Transmit enable valid delay time|9|10|11|11|
|td(TXD)|Transmit data valid delay time|8.5|9.5|12.5|12.5|


1. Guaranteed by characterization results.















**JTAG/SWD interface characteristics**


Unless otherwise specified, the parameters given in _Table 216_ and _Table 217_ for
JTAG/SWD are derived from tests performed under the ambient temperature, f rcc_c_ck
frequency and V DD supply voltage summarized in _Table 122: General operating conditions_,
with the following configuration:


      - Output speed is set to OSPEEDRy[1:0] = 0x10


      - Capacitive load C L =30 pF


      - Measurement points are done at CMOS levels: 0.5V DD

      - VOS level set to VOS1

Refer to _Section 7.3.15: I/O port characteristics_ for more details on the input/output

characteristics:


318/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Electrical characteristics (rev V)**


**Table 216. Dynamics JTAG characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fpp|TCK clock frequency|2.7V <VDD< 3.6 V|-|-|37|MHz|
|1/tc(TCK)|1/tc(TCK)|1.62 <VDD< 3.6 V|-|-|27.5|27.5|
|tisu(TMS)|TMS input setup time|-|2.5|-|-|-|
|tih(TMS)|TMS input hold time|-|1|-|-|-|
|tisu(TDI)|TDI input setup time|-|1.5|-|-|-|
|tih(TDI)|TDI input hold time|-|1|-|-|-|
|tov(TDO)|TDO output valid time|2.7V <VDD< 3.6 V|-|8|13.5|-|
|tov(TDO)|TDO output valid time|1.62 <VDD< 3.6 V|-|8|18|-|
|toh(TDO)|TDO output hold time|-|7|-|-|-|



**Table 217. Dynamics SWD characteristics:**









|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Fpp|SWCLK clock frequency|2.7V <VDD< 3.6 V|-|-|71|MHz|
|1/tc(SWCLK)|1/tc(SWCLK)|1.62 <VDD< 3.6 V|-|-|52.5|52.5|
|tisu(SWDIO)|SWDIO input setup time|-|2.5|-|-|ns|
|tih(SWDIO)|SWDIO input hold time|-|1|-|-|-|
|tov(SWDIO)|SWDIO output valid time|2.7V <VDD< 3.6 V|-|8.5|14|14|
|tov(SWDIO)|SWDIO output valid time|1.62 <VDD< 3.6 V|-|8.5|19|19|
|toh(SWDIO)|SWDIO output hold time|-|8|-|-|-|


**Figure 118. JTAG timing diagram**











DS12110 Rev 10 319/357



320


**Electrical characteristics (rev V)** **STM32H742xI/G STM32H743xI/G**


**Figure 119. SWD timing diagram**






|Col1|Col2|
|---|---|
||th(SWDIO)|
|||


|t|Col2|
|---|---|
|||





320/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**

#### **8 Package information**


In order to meet environmental requirements, ST offers these devices in different grades of
ECOPACK packages, depending on their level of environmental compliance. ECOPACK
specifications, grade definitions and product status _are available at www.st.com._ ECOPACK
is an ST trademark

###### **8.1 Device marking**


Refer to technical note “Reference device marking schematics for STM32 microcontrollers
and microprocessors” (TN1433) available on _[www.st.com](http://www.st.com)_, for the location of pin 1 / ball A1
as well as the location and orientation of the marking areas versus pin 1 / ball A1.


Parts marked as “ES”, “E” or accompanied by an engineering sample notification letter, are
not yet qualified and therefore not approved for use in production. ST is not responsible for
any consequences resulting from such use. In no event will ST be liable for the customer
using any of these engineering samples in production. ST’s Quality department must be
contacted prior to any decision to use these engineering samples to run a qualification
activity.


A WLCSP simplified marking example (if any) is provided in the corresponding package
information subsection.

###### **8.2 LQFP100 package information (1L)**


This LQFP is 100 lead, 14 x 14 mm low-profile quad flat package.


_Note:_ _See list of notes in the notes section._


DS12110 Rev 10 321/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


**Figure 120. LQFP100 - Outline** **[(15)]**









































































**Table 218. LQFP100 - Mechanical data**

|Symbol|millimeters|Col3|inches(14)|Col5|Col6|
|---|---|---|---|---|---|
|**Symbol**|**Min**<br>**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A|-<br>1.50|1.60|-|0.0590|0.0630|
|A1(12)|0.05<br>-|0.15|0.0019|-|0.0059|
|A2|1.35<br>1.40|1.45|0.0531|0.0551|0.0570|



322/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Table 218. LQFP100 - Mechanical data (continued)**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0090|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|16.00 BSC|16.00 BSC|16.00 BSC|0.6299 BSC|0.6299 BSC|0.6299 BSC|
|D1(2)(5)|14.00 BSC|14.00 BSC|14.00 BSC|0.5512 BSC|0.5512 BSC|0.5512 BSC|
|E(4)|16.00 BSC|16.00 BSC|16.00 BSC|0.6299 BSC|0.6299 BSC|0.6299 BSC|
|E1(2)(5)|14.00 BSC|14.00 BSC|14.00 BSC|0.5512 BSC|0.5512 BSC|0.5512 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.0197 BSC|0.0197 BSC|0.0197 BSC|
|L|0.45|0.60|0.75|0.177|0.0236|0.0295|
|L1(1)(11)|1.00|1.00|1.00|-|0.0394|-|
|N(13)|100|100|100|100|100|100|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa(1)|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|bbb(1)|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ccc(1)|0.08|0.08|0.08|0.0031|0.0031|0.0031|
|ddd(1)|0.08|0.08|0.08|0.0031|0.0031|0.0031|



DS12110 Rev 10 323/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


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


**Figure 121. LQFP100 - Footprint example**











1. Dimensions are expressed in millimeters.


324/357 DS12110 Rev 10








**STM32H742xI/G STM32H743xI/G** **Package information**

###### **8.3 TFBGA100 package information (A08Q)**


This TFBGA is 100 - ball, 8X8 mm, 0.8 mm pitch fine pitch ball grid array package.


_Note:_ _See list of notes in the notes section._






|ØeeeM|C|A|B|
|---|---|---|---|
|fff<br>Ø<br>M|C|C|C|




































|Col1|(DATUM A)|D|Col4|Col5|
|---|---|---|---|---|
||(DATUM B)|(DATUM B)|(DATUM B)|(DATUM B)|
||(DATUM B)|(DATUM B)|aaa|C|



|Col1|Figure 122. TFBGA100 - Outline(13)|
|---|---|
|||
||A08Q_UFBGA100_ME_V2<br>e<br>D<br>A<br>Øb (N balls)<br>E<br>SIDE VIEW<br>BOTTOM VIEW<br>1<br>A<br>A<br>B<br>ddd<br>C<br>D1<br>E1<br>eee<br>C A B<br>fff<br>Ø<br>Ø<br>M<br>M C<br>A1 ball pad<br>corner<br>A1 ball pad<br>corner<br>SD<br>e<br>B<br>C<br>D<br>E<br>G<br>H<br>J<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>A2<br>C<br>(4x)<br>8<br>Seating<br>plane<br>A1<br>aaa C<br>ccc<br>C<br>(DATUM A)<br>(DATUM B)<br>7<br>F<br>SE<br>10<br>K<br>TOP VIEW|


DS12110 Rev 10 325/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


**Table 219. TFBGA100 - Mechanical data**

|Symbol|millimeters(1)|Col3|Col4|inches(12)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A(2)(3)|-|-|1.20|-|-|0.0472|
|A1(4)|0.15|-|-|0.0059|-|-|
|A2|-|0.74|-|-|0.0291|-|
|b(5)|0.35|0.40|0.45|0.0138|0.0157|0.0177|
|D|8.00 BSC(6)|8.00 BSC(6)|8.00 BSC(6)|0.3150 BSC|0.3150 BSC|0.3150 BSC|
|D1|7.20 BSC|7.20 BSC|7.20 BSC|0.2835 BSC|0.2835 BSC|0.2835 BSC|
|E|8.00 BSC|8.00 BSC|8.00 BSC|0.3150 BSC|0.3150 BSC|0.3150 BSC|
|E1|7.20 BSC|7.20 BSC|7.20 BSC|0.2835 BSC|0.2835 BSC|0.2835 BSC|
|e(9)|0.80 BSC|0.80 BSC|0.80 BSC|0.0315 BSC|0.0315 BSC|0.0315 BSC|
|N(11)|100|100|100|100|100|100|
|SD(12)|0.40 BSC|0.40 BSC|0.40 BSC|0.0157|0.0157|0.0157|
|SE(12)|0.40 BSC|0.40 BSC|0.40 BSC|0.0157|0.0157|0.0157|
|aaa|0.15|0.15|0.15|0.0059|0.0059|0.0059|
|ccc|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ddd|0.10|0.10|0.10|0.0039|0.0039|0.0039|
|eee|0.15|0.15|0.15|0.0059|0.0059|0.0059|
|fff|0.08|0.08|0.08|0.0031|0.0031|0.0031|



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


326/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


integral heat slug. A distinguish feature is allowable on the bottom surface of the
package to identify the terminal A1 corner. Exact shape of each corner is optional.


9. e represents the solder ball grid pitch.


10. N represents the total number of balls on the BGA.


11. Basic dimensions SD and SE are defined with respect to datums A and B. It defines the
position of the centre ball(s) in the outer row or column of a fully populated matrix.


12. Values in inches are converted from mm and rounded to 4 decimal digits.


13. Drawing is not to scale.


**Figure 123. TFBGA100 - Footprint example**


**Table 220. TFBGA100 - Example of PCB design rules (0.8 mm pitch BGA)**

|Dimension|Values|
|---|---|
|Pitch|0.8|
|Dpad|0.400 mm|
|Dsm|0.470 mm typ. (depends on the soldermask<br>registration tolerance)|
|Stencil opening|0.400 mm|
|Stencil thickness|Between 0.100 mm and 0.125 mm|
|Pad trace width|0.120 mm|



DS12110 Rev 10 327/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**

###### **8.4 LQFP144 package information**


This LQFP is a 144-pin, 20 x 20 mm low-profile quad flat package.


_Note:_ _See list of notes in the notes section._


**Figure 124. LQFP144 - Outline** **[(15)]**


























|Col1|aaa|C|A-B|D|
|---|---|---|---|---|
||||||


|Col1|bb|bH A-B D|
|---|---|---|
||||


|A|Col2|Col3|Col4|
|---|---|---|---|
|A||||







































|Col1|Col2|
|---|---|
|||
|||
|A<br>(Section A-A)|A<br>(Section A-A)|


328/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Package information**


**Table 221. LQFP144 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A|-|-|1.60|-|-|0.0630|
|A1(12)|0.05|-|0.15|0.0020|-|0.0059|
|A2|1.35|1.40|1.45|0.0531|0.0551|0.0571|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0090|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|22.00 BSC|22.00 BSC|22.00 BSC|0.8661 BSC|0.8661 BSC|0.8661 BSC|
|D1(2)(5)|20.00 BSC|20.00 BSC|20.00 BSC|0.7874 BSC|0.7874 BSC|0.7874 BSC|
|E(4)|22.00 BSC|22.00 BSC|22.00 BSC|0.8661 BSC|0.8661 BSC|0.8661 BSC|
|E1(2)(5)|20.00 BSC|20.00 BSC|20.00 BSC|0.7874 BSC|0.7874 BSC|0.7874 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.0197 BSC|0.0197 BSC|0.0197 BSC|
|L|0.45|0.60|0.75|0.0177|0.0236|0.0295|
|L1|1.00 REF|1.00 REF|1.00 REF|0.0394 REF|0.0394 REF|0.0394 REF|
|N(13)|144|144|144|144|144|144|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|bbb|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ccc|0.08|0.08|0.08|0.0031|0.0031|0.0031|
|ddd|0.08|0.08|0.08|0.0031|0.0031|0.0031|



DS12110 Rev 10 329/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


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


330/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Figure 125. LQFP144 - Footprint example**












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||





1. Dimensions are expressed in millimeters.

###### **8.5 UFBGA169 package information**





This UFBGA is a 169-ball, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array package.


DS12110 Rev 10 331/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


**Figure 126. UFBGA169 - Outline**












|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||






















|Col1|ØeeeM|Z|X|Y|
|---|---|---|---|---|
||fff<br>Ø<br>M|Z|Z|Z|



1. Drawing is not to scale.


**Table 222. UFBGA169 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min.**|**Typ.**|**Max.**|**Min.**|**Typ.**|**Max.**|
|A|0.460|0.530|0.600|0.0181|0.0209|0.0236|
|A1|0.050|0.080|0.110|0.0020|0.0031|0.0043|
|A2|0.400|0.450|0.500|0.0157|0.0177|0.0197|
|A3|-|0.130|-|-|0.0051|-|
|A4|0.270|0.320|0.370|0.0106|0.0126|0.0146|
|b|0.230|0.280|0.330|0.0091|0.0110|0.0130|
|D|6.950|7.000|7.050|0.2736|0.2756|0.2776|
|D1|5.950|6.000|6.050|0.2343|0.2362|0.2382|
|E|6.950|7.000|7.050|0.2736|0.2756|0.2776|
|E1|5.950|6.000|6.050|0.2343|0.2362|0.2382|
|e|-|0.500|-|-|0.0197|-|
|F|0.450|0.500|0.550|0.0177|0.0197|0.0217|
|ddd|-|-|0.100|-|-|0.0039|



332/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Table 222. UFBGA169 - Mechanical data (continued)**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min.**|**Typ.**|**Max.**|**Min.**|**Typ.**|**Max.**|
|eee|-|-|0.150|-|-|0.0059|
|fff|-|-|0.050|-|-|0.0020|



1. Values in inches are converted from mm and rounded to 4 decimal digits.


**Figure 127. UFBGA169 - Footprint example**


**Table 223. UFBGA169 - Example of PCB design rules (0.5 mm pitch BGA)**

|Dimension|Values|
|---|---|
|Pitch|0.5 mm|
|Dpad|0.27 mm|
|Dsm|0.35 mm typ. (depends on the soldermask<br>registration tolerance)|
|Solder paste|0.27 mm aperture diameter.|



_Note:_ _Non-solder mask defined (NSMD) pads are recommended._


_Note:_ _4 to 6 mils solder paste screen printing process._


DS12110 Rev 10 333/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**

###### **8.6 LQFP176 package information**


This LQFP is a 176-pin, 24 x 24 mm, 0.5 mm pitch, low profile quad flat package.


_Note:_ _See list of notes in the notes section._


**Figure 128. LQFP176 - Outline** **[(15)]**





































































334/357 DS12110 Rev 10






**STM32H742xI/G STM32H743xI/G** **Package information**


**Table 224. LQFP176 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A<br>|-|-|1.600|-|-|0.0630|
|A1~~(12)~~|0.050|-|0.150|0.0020|-|0.0059|
|A2<br>|1.350|1.400|1.450|0.0531|0.0551|0.0571|
|b~~(9)(11)~~<br>|0.170|0.220|0.270|0.0067|0.0087|0.0106|
|b1~~(11)~~<br>|0.170|0.200|0.230|0.0067|0.0079|0.0091|
|c~~(11)~~<br>|0.090|-|0.200|0.0035|-|0.0079|
|c1~~(11)~~<br>|0.090|-|0.160|0.0035|-|0.063|
|D~~(4)~~<br>|26.000|26.000|26.000|1.0236|1.0236|1.0236|
|D1~~(2)(5)~~<br>|24.000|24.000|24.000|0.9449|0.9449|0.9449|
|E~~(4)~~<br>|26.000|26.000|26.000|0.0197|0.0197|0.0197|
|E1~~(2)(5)~~|24.000|24.000|24.000|0.9449|0.9449|0.9449|
|e|0.500|0.500|0.500|0.1970|0.1970|0.1970|
|L<br>|0.450|0.600|0.750|0.0177|0.0236|0.0295|
|L1~~(1)(11)~~<br>|1|1|1|0.0394 REF|0.0394 REF|0.0394 REF|
|N~~(13)~~|176|176|176|176|176|176|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.080|-|-|0.0031|-|-|
|R2|0.080|-|0.200|0.0031|-|0.0079|
|S<br>|0.200|-|-|0.0079|-|-|
|aaa~~(1)~~<br>|0.200|0.200|0.200|0.0079|0.0079|0.0079|
|bbb~~(1)~~<br>|0.200|0.200|0.200|0.0079|0.0079|0.0079|
|ccc~~(1)~~<br>|0.080|0.080|0.080|0.0031|0.0031|0.0031|
|ddd~~(1)~~|0.080|0.080|0.080|0.0031|0.0031|0.0031|



DS12110 Rev 10 335/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


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


336/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Figure 129. LQFP176 - Footprint example**










|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|1 176|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|133<br>132<br>0.3<br>0.5|
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
||44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|44<br>45|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88|89<br>88||
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


DS12110 Rev 10 337/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**

###### **8.7 LQFP208 package information**


This LQFP is a 208-pin, 28 x 28 mm low-profile quad flat package.


_Note:_ _See list of notes in the notes section._


**Figure 130. LQFP208 - Outline** **[(15)]**









































































338/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Table 225. LQFP208 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(15)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A|-|-|1.60|-|-|0.0630|
|A1(12)|0.05|-|0.15|0.0020|-|0.0059|
|A2|1.35|1.40|1.45|0.0531|0.0551|0.0571|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0091|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|30.00 BSC|30.00 BSC|30.00 BSC|1.1732 BSC|1.1732 BSC|1.1732 BSC|
|D1(2)(5)|28.00 BSC|28.00 BSC|28.00 BSC|1.0945 BSC|1.0945 BSC|1.0945 BSC|
|E(4)|30.00 BSC|30.00 BSC|30.00 BSC|1.1732 BSC|1.1732 BSC|1.1732 BSC|
|E1(2)(5)|28.00 BSC|28.00 BSC|28.00 BSC|1.0945 BSC|1.0945 BSC|1.0945 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.0197 BSC|0.0197 BSC|0.0197 BSC|
|L|0.45|0.60|0.75|0.0177|0.0236|0.0295|
|L1|1.00 REF|1.00 REF|1.00 REF|0.0394 REF|0.0394 REF|0.0394 REF|
|N(13)|208|208|208|208|208|208|
|θ|0°|3.5°|7°|0°|3.5°|7°|
|θ1|0°|-|-|0°|-|-|
|θ2|10°|12°|14°|10°|12°|14°|
|θ3|10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa(1)(7)|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|bbb(1)(7)|0.20|0.20|0.20|0.0079|0.0079|0.0079|
|ccc(1)(7)|0.08|0.08|0.08|0.0031|0.0031|0.0031|
|ddd(1)(7)|0.08|0.08|0.08|0.0031|0.0031|0.0031|



DS12110 Rev 10 339/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


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


**Figure 131. LQFP208 - footprint example**













1. Dimensions are expressed in millimeters.


340/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**

###### **8.8 UFBGA(176+25) package information**


This UFBGA is a 176+25-ball, 10 x 10 mm, 0.65 mm pitch, ultra fine pitch ball grid array
package


**Figure 132. UFBGA(176+25) - Outline**








|Col1|Col2|Col3|Col4|Col5|Col6|Col7|ddd|C|
|---|---|---|---|---|---|---|---|---|
||||||||||




















|Col1|Col2|Col3|
|---|---|---|
||||














|Col1|ØeeeM|C|A|B|
|---|---|---|---|---|
||fff<br>Ø<br>M|C|C|C|





1. Drawing is not to scale.

|Col1|Table 226. UFBGA(176+25) -|Col3|Col4|Mechanical data|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**millimeters**|**millimeters**|**millimeters**|**inches(1)**|**inches(1)**|**inches(1)**|
|**Symbol**|**Min.**|**Typ.**|**Max.**|**Min.**|**Typ.**|**Max.**|
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



DS12110 Rev 10 341/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


**Table 226. UFBGA(176+25) - Mechanical data (continued)**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min.**|**Typ.**|**Max.**|**Min.**|**Typ.**|**Max.**|
|eee|-|-|0.150|-|-|0.0059|
|fff|-|-|0.050|-|-|0.0020|



1. Values in inches are converted from mm and rounded to 4 decimal digits.


**Figure 133. UFBGA(176+25) - Footprint example**


**Table 227. UFBGA(176+25) - Example of PCB design rules (0.65 mm pitch BGA)**

|Dimension|Values|
|---|---|
|Pitch|0.65 mm|
|Dpad|0.300 mm|
|Dsm|0.400 mm typ. (depends on the soldermask<br>registration tolerance)|
|Stencil opening|0.300 mm|
|Stencil thickness|Between 0.100 mm and 0.125 mm|
|Pad trace width|0.100 mm|



342/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**

###### **8.9 TFBGA240+25 package information**


This TFBGA is a 240+25-ball, 14x14 mm, 0.8 mm pitch, fine pitch ball grid array package.


**Figure 134. TFBGA240+25 - Outline**

















1. Dimensions are expressed in millimeters.


DS12110 Rev 10 343/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


**Table 228. TFBGA240+25 - Mechanical data**


















|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
|**Symbol**|**Min**|**Typ**|**Max**|**Min**|**Typ**|**Max**|
|A(2)|-|-|1.200|-|-|0.0472|
|A1(3)|0.150|-|-|0.0059|-|-|
|A2|-|0.760|-|-|0.0299|-|
|b(4)|0.320|-|0.450|0.0126|-|0.0177|
|D|13.850|14.000|14.150|0.5453|0.5512|0.5571|
|D1|-|12.800|-|-|0.5039|-|
|E|13.850|14.000|14.150|0.5453|0.5512|0.5571|
|E1|-|12.800|-|-|0.5039|-|
|e|-|0.800|-|-|0.0315|-|
|F|-|0.600|-|-|0.0236|-|
|G|-|0.600|-|-|0.0236|-|
|ddd|-|-|0.100|-|-|0.0039|
|eee(5)|-|-|0.150|-|-|0.0059|
|fff(6)|-|-|0.080|-|-|0.0031|



1. Values in inches are converted from mm and rounded to 4 decimal digits.


2. The total profile height (Dim A) is measured from the seating plane to the top of the component.


3.         - The terminal A1 corner must be identified on the top surface by using a corner chamfer,
ink or metalized markings, or other feature of package body or integral heat slug.

           - A distinguishing feature is allowable on the bottom surface of the package to identify the terminal A1
corner. Exact shape of each corner is optional.


4. Initial ball equal 0.350mm


5. The tolerance of position that controls the location of the pattern of balls with respect to datums A and B.
For each ball there is a cylindrical tolerance zone eee perpendicular to datum C and located on true
position with respect to datums A and B as defined by e. The axis perpendicular to datum C of each ball
must lie within this tolerance zone.


6. The tolerance of position that controls the location of the balls within the matrix with respect to each other.
For each ball there is a cylindrical tolerance zone fff perpendicular to datum C and located on true position
as defined by e. The axis perpendicular to datum C of each ball must lie within this tolerance zone. Each
tolerance zone fff in the array is contained entirely in the respective zone eee above The axis of each ball
must lie simultaneously in both tolerance zones.


344/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Figure 135. TFBGA240+25 - Footprint example**


**Table 229. TFBGA240+25 - Example of PCB design rules**

|Dimension|Values|
|---|---|
|Pitch|0.8 mm|
|Dpad|0.300 mm|
|Dsm|0.400 mm typ. (depends on the soldermask<br>registration tolerance)|
|Stencil opening|0.400 mm|
|Stencil thickness|0.100 mm|


###### **8.10 Thermal characteristics**


The maximum chip-junction temperature, T J max, in degrees Celsius, may be calculated
using the following equation:


T J max = T A max + (P D max × Θ JA )


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


DS12110 Rev 10 345/357



348


**Package information** **STM32H742xI/G STM32H743xI/G**


**Table 230. Thermal characteristics**








|Symbol|Definition|Parameter|Value|Unit|
|---|---|---|---|---|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>LQFP100 - 14 x 14 mm /0.5 mm pitch|45.0|°C/W|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>TFBGA100 - 8 x 8 mm /0.8 mm pitch|39.3|39.3|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>LQFP144 - 20 x 20 mm /0.5 mm pitch|43.7|43.7|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>UFBGA169 - 7 x 7 mm /0.5 mm pitch|37.7|37.7|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>LQFP176 - 24 x 24 mm /0.5 mm pitch|43.0|43.0|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>LQFP208 - 28 x 28 mm /0.5 mm pitch|42.4|42.4|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>UFBGA176+25 - 10 x 10 mm /0.65 mm pitch|37.4|37.4|
|ΘJA|Thermal resistance<br>junction-ambient|**Thermal resistance junction-ambient**<br>TFBGA240+25 - 14 x 14 mm / 0.8 mm pitch|36.6|36.6|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>LQFP100 - 14 x 14 mm /0.5 mm pitch|36.3|°C/W|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>TFBGA100 - 8 x 8 mm /0.8 mm pitch|21.1|21.1|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>LQFP144 - 20 x 20 mm /0.5 mm pitch|38.3|38.3|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>UFBGA169 - 7 x 7 mm /0.5 mm pitch|17.3|17.3|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>LQFP176 - 24 x 24 mm /0.5 mm pitch|39.4|39.4|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>LQFP208 - 28 x 28 mm /0.5 mm pitch|40.3|40.3|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>UFBGA176+25 - 10 x 10 mm /0.65 mm pitch|19.3|19.3|
|ΘJB|Thermal resistance<br>junction-board|**Thermal resistance junction-ambient**<br>TFBGA240+25 - 14 x 14 mm / 0.8 mm pitch|24.3|24.3|



346/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Package information**


**Table 230. Thermal characteristics (continued)**



|Symbol|Definition|Parameter|Value|Unit|
|---|---|---|---|---|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>LQFP100 - 14 x 14 mm /0.5 mm pitch|11.5|°C/W|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>TFBGA100 - 8 x 8 mm /0.8 mm pitch|17.1|17.1|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>LQFP144 - 20 x 20 mm /0.5 mm pitch|11.3|11.3|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>UFBGA169 - 7 x 7 mm /0.5 mm pitch|11|11|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>LQFP176 - 24 x 24 mm /0.5 mm pitch|11.2|11.2|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>LQFP208 - 28 x 28 mm /0.5 mm pitch|11.1|11.1|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>UFBGA176+25 - 10 x 10 mm /0.65 mm pitch|23.9|23.9|
|ΘJC|Thermal resistance<br>junction-case|**Thermal resistance junction-ambient**<br>TFBGA240+25 - 14 x 14 mm / 0.8 mm pitch|7.4|7.4|


**8.10.1** **Reference documents**








- JESD51-2 Integrated Circuits Thermal Test Method Environment Conditions - Natural
Convection (Still Air). Available from www.jedec.org.


- For information on thermal management, refer to application note “Thermal
management guidelines for STM32 32-bit Arm Cortex MCUs applications” (AN5036)
available from _www.st.com_ .


DS12110 Rev 10 347/357



348


**Ordering information** **STM32H742xI/G STM32H743xI/G**

#### **9 Ordering information**


Example: STM32 H 743 X I T 6 TR [(1)]


TR = tape and reel


No character = tray or tube


1. The tape and reel packing is not available on all packages.


For a list of available options (speed, package, etc.) or for further information on any aspect
of this device, please contact your nearest ST sales office.


348/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Important security notice**

#### **10 Important security notice**


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


DS12110 Rev 10 349/357



349


**Revision history** **STM32H742xI/G STM32H743xI/G**

#### **11 Revision history**


**Table 231. Document revision history**






|Date|Revision|Changes|
|---|---|---|
|22-Jun-2017|1|Initial release.|
|27-Sep-2017|2|Updated list of features. Changed datasheet status to “production data”.<br>Added UFBGA169 and TFBGA100 packages and well as notes related their status on<br>cover page and in_Table 2: STM32H742xI/G and STM32H743xI/G features and_<br>_peripheral counts_. Differentiated number of GPIOs for each package in_Table 2:_<br>_STM32H742xI/G and STM32H743xI/G features and peripheral counts_.<br>Updated_Error code correction (ECC)_ in_Section 3.3.2: Embedded SRAM_. Change<br>PWR_CR3 into PWR_D3CR in_Section 3.5.1: Power supply scheme_. Updated<br>_Section 3.12: Nested vectored interrupt controller (NVIC)_.<br>Added ADC sampling rate values in_Section 3.17: Analog-to-digital converters (ADCs)_.<br>Added_Table 4: DFSDM implementation_ in_Section 3.23: Digital filter for sigma-delta_<br>_modulators (DFSDM)_<br>Changed PC2/3 to PC2/3_C and VDD33USB to VDD in_Figure 5: LQFP100 pinout_. <br>Changed PC2/3 to PC2/3_C in_Figure 7: LQFP144 pinout_. Changed PC2/3 to PC2/3_C<br>in_Figure 9: LQFP176 pinout_. Changed PC2/3 to PC2/3_C in_Figure 11: LQFP208_<br>_pinout_. <br>_Table 9: Pin/ball definition_:<br>– Modified PA7, PC4, PC5, PB1, PG1, PE7, PE8 and PE9 I/O structure<br>– TFBGA240 +25: removed duplicate occurrence of F1, F2 and P17 pin; added notes<br>related to F1, F2, G2 pin connection; added note on E1, L16, L17, M16, M17, K16,<br>K17, N17.<br>– UFBGA176+25: changed G10 pin name to VSS.<br>– Added note to VREF+ pin.<br>Added current consumption corresponding to 125 °C ambient temperature in<br>_Section 6.3.6: Supply current characteristics_. Removed CRYP peripheral from_Table 39:_<br>_Peripheral current consumption in Run mode_. <br>Replaced FMC_CLK by FMC_SDCLK in_Section : SDRAM waveforms and timings_.<br>Changed description of the last five fS values and updated tLATRINJin_Table 87: ADC_<br>_characteristics_.<br>For TFBGA100, TFBGA240+25 and UFBGA169, updated thermal resistance power-<br>junction in_Table 230: Thermal characteristics_ as well as power dissipation in_Table 24:_<br>_General operating conditions_.|
|23-Oct-2017|3|_Features_:<br>– Removed secure firmware upgrade support.<br>– Total current consumption changed to 4µA minimum.<br>Updated_Figure 8: UFBGA169 ballout_.<br>Updated dpad and dsm in_Table 136: TFBGA240+25 - Recommended PCB design_<br>_rules_.|



350/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Revision history**


**Table 231. Document revision history**





|Date|Revision|Changes|
|---|---|---|
|18-May-2018|4|Updated LSI clock frequency and ADC on cover page. Removed note related to<br>UFBGA169 package.<br>Updated USB OTG interfaces to add crystal-less capability.<br>Updated ADC features on cover page and in_Table 2: STM32H742xI/G and_<br>_STM32H743xI/G features and peripheral counts_.<br>Added Arm trademark notice in_Section 1: Introduction_.<br>Updated_Figure 1: STM32H743xI/G block diagram_.<br>Updated GPIO default mode in_Section 3.8: General-purpose input/outputs (GPIOs)_.<br>Added ADC sampling rate values in_Section 3.17: Analog-to-digital converters (ADCs)_.<br>Updated_Section 3.18: Temperature sensor_.<br>Updated LCD-TFT FIFO Size in_Section 3.25: LCD-TFT controller_.<br>_Section 3.33: Serial peripheral interfaces (SPI)/integrated interchip sound interfaces_<br>_(I2S)_: changed maximum SPI frequency to 150 Mbits/s.<br>Modified number of bidirectional endpoints in_Section 3.40: Universal serial bus on-the-_<br>_go high-speed (OTG_HS)_.<br>_Table 9: Pin/ball definition_: updated PC14 and PC15 function after reset; changed<br>CAN1_TX/RX to FDCAN1_TX/RX and CAN1_TXFD/RXFD to<br>FDCAN1_TXFD_MODE/RXFD_MODE; changed CAN2_TX/RX to FDCAN2_TX/RX<br>and CAN2_TXFD/RXFD to FDCAN2_TXFD_MODE/RXFD_MODE and replaced<br>VCAP1/2/3 and VDDLDO1/2/3 by VCAP and VDDLDO, respectively.<br>Updated PA0, PA13, PA14, PC14 and PC15 pin/ball signals in pinout/ballout<br>schematics.<br>Replaced fACLK by frcc_c_ck in_Section : Typical and maximum current consumption_. <br>Replaced system clock by CPU clock and fACLK by frcc_c_ckin_Section : On-chip_<br>_peripheral current consumption_.<br>Updated Note_2._ in_Table 27: Reset and power control block characteristics_, _Table 28:_<br>_Embedded reference voltage_, _Table 30: Typical and maximum current consumption in_<br>_Run mode, code with data processing running from ITCM, regulator ON_, _Table 31:_<br>_Typical and maximum current consumption in Run mode, code with data processing_<br>_running from flash memory, cache ON, regulator ON_, _Table 36: Typical and maximum_<br>_current consumption in Stop mode, regulator ON_, _Table 37: Typical and maximum_<br>_current consumption in Standby mode_ and_Table 38: Typical and maximum current_<br>_consumption in VBAT mode_.<br>Added note to fLSI in_Table 49: LSI oscillator characteristics_.<br>Updated_Figure 22: VIL/VIH for all I/Os except BOOT0_.<br>Added note in_Table 84: QUADSPI characteristics in SDR mode_, _Table 85: QUADSPI_<br>_characteristics in DDR mode_ and_Table 86: Dynamics characteristics: Delay Block_<br>_characteristics_.<br>_Section 6.3.20: 16-bit ADC characteristics_: updated THD conditions in_Table 88: ADC_<br>_accuracy_; removed formula to compute RAIN.<br>Changed decoupling capacitor value to 100 nF in_Section : General PCB design_<br>_guidelines_.<br>Added note in_Table 89: DAC characteristics_, _Table 97: Voltage booster for analog_<br>_switch characteristics_, _Table 100: DFSDM measured timing - 1.62-3.6 V_, _Table 117:_<br>_Dynamics JTAG characteristics_ and_Table 118: Dynamics SWD characteristics_.<br>Updated_Figure 128: LQFP144 marking example (package top view)_, _Figure 134:_<br>_LQFP176 marking example (package top view)_ and_Figure 137: LQFP208 marking_<br>_example (package top view)_. <br>Updated TFBGA240+25 package information to final mechanical data.|


DS12110 Rev 10 351/357



356


**Revision history** **STM32H742xI/G STM32H743xI/G**


**Table 231. Document revision history**






|Date|Revision|Changes|
|---|---|---|
|13-Jul-2018|5|Added description of power-up and power-down phases in_Section 3.5.1: Power supply_<br>_scheme_.<br>Removed ETH_TX_ER from_Table 9: Pin/ball definition_ and_Table 10: Port A alternate_<br>_functions_ to_Table 20: Port K alternate functions_.<br>Added note related to decoupling capacitor tolerance below_Figure 15: Power supply_<br>_scheme_. Added note_2._ related to CEXT in_Table 25: VCAP operating conditions_. <br>Updated_Table 46: HSI48 oscillator characteristics_, _Table 47: HSI oscillator_<br>_characteristics_ and_Table 48: CSI oscillator characteristics_. Renamed_Table 50_ into “PLL<br>characteristics (wide VCO frequency range)” and updated note_2._. Added_Table 51: PLL_<br>_characteristics (medium VCO frequency range)_.<br>Updated Tcoeffin_Table 91: VREFBUF characteristics_ and tS_vbat in_Table 94: VBAT _<br>_monitoring characteristics_. Updated_Table 99: OPAMP characteristics_.|
|05-Apr-2019|6|Added STM32H743xG part numbers corresponding to 1 Mbyte of flash memory as well<br>as STM32H742xI/G part numbers.<br>Changed maximum Arm Core-M7 frequency to 480 MHz.<br>_Features_: <br>– Changed operational amplifier bandwidth to 7.3 MHz<br>– Updated high-resolution timer to 2.1 ns<br>– Updated low-power consumption feature.<br>– Updated_Figure 2: STM32H743xI/G block diagram_.<br>Updated voltage scaling in_Section 3.5.1: Power supply scheme_. Added VOS0 in<br>_Section 3.5.3: Voltage regulator_. Updated HSE clock in_Section 3.7.1: Clock_<br>_management_.<br>Changed FMC NOR/NAND maximum clock frequency to 100 MHz in_Features_ and<br>_Synchronous waveforms and timings_.<br>Added note related to VDDLDO in_Table 9: Pin/ball definition_.<br>Updated_Section 6: Electrical characteristics (rev Y)_:<br>– Added note_2._ related to CEXT in_Table 25: VCAP operating conditions_.<br>– Updated fHSI48 in_Table 46: HSI48 oscillator characteristics_.<br>– Updated tstab in_Table 47: HSI oscillator characteristics_.<br>– Updated_Table 60: I/O static characteristics_ and_Figure 22: VIL/VIH for all I/Os except_<br>_BOOT0_.<br>– Added_Table 62: Output voltage characteristics for PC13, PC14, PC15 and PI8_.<br>– Added note related to PC13, PC14, PC15 an PI8 limited frequency in_Table 63: Output_<br>_timing characteristics (HSLV OFF)_.<br>– Updated note 2 below_Figure 23: Recommended NRST pin protection_.<br>–_ Table 87: ADC characteristics_: updated fS and added note related to fS formula;<br>updated tCAL.<br>– Renamed_Section 6.3.24_ into_Temperature and VBAT monitoring_ and content<br>updated.<br>– Updated fDFSDMCLKin_Table 100: DFSDM measured timing - 1.62-3.6 V_.<br>Added_Section 7: Electrical characteristics (rev V)_.<br>Updated paragraph introducing all package marking schematics to add the new<br>sentence “The printed markings may differ depending on the supply chain”. Updated<br>_Table 230: Thermal characteristics_. Added note related to ECOPACK®2 compliance in<br>_Section 9: Ordering information_.|



352/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Revision history**


**Table 231. Document revision history**





|Date|Revision|Changes|
|---|---|---|
|24-Apr-2019|7|Updated_Figure 1: STM32H742xI/G block diagram_<br>Updated_Figure 2: STM32H743xI/G block diagram_<br>Updated_Table 9: Pin/ball definition_.<br>Updated_Table 10_ to_Table 20_ (alternate functions).<br>Updated_Table 39: Peripheral current consumption in Run mode_.<br>Updated_Table 137: Peripheral current consumption in Run mode_.<br>Updated_Table 184: ADC characteristics_.<br>Updated_Table 185: Minimum sampling time vs RAIN_.<br>Updated_Table 186: ADC accuracy_.|
|02-Mar-2021|8|Added reference to errata sheet ES0392 in_Section 1: Introduction_.<br>Added connection between SDMMC2 and D2-to-D3 AHB bus in_Figure 4:_<br>_STM32H743xI/G bus matrix_.<br>Updated_Section 3.27: True random number generator (RNG)_.<br>Added Full-duplex mode in_Section 3.33: Serial peripheral interfaces (SPI)/integrated_<br>_interchip sound interfaces (I2S)_.<br>In_Table 2: STM32H742xI/G and STM32H743xI/G features and peripheral counts_, split<br>number of ADC channels into Direct, Fast and Slow channels; and added number of<br>wakeup and tamper pins.<br>Updated J1 and F2 signals in_Figure 12: TFBGA240+25 ballout_<br>**_Section 6: Electrical characteristics (rev Y)_**:<br>– Updated_Section 6.2: Absolute maximum ratings_ introduction to device mission<br>profile.<br>– Added a 1 μF capacitor between VDD33USB and ground in_Figure 15: Power supply_<br>_scheme_. <br>– Power dissipation (PD) removed from_Table 24: General operating conditions_ since<br>this parameter is redundant withΘJAthermal resistance.<br>–_ Table 53: Flash memory programming_: removed reference to single bank<br>configuration in title and added tERASE128KB typical and maximum values.<br>– Added reference to AN4899 in_Section 6.3.15: I/O port characteristics_. Updated notes<br>in_Table 64: Output timing characteristics (HSLV ON)_. <br>– Updated tsu(DV-CLKH)/th(DV-CLKH)and tsu(NWAIT-CLKH)/th(NWAIT-CLKH)in_Table 74:_<br>_Synchronous multiplexed NOR/PSRAM read timings_. Changed t(NWAIT-CLKH)to<br>tsu(NWAIT-CLKH)and updated tsu(DV-CLKH)/th(DV-CLKH)and tsu(NWAIT-CLKH)/th(NWAIT-CLKH)<br>in_Table 76: Synchronous non-multiplexed NOR/PSRAM read timings_. Updated<br>tsu(SDCLKH _Data)and th(SDCLKH _Data)in_Table 80: SDRAM read timings_ and_Table 81:_<br>_LPSDR SDRAM read timings_.<br>– Updated ts(IN) and th(IN) in_Table 84: QUADSPI characteristics in SDR mode_ and<br>tsr(IN)/tsf(IN) and thr(IN)/thf(IN)in_Table 85: QUADSPI characteristics in DDR mode_.<br>– Updated maximum sampling time (tS) value in_Table 87: ADC characteristics_. <br>Specified that_Figure 40: ADC accuracy characteristics_ is an example for 12-bit<br>resolution.<br>– Updated DuCyCKOUT in_Table 100: DFSDM measured timing - 1.62-3.6 V_.<br>– Updated tsu(MI)and th(MI)minimum values in_Table 106: SPI dynamic characteristics_.<br>– Updated tISU,tIH, tISUDand tIHD in_Table 110: Dynamic characteristics: SD / MMC_<br>_characteristics, VDD = 2.7 to 3.6 V_<br>– Updated tISU,tIH in_Table 111: Dynamic characteristics: eMMC characteristics,_<br>_VDD = 1.71 to 1.9 V_.<br>– Updated DuCyCKOUT in_Table 100: DFSDM measured timing - 1.62-3.6 V_.|


DS12110 Rev 10 353/357



356


**Revision history** **STM32H742xI/G STM32H743xI/G**






|Col1|Col2|Table 231. Document revision history|
|---|---|---|
|**Date**|**Revision**|**Changes**|
|13-Apr-2021|8 <br>(continued)|**_Section 7: Electrical characteristics (rev V)_:**<br>– Updated_Section 7.2: Absolute maximum ratings_ introduction to device mission<br>profile.<br>– Added a 1 μF capacitor between VDD33USB and ground in_Figure 68: Power supply_<br>_scheme_. <br>– Power dissipation (PD) removed from_Table 122: General operating conditions_ since<br>this parameter is redundant withΘJAthermal resistance.<br>– Replaced Min VDDby Min VDDLDO in_Table 123: Supply voltage and maximum_<br>_frequency configuration_.<br>–_ Table 150: Flash memory programming_: removed reference to single bank<br>configuration in title and added tERASE128KB typical and maximum values.<br>– Updated condition related tofrcc_c_ckin_Section : On-chip peripheral current_<br>_consumption_.<br>– Added reference to AN4899 in_Section 7.3.15: I/O port characteristics_. Changed<br>capacitance value for speed 10 and tr/tf, and speed for 11 and tr/tf/Fmax _Table 161:_<br>_Output timing characteristics (HSLV ON)_.<br>– Updated tsu(DV-CLKH)/th(DV-CLKH)and tsu(NWAIT-CLKH)/th(NWAIT-CLKH)in_Table 171:_<br>_Synchronous multiplexed NOR/PSRAM read timings_. Changed t(NWAIT-CLKH)to<br>tsu(NWAIT-CLKH)and updated tsu(DV-CLKH)/th(DV-CLKH)and tsu(NWAIT-CLKH)/th(NWAIT-CLKH)<br>in_Table 173: Synchronous non-multiplexed NOR/PSRAM read timings_. Updated<br>tsu(SDCLKH _Data)and th(SDCLKH _Data)in_Table 177: SDRAM read timings_ and<br>_Table 178: LPSDR SDRAM read timings_.<br>– Updated ts(IN) and th(IN) in_Table 181: QUADSPI characteristics in SDR mode_ and<br>tsr(IN)/tsf(IN) and thr(IN)/thf(IN)in_Table 182: QUADSPI characteristics in DDR mode_.<br>– Updated notes_4._ and_5._ in_Table 185: Minimum sampling time vs RAIN_. Added<br>reference to AN5354 application note in note of_Table 184: ADC characteristics_. <br>Specified that_Figure 40: ADC accuracy characteristics_ is an example for 12-bit<br>resolution.<br>– Changed temperature condition to 130 °C for TS_CAL2 in_Table 191: Temperature_<br>_sensor calibration values_.<br>– Updated DuCyCKOUT in_Table 198: DFSDM measured timing - 1.62-3.6 V_.<br>– Updated_Figure 101: USART timing diagram in Master mode_ and_Figure 102: USART_<br>_timing diagram in Slave mode_.<br>– Updated tsu(MI)and th(MI)in_Table 205: SPI dynamic characteristics_.<br>– Updated tISU,tIH, tISUDand tIHD in_Table 209: Dynamics characteristics: SD / MMC_<br>_characteristics, VDD = 2.7 to 3.6 V_<br>Updated tISU,tIH in_Table 210: Dynamics characteristics: eMMC characteristics_<br>_VDD = 1.71V to 1.9V_.<br>Added ΘJB and ΘJC for UFBGA169.<br>Updated_Figure 124: TFBGA100 - Recommended footprint_<br>Added_Figure 151: UFBGA169 - Recommended footprint_ and_Table 304: UFBGA169 -_<br>_Recommended PCB design rules (0.5 mm pitch BGA)_. <br>Updated_Section 8.8: UFBGA(176+25) package information_.<br>Added note related to the availability of tape and reel packing in_Section 9: Ordering_<br>_information_.|



354/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G** **Revision history**





|Col1|Col2|Table 231. Document revision history|
|---|---|---|
|**Date**|**Revision**|**Changes**|
|4-Mar-2022|9|**_Section 2: Description_**<br>Removed note indicating that packages are under development from_Table 2:_<br>_STM32H742xI/G and STM32H743xI/G features and peripheral counts_.<br>**_Section 3: Functional overview_**<br>Updated number of microphones that can be supported by the SAI in_Section 3.34:_<br>_Serial audio interfaces (SAI)_.<br>**_Section 5: Pin descriptions_**<br>Updated F1, F2 and G2 signals, and added notes 2, 3 and 4 in_Figure 12:_<br>_TFBGA240+25 ballout_.<br>Removed FDCAN1_RXFD_MODE, FDCAN1_TXFD_MODE, FDCAN2_RXFD_MODE<br>and FDCAN2_TXFD_MODE functions from_Table 9: Pin/ball definition_ and all alternate<br>function tables.<br>Additional modifications made on_Table 9: Pin/ball definition_: added note to VDD50USB,<br>added note to PB12 and PB13, changed PB1 I/O structure to TT_a, replaced PI8<br>WKUP3 additional function by WKUP2 and PC13 WKUP2 additional function by<br>WKUP3, and changed F1 and G2 to VSS.<br>**_Section 6: Electrical characteristics (rev Y)_**<br>– Updated_Figure 15: Power supply scheme_.<br>– Updated_Table 42: High-speed external user clock characteristics_.<br>– Added tERASE128KB typical and maximum values in_Table 52: Flash memory_<br>_characteristics_.<br>– Updated Fmax for speed 10 and 11 in_Table 63: Output timing characteristics (HSLV_<br>_OFF)_.<br>– Replaced FMC_CLK by FMC_SDCLK in_Section : SDRAM waveforms and timings_.<br>– Updated_Figure 40: ADC accuracy characteristics_ and_Figure 41: Typical connection_<br>_diagram when using the ADC with FT/TT pins featuring analog switch function_.<br>– Updated TL maximum value in_Table 92: Temperature sensor characteristics_.<br>– .Changed fTIMxCLK maximum frequency to 240 MHz in_Table 103: TIMx_<br>_characteristics_.<br>**_Section 7: Electrical characteristics (rev V)_**<br>– Updated_Figure 68: Power supply scheme_.<br>– Updated_Table 139: High-speed external user clock characteristics_.<br>– Added tERASE128KB typical and maximum values in_Table 149: Flash memory_<br>_characteristics_.<br>– Updated Fmax for speed 10 and 11 in_Table 160: Output timing characteristics (HSLV_<br>_OFF)_.<br>– Replaced FMC_CLK by FMC_SDCLK in_Section : SDRAM waveforms and timings_.<br>– Updated_Figure 92: ADC accuracy characteristics_ and_Figure 93: Typical connection_<br>_diagram when using the ADC with FT/TT pins featuring analog switch function_.<br>– Updated tERASE128KB in_Table 150: Flash memory programming_.<br>– Updated TL maximum value in_Table 190: Temperature sensor characteristics_.<br>– Changed VDAC_OUTmaximum value to VREF+ −0.2 in_Table 188: DAC accuracy_.<br>– Updated tOHin_Table 209: Dynamics characteristics: SD / MMC characteristics,_<br>_VDD = 2.7 to 3.6 V_<br>– Added_Section : USB OTG_FS characteristics_.|


DS12110 Rev 10 355/357



356


**Revision history** **STM32H742xI/G STM32H743xI/G**






|Col1|Col2|Table 231. Document revision history|
|---|---|---|
|**Date**|**Revision**|**Changes**|
|4-Mar-2022|9 <br>(continued)|**_Section 8: Package information_**<br>Updated_Section 8.1: LQFP100 package information (1L)_, _Section 8.3: LQFP144_<br>_package information_, _Section 8.6: LQFP176 package information_, _Section 8.8:_<br>_UFBGA(176+25) package information_, _Figure 137: LQFP208 marking example_<br>_(package top view)_and_Table 136: TFBGA240+25 - Recommended PCB design rules_.|
|30-Mar-2023|10|Removed note 1 (“SDRAM is not available on LQFP144 package”) below_Table 2:_<br>_STM32H742xI/G and STM32H743xI/G features and peripheral counts_<br>Changed WKUP[5:0] to WKUP[6:1] in_Figure 1: STM32H742xI/G block diagram_ and in<br>_Table 9: Pin/ball definition_. <br>Modified_Section 3.5.1: Power supply scheme_ <br>Updated_Section 3.24: Digital camera interface (DCMI)_ (modified supported format)<br>Updated_Figure 4: STM32H743xI/G bus matrix_.<br>Changed Ileak to AIlkgin_Table 60: I/O static characteristics_ and_Table 157: I/O static_<br>_characteristics_ <br>Modified_Table 153: EMI characteristics for fHSE = 8 MHz and fCPU = 400 MHz_<br>Updated section_I/O dynamic current consumption_ and I/_O static current consumption in_<br>_Section 6: Electrical characteristics (rev Y) andSection 7: Electrical characteristics (rev_<br>_V)_.<br>Updated_Table 22: Current characteristics_ and_Table 120: Current characteristics_ <br>Updated note below_Figure 41: Typical connection diagram when using the ADC with_<br>_FT/TT pins featuring analog switch function_ and_Figure 93: Typical connection diagram_<br>_when using the ADC with FT/TT pins featuring analog switch function_  <br>Updated VCOREmax value in_Table 122: General operating conditions_<br>Updated_Table 113: Dynamic characteristics: USB ULPI_ <br>Added_Section 8.1: Device marking_(device marking information removed from package<br>sections and moved to this section)<br>Updated_Section 8: Package information_ and_Section 8.8: UFBGA(176+25) package_<br>_information_. <br>Modified title for footprint figure and PCB design rules table (examples instead of<br>recommendations)<br>Updated information on pin count in_Section 9: Ordering information_<br>Added_Section 10: Important security notice_.|



356/357 DS12110 Rev 10


**STM32H742xI/G STM32H743xI/G**


**IMPORTANT NOTICE – PLEASE READ CAREFULLY**


STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on
ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order
acknowledgement.


Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or
the design of Purchasers’ products.


No license, express or implied, to any intellectual property right is granted by ST herein.


Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.


ST and the ST logo are trademarks of ST. For additional information about ST trademarks, please refer to _www.st.com/trademarks_ . All other
product or service names are the property of their respective owners.


Information in this document supersedes and replaces information previously supplied in any prior versions of this document.


© 2023 STMicroelectronics – All rights reserved


DS12110 Rev 10 357/357



357


