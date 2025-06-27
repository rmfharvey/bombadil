# **SPC564Bxx ** **SPC56ECxx**
#### 32-bit MCU family built on the Power Architecture [® ] for automotive body electronics applications
###### Datasheet - production data


LBGA256 LQFP208 LQFP176
(17 x 17 x 1.7 mm) (28 x 28 x 1.4 mm) (24 x 24 x 1.4 mm)
##### **Features**
######  e200z4d, 32-bit Power Architecture [®] – Up to 120 MHz and 200 MIPs operation  e200z0h, 32-bit Power Architecture – Up to 80 MHz and 75 MIPs operation  Memory – Up to 3 MByte on-chip Flash with ECC – Up to 256 KByte on-chip SRAM with ECC – 64KByte on-chip Data Flash with ECC – 16-entry memory protection unit (MPU) – User selectable Memory BIST  Interrupts – 255 interrupt sources with 16 priority levels – Up to 54 ext. IRQ including 30 wake-up  GPIOs: from 147 (LQFP176) to 199 (LBGA256)  System timer units – 8-ch. 32-bit periodic interrupt timer (PIT) – 4-channel 32-bit system timer (STM) – Safety System Watchdog Timer (SWT) – Real-time clock timer (RTC/API)  eMIOS, 16-bit counter timed I/O units – Up to 64 channels with PWM/MC/IC/OC  Two ADC (10-bit and 12-bit) – Up to 62 channels extendable to 90 ch. – Multiple Analog Watchdog  Dedicated diagnostic features for lighting – Advanced shiffted PWM generation – ADC conversion synchronized on PWM  Communication interfaces

###### – Up to 6 FlexCAN with 64 buffers each – Up to 10 LINFlex/UART channels – Up to 8 buffered DSPI channels – I [2] C interface – One FleyRay (dual-ch.) with 128 buffers – Fast Ethernet Controller  Cryptographic Services Engine (CSE) – AES-128 en/decryption, CMAC auth. – Secured device boot mode  32-ch. eDMA with multiple request sources  Clock generation – 4 to 40 MHz main oscillator – 16 MHz internal RC oscillator – Software-controlled FMPLL – 128 kHz internal RC oscillator – 32 kHz auxiliary oscillator – Clock Monitoring Unit (CMU)  Low power capabilities – Ultra low power STANDBY – CAN Sampler to store CAN ID in STBY – Fast wake-up and exectute from RAM  Exhaustive debugging capability – Nexus 3+ interface on LBGA256 only – Nexus 1 on all devices  Voltage supply – Single 5 V or 3.3 V supply – On-chip Vreg with external ballast transitor  Operating temperature range -40 to 125 °C


March 2016 DocID17478 Rev 9 1/123

This is information on a product in full production. *[www.st.com](http://www.st.com)*


-----

###### **SPC564Bxx-SPC56ECxx**

|Col1|Table 1. Device summary|Col3|Col4|
|---|---|---|---|
|Package|Part number|||
||1.5 MByte|2 MByte|3 MByte|
|LQFP176|SPC564B64L7 SPC56EC64L7|SPC564B70L7 SPC56EC70L7|SPC564B74L7 SPC56EC74L7|
|LQFP208|SPC564B64L8 SPC56EC64L8|SPC564B70L8 SPC56EC70L8|SPC564B74L8 SPC56EC74L8|
|LBGA256|SPC56EC64B3|SPC56EC70B3|SPC56EC74B3|


2/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Contents**
## **Contents**
###### **1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9** 1.1 Document Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.2 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.3 Block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 **2 Package pinouts and signal descriptions . . . . . . . . . . . . . . . . . . . . . . . 15** 2.1 Pad types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 2.2 System pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 2.3 Functional ports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 **3 Electrical Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51** 3.1 Parameter classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 3.2 NVUSRO register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 3.2.1 NVUSRO [PAD3V5V(0)] field description . . . . . . . . . . . . . . . . . . . . . . . 52 3.2.2 NVUSRO [PAD3V5V(1)] field description . . . . . . . . . . . . . . . . . . . . . . . 52 3.3 Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 3.4 Recommended operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54 3.5 Thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 3.5.1 Package thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 3.5.2 Power considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 3.6 I/O pad electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 3.6.1 I/O pad types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 3.6.2 I/O input DC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 3.6.3 I/O output DC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60 3.6.4 Output pin transition times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 3.6.5 I/O pad current specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63 3.7 RESET electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 3.8 Power management electrical characteristics . . . . . . . . . . . . . . . . . . . . . 67 3.8.1 Voltage regulator electrical characteristics . . . . . . . . . . . . . . . . . . . . . . 67 3.8.2 VDD_BV options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68 3.8.3 Voltage monitor electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . 69 3.9 Low voltage domain power consumption . . . . . . . . . . . . . . . . . . . . . . . . . 70 3.10 Flash memory electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 72

DocID17478 Rev 9 3/123


5


-----

###### **Contents SPC564Bxx-SPC56ECxx** 3.10.1 Program/Erase characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72 3.10.2 Flash memory power supply DC characteristics . . . . . . . . . . . . . . . . . . 74 3.10.3 Flash memory start-up/switch-off timings . . . . . . . . . . . . . . . . . . . . . . . 75 3.11 Electromagnetic compatibility (EMC) characteristics . . . . . . . . . . . . . . . . 75 3.11.1 Designing hardened software to avoid noise problems . . . . . . . . . . . . . 75 3.11.2 Electromagnetic interference (EMI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 3.11.3 Absolute maximum ratings (electrical sensitivity) . . . . . . . . . . . . . . . . . 76 3.12 Fast external crystal oscillator (4–40 MHz) electrical characteristics . . . . 77 3.13 Slow external crystal oscillator (32 kHz) electrical characteristics . . . . . . 80 3.14 FMPLL electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83 3.15 Fast internal RC oscillator (16 MHz) electrical characteristics . . . . . . . . . 83 3.16 Slow internal RC oscillator (128 kHz) electrical characteristics . . . . . . . . 85 3.17 ADC electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 3.17.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 3.18 Fast Ethernet Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96 3.18.1 MII Receive Signal Timing (RXD[3:0], RX_DV, RX_ER, and RX_CLK) . 96 3.18.2 MII Transmit Signal Timing (TXD[3:0], TX_EN, TX_ER, TX_CLK) . . . . 97 3.18.3 MII Async Inputs Signal Timing (CRS and COL) . . . . . . . . . . . . . . . . . . 97 3.18.4 MII Serial Management Channel Timing (MDIO and MDC) . . . . . . . . . . 98 3.19 On-chip peripherals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 3.19.1 Current consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 3.19.2 DSPI characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100 3.19.3 Nexus characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106 3.19.4 JTAG characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108 **4 Package characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110** 4.1 ECOPACK® . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .110 4.2 Package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .110 4.2.1 LQFP176 package mechanical drawing . . . . . . . . . . . . . . . . . . . . . . . 110 4.2.2 LQFP208 package mechanical drawing . . . . . . . . . . . . . . . . . . . . . . . 112 4.2.3 LBGA256 package mechanical drawing . . . . . . . . . . . . . . . . . . . . . . . 114 **5 Ordering information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116** **Appendix A Abbreviations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117**

4/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Contents** **Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118**

DocID17478 Rev 9 5/123


5


-----

###### **List of tables SPC564Bxx-SPC56ECxx**
## **List of tables**
###### Table 1. Device summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 Table 2. SPC564Bxx and SPC56ECxx family comparison. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 Table 3. SPC564Bxx and SPC56ECxx series block summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 Table 4. System pin descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 Table 5. Functional port pin descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 Table 6. Parameter classifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 Table 7. PAD3V5V(0) field description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 Table 8. PAD3V5V(1) field description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 Table 9. Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 Table 10. Recommended operating conditions (3.3 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54 Table 11. Recommended operating conditions (5.0 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55 Table 12. LQFP thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 Table 13. LBGA256 thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 Table 14. I/O input DC electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 Table 15. I/O pull-up/pull-down DC electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60 Table 16. SLOW configuration output buffer electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . 60 Table 17. MEDIUM configuration output buffer electrical characteristics . . . . . . . . . . . . . . . . . . . . . . 61 Table 18. FAST configuration output buffer electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . 62 Table 19. Output pin transition times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 Table 20. I/O supplies. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63 Table 21. I/O consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64 Table 22. Reset electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 Table 23. Voltage regulator electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68 Table 24. Low voltage monitor electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 Table 25. Low voltage power domain electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71 Table 26. Code flash memory—Program and erase specifications . . . . . . . . . . . . . . . . . . . . . . . . . . 72 Table 27. Data flash memory—Program and erase specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . 73 Table 28. Flash memory module life. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73 Table 29. Flash memory read access timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74 Table 30. Flash memory power supply DC electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . 74 Table 31. Start-up time/Switch-off time. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75 Table 32. EMI radiated emission measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 Table 33. ESD absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76 Table 34. Latch-up results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 Table 35. Crystal description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 Table 36. Fast external crystal oscillator (4 to 40 MHz) electrical characteristics. . . . . . . . . . . . . . . . 79 Table 37. Crystal motional characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81 Table 38. Slow external crystal oscillator (32 kHz) electrical characteristics . . . . . . . . . . . . . . . . . . . 82 Table 39. FMPLL electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83 Table 40. Fast internal RC oscillator (16 MHz) electrical characteristics . . . . . . . . . . . . . . . . . . . . . . 83 Table 41. Slow internal RC oscillator (128 kHz) electrical characteristics . . . . . . . . . . . . . . . . . . . . . 85 Table 42. ADC input leakage current . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 Table 43. ADC conversion characteristics (10-bit ADC_0). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 Table 44. Conversion characteristics (12-bit ADC_1). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94 Table 45. MII Receive Signal Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96 Table 46. MII transmit signal timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97 Table 47. MII Async Inputs Signal Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97 Table 48. MII serial management channel timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98

6/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx List of tables** Table 49. On-chip peripherals current consumption. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 Table 50. DSPI timing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100 Table 51. Nexus debug port timing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106 Table 52. JTAG characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108 Table 53. LQFP176 mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111 Table 54. LQFP208 mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113 Table 55. LBGA256 mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115 Table 56. Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117 Table 57. Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

DocID17478 Rev 9 7/123


7


-----

###### **List of figures SPC564Bxx-SPC56ECxx**
## **List of figures**
###### Figure 1. SPC564Bxx and SPC56ECxx block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 Figure 2. 176-pin LQFP configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 Figure 3. 208-pin LQFP configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 Figure 4. 256-pin BGA configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 Figure 5. I/O input DC electrical characteristics definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 Figure 6. Start-up reset requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 Figure 7. Noise filtering on reset signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 Figure 8. Voltage regulator capacitance connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 Figure 9. Low voltage monitor vs. Reset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70 Figure 10. Crystal oscillator and resonator connection scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 Figure 11. Fast external crystal oscillator (4 to 40 MHz) electrical characteristics. . . . . . . . . . . . . . . . 79 Figure 12. Crystal oscillator and resonator connection scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80 Figure 13. Equivalent circuit of a quartz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81 Figure 14. Slow external crystal oscillator (32 kHz) electrical characteristics . . . . . . . . . . . . . . . . . . . 82 Figure 15. ADC_0 characteristic and error definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86 Figure 16. Input equivalent circuit (precise channels) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 Figure 17. Input equivalent circuit (extended channels) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 Figure 18. Transient behavior during sampling phase. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 Figure 19. Spectral representation of input signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 Figure 20. ADC_1 characteristic and error definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93 Figure 21. MII receive signal timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96 Figure 22. MII transmit signal timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97 Figure 23. MII async inputs timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 Figure 24. MII serial management channel timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 Figure 25. DSPI classic SPI timing–master, CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102 Figure 26. DSPI classic SPI timing–master, CPHA = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102 Figure 27. DSPI classic SPI timing–slave, CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 Figure 28. DSPI classic SPI timing–slave, CPHA = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 Figure 29. DSPI modified transfer format timing–master, CPHA = 0. . . . . . . . . . . . . . . . . . . . . . . . . 104 Figure 30. DSPI modified transfer format timing–master, CPHA = 1. . . . . . . . . . . . . . . . . . . . . . . . . 104 Figure 31. DSPI modified transfer format timing–slave, CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . 105 Figure 32. DSPI modified transfer format timing–slave, CPHA = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . 105 Figure 33. DSPI PCS strobe (PCSS) timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106 Figure 34. Nexus output timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107 Figure 35. Nexus TDI, TMS, TDO timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108 Figure 36. Timing diagram - JTAG boundary scan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109 Figure 37. LQFP176 package mechanical drawing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110 Figure 38. LQFP208 mechanical drawing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112 Figure 39. LBGA256 mechanical drawing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114 Figure 40. Ordering information scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116

8/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Introduction**
### **1 Introduction**
##### **1.1 Document Overview**
###### This document describes the features of the family and options available within the family members, and highlights important electrical and physical characteristics of the SPC564Bxx and SPC56ECxx device. To ensure a complete understanding of the device functionality, refer also to the SPC564Bxx and SPC56ECxx Reference Manual.
##### **1.2 Description**
###### The SPC564Bxx and SPC56ECxx is a new family of next generation microcontrollers built on the Power Architecture embedded category. This document describes the features of the family and options available within the family members, and highlights important electrical and physical characteristics of the device. The SPC564Bxx and SPC56ECxx family expands the range of the SPC560B microcontroller family. It provides the scalability needed to implement platform approaches and delivers the performance required by increasingly sophisticated software architectures. The advanced and cost-efficient host processor core of the SPC564Bxx and SPC56ECxx automotive controller family complies with the Power Architecture embedded category, which is 100 percent user-mode compatible with the original Power Architecture user instruction set architecture (UISA). It operates at speeds of up to 120 MHz and offers high performance processing optimized for low power consumption. It also capitalizes on the available development infrastructure of current Power Architecture devices and is supported with software drivers, operating systems and configuration code to assist with users implementations.

DocID17478 Rev 9 9/123


122


-----

###### **Table 2. SPC564Bxx and SPC56ECxx famil y com p arison [(1)]**

|Feature|Col2|SPC564B64|Col4|SPC56EC64|Col6|Col7|SPC564B70|Col9|SPC56EC70|Col11|Col12|SPC564B74|Col14|SPC56EC74|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Package||LQFP 176|LQFP 208|LQFP 176|LQFP 208|LBGA 256|LQFP 176|LQFP 208|LQFP 176|LQFP 208|LBGA 256|LQFP 176|LQFP 208|LQFP 176|LQFP 208|LBGA 256|
|CPU||e200z4d||e200z4d + e200z0h|||e200z4d||e200z4d + e200z0h|||e200z4d||e200z4d + e200z0h|||
|Execution speed(2)||Up to 120 MHz (e200z4d)||Up to 120 MHz (e200z4d) Up to 80 MHz (e200z0h)(3)|||Up to 120 MHz (e200z4d)||Up to 120 MHz (e200z4d) Up to 80 MHz (e200z0h)(3)|||Up to 120 MHz (e200z4d)||Up to 120 MHz (e200z4d) Up to 80 MHz (e200z0h)(3)|||
|Code flash memory||1.5 MB|||||2 MB|||||3 MB|||||
|Data flash memory||4 x16 KB|||||||||||||||
|SRAM||128 KB||192 KB|||160 KB||256 KB|||192 KB||256 KB|||
|MPU||16-entry|||||||||||||||
|eDMA(4)||32 ch|||||||||||||||
|10-bit ADC||27 ch|33 ch|27 ch|33 ch||27 ch|33 ch|27 ch|33 ch||27 ch|33 ch|27 ch|33 ch||
||dedicated(5), (6)||||||||||||||||
||shared with 12-bit ADC(7)|19 ch|||||||||||||||
|12-bit ADC||5 ch|10 ch|5 ch|10 ch||5 ch|10 ch|5 ch|10 ch||5 ch|10 ch|5 ch|10 ch||
||dedicated(8)||||||||||||||||
||shared with 10-bit ADC(7)|19 ch|||||||||||||||
|CTU||64 ch|||||||||||||||
|Total timer I/O(9) eMIOS||64 ch, 16-bit|||||||||||||||
|SCI (LINFlexD)||10|||||||||||||||
|SPI (DSPI)||8|||||||||||||||
|CAN (FlexCAN)(10)||6|||||||||||||||


-----

###### **Table 2. SPC564Bxx and SPC56ECxx famil y com p arison [(1)] (continued)**

1. Feature set dependent on selected peripheral multiplexing; table shows example.

2. Based on 125 C ambient operating temperature and subject to full device characterization.

3. The e200z0h can run at speeds up to 80 MHz. However, if system frequency is >80 MHz (e.g., e200z4d running at 120 MHz) the e200z0h needs to run at 1/2 system
frequency. There is a configurable e200z0 system clock divider for this purpose.

4. DMAMUX also included that allows for software selection of 32 out of a possible 57 sources.

5. Not shared with 12-bit ADC, but possibly shared with other alternate functions.

6. There are 23 dedicated ANS plus 4 dedicated ANX channels on LQPF176. For higher pin count packages, there are 29 dedicated ANS plus 4 dedicated ANX channels.

7. 16x precision channels (ANP) and 3x standard (ANS).

8. Not shared with 10-bit ADC, but possibly shared with other alternate functions.

9. As a minimum, all timer channels can function as PWM or Input Capture and Output Control. Refer to the eMIOS section of the device reference manual for information on
the channel configuration and functions.

10. CAN Sampler also included that allows ID of CAN message to be captured when in low power mode.

11. STCU controls MBIST activation and reporting.

12. Estimated I/O count for proposed packages based on multiplexing with peripherals.

|Feature|SPC564B64|Col3|SPC56EC64|Col5|Col6|SPC564B70|Col8|SPC56EC70|Col10|Col11|SPC564B74|Col13|SPC56EC74|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Package|LQFP 176|LQFP 208|LQFP 176|LQFP 208|LBGA 256|LQFP 176|LQFP 208|LQFP 176|LQFP 208|LBGA 256|LQFP 176|LQFP 208|LQFP 176|LQFP 208|LBGA 256|
|FlexRay|Yes|||||||||||||||
|STCU(11)|Yes|||||||||||||||
|Ethernet|No||Yes|||No||Yes|||No||Yes|||
|I2C|1|||||||||||||||
|32 kHz oscillator (SXOSC)|Yes|||||||||||||||
|GPIO(12)|147|177|147|177|199|147|177|147|177|199|147|177|147|177|199|
|Debug|JTAG||||Nexus 3+|JTAG||||Nexus 3+|JTAG||||Nexus 3+|
|Cryptographic Services Engine (CSE)|Optional|||||||||||||||


-----

###### **Introduction SPC564Bxx-SPC56ECxx**
##### **1.3 Block diagram**
###### Figure 1 shows the detailed block diagram of the SPC564Bxx and SPC56ECxx. **Figure 1. SPC564Bxx and SPC56ECxx block diagram**


|Code Flash 2 1.5 MB|Data Flash 64 KB|
|---|---|


2  SRAM Flash memory

controller controller

(Slave)

(Slave)

(Slave)

DMAMUX


FEC

CSE

FlexRay

Instructions

(Master)

Data

(Master)

Instructions
(Master)

Data
(Master)


JTAG Port

Nexus Port


JTAGC

Nexus


Voltage
regulator


NMI1

Interrupt requests

from peripheral

blocks


NMI0

NMI1


INTC


MPU

registers




|Col1|Col2|STCU|Col4|
|---|---|---|---|
||BAM SSCM WK|||
|||||
|Peripheral Bridge||||
|||||
|||6  FlexCAN||


Request

|Col1|Col2|
|---|---|
| SPI|I2C|


External

Interrupt
Request

IMUX

GPIO &

Pad Control




(3) (3)

I/O

Legend: ADC Analog-to-Digital Converter JTAGC JTAG controller

BAM Boot Assist Module LINFlexD Local Interconnect Network Flexible with DMA sup
CSE Cryptographic Services Engine MC_ME Mode Entry Module
CAN Controller Area Network (FlexCAN) MC_CGM Clock Generation Module
CMU Clock Monitor Unit MC_PCU Power Control Unit
CTU Cross Triggering Unit MC_RGM Reset Generation Module
DMAMUX DMA Channel Multiplexer MPU Memory Protection Unit
DSPI Deserial Serial Peripheral Interface Nexus Nexus Development Interface
eDMA enhanced Direct Memory Access NMI Non-Maskable Interrupt
FlexCAN Controller Area Network controller modules PIT_RTI Periodic Interrupt Timer with Real-Time Interrupt
FEC Fast Ethernet Controller RTC/API Real-Time Clock/ Autonomous Periodic Interrupt
eMIOS Enhanced Modular Input Output System SIUL System Integration Unit Lite
ECSM Error Correction Status Module SRAM Static Random-Access Memory
FMPLL Frequency-Modulated Phase-Locked Loop SSCM System Status Configuration Module
FlexRay FlexRay Communication Controller STM System Timer Module
I2C Inter-integrated Circuit Bus SWT Software Watchdog Timer
IMUX Internal Multiplexer STCU Self Test Control Unit
INTC Interrupt Controller WKPU Wakeup Unit

Notes: 1) 10 dedicated channels plus up to 19 shared channels . See the device-comparison table.
2) Package dependent. 27 or 33 dedicated channels plus up to 19 shared channels. See the device-comparison table.
3) 16 x precision channels (ANP) are mapped on input only I/O cells.

12/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Introduction** Table 3 summarizes the functions of the blocks present on the SPC564Bxx and SPC56ECxx. **Table 3. SPC564Bxx and SPC56ECxx series block summar y**

DocID17478 Rev 9 13/123

|Block|Function|
|---|---|
|Analog-to-digital converter (ADC)|Converts analog voltages to digital values|
|Boot assist module (BAM)|A block of read-only memory containing VLE code which is executed according to the boot mode of the device|
|Clock monitor unit (CMU)|Monitors clock source (internal and external) integrity|
|Cross triggering unit (CTU)|Enables synchronization of ADC conversions with a timer event from the eMIOS or from the PIT|
|Cryptographic Security Engine (CSE)|Supports the encoding and decoding of any kind of data|
|Crossbar (XBAR) switch|Supports simultaneous connections between two master ports and three slave ports. The crossbar supports a 32-bit address bus width and a 64-bit data bus width|
|DMA Channel Multiplexer (DMAMUX)|Allows to route DMA sources (called slots) to DMA channels|
|Deserial serial peripheral interface (DSPI)|Provides a synchronous serial interface for communication with external devices|
|Error Correction Status Module (ECSM)|Provides a myriad of miscellaneous control functions for the device including program-visible information about configuration and revision levels, a reset status register, wakeup control for exiting sleep modes, and optional features such as information on memory errors reported by error-correcting codes|
|Enhanced Direct Memory Access (eDMA)|Performs complex data transfers with minimal intervention from a host processor via “n” programmable channels.|
|Enhanced modular input output system (eMIOS)|Provides the functionality to generate or measure events|
|Flash memory|Provides non-volatile storage for program code, constants and variables|
|FlexCAN (controller area network)|Supports the standard CAN communications protocol|
|FMPLL (frequency-modulated phase-locked loop)|Generates high-speed system clocks and supports programmable frequency modulation|
|FlexRay (FlexRay communication controller)|Provides high-speed distributed control for advanced automotive applications|
|Fast Ethernet Controller (FEC)|Ethernet Media Access Controller (MAC) designed to support both 10 and 100 Mbps Ethernet/IEEE 802.3 networks|
|Internal multiplexer (IMUX) SIUL subblock|Allows flexible mapping of peripheral interface on the different pins of the device|
|Inter-integrated circuit (I2C™) bus|A two wire bidirectional serial bus that provides a simple and efficient method of data exchange between devices|
|Interrupt controller (INTC)|Provides priority-based preemptive scheduling of interrupt requests for both e200z0h and e200z4d cores|
|JTAG controller|Provides the means to test chip functionality and connectivity while remaining transparent to system logic when not in test mode|


122


-----

###### **Introduction SPC564Bxx-SPC56ECxx** **Table 3. SPC564Bxx and SPC56ECxx series block summar y ( continued )**

14/123 DocID17478 Rev 9

|Block|Function|
|---|---|
|LinFlexD (Local Interconnect Network Flexible with DMA support)|Manages a high number of LIN (Local Interconnect Network protocol) messages efficiently with a minimum of CPU load|
|Memory protection unit (MPU)|Provides hardware access control for all memory references generated in a device|
|Clock generation module (MC_CGM)|Provides logic and control required for the generation of system and peripheral clocks|
|Power control unit (MC_PCU)|Reduces the overall power consumption by disconnecting parts of the device from the power supply via a power switching device; device components are grouped into sections called “power domains” which are controlled by the PCU|
|Reset generation module (MC_RGM)|Centralizes reset sources and manages the device reset sequence of the device|
|Mode entry module (MC_ME)|Provides a mechanism for controlling the device operational mode and mode transition sequences in all functional states; also manages the power control unit, reset generation module and clock generation module, and holds the configuration, control and status registers accessible for applications|
|Non-Maskable Interrupt (NMI)|Handles external events that must produce an immediate response, such as power down detection|
|Nexus Development Interface (NDI)|Provides real-time development capabilities for e200z0h and e200z4d core processor|
|Periodic interrupt timer/ Real Time Interrupt Timer (PIT_RTI)|Produces periodic interrupts and triggers|
|Real-time counter (RTC/API)|A free running counter used for time keeping applications, the RTC can be configured to generate an interrupt at a predefined interval independent of the mode of operation (run mode or low-power mode). Supports autonomous periodic interrupt (API) function to generate a periodic wakeup request to exit a low power mode or an interrupt request|
|Static random-access memory (SRAM)|Provides storage for program code, constants, and variables|
|System integration unit lite (SIUL)|Provides control over all the electrical pad controls and up 32 ports with 16 bits of bidirectional, general-purpose input and output signals and supports up to 32 external interrupts with trigger event configuration|
|System status and configuration module (SSCM)|Provides system configuration and status data (such as memory size and status, device mode and security status), device identification data, debug status port enable and selection, and bus and peripheral abort enable/disable|
|System timer module (STM)|Provides a set of output compare events to support AutoSAR and operating system tasks|
|Semaphores|Provides the hardware support needed in multi-core systems for sharing resources and provides a simple mechanism to achieve lock/unlock operations via a single write access.|
|Wake Unit (WKPU)|Supports external sources that can generate interrupts or wakeup events, of which can cause non-maskable interrupt requests or wakeup events.|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions**
### **2 Package pinouts and signal descriptions**
###### The available LQFP pinouts and the LBGA ballmaps are provided in the following figures. For functional port pin description, see Table 6 . **Figure 2. 176-pin LQFP configuration**


PB[3]
PC[9]
PC[14]
PC[15]
PJ[4]
VDD_HV_A
VSS_HV
PH[15]
PH[13]
PH[14]
PI[6]
PI[7]
PG[5]
PG[4]
PG[3]
PG[2]
PA[2]
PE[0]
PA[1]
PE[1]
PE[8]
PE[9]
PE[10]
PA[0]
PE[11]
VSS_HV
VDD_HV_A
VSS RESET_ HV
VSS_LV
VDD_LV
VRC_CTRL
PG[9]
PG[8]
PC[11]
PC[10]
PG[7]
PG[6]
PB[0]
PB[1]
PF[9]
PF[8]
PF[12]
PC[6]

**NOTE**

|PB[2] PC[8] PC[13 PC[12 PI[0] PI[1] PI[2] PI[3] PE[7] PE[6] PH[8] PH[7] PH[6] PH[5] PH[4] PE[5] PE[4] PC[4] PC[5] PE[3] PE[2] PH[9] PC[0]|PC[0] VSS_ VDD_ VDD_ VSS_ PC[1] PH[10 PA[6] PA[5] PC[2] PC[3] PI[4] PI[5] PH[12 PH[11 PG[11 PG[10 PE[15 PE[14 PG[15 PG[14 PE[12|
|---|---|
|176 175 174 173 172 171 170 169 168 167 166 165 164 163 162 161 160 159 158 157 156 155 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 LQF 22|154 153 152 151 150 149 148 147 146 145 144 143 142 141 140 139 138 137 136 135 134 133 132 131 130 129 128 127 126 125 124 123 122 121 120 119 118 117 116 115 114 113 P176 112 111|
|23 Top 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66|view 110 109 108 107 106 105 104 103 102 101 100 99 98 97 96 95 94 93 92 91 90 89 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88|

1) VDD_HV_B supplies the IO voltage domain for the
pins PE[12], PA[11], PA[10], PA[9], PA[8], PA[7],
PE[13], PF[14], PF[15], PG[0], PG[1], PH[3], PH[2],
PH[1], PH[0], PG[12], PG[13], and PA[3].

2)Availability of port pin alternate functions depends
on product selection.


132 PA[11]
131 PA[10]
130 PA[9]
129 PA[8]
128 PA[7]
127 PE[13]
126 PF[14]
125 PF[15]
124 VDD_HV_B
123 VSS_HV
122 PG[0]
121 PG[1]
120 PH[3]
119 PH[2]
118 PH[1]
117 PH[0]
116 PG[12]
115 PG[13]
114 PA[3]
113 PI[13]

110 VDD_LV

107 PB[15]
106 PD[15]
105 PB[14]
104 PD[14]
103 PB[13]
102 PD[13]
101 PB[12]
100 PD[12]
99 VDD_HV_ADC1
98 VSS_HV_ADC1
97 PB[11]
96 PD[11]
95 PD[10]
94 PD[9]
93 PB[7]
92 PB[6]
91 PB[5]
90 VDD_HV_ADC0
89 VSS_HV_ADC0

DocID17478 Rev 9 15/123


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Figure 3. 208-pin LQFP configuration**


PB[3]
PC[9]
PC[14]
PC[15]
PJ[4]
VDD_HV_A
VSS_HV
PH[15]
PH[13]
PH[14]
P[I6]
P[I7]
PG[5]
PG[4]
PG[3]
PG[2]
PA[2]
PE[0]
PA[1]
PE[1]
PE[8]
PE[9]
PE[10]
PA[0]
PE[11]
VSS_HV
VDD_HV_A
VSS RESET_ HV
VSS_LV
VDD_LV
VRC_CTRL
PG[9]
PG[8]
PC[11]
PC[10]
PG[7]
PG[6]
PB[0]
PB[1]
PK[1]
PK[2]
PK[3]
PK[4]
PK[5]
PK[6]
PK[7]
PK[8]
PF[9]
PF[8]
PF[12]
PC[6]


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52

###### LQFP208

Top view


156
155
154
153
152
151
150
149
148
147
146
145
144
143
142
141
140
139
138
137
136
135
134
133
132
131
130
129
128
127
126
125
124
123
122
121
120
119
118
117
116
115
114
113
112
111
110
109
108
107
106
105


PA[11]
PA[10]
PA[9]
PA[8]
PA[7]
PE[13]
PF[14]
PF[15]
VDD_HV_B
VSS_HV
PG[0]
PG[1]
PH[3]
PH[2]
PH[1]
PH[0]
PG[12]
PG[13]
PA[3]
PI[13]
PI[12]
PI[11]
PI[10]
VDD_LV
VSS_LV
PI[9]
PI[8]
PB[15]
PD[15]
PB[14]
PD[14]
PB[13]
PD[13]
PB[12]
VDD_HV_A
VSS_HV
PD[12]
VDD_HV_ADC1
VSS_HV_ADC1
PB[11]
PD[11]
PD[10]
PD[9]
PJ[5]
PJ[6]
PJ[7]
PJ[8]
PB[7]
PB[6]
PB[5]
VDD_HV_ADC0
VSS_HV_ADC0


NOTE
1) VDD_HV_B supplies the IO voltage domain for the pins PE[12], PA[11], PA[10], PA[9],
PA[8], PA[7], PE[13], PF[14], PF[15], PG[0], PG[1], PH[3], PH[2], PH[1], PH[0], PG[12],
PG[13], and PA[3].
2) Availability of port pin alternate functions depends on product selection.

16/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions**

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Notes:

|PC[15]|PB[2]|PC[13]|PI[1]|PE[7]|PH[8]|PE[2]|PE[4]|PC[4]|PE[3]|PH[9]|PI[4]|PH[11]|PE[14]|PA[10]|PG[11]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PH[13]|PC[14]|PC[8]|PC[12]|PI[3]|PE[6]|PH[5]|PE[5]|PC[5]|PC[0]|PC[2]|PH[12]|PG[10]|PA[11]|PA[9]|PA[8]|
|PH[14]|VDD_HV _A|PC[9]|PL[0]|PI[0]|PH[7]|PH[6]|VSS_LV|VDD_HV _A|PA[5]|PC[3]|PE[15]|PG[14]|PE[12]|PA[7]|PE[13]|
|PG[5]|PI[6]|PJ[4]|PB[3]|PK[15]|PI[2]|PH[4]|VDD_LV|PC[1]|PH[10]|PA[6]|PI[5]|PG[15]|PF[14]|PF[15]|PH[2]|
|PG[3]|PI[7]|PH[15]|PG[2]|VDD_LV|VSS_LV|PK[10]|PK[9]|PM[1]|PM[0]|PL[15]|PL[14]|PG[0]|PG[1]|PH[0]|VDD_HV _A|
|PA[2]|PG[4]|PA[1]|PE[1]|PL[2]|PM[6]|PL[1]|PK[11]|PM[5]|PL[13]|PL[12]|PM[2]|PH[1]|PH[3]|PG[12]|PG[13]|
|PE[8]|PE[0]|PE[10]|PA[0]|PL[3]|VSS_HV|VSS_HV|VSS_HV|VSS_HV|VSS_HV|VSS_HV|PK[12]|VDD_HV _B|PI[13]|PI[12]|PA[3]|
|PE[9]|VDD_HV _A|PE[11]|PK[1]|PL[4]|VSS_LV|VSS_LV|VSS_HV|VSS_HV|VSS_HV|VSS_HV|PK[13]|VDD_HV _A|VDD_LV|VSS_LV|PI[11]|
|VSS_HV|VRC_CT RL|VDD_LV|PG[9]|PL[5]|VSS_LV|VSS_LV|VSS_LV|VSS_HV|VSS_HV|VSS_HV|PK[14]|PD[15]|PI[8]|PI[9]|PI[10]|
|RESET|VSS_LV|PG[8]|PC[11]|PL[6]|VSS_LV|VSS_LV|VSS_LV|VSS_LV|VDD_LV|VDD_LV|PM[3]|PD[14]|PD[13]|PB[14]|PB[15]|
|PC[10]|PG[7]|PB[0]|PK[2]|PL[7]|VSS_LV|VSS_LV|VSS_LV|VSS_LV|VDD_LV|VDD_LV|PM[4]|PD[12]|PB[12]|PB[13]|VDD_HV _ADC1|
|PG[6]|PB[1]|PK[4]|PF[9]|PK[5]|PK[6]|PK[7]|PK[8]|PL[8]|PL[9]|PL[10]|PL[11]|PB[11]|PD[10]|PD[11]|VSS_HV _ADC1|
|PK[3]|PF[8]|PC[6]|PC[7]|PJ[13]|VDD_HV _A|PB[10]|PF[6]|VDD_HV _A|PJ[1]|PD[2]|PJ[5]|PB[5]|PB[6]|PJ[6]|PD[9]|
|PF[12]|PF[10]|PF[13]|PA[14]|PJ[9]|PA[12]|PF[0]|PF[5]|PF[7]|PJ[3]|PI[15]|PD[4]|PD[7]|PD[8]|PJ[8]|PJ[7]|
|PF[11]|PA[15]|PJ[11]|PJ[15]|PA[13]|PF[2]|PF[3]|PF[4]|VDD_LV|PJ[2]|PJ[0]|PD[0]|PD[3]|PD[6]|VDD_HV _ADC0|PB[7]|
|PJ[12]|PA[4]|PK[0]|PJ[14]|PJ[10]|PF[1]|XTAL|EXTAL|VSS_LV|PB[9]|PB[8]|PI[14]|PD[1]|PD[5]|VSS_HV _ADC0|PB[4]|


1) VDD_HV_B supplies the IO voltage domain for the pins PE[12], PA[11], PA[10], PA[9], PA[8], PA[7], PE[13], PF[14], PF[15], PG[0], PG[1],
PH[3], PH[2], PH[1], PH[0], PG[12], PG[13], PA[3], PM[3], and PM[4].
2)Availability of port pin alternate functions depends on product selection. **Figure 4. 256-pin BGA configuration**

DocID17478 Rev 9 17/123


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx**
##### **2.1 Pad types**
###### In the device the following types of pads are available for system pins and functional port pins: S = Slow [(a)] M = Medium [(a),(b)] F = Fast [(a),(b)] I = Input only with analog feature [(a)] A = Analog
##### **2.2 System pins**
###### The system pins are listed in Table 4 . **Table 4. S y stem p in descri p tions **

1. For analog pads, it is not recommended to enable IBE if APC is enabled to avoid extra current in middle range voltage.

a. See the I/O pad electrical characteristics in the device datasheet for details.

|Port pin|Function|I/O direction|Pad type|RESET config.|Pin number|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||||LQFP 176|LQFP 208|LBGA 256|
|RESET|Bidirectional reset with Schmitt-Trigger characteristics and noise filter.|I/O|M|Input, weak pull-up only after PHASE2|29|29|K1|
|EXTAL|Analog input of the oscillator amplifier circuit. Needs to be grounded if oscillator bypass mode is used.|I|A(1)|—|58|74|T8|
|XTAL|Analog output of the oscillator amplifier circuit, when the oscillator is not in bypass mode.  Analog input for the clock generator when the oscillator is in bypass mode.|I/O|A(1)|—|56|72|T7|



b. All medium and fast pads are in slow configuration by default at reset and can be configured as fast or medium.
For example, Fast/Medium pad will be Medium by default at reset. Similarly, Slow/Medium pad will be Slow by
default. Only exception is PC[1] which is in medium configuration by default (refer to PCR.SRC in the reference
manual, Pad Configuration Registers (PCR0—PCR198)).

18/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions**
##### **2.3 Functional ports**
###### The functional port pins are listed in Table 5 . **Table 5. Functional p ort p in descri p tions **

DocID17478 Rev 9 19/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PA[0]|PCR[0]|AF0 AF1 AF2 AF3 — —|GPIO[0] E0UC[0] CLKOUT E0UC[13] WKPU[19] CAN1RX|SIUL eMIOS_0 MC_CGM eMIOS_0 WKPU FlexCAN_1|I/O I/O O I/O I I|M/S|Tristate|24|24|G4|
|PA[1]|PCR[1]|AF0 AF1 AF2 AF3 — — —|GPIO[1] E0UC[1] — — WKPU[2] CAN3RX NMI[0](3)|SIUL eMIOS_0 — — WKPU FlexCAN_3 WKPU|I/O I/O — — I I I|S|Tristate|19|19|F3|
|PA[2]|PCR[2]|AF0 AF1 AF2 AF3 — —|GPIO[2] E0UC[2] — MA[2] WKPU[3] NMI[1](3)|SIUL eMIOS_0 — ADC_0 WKPU WKPU|I/O I/O — O I I|S|Tristate|17|17|F1|
|PA[3]|PCR[3]|AF0 AF1 AF2 AF3 — — —|GPIO[3] E0UC[3] LIN5TX CS4_1 RX_ER_CLK EIRQ[0] ADC1_S[0]|SIUL eMIOS_0 LINFlexD_5 DSPI_1 FEC SIUL ADC_1|I/O I/O O O I I I|M/S|Tristate|114|138|G16|
|PA[4]|PCR[4]|AF0 AF1 AF2 AF3 — —|GPIO[4] E0UC[4] — CS0_1 LIN5RX WKPU[9]|SIUL eMIOS_0 — DSPI_1 LINFlexD_5 WKPU|I/O I/O — I/O I I|S|Tristate|51|61|T2|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

20/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PA[5]|PCR[5]|AF0 AF1 AF2|GPIO[5] E0UC[5] LIN4TX|SIUL eMIOS_0 LINFlexD_4|I/O I/O O|M/S|Tristate|146|170|C10|
|PA[6]|PCR[6]|AF0 AF1 AF2 AF3 — —|GPIO[6] E0UC[6] — CS1_1 LIN4RX EIRQ[1]|SIUL eMIOS_0 — DSPI_1 LINFlexD_4 SIUL|I/O I/O — O I I|S|Tristate|147|171|D11|
|PA[7]|PCR[7]|AF0 AF1 AF2 AF3 — — —|GPIO[7] E0UC[7] LIN3TX — RXD[2] EIRQ[2] ADC1_S[1]|SIUL eMIOS_0 LINFlexD_3 — FEC SIUL ADC_1|I/O I/O O — I I I|M/S|Tristate|128|152|C15|
|PA[8]|PCR[8]|AF0 AF1 AF2 AF3 — — — —|GPIO[8] E0UC[8] E0UC[14] — RXD[1] EIRQ[3] ABS[0] LIN3RX|SIUL eMIOS_0 eMIOS_0 — FEC SIUL MC_RGM LINFlexD_3|I/O I/O I/O — I I I I|M/S|Input, weak pull-up|129|153|B16|
|PA[9]|PCR[9]|AF0 AF1 AF2 AF3 — —|GPIO[9] E0UC[9] — CS2_1 RXD[0] FAB|SIUL eMIOS_0 — DSPI1 FEC MC_RGM|I/O I/O — O I I|M/S|Pull- down|130|154|B15|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 21/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PA[10]|PCR[10]|AF0 AF1 AF2 AF3 — — —|GPIO[10] E0UC[10] SDA LIN2TX COL ADC1_S[2] SIN_1|SIUL eMIOS_0 I2C LINFlexD_2 FEC ADC_1 DSPI_1|I/O I/O I/O O I I I|M/S|Tristate|131|155|A15|
|PA[11]|PCR[11]|AF0 AF1 AF2 AF3 — — — —|GPIO[11] E0UC[11] SCL — RX_ER EIRQ[16] LIN2RX ADC1_S[3]|SIUL eMIOS_0 I2C — FEC SIUL LINFlexD_2 ADC_1|I/O I/O I/O — I I I I|M/S|Tristate|132|156|B14|
|PA[12]|PCR[12]|AF0 AF1 AF2 AF3 — —|GPIO[12] — E0UC[28] CS3_1 EIRQ[17] SIN_0|SIUL — eMIOS_0 DSPI1 SIUL DSPI_0|I/O — I/O O I I|S|Tristate|53|69|P6|
|PA[13]|PCR[13]|AF0 AF1 AF2 AF3|GPIO[13] SOUT_0 E0UC[29] —|SIUL DSPI_0 eMIOS_0 —|I/O O I/O —|M/S|Tristate|52|66|R5|
|PA[14]|PCR[14]|AF0 AF1 AF2 AF3 —|GPIO[14] SCK_0 CS0_0 E0UC[0] EIRQ[4]|SIUL DSPI_0 DSPI_0 eMIOS_0 SIUL|I/O I/O I/O I/O I|M/S|Tristate|50|58|P4|
|PA[15]|PCR[15]|AF0 AF1 AF2 AF3 —|GPIO[15] CS0_0 SCK_0 E0UC[1] WKPU[10]|SIUL DSPI_0 DSPI_0 eMIOS_0 WKPU|I/O I/O I/O I/O I|M/S|Tristate|48|56|R2|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

22/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PB[0]|PCR[16]|AF0 AF1 AF2 AF3|GPIO[16] CAN0TX E0UC[30] LIN0TX|SIUL FlexCAN_0 eMIOS_0 LINFlexD_0|I/O O I/O I|M/S|Tristate|39|39|L3|
|PB[1]|PCR[17]|AF0 AF1 AF2 — — —|GPIO[17] — E0UC[31] LIN0RX WKPU[4] CAN0RX|SIUL — eMIOS_0 LINFlexD_0 WKPU FlexCAN_0|I/O — I/O I I I|S|Tristate|40|40|M2|
|PB[2]|PCR[18]|AF0 AF1 AF2 AF3|GPIO[18] LIN0TX SDA E0UC[30]|SIUL LINFlexD_0 I2C eMIOS_0|I/O O I/O I/O|M/S|Tristate|176|208|A2|
|PB[3]|PCR[19]|AF0 AF1 AF2 AF3 — —|GPIO[19] E0UC[31] SCL — WKPU[11] LIN0RX|SIUL eMIOS_0 I2C — WKPU LINFlexD_0|I/O I/O I/O — I I|S|Tristate|1|1|D4|
|PB[4]|PCR[20]|AF0 AF1 AF2 AF3 — —|GPI[20] — — — ADC0_P[0] ADC1_P[0]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|88|104|T16|
|PB[5]|PCR[21]|AF0 AF1 AF2 AF3 — —|GPI[21] — — — ADC0_P[1] ADC1_P[1]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|91|107|N13|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 23/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PB[6]|PCR[22]|AF0 AF1 AF2 AF3 — —|GPI[22] — — — ADC0_P[2] ADC1_P[2]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|92|108|N14|
|PB[7]|PCR[23]|AF0 AF1 AF2 AF3 — —|GPI[23] — — — ADC0_P[3] ADC1_P[3]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|93|109|R16|
|PB[8]|PCR[24]|AF0 AF1 AF2 AF3 — — — —|GPI[24] — — — ADC0_S[0] ADC1_S[4] WKPU[25] OSC32k_XTAL(4)|SIUL — — — ADC_0 ADC_1 WKPU SXOSC|I — — — I I I I|I|—|61|77|T11|
|PB[9](5)|PCR[25]|AF0 AF1 AF2 AF3 — — — —|GPI[25] — — — ADC0_S[1] ADC1_S[5] WKPU[26] OSC32k_EXTAL( 4)|SIUL — — — ADC_0 ADC_1 WKPU SXOSC|I — — — I I I I|I|—|60|76|T10|
|PB[10]|PCR[26]|AF0 AF1 AF2 AF3 — — —|GPIO[26] SOUT_1 CAN3TX — ADC0_S[2] ADC1_S[6] WKPU[8]|SIUL DSPI_1 FlexCAN_3 — ADC_0 ADC_1 WKPU|I/O O — — I I I|S|Tristate|62|78|N7|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

24/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PB[11]|PCR[27]|AF0 AF1 AF2 AF3 —|GPIO[27] E0UC[3] — CS0_0 ADC0_S[3]|SIUL eMIOS_0 — DSPI_0 ADC_0|I/O I/O — I/O I|S|Tristate|97|117|M13|
|PB[12]|PCR[28]|AF0 AF1 AF2 AF3 —|GPIO[28] E0UC[4] — CS1_0 ADC0_X[0]|SIUL eMIOS_0 — DSPI_0 ADC_0|I/O I/O — O I|S|Tristate|101|123|L14|
|PB[13]|PCR[29]|AF0 AF1 AF2 AF3 —|GPIO[29] E0UC[5] — CS2_0 ADC0_X[1]|SIUL eMIOS_0 — DSPI_0 ADC_0|I/O I/O — O I|S|Tristate|103|125|L15|
|PB[14]|PCR[30]|AF0 AF1 AF2 AF3 —|GPIO[30] E0UC[6] — CS3_0 ADC0_X[2]|SIUL eMIOS_0 — DSPI_0 ADC_0|I/O I/O — O I|S|Tristate|105|127|K15|
|PB[15]|PCR[31]|AF0 AF1 AF2 AF3 —|GPIO[31] E0UC[7] — CS4_0 ADC0_X[3]|SIUL eMIOS_0 — DSPI_0 ADC_0|I/O I/O — O I|S|Tristate|107|129|K16|
|PC[0](6)|PCR[32]|AF0 AF1 AF2 AF3|GPIO[32] — TDI —|SIUL — JTAGC —|I/O — I —|M/S|Input, weak pull-up|154|178|B10|
|PC[1](6)|PCR[33]|AF0 AF1 AF2 AF3|GPIO[33] — TDO —|SIUL — JTAGC —|I/O — O —|F/M|Tristate|149|173|D9|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 25/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PC[2]|PCR[34]|AF0 AF1 AF2 AF3 —|GPIO[34] SCK_1 CAN4TX — EIRQ[5]|SIUL DSPI_1 FlexCAN_4 — SIUL|I/O I/O O — I|M/S|Tristate|145|169|B11|
|PC[3]|PCR[35]|AF0 AF1 AF2 AF3 — — —|GPIO[35] CS0_1 MA[0] — CAN1RX CAN4RX EIRQ[6]|SIUL DSPI_1 ADC_0 — FlexCAN_1 FlexCAN_4 SIUL|I/O I/O O I I I|S|Tristate|144|168|C11|
|PC[4]|PCR[36]|AF0 AF1 AF2 AF3 ALT4 — — —|GPIO[36] E1UC[31] — FR_B_TX_EN SIN_1 CAN3RX EIRQ[18]|SIUL eMIOS_1 — Flexray DSPI_1 FlexCAN_3 SIUL|I/O I/O — O I I I|M/S|Tristate|159|183|A9|
|PC[5]|PCR[37]|AF0 AF1 AF2 AF3 ALT4 —|GPIO[37] SOUT_1 CAN3TX — FR_A_TX EIRQ[7]|SIUL DSPI_1 FlexCAN_3 — Flexray SIUL|I/O O O — O I|M/S|Tristate|158|182|B9|
|PC[6]|PCR[38]|AF0 AF1 AF2 AF3|GPIO[38] LIN1TX E1UC[28] —|SIUL LINFlexD_1 eMIOS_1 —|I/O O I/O —|S|Tristate|44|52|N3|
|PC[7]|PCR[39]|AF0 AF1 AF2 AF3 — —|GPIO[39] — E1UC[29] — LIN1RX WKPU[12]|SIUL — eMIOS_1 — LINFlexD_1 WKPU|I/O — I/O — I I|S|Tristate|45|53|N4|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

26/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PC[8]|PCR[40]|AF0 AF1 AF2 AF3|GPIO[40] LIN2TX E0UC[3] —|SIUL LINFlexD_2 eMIOS_0 —|I/O O I/O —|S|Tristate|175|207|B3|
|PC[9]|PCR[41]|AF0 AF1 AF2 AF3 — —|GPIO[41] — E0UC[7] — LIN2RX WKPU[13]|SIUL — eMIOS_0 — LINFlexD_2 WKPU|I/O — I/O — I I|S|Tristate|2|2|C3|
|PC[10]|PCR[42]|AF0 AF1 AF2 AF3|GPIO[42] CAN1TX CAN4TX MA[1]|SIUL FlexCAN_1 FlexCAN_4 ADC_0|I/O O O O|M/S|Tristate|36|36|L1|
|PC[11]|PCR[43]|AF0 AF1 AF2 AF3 — — —|GPIO[43] — — MA[2] CAN1RX CAN4RX WKPU[5]|SIUL — — ADC_0 FlexCAN_1 FlexCAN_4 WKPU|I/O — — O I I I|S|Tristate|35|35|K4|
|PC[12]|PCR[44]|AF0 AF1 AF2 AF3 ALT4 — —|GPIO[44] E0UC[12] — — FR_DBG[0] SIN_2 EIRQ[19]|SIUL eMIOS_0 — — Flexray DSPI_2 SIUL|I/O I/O — — O I I|M/S|Tristate|173|205|B4|
|PC[13]|PCR[45]|AF0 AF1 AF2 AF3 ALT4|GPIO[45] E0UC[13] SOUT_2 — FR_DBG[1]|SIUL eMIOS_0 DSPI_2 — Flexray|I/O I/O O — O|M/S|Tristate|174|206|A3|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 27/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PC[14]|PCR[46]|AF0 AF1 AF2 AF3 ALT4 —|GPIO[46] E0UC[14] SCK_2 — FR_DBG[2] EIRQ[8]|SIUL eMIOS_0 DSPI_2 — Flexray SIUL|I/O I/O I/O — O I|M/S|Tristate|3|3|B2|
|PC[15]|PCR[47]|AF0 AF1 AF2 AF3 ALT4|GPIO[47] E0UC[15] CS0_2 — FR_DBG[3] EIRQ[20]|SIUL eMIOS_0 DSPI_2 — Flexray SIUL|I/O I/O I/O — O I|M/S|Tristate|4|4|A1|
|PD[0]|PCR[48]|AF0 AF1 AF2 AF3 — — —|GPI[48] — — — ADC0_P[4] ADC1_P[4] WKPU[27]|SIUL — — — ADC_0 ADC_1 WKPU|I — — — I I I|I|Tristate|77|93|R12|
|PD[1]|PCR[49]|AF0 AF1 AF2 AF3 — — —|GPI[49] — — — ADC0_P[5] ADC1_P[5] WKPU[28]|SIUL — — — ADC_0 ADC_1 WKPU|I — — — I I I|I|Tristate|78|94|T13|
|PD[2]|PCR[50]|AF0 AF1 AF2 AF3 — —|GPI[50] — — — ADC0_P[6] ADC1_P[6]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|79|95|N11|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

28/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PD[3]|PCR[51]|AF0 AF1 AF2 AF3 — —|GPI[51] — — — ADC0_P[7] ADC1_P[7]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|80|96|R13|
|PD[4]|PCR[52]|AF0 AF1 AF2 AF3 — —|GPI[52] — — — ADC0_P[8] ADC1_P[8]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|81|97|P12|
|PD[5]|PCR[53]|AF0 AF1 AF2 AF3 — —|GPI[53] — — — ADC0_P[9] ADC1_P[9]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|82|98|T14|
|PD[6]|PCR[54]|AF0 AF1 AF2 AF3 — —|GPI[54] — — — ADC0_P[10] ADC1_P[10]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|83|99|R14|
|PD[7]|PCR[55]|AF0 AF1 AF2 AF3 — —|GPI[55] — — — ADC0_P[11] ADC1_P[11]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|84|100|P13|
|PD[8]|PCR[56]|AF0 AF1 AF2 AF3 — —|GPI[56] — — — ADC0_P[12] ADC1_P[12]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|87|103|P14|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 29/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PD[9]|PCR[57]|AF0 AF1 AF2 AF3 — —|GPI[57] — — — ADC0_P[13] ADC1_P[13]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|94|114|N16|
|PD[10]|PCR[58]|AF0 AF1 AF2 AF3 — —|GPI[58] — — — ADC0_P[14] ADC1_P[14]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|95|115|M14|
|PD[11]|PCR[59]|AF0 AF1 AF2 AF3 — —|GPI[59] — — — ADC0_P[15] ADC1_P[15]|SIUL — — — ADC_0 ADC_1|I — — — I I|I|Tristate|96|116|M15|
|PD[12]|PCR[60]|AF0 AF1 AF2 AF3 —|GPIO[60] CS5_0 E0UC[24] — ADC0_S[4]|SIUL DSPI_0 eMIOS_0 — ADC_0|I/O O I/O — I|S|Tristate|100|120|L13|
|PD[13]|PCR[61]|AF0 AF1 AF2 AF3 —|GPIO[61] CS0_1 E0UC[25] — ADC0_S[5]|SIUL DSPI_1 eMIOS_0 — ADC_0|I/O I/O I/O — I|S|Tristate|102|124|K14|
|PD[14]|PCR[62]|AF0 AF1 AF2 AF3 ALT4 —|GPIO[62] CS1_1 E0UC[26] — FR_DBG[0] ADC0_S[6]|SIUL DSPI_1 eMIOS_0 — Flexray ADC_0|I/O O I/O — O I|S|Tristate|104|126|K13|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

30/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PD[15]|PCR[63]|AF0 AF1 AF2 AF3 ALT4 —|GPIO[63] CS2_1 E0UC[27] — FR_DBG[1] ADC0_S[7]|SIUL DSPI_1 eMIOS_0 — Flexray ADC_0|I/O O I/O — O I|S|Tristate|106|128|J13|
|PE[0]|PCR[64]|AF0 AF1 AF2 AF3 — —|GPIO[64] E0UC[16] — — CAN5RX WKPU[6]|SIUL eMIOS_0 — — FlexCAN_5 WKPU|I/O I/O — — I I|S|Tristate|18|18|G2|
|PE[1]|PCR[65]|AF0 AF1 AF2 AF3|GPIO[65] E0UC[17] CAN5TX —|SIUL eMIOS_0 FlexCAN_5 —|I/O I/O O —|M/S|Tristate|20|20|F4|
|PE[2]|PCR[66]|AF0 AF1 AF2 AF3 ALT4 — —|GPIO[66] E0UC[18] — — FR_A_TX_EN SIN_1 EIRQ[21]|SIUL eMIOS_0 — — Flexray DSPI_1 SIUL|I/O I/O — — O I I|M/S|Tristate|156|180|A7|
|PE[3]|PCR[67]|AF0 AF1 AF2 AF3 — —|GPIO[67] E0UC[19] SOUT_1 — FR_A_RX WKPU[29]|SIUL eMIOS_0 DSPI_1 — Flexray WKPU|I/O I/O O — I I|M/S|Tristate|157|181|A10|
|PE[4]|PCR[68]|AF0 AF1 AF2 AF3 ALT4 —|GPIO[68] E0UC[20] SCK_1 — FR_B_TX EIRQ[9]|SIUL eMIOS_0 DSPI_1 — Flexray SIUL|I/O I/O I/O — O I|M/S|Tristate|160|184|A8|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 31/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PE[5]|PCR[69]|AF0 AF1 AF2 AF3 — —|GPIO[69] E0UC[21] CS0_1 MA[2] FR_B_RX WKPU[30]|SIUL eMIOS_0 DSPI_1 ADC_0 Flexray WKPU|I/O I/O I/O O I I|M/S|Tristate|161|185|B8|
|PE[6]|PCR[70]|AF0 AF1 AF2 AF3 —|GPIO[70] E0UC[22] CS3_0 MA[1] EIRQ[22]|SIUL eMIOS_0 DSPI_0 ADC_0 SIUL|I/O I/O O O I|M/S|Tristate|167|191|B6|
|PE[7]|PCR[71]|AF0 AF1 AF2 AF3 —|GPIO[71] E0UC[23] CS2_0 MA[0] EIRQ[23]|SIUL eMIOS_0 DSPI_0 ADC_0 SIUL|I/O I/O O O I|M/S|Tristate|168|192|A5|
|PE[8]|PCR[72]|AF0 AF1 AF2 AF3|GPIO[72] CAN2TX E0UC[22] CAN3TX|SIUL FlexCAN_2 eMIOS_0 FlexCAN_3|I/O O I/O O|M/S|Tristate|21|21|G1|
|PE[9]|PCR[73]|AF0 AF1 AF2 AF3 — — —|GPIO[73] — E0UC[23] — WKPU[7] CAN2RX CAN3RX|SIUL — eMIOS_0 — WKPU FlexCAN_2 FlexCAN_3|I/O — I/O — I I I|S|Tristate|22|22|H1|
|PE[10]|PCR[74]|AF0 AF1 AF2 AF3 —|GPIO[74] LIN3TX CS3_1 E1UC[30] EIRQ[10]|SIUL LINFlexD_3 DSPI_1 eMIOS_1 SIUL|I/O O O I/O I|S|Tristate|23|23|G3|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

32/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PE[11]|PCR[75]|AF0 AF1 AF2 AF3 — —|GPIO[75] E0UC[24] CS4_1 — LIN3RX WKPU[14]|SIUL eMIOS_0 DSPI_1 — LINFlexD_3 WKPU|I/O I/O O — I I|S|Tristate|25|25|H3|
|PE[12]|PCR[76]|AF0 AF1 AF2 AF3 — — — —|GPIO[76] — E1UC[19] — CRS SIN_2 EIRQ[11] ADC1_S[7]|SIUL — eMIOS_1 — FEC DSPI_2 SIUL ADC_1|I/O — I/O — I I I I|M/S|Tristate|133|157|C14|
|PE[13]|PCR[77]|AF0 AF1 AF2 AF3 —|GPIO[77] SOUT_2 E1UC[20] — RXD[3]|SIUL DSPI_2 eMIOS_1 — FEC|I/O O I/O — I|M/S|Tristate|127|151|C16|
|PE[14]|PCR[78]|AF0 AF1 AF2 AF3 —|GPIO[78] SCK_2 E1UC[21] — EIRQ[12]|SIUL DSPI_2 eMIOS_1 — SIUL|I/O I/O I/O — I|M/S|Tristate|136|160|A14|
|PE[15]|PCR[79]|AF0 AF1 AF2 AF3|GPIO[79] CS0_2 E1UC[22] SCK_6|SIUL DSPI_2 eMIOS_1 DSPI_6|I/O I/O I/O I/O|M/S|Tristate|137|161|C12|
|PF[0]|PCR[80]|AF0 AF1 AF2 AF3 —|GPIO[80] E0UC[10] CS3_1 — ADC0_S[8]|SIUL eMIOS_0 DSPI_1 — ADC_0|I/O I/O O — I|S|Tristate|63|79|P7|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 33/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PF[1]|PCR[81]|AF0 AF1 AF2 AF3 —|GPIO[81] E0UC[11] CS4_1 — ADC0_S[9]|SIUL eMIOS_0 DSPI_1 — ADC_0|I/O I/O O — I|S|Tristate|64|80|T6|
|PF[2]|PCR[82]|AF0 AF1 AF2 AF3 —|GPIO[82] E0UC[12] CS0_2 — ADC0_S[10]|SIUL eMIOS_0 DSPI_2 — ADC_0|I/O I/O I/O — I|S|Tristate|65|81|R6|
|PF[3]|PCR[83]|AF0 AF1 AF2 AF3 —|GPIO[83] E0UC[13] CS1_2 — ADC0_S[11]|SIUL eMIOS_0 DSPI_2 — ADC_0|I/O I/O O — I|S|Tristate|66|82|R7|
|PF[4]|PCR[84]|AF0 AF1 AF2 AF3 —|GPIO[84] E0UC[14] CS2_2 — ADC0_S[12]|SIUL eMIOS_0 DSPI_2 — ADC_0|I/O I/O O — I|S|Tristate|67|83|R8|
|PF[5]|PCR[85]|AF0 AF1 AF2 AF3 —|GPIO[85] E0UC[22] CS3_2 — ADC0_S[13]|SIUL eMIOS_0 DSPI_2 — ADC_0|I/O I/O O — I|S|Tristate|68|84|P8|
|PF[6]|PCR[86]|AF0 AF1 AF2 AF3 —|GPIO[86] E0UC[23] CS1_1 — ADC0_S[14]|SIUL eMIOS_0 DSPI_1 — ADC_0|I/O I/O O — I|S|Tristate|69|85|N8|
|PF[7]|PCR[87]|AF0 AF1 AF2 AF3 —|GPIO[87] — CS2_1 — ADC0_S[15]|SIUL — DSPI_1 — ADC_0|I/O — O — I|S|Tristate|70|86|P9|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

34/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PF[8]|PCR[88]|AF0 AF1 AF2 AF3|GPIO[88] CAN3TX CS4_0 CAN2TX|SIUL FlexCAN_3 DSPI_0 FlexCAN_2|I/O O O O|M/S|Tristate|42|50|N2|
|PF[9]|PCR[89]|AF0 AF1 AF2 AF3 — — —|GPIO[89] E1UC[1] CS5_0 — CAN2RX CAN3RX WKPU[22]|SIUL eMIOS_1 DSPI_0 — FlexCAN_2 FlexCAN_3 WKPU|I/O I/O O — I I I|S|Tristate|41|49|M4|
|PF[10]|PCR[90]|AF0 AF1 AF2 AF3|GPIO[90] CS1_0 LIN4TX E1UC[2]|SIUL DSPI_0 LINFlexD_4 eMIOS_1|I/O O O I/O|M/S|Tristate|46|54|P2|
|PF[11]|PCR[91]|AF0 AF1 AF2 AF3 — —|GPIO[91] CS2_0 E1UC[3] — LIN4RX WKPU[15]|SIUL DSPI_0 eMIOS_1 — LINFlexD_4 WKPU|I/O O I/O — I I|S|Tristate|47|55|R1|
|PF[12]|PCR[92]|AF0 AF1 AF2 AF3|GPIO[92] E1UC[25] LIN5TX —|SIUL eMIOS_1 LINFlexD_5 —|I/O I/O O —|M/S|Tristate|43|51|P1|
|PF[13]|PCR[93]|AF0 AF1 AF2 AF3 — —|GPIO[93] E1UC[26] — — LIN5RX WKPU[16]|SIUL eMIOS_1 — — LINFlexD_5 WKPU|I/O I/O — — I I|S|Tristate|49|57|P3|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 35/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PF[14]|PCR[94]|AF0 AF1 AF2 AF3 ALT4|GPIO[94] CAN4TX E1UC[27] CAN1TX MDIO|SIUL FlexCAN_4 eMIOS_1 FlexCAN_1 FEC|I/O O I/O O I/O|M/S|Tristate|126|150|D14|
|PF[15]|PCR[95]|AF0 AF1 AF2 AF3 — — — —|GPIO[95] E1UC[4] — — RX_DV CAN1RX CAN4RX EIRQ[13]|SIUL eMIOS_1 — — FEC FlexCAN_1 FlexCAN_4 SIUL|I/O I/O — — I I I I|M/S|Tristate|125|149|D15|
|PG[0]|PCR[96]|AF0 AF1 AF2 AF3 ALT4|GPIO[96] CAN5TX E1UC[23] — MDC|SIUL FlexCAN_5 eMIOS_1 — FEC|I/O O I/O — O|F|Tristate|122|146|E13|
|PG[1]|PCR[97]|AF0 AF1 AF2 AF3 — — —|GPIO[97] — E1UC[24] — TX_CLK CAN5RX EIRQ[14]|SIUL — eMIOS_1 — FEC FlexCAN_5 SIUL|I/O — I/O — I I I|M|Tristate|121|145|E14|
|PG[2]|PCR[98]|AF0 AF1 AF2 AF3|GPIO[98] E1UC[11] SOUT_3 —|SIUL eMIOS_1 DSPI_3 —|I/O I/O O —|M/S|Tristate|16|16|E4|
|PG[3]|PCR[99]|AF0 AF1 AF2 AF3 —|GPIO[99] E1UC[12] CS0_3 — WKPU[17]|SIUL eMIOS_1 DSPI_3 — WKPU|I/O I/O I/O — I|S|Tristate|15|15|E1|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

36/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PG[4]|PCR[100]|AF0 AF1 AF2 AF3|GPIO[100] E1UC[13] SCK_3 —|SIUL eMIOS_1 DSPI_3 —|I/O I/O I/O —|M/S|Tristate|14|14|F2|
|PG[5]|PCR[101]|AF0 AF1 AF2 AF3 — —|GPIO[101] E1UC[14] — — WKPU[18] SIN_3|SIUL eMIOS_1 — — WKPU DSPI_3|I/O I/O — — I I|S|Tristate|13|13|D1|
|PG[6]|PCR[102]|AF0 AF1 AF2 AF3|GPIO[102] E1UC[15] LIN6TX —|SIUL eMIOS_1 LINFlexD_6 —|I/O I/O O —|M/S|Tristate|38|38|M1|
|PG[7]|PCR[103]|AF0 AF1 AF2 AF3 — —|GPIO[103] E1UC[16] E1UC[30] — LIN6RX WKPU[20]|SIUL eMIOS_1 eMIOS_1 — LINFlexD_6 WKPU|I/O I/O I/O — I I|S|Tristate|37|37|L2|
|PG[8]|PCR[104]|AF0 AF1 AF2 AF3 —|GPIO[104] E1UC[17] LIN7TX CS0_2 EIRQ[15]|SIUL eMIOS_1 LINFlexD_7 DSPI_2 SIUL|I/O I/O O I/O I|S|Tristate|34|34|K3|
|PG[9]|PCR[105]|AF0 AF1 AF2 AF3 — —|GPIO[105] E1UC[18] — SCK_2 LIN7RX WKPU[21]|SIUL eMIOS_1 — DSPI_2 LINFlexD_7 WKPU|I/O I/O — I/O I I|S|Tristate|33|33|J4|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 37/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PG[10]|PCR[106]|AF0 AF1 AF2 AF3 —|GPIO[106] E0UC[24] E1UC[31] — SIN_4|SIUL eMIOS_0 eMIOS_1 — DSPI_4|I/O I/O I/O — I|S|Tristate|138|162|B13|
|PG[11]|PCR[107]|AF0 AF1 AF2 AF3|GPIO[107] E0UC[25] CS0_4 CS0_6|SIUL eMIOS_0 DSPI_4 DSPI_6|I/O I/O I/O I/O|M/S|Tristate|139|163|A16|
|PG[12]|PCR[108]|AF0 AF1 AF2 AF3 ALT4|GPIO[108] E0UC[26] SOUT_4 — TXD[2]|SIUL eMIOS_0 DSPI_4 — FEC|I/O I/O O — O|M/S|Tristate|116|140|F15|
|PG[13]|PCR[109]|AF0 AF1 AF2 AF3 ALT4|GPIO[109] E0UC[27] SCK_4 — TXD[3]|SIUL eMIOS_0 DSPI_4 — FEC|I/O I/O I/O — O|M/S|Tristate|115|139|F16|
|PG[14]|PCR[110]|AF0 AF1 AF2 AF3 —|GPIO[110] E1UC[0] LIN8TX — SIN_6|SIUL eMIOS_1 LINFlexD_8 — DSPI_6|I/O I/O O — I|S|Tristate|134|158|C13|
|PG[15]|PCR[111]|AF0 AF1 AF2 AF3 —|GPIO[111] E1UC[1] SOUT_6 — LIN8RX|SIUL eMIOS_1 DSPI_6 — LINFlexD_8|I/O I/O O — I|M/S|Tristate|135|159|D13|
|PH[0]|PCR[112]|AF0 AF1 AF2 AF3 ALT4 —|GPIO[112] E1UC[2] — — TXD[1] SIN_1|SIUL eMIOS_1 — — FEC DSPI_1|I/O I/O — — O I|M/S|Tristate|117|141|E15|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

38/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PH[1]|PCR[113]|AF0 AF1 AF2 AF3 ALT4|GPIO[113] E1UC[3] SOUT_1 — TXD[0]|SIUL eMIOS_1 DSPI_1 — FEC|I/O I/O O — O|M/S|Tristate|118|142|F13|
|PH[2]|PCR[114]|AF0 AF1 AF2 AF3 ALT4|GPIO[114] E1UC[4] SCK_1 — TX_EN|SIUL eMIOS_1 DSPI_1 — FEC|I/O I/O I/O — O|M/S|Tristate|119|143|D16|
|PH[3]|PCR[115]|AF0 AF1 AF2 AF3 ALT4|GPIO[115] E1UC[5] CS0_1 — TX_ER|SIUL eMIOS_1 DSPI_1 — FEC|I/O I/O I/O — O|M/S|Tristate|120|144|F14|
|PH[4]|PCR[116]|AF0 AF1 AF2 AF3|GPIO[116] E1UC[6] SOUT_7 —|SIUL eMIOS_1 DSPI_7 —|I/O I/O O —|M/S|Tristate|162|186|D7|
|PH[5]|PCR[117]|AF0 AF1 AF2 AF3 —|GPIO[117] E1UC[7] — — SIN_7|SIUL eMIOS_1 — — DSPI_7|I/O I/O — — I|S|Tristate|163|187|B7|
|PH[6]|PCR[118]|AF0 AF1 AF2 AF3|GPIO[118] E1UC[8] SCK_7 MA[2]|SIUL eMIOS_1 DSPI_7 ADC_0|I/O I/O I/O O|M/S|Tristate|164|188|C7|
|PH[7]|PCR[119]|AF0 AF1 AF2 AF3 ALT4|GPIO[119] E1UC[9] CS3_2 MA[1] CS0_7|SIUL eMIOS_1 DSPI_2 ADC_0 DSPI_7|I/O I/O O O I/O|M/S|Tristate|165|189|C6|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 39/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PH[8]|PCR[120]|AF0 AF1 AF2 AF3|GPIO[120] E1UC[10] CS2_2 MA[0]|SIUL eMIOS_1 DSPI_2 ADC_0|I/O I/O O O|M/S|Tristate|166|190|A6|
|PH[9](6)|PCR[121]|AF0 AF1 AF2 AF3 —|GPIO[121] — — — TCK|SIUL — — — JTAGC|I/O — — — I|S|Input, weak pull-up|155|179|A11|
|PH[10](6)|PCR[122]|AF0 AF1 AF2 AF3 —|GPIO[122] — — — TMS|SIUL — — — JTAGC|I/O — — — I|M/S|Input, weak pull-up|148|172|D10|
|PH[11]|PCR[123]|AF0 AF1 AF2 AF3|GPIO[123] SOUT_3 CS0_4 E1UC[5]|SIUL DSPI_3 DSPI_4 eMIOS_1|I/O O I/O I/O|M/S|Tristate|140|164|A13|
|PH[12]|PCR[124]|AF0 AF1 AF2 AF3|GPIO[124] SCK_3 CS1_4 E1UC[25]|SIUL DSPI_3 DSPI_4 eMIOS_1|I/O I/O O I/O|M/S|Tristate|141|165|B12|
|PH[13]|PCR[125]|AF0 AF1 AF2 AF3|GPIO[125] SOUT_4 CS0_3 E1UC[26]|SIUL DSPI_4 DSPI_3 eMIOS_1|I/O O I/O I/O|M/S|Tristate|9|9|B1|
|PH[14]|PCR[126]|AF0 AF1 AF2 AF3|GPIO[126] SCK_4 CS1_3 E1UC[27]|SIUL DSPI_4 DSPI_3 eMIOS_1|I/O I/O O I/O|M/S|Tristate|10|10|C1|
|PH[15]|PCR[127]|AF0 AF1 AF2 AF3|GPIO[127] SOUT_5 — E1UC[17]|SIUL DSPI_5 — eMIOS_1|I/O O — I/O|M/S|Tristate|8|8|E3|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

40/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PI[0]|PCR[128]|AF0 AF1 AF2 AF3|GPIO[128] E0UC[28] LIN8TX —|SIUL eMIOS_0 LINFlexD_8 —|I/O I/O O —|S|Tristate|172|196|C5|
|PI[1]|PCR[129]|AF0 AF1 AF2 AF3 — —|GPIO[129] E0UC[29] — — WKPU[24] LIN8RX|SIUL eMIOS_0 — — WKPU LINFlexD_8|I/O I/O — — I I|S|Tristate|171|195|A4|
|PI[2]|PCR[130]|AF0 AF1 AF2 AF3|GPIO[130] E0UC[30] LIN9TX —|SIUL eMIOS_0 LINFlexD_9 —|I/O I/O O —|S|Tristate|170|194|D6|
|PI[3]|PCR[131]|AF0 AF1 AF2 AF3 — —|GPIO[131] E0UC[31] — — WKPU[23] LIN9RX|SIUL eMIOS_0 — — WKPU LINFlexD_9|I/O I/O — — I I|S|Tristate|169|193|B5|
|PI[4]|PCR[132]|AF0 AF1 AF2 AF3|GPIO[132] E1UC[28] SOUT_4 —|SIUL eMIOS_1 DSPI_4 —|I/O I/O O —|M/S|Tristate|143|167|A12|
|PI[5]|PCR[133]|AF0 AF1 AF2 AF3 ALT4|GPIO[133] E1UC[29] SCK_4 CS2_5 CS2_6|SIUL eMIOS_1 DSPI_4 DSPI_5 DSPI_6|I/O I/O I/O O O|M/S|Tristate|142|166|D12|
|PI[6]|PCR[134]|AF0 AF1 AF2 AF3 ALT4|GPIO[134] E1UC[30] CS0_4 CS0_5 CS0_6|SIUL eMIOS_1 DSPI_4 DSPI_5 DSPI_6|I/O I/O I/O I/O I/O|S|Tristate|11|11|D2|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 41/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PI[7]|PCR[135]|AF0 AF1 AF2 AF3 ALT4|GPIO[135] E1UC[31] CS1_4 CS1_5 CS1_6|SIUL eMIOS_1 DSPI_4 DSPI_5 DSPI_6|I/O I/O O O O|S|Tristate|12|12|E2|
|PI[8]|PCR[136]|AF0 AF1 AF2 AF3 —|GPIO[136] — — — ADC0_S[16]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|108|130|J14|
|PI[9]|PCR[137]|AF0 AF1 AF2 AF3 —|GPIO[137] — — — ADC0_S[17]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|—|131|J15|
|PI[10]|PCR[138]|AF0 AF1 AF2 AF3 —|GPIO[138] — — — ADC0_S[18]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|—|134|J16|
|PI[11]|PCR[139]|AF0 AF1 AF2 AF3 — —|GPIO[139] — — — ADC0_S[19] SIN_3|SIUL — — — ADC_0 DSPI_3|I/O — — — I I|S|Tristate|111|135|H16|
|PI[12]|PCR[140]|AF0 AF1 AF2 AF3 —|GPIO[140] CS0_3 CS0_2 — ADC0_S[20]|SIUL DSPI_3 DSPI_2 — ADC_0|I/O I/O I/O — I|S|Tristate|112|136|G15|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

42/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PI[13]|PCR[141]|AF0 AF1 AF2 AF3 —|GPIO[141] CS1_3 CS1_2 — ADC0_S[21]|SIUL DSPI_3 DSPI_2 — ADC_0|I/O O O — I|S|Tristate|113|137|G14|
|PI[14]|PCR[142]|AF0 AF1 AF2 AF3 — —|GPIO[142] — — — ADC0_S[22] SIN_4|SIUL — — — ADC_0 DSPI_4|I/O — — — I I|S|Tristate|76|92|T12|
|PI[15]|PCR[143]|AF0 AF1 AF2 AF3 —|GPIO[143] CS0_4 CS2_2 — ADC0_S[23]|SIUL DSPI_4 DSPI_2 — ADC_0|I/O I/O O — I|S|Tristate|75|91|P11|
|PJ[0]|PCR[144]|AF0 AF1 AF2 AF3 —|GPIO[144] CS1_4 CS3_2 — ADC0_S[24]|SIUL DSPI_4 DSPI_2 — ADC_0|I/O O O — I|S|Tristate|74|90|R11|
|PJ[1]|PCR[145]|AF0 AF1 AF2 AF3 — —|GPIO[145] — — — ADC0_S[25] SIN_5|SIUL — — —— ADC_0 DSPI_5|I/O — — — I I|S|Tristate|73|89|N10|
|PJ[2]|PCR[146]|AF0 AF1 AF2 AF3 —|GPIO[146] CS0_5 CS0_6 CS0_7 ADC0_S[26]|SIUL DSPI_5 DSPI_6 DSPI_7 ADC_0|I/O I/O I/O I/O I|S|Tristate|72|88|R10|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 43/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PJ[3]|PCR[147]|AF0 AF1 AF2 AF3 —|GPIO[147] CS1_5 CS1_6 CS1_7 ADC0_S[27]|SIUL DSPI_5 DSPI_6 DSPI_7 ADC_0|I/O O O O I|S|Tristate|71|87|P10|
|PJ[4]|PCR[148]|AF0 AF1 AF2 AF3|GPIO[148] SCK_5 E1UC[18] —|SIUL DSPI_5 eMIOS_1 —|I/O I/O I/O —|M/S|Tristate|5|5|D3|
|PJ[5]|PCR[149]|AF0 AF1 AF2 AF3 —|GPIO[149] — — — ADC0_S[28]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|—|113|N12|
|PJ[6]|PCR[150]|AF0 AF1 AF2 AF3 —|GPIO[150] — — — ADC0_S[29]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|—|112|N15|
|PJ[7]|PCR[151]|AF0 AF1 AF2 AF3 —|GPIO[151] — — — ADC0_S[30]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|—|111|P16|
|PJ[8]|PCR[152]|AF0 AF1 AF2 AF3 —|GPIO[152] — — — ADC0_S[31]|SIUL — — — ADC_0|I/O — — — I|S|Tristate|—|110|P15|
|PJ[9]|PCR[153]|AF0 AF1 AF2 AF3 —|GPIO[153] — — — ADC1_S[8]|SIUL — — — ADC_1|I/O — — — I|S|Tristate|—|68|P5|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

44/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PJ[10]|PCR[154]|AF0 AF1 AF2 AF3 —|GPIO[154] — — — ADC1_S[9]|SIUL — — — ADC_1|I/O — — — I|S|Tristate|—|67|T5|
|PJ[11]|PCR[155]|AF0 AF1 AF2 AF3 —|GPIO[155] — — — ADC1_S[10]|SIUL — — — ADC_1|I/O — — — I|S|Tristate|—|60|R3|
|PJ[12]|PCR[156]|AF0 AF1 AF2 AF3 —|GPIO[156] — — — ADC1_S[11]|SIUL — — — ADC_1|I/O — — — I|S|Tristate|—|59|T1|
|PJ[13]|PCR[157]|AF0 AF1 AF2 AF3 — — — —|GPIO[157] — CS1_7 — CAN4RX ADC1_S[12] CAN1RX WKPU[31]|SIUL — DSPI_7 — FlexCAN_4 ADC_1 FlexCAN_1 WKPU|I/O — O — I I I I|S|Tristate|—|65|N5|
|PJ[14]|PCR[158]|AF0 AF1 AF2 AF3|GPIO[158] CAN1TX CAN4TX CS2_7|SIUL FlexCAN_1 FlexCAN_4 DSPI_7|I/O O O O|M/S|Tristate|—|64|T4|
|PJ[15]|PCR[159]|AF0 AF1 AF2 AF3 —|GPIO[159] — CS1_6 — CAN1RX|SIUL — DSPI_6 — FlexCAN_1|I/O — O — I|M/S|Tristate|—|63|R4|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 45/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PK[0]|PCR[160]|AF0 AF1 AF2 AF3|GPIO[160] CAN1TX CS2_6 —|SIUL FlexCAN_1 DSPI_6 —|I/O O O —|M/S|Tristate|—|62|T3|
|PK[1]|PCR[161]|AF0 AF1 AF2 AF3 —|GPIO[161] CS3_6 — — CAN4RX|SIUL DSPI_6 — — FlexCAN_4|I/O O — — I|M/S|Tristate|—|41|H4|
|PK[2]|PCR[162]|AF0 AF1 AF2 AF3|GPIO[162] CAN4TX — —|SIUL FlexCAN_4 — —|I/O O — —|M/S|Tristate|—|42|L4|
|PK[3]|PCR[163]|AF0 AF1 AF2 AF3 — —|GPIO[163] E1UC[0] — — CAN5RX LIN8RX|SIUL eMIOS_1 — — FlexCAN_5 LINFlexD_8|I/O I/O — — I I|M/S|Tristate|—|43|N1|
|PK[4]|PCR[164]|AF0 AF1 AF2 AF3|GPIO[164] LIN8TX CAN5TX E1UC[1]|SIUL LINFlexD_8 FlexCAN_5 eMIOS_1|I/O O O I/O|M/S|Tristate|—|44|M3|
|PK[5]|PCR[165]|AF0 AF1 AF2 AF3 — —|GPIO[165] — — — CAN2RX LIN2RX|SIUL — — — FlexCAN_2 LINFlexD_2|I/O — — — I I|M/S|Tristate|—|45|M5|
|PK[6]|PCR[166]|AF0 AF1 AF2 AF3|GPIO[166] CAN2TX LIN2TX —|SIUL FlexCAN_2 LINFlexD_2 —|I/O O O —|M/S|Tristate|—|46|M6|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

46/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PK[7]|PCR[167]|AF0 AF1 AF2 AF3 — —|GPIO[167] — — — CAN3RX LIN3RX|SIUL — — — FlexCAN_3 LINFlexD_3|I/O — — — I I|M/S|Tristate|—|47|M7|
|PK[8]|PCR[168]|AF0 AF1 AF2 AF3|GPIO[168] CAN3TX LIN3TX —|SIUL FlexCAN_3 LINFlexD_3 —|I/O O O —|M/S|Tristate|—|48|M8|
|PK[9]|PCR[169]|AF0 AF1 AF2 AF3 —|GPIO[169] — — — SIN_4|SIUL — — — DSPI_4|I/O — — — I|M/S|Tristate|—|197|E8|
|PK[10]|PCR[170]|AF0 AF1 AF2 AF3|GPIO[170] SOUT_4 — —|SIUL DSPI_4 — —|I/O O — —|M/S|Tristate|—|198|E7|
|PK[11]|PCR[171]|AF0 AF1 AF2 AF3|GPIO[171] SCK_4 — —|SIUL DSPI_4 — —|I/O I/O — —|M/S|Tristate|—|199|F8|
|PK[12]|PCR[172]|AF0 AF1 AF2 AF3|GPIO[172] CS0_4 — —|SIUL DSPI_4 — —|I/O I/O — —|M/S|Tristate|—|200|G12|
|PK[13]|PCR[173]|AF0 AF1 AF2 AF3 —|GPIO[173] CS3_6 CS2_7 SCK_1 CAN3RX|SIUL DSPI_6 DSPI_7 DSPI_1 FlexCAN_3|I/O O O I/O I|M/S|Tristate|—|201|H12|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 47/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PK[14]|PCR[174]|AF0 AF1 AF2 AF3|GPIO[174] CAN3TX CS3_7 CS0_1|SIUL FlexCAN_3 DSPI_7 DSPI_1|I/O O O I/O|M/S|Tristate|—|202|J12|
|PK[15]|PCR[175]|AF0 AF1 AF2 AF3 — —|GPIO[175] — — — SIN_1 SIN_7|SIUL — — — DSPI_1 DSPI_7|I/O — — — I I|M/S|Tristate|—|203|D5|
|PL[0]|PCR[176]|AF0 AF1 AF2 AF3|GPIO[176] SOUT_1 SOUT_7 —|SIUL DSPI_1 DSPI_7 —|I/O O O —|M/S|Tristate|—|204|C4|
|PL[1]|PCR[177]|AF0 AF1 AF2 AF3|GPIO[177] — — —|SIUL — — —|I/O — — —|M/S|Tristate|—|—|F7|
|PL[2]|PCR[178] (7)|AF0 AF1 AF2 AF3|GPIO[178] — MDO0(8) —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|F5|
|PL[3]|PCR[179]|AF0 AF1 AF2 AF3|GPIO[179] — MDO1 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|G5|
|PL[4]|PCR[180]|AF0 AF1 AF2 AF3|GPIO[180] — MDO2 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|H5|
|PL[5]|PCR[181]|AF0 AF1 AF2 AF3|GPIO[181] — MDO3 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|J5|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

48/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PL[6]|PCR[182]|AF0 AF1 AF2 AF3|GPIO[182] — MDO4 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|K5|
|PL[7]|PCR[183]|AF0 AF1 AF2 AF3|GPIO[183] — MDO5 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|L5|
|PL[8]|PCR[184]|AF0 AF1 AF2 AF3 —|GPIO[184] — — — EVTI|SIUL — — — Nexus|I/O — — — I|S|Pull-up|—|—|M9|
|PL[9]|PCR[185]|AF0 AF1 AF2 AF3|GPIO[185] — MSEO —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|M10|
|PL[10]|PCR[186]|AF0 AF1 AF2 AF3|GPIO[186] — MCKO —|SIUL — Nexus —|I/O — O —|F/S|Tristate|—|—|M11|
|PL[11]|PCR[187]|AF0 AF1 AF2 AF3|GPIO[187] — — —|SIUL — — —|I/O — — —|M/S|Tristate|—|—|M12|
|PL[12]|PCR[188]|AF0 AF1 AF2 AF3|GPIO[188] — EVTO —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|F11|
|PL[13]|PCR[189]|AF0 AF1 AF2 AF3|GPIO[189] — MDO6 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|F10|


-----

###### **SPC564Bxx-SPC56ECxx Package pinouts and signal descriptions** **Table 5. Functional p ort p in descri p tions ( continued )**

DocID17478 Rev 9 49/123

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PL[14]|PCR[190]|AF0 AF1 AF2 AF3|GPIO[190] — MDO7 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|E12|
|PL[15]|PCR[191]|AF0 AF1 AF2 AF3|GPIO[191] — MDO8 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|E11|
|PM[0]|PCR[192]|AF0 AF1 AF2 AF3|GPIO[192] — MDO9 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|E10|
|PM[1]|PCR[193]|AF0 AF1 AF2 AF3|GPIO[193] — MDO10 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|E9|
|PM[2]|PCR[194]|AF0 AF1 AF2 AF3|GPIO[194] — MDO11 —|SIUL — Nexus —|I/O — O —|M/S|Tristate|—|—|F12|
|PM[3]|PCR[195]|AF0 AF1 AF2 AF3|GPIO[195] — — —|SIUL — — —|I/O — — —|M/S|Tristate|—|—|K12|
|PM[4]|PCR[196]|AF0 AF1 AF2 AF3|GPIO[196] — — —|SIUL — — —|I/O — — —|M/S|Tristate|—|—|L12|


122


-----

###### **Package pinouts and signal descriptions SPC564Bxx-SPC56ECxx** **Table 5. Functional p ort p in descri p tions ( continued )**

1. Alternate functions are chosen by setting the values of the PCR.PA bitfields inside the SIUL module. PCR.PA =
000  AF0; PCR.PA = 001 AF1; PCR.PA = 010 AF2; PCR.PA = 011  AF3; PCR.PA = 100  ALT4. This is
intended to select the output functions; to use one of the input functions, the PCR.IBE bit must be written to ‘1’, regardless
of the values selected in the PCR.PA bitfields. For this reason, the value corresponding to an input only function is reported
as “—”.

2. Multiple inputs are routed to all respective modules internally. The input of some modules must be configured by setting the
values of the PSMIO.PADSELx bitfields inside the SIUL module.

3. NMI[0] and NMI[1] have a higher priority than alternate functions. When NMI is selected, the PCR.PA field is ignored.

4. SXOSC’s OSC32k_XTAL and OSC32k_EXTAL pins are shared with GPIO functionality. When used as crystal pins, other
functionality of the pin cannot be used and it should be ensured that application never programs OBE and PUE bit of the
corresponding PCR to "1".

5. If you want to use OSC32K functionality through PB[8] and PB[9], you must ensure that PB[10] is static in nature as PB[10]
can induce coupling on PB[9] and disturb oscillator frequency.

6. Out of reset all the functional pins except PC[0:1] and PH[9:10] are available to the user as GPIO.
PC[0:1] are available as JTAG pins (TDI and TDO respectively).
PH[9:10] are available as JTAG pins (TCK and TMS respectively).
It is up to the user to configure these pins as GPIO when needed.

7. When MBIST is enabled to run (STCU Enable = 1), the application must not drive or tie PAD[178) (MDO[0]) to 0 V before
the device exits reset (external reset is removed) as the pad is internally driven to 1 to indicate MBIST operation. When
MBIST is not enabled (STCU Enable = 0), there are no restriction as the device does not internally drive the pad.

8. These pins can be configured as Nexus pins during reset by the debugger writing to the Nexus Development Interface
"Port Control Register" rather than the SIUL. Specifically, the debugger can enable the MDO[7:0], MSEO, and MCKO ports
by programming NDI (PCR[MCKO_EN] or PCR[PSTAT_EN]). MDO[8:11] ports can be enabled by programming NDI
((PCR[MCKO_EN] and PCR[FPM]) or PCR[PSTAT_EN]).

50/123 DocID17478 Rev 9

|Port pin|PCR|Alternate function(1)|Function|Peripheral|I/O direction(2)|Pad type|RESET config.|Pin number|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||LQFP 176|LQFP 208|LBGA256|
|PM[5]|PCR[197]|AF0 AF1 AF2 AF3|GPIO[197] — — —|SIUL — — —|I/O — — —|M/S|Tristate|—|—|F9|
|PM[6]|PCR[198]|AF0 AF1 AF2 AF3|GPIO[198] — — —|SIUL — — —|I/O — — —|M/S|Tristate|—|—|F6|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**
### **3 Electrical Characteristics**
###### This section contains electrical characteristics of the device as well as temperature and power considerations. This product contains devices to protect the inputs against damage due to high static voltages. However, it is advisable to take precautions to avoid application of any voltage higher than the specified maximum rated voltages. To enhance reliability, unused inputs can be driven to an appropriate logic voltage level (V DD or V SS_HV ). This could be done by the internal pull-up and pull-down, which is provided by the product for most general purpose pins. The parameters listed in the following tables represent the characteristics of the device and its demands on the system. In the tables where the device logic provides signals with their respective timing characteristics, the symbol “CC” for Controller Characteristics is included in the Symbol column. In the tables where the external system must provide signals with their respective timing characteristics to the device, the symbol “SR” for System Requirement is included in the Symbol column.
##### **3.1 Parameter classification**
###### The electrical parameters shown in this supplement are guaranteed by various methods. To give the customer a better understanding, the classifications listed in Table 6 are used and the parameters are tagged accordingly in the tables where appropriate. *Note: The classification is shown in the column labeled “C” in the parameter tables where * *appropriate.*
##### **3.2 NVUSRO register**
###### Portions of the device configuration, such as high voltage supply is controlled via bit values in the Non-Volatile User Options Register (NVUSRO). For a detailed description of the NVUSRO register, see SPC564Bxx and SPC56ECxx Reference Manual.

DocID17478 Rev 9 51/123

|Col1|Table 6. Parameter classifications|
|---|---|
|Classification tag|Tag description|
|P|Those parameters are guaranteed during production testing on each individual device.|
|C|Those parameters are achieved by the design characterization by measuring a statistically relevant sample size across process variations.|
|T|Those parameters are achieved by design characterization on a small sample size from typical devices under typical conditions unless otherwise noted. All values shown in the typical column are within this category.|
|D|Those parameters are derived mainly from simulations.|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **3.2.1 NVUSRO [PAD3V5V(0)] field description** Table 7 shows how NVUSRO [PAD3V5V(0)] controls the device configuration for V DD_HV_A domain. **Table 7. PAD3V5V ( 0 ) field descri p tion**

1. '1' is delivery value. It is part of shadow flash memory, thus programmable by customer. The DC electrical characteristics are dependent on the PAD3V5V(0,1) bit value. **3.2.2 NVUSRO [PAD3V5V(1)] field description** Table 8 shows how NVUSRO [PAD3V5V(1)] controls the device configuration the device configuration for V DD_HV_B domain. **Table 8. PAD3V5V ( 1 ) field descri p tion**

1. '1' is delivery value. It is part of shadow flash memory, thus programmable by customer. The DC electrical characteristics are dependent on the PAD3V5V(0,1) bit value.
##### **3.3 Absolute maximum ratings**
###### **Table 9. Absolute maximum ratin g s **

52/123 DocID17478 Rev 9

|Value(1)|Description|
|---|---|
|0|High voltage supply is 5.0 V|
|1|High voltage supply is 3.3 V|

|Value(1)|Description|
|---|---|
|0|High voltage supply is 5.0 V|
|1|High voltage supply is 3.3 V|

|Symbol|Col2|Parameter|Conditions|Value|Col6|Unit|
|---|---|---|---|---|---|---|
|||||Min|Max||
|V SS_HV|S R|Digital ground on VSS_HV pins|—|0|0|V|
|V DD_HV_A|S R|Voltage on VDD_HV_A pins with respect to ground (V ) SS_HV|—|–0.3|6.0|V|
|V (1) DD_HV_B|S R|Voltage on VDD_HV_B pins with respect to common ground (V ) SS_HV|—|–0.3|6.0|V|
|V SS_LV|S R|Voltage on VSS_LV (low voltage digital supply) pins with respect to ground (V ) SS_HV|—|V 0.1 SS_HV|V 0.1 SS_HV|V|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 9. Absolute maximum ratin g s ( continued )**

1. V DD_HV_B can be independently controlled from V DD_HV_A . These can ramp up or ramp down in any order. Design is robust
against any supply order.

2. This voltage is internally generated by the device and no external voltage should be supplied.

3. Both the relative and the fixed conditions must be met. For instance: If V DD_HV_A is 5.9 V, V DD_HV_ADC0 maximum value is
6.0 V then, despite the relative condition, the max value is V DD_HV_A + 0.3 = 6.2 V.

4. PA3, PA7, PA10, PA11 and PE12 ADC_1 channels are coming from V DD_HV_B domain hence V DD_HV_ADC1 should be
within ±300 mV of V DD_HV_B when these channels are used for ADC_1.

5. Any temperature beyond 125 °C should limit the current to 50 mA (max).

6. This is the storage temperature for the flash memory.

|Symbol|Col2|Parameter|Conditions|Value|Col6|Unit|
|---|---|---|---|---|---|---|
|||||Min|Max||
|V (2) RC_CTRL||Base control voltage for external BCP68 NPN device|Relative to V DD_LV|0|V + 1 DD_LV|V|
|V SS_ADC|S R|Voltage on VSS_HV_ADC0, VSS_HV_ADC1 (ADC reference) pin with respect to ground (V ) SS_HV|—|V 0.1 SS_HV|V + 0.1 SS_HV|V|
|V DD_HV_ADC0|S R|Voltage on VDD_HV_ADC0 with respect to ground (V ) SS_HV|—|–0.3|6.0|V|
||||Relative to V (3) DD_HV_A|V 0.3 DD_HV_A|V +0.3 DD_HV_A||
|V DD_HV_ADC1 (4)|S R|Voltage on VDD_HV_ADC1 with respect to ground (V ) SS_HV|—|–0.3|6.0|V|
||||Relative to V 2 DD_HV_A|V 0.3 DD_HV_A|V +0.3 DD_HV_A||
|V IN|S R|Voltage on any GPIO pin with respect to ground (V ) SS_HV|Relative to V DD_HV_A/HV_B|V  DD_HV_A/HV_B 0.3|V + DD_HV_A/HV_B 0.3|V|
|I INJPAD|S R|Injected input current on any pin during overload condition|—|–10|10|mA|
|I INJSUM|S R|Absolute sum of all injected input currents during overload condition|—|–50|50||
|I (5) AVGSEG|S R|Sum of all the static I/O current within a supply segment (V or V ) DD_HV_A DD_HV_B|V = 5.0 V ± 10%, DD PAD3V5V = 0||70|mA|
||||V = 3.3 V ± 10%, DD PAD3V5V = 1||64||
|T STORAGE|S R|Storage temperature|—|–55(6)|150|°C| *Note: Stresses exceeding the recommended absolute maximum ratings may cause permanent * *damage to the device. This is a stress rating only and functional operation of the device at * *these or any other conditions above those indicated in the operational sections of this * *specification are not implied. Exposure to absolute maximum rating conditions for extended * *periods may affect device reliability. During overload conditions (V IN > V DD_HV_A/HV_B or * *V IN < V SS_HV ), the voltage on pins with respect to ground (V SS_HV ) must not exceed the * *recommended values.*

DocID17478 Rev 9 53/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx**
##### **3.4 Recommended operating conditions**
###### **Table 10. Recommended o p eratin g conditions ( 3.3 V )**

54/123 DocID17478 Rev 9

|Symbol|Col2|Parameter|Conditions|Value|Col6|Unit|
|---|---|---|---|---|---|---|
|||||Min|Max||
|V SS_HV|SR|Digital ground on VSS_HV pins|—|0|0|V|
|V (1) DD_HV_A|SR|Voltage on V pins DD_HV_A with respect to ground (V ) SS_HV|—|3.0|3.6|V|
|V (1) DD_HV_B|SR|Voltage on V pins DD_HV_B with respect to ground (V ) SS_HV|—|3.0|3.6|V|
|V (2) SS_LV|SR|Voltage on VSS_LV (low voltage digital supply) pins with respect to ground (V ) SS_HV|—|V 0.1 SS_HV|V + 0.1 SS_HV|V|
|V (3) RC_CTRL||Base control voltage for external BCP68 NPN device|Relative to V DD_LV|0|V + 1 DD_LV|V|
|V SS_ADC|SR|Voltage on VSS_HV_ADC0, VSS_HV_ADC1 (ADC reference) pin with respect to ground (V ) SS_HV|—|V 0.1 SS_HV|V + 0.1 SS_HV|V|
|V DD_HV_ADC0 (4)|SR|Voltage on VDD_HV_ADC0 with respect to ground (V ) SS_HV|—|3.0(5)|3.6|V|
||||Relative to V (6) DD_HV_A|V 0.1 DD_HV_A|V + 0.1 DD_HV_A||
|V DD_HV_ADC1 (7)|SR|Voltage on VDD_HV_ADC1 with respect to ground (V ) SS_HV|—|3.0|3.6|V|
||||Relative to V (6) DD_HV_A|V 0.1 DD_HV_A|V + 0.1 DD_HV_A||
|V IN|SR|Voltage on any GPIO pin with respect to ground (V ) SS_HV|—|V 0.1 SS_HV|—|V|
||||Relative to V DD_HV_A/HV_B|—|V + 0.1 DD_HV_A/HV_B||
|I INJPAD|SR|Injected input current on any pin during overload condition|—|5|5|mA|
|I INJSUM|SR|Absolute sum of all injected input currents during overload condition|—|50|50||
|TV DD|SR|V slope to ensure DD_HV_A correct power up(8)|—|—|0.5|V/µs|
||||—|0.5|—|V/min|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 10. Recommended o p eratin g conditions ( 3.3 V ) ( continued )**

1. 100 nF EMI capacitance need to be provided between each VDD/VSS_HV pair.

2. 100 nF EMI capacitance needs to be provided between each VDD_LV/VSS_LV supply pair. 10 µF bulk capacitance needs
to be provided as CREG on each VDD_LV pin. For details refer to the Power Management chapter of the MPC5646C
Reference Manual.

3. This voltage is internally generated by the device and no external voltage should be supplied.

4. 100 nF capacitance needs to be provided between V DD_ADC /V SS_ADC pair.

5. Full electrical specification cannot be guaranteed when voltage drops below 3.0 V. In particular, ADC electrical
characteristics and I/Os DC electrical specification may not be guaranteed. When voltage drops below V LVDHVL, device is
reset.

6. Both the relative and the fixed conditions must be met. For instance: If V DD_HV_A is 5.9 V, V DD_HV_ADC0 maximum value is
6.0 V then, despite the relative condition, the max value is V DD_HV_A + 0.3 = 6.2 V.

7. PA3, PA7, PA10, PA11 and PE12 ADC_1 channels are coming from V DD_HV_B domain hence V DD_HV_ADC1 should be
within ±100 mV of V DD_HV_B when these channels are used for ADC_1.

8. Guaranteed by the device validation. **Table 11. Recommended o p eratin g conditions ( 5.0 V )**

DocID17478 Rev 9 55/123

|Symbol|Col2|Parameter|Conditions|Value|Col6|Unit|
|---|---|---|---|---|---|---|
|||||Min|Max||
|T A|SR|Ambient temperature under bias|f up to CPU 120 MHz  2%|–40|125|°C|
|T J|SR|Junction temperature under bias|—|40|150||

|Symbol|Col2|Parameter|Conditions|Value|Col6|Unit|
|---|---|---|---|---|---|---|
|||||Min|Max||
|V SS_HV|S R|Digital ground on VSS_HV pins|—|0|0|V|
|V (1) DD_HV_A|S R|Voltage on VDD_HV_A pins with respect to ground (V ) SS_HV|—|4.5|5.5|V|
||||Voltage drop(2)|3.0|5.5||
|V DD_HV_B|S R|Generic GPIO functionality|—|3.0|5.5|V|
|||Ethernet/3.3 V functionality (See the notes in all figures in Section 2: Package pinouts and signal descriptions for the list of channels operating in V DD_HV_B domain)|—|3.0|3.6|V|
|V (3) SS_LV|S R|Voltage on VSS_LV (Low voltage digital supply) pins with respect to ground (V ) SS_HV|—|V – 0.1 SS_HV|V + 0.1 SS_HV|V|
|V (4) RC_CTRL||Base control voltage for external BCP68 NPN device|Relative to V DD_LV|0|V + 1 DD_LV|V|
|V SS_ADC|S R|Voltage on VSS_HV_ADC0, VSS_HV_ADC1 (ADC reference) pin with respect to ground (V ) SS_HV|—|V – 0.1 SS_HV|V + 0.1 SS_HV|V|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 11. Recommended o p eratin g conditions ( 5.0 V ) ( continued )**

1. 100 nF EMI capacitance need to be provided between each VDD/VSS_HV pair.

2. Full device operation is guaranteed by design from 3.0 V–5.5 V. OSC functionality is guaranteed from the entire range
3.0V–5.5 V, the parametrics measured are at 3.0V and 5.5V (extreme voltage ranges to cover the range of operation). The
parametrics might have some variation in the intermediate voltage range, but there is no impact to functionality.

3. 100 nF EMI capacitance needs to be provided between each VDD_LV/VSS_LV supply pair. 10 µF bulk capacitance needs
to be provided as CREG on each VDD_LV pin.

4. This voltage is internally generated by the device and no external voltage should be supplied.

5. 100 nF capacitance needs to be provided between V DD_HV_(ADC0/ADC1) /V SS_HV_(ADC0/ADC1) pair.

6. Both the relative and the fixed conditions must be met. For instance: If V DD_HV_A is 5.9 V, V DD_HV_ADC0 maximum value is
6.0 V then, despite the relative condition, the max value is V DD_HV_A + 0.3 = 6.2 V.

7. PA3, PA7, PA10, PA11 and PE12 ADC_1 channels are coming from V DD_HV_B domain hence VDD_HV_ADC1 should be
within ±100 mV of V DD_HV_B when these channels are used for ADC_1.

56/123 DocID17478 Rev 9

|Symbol|Col2|Parameter|Conditions|Value|Col6|Unit|
|---|---|---|---|---|---|---|
|||||Min|Max||
|V DD_HV_ADC0 (5)|S R|Voltage on VDD_HV_ADC0 with respect to ground (V ) SS_HV|—|4.5|5.5|V|
||||Voltage drop(2)|3.0|5.5||
||||Relative to V (6) DD_HV_A|V – 0.1 DD_HV_A|V + 0.1 DD_HV_A||
|V DD_HV_ADC1 (7)|S R|Voltage on VDD_HV_ADC1 with respect to ground (V ) SS_HV|—|4.5|5.5|V|
||||Voltage drop(2)|3.0|5.5||
||||Relative to V (6) DD_HV_A|V 0.1 DD_HV_A|V + 0.1 DD_HV_A||
|V IN|S R|Voltage on any GPIO pin with respect to ground (V ) SS_HV|—|V –0.1 SS_HV|—|V|
||||Relative to V DD_HV_A/HV_B|—|V DD_HV_A/HV_B + 0.1||
|I INJPAD|S R|Injected input current on any pin during overload condition|—|–5|5|mA|
|I INJSUM|S R|Absolute sum of all injected input currents during overload condition|—|–50|50||
|TV DD|S R|V slope to ensure correct DD_HV_A power up(8)|—|—|0.5|V/µs|
||||—|0.5|—|V/min|
|T A C-Grade Part|S R|Ambient temperature under bias|—|40|85|°C|
|T J C-Grade Part|S R|Junction temperature under bias|—|40|110||
|T A V-Grade Part|S R|Ambient temperature under bias|—|40|105||
|T J V-Grade Part|S R|Junction temperature under bias|—|40|130||
|T A M-Grade Part|S R|Ambient temperature under bias|—|40|125||
|T J M-Grade Part|S R|Junction temperature under bias|—|40|150||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**

8. Guaranteed by device validation. *Note: SRAM retention guaranteed to LVD levels.*
##### **3.5 Thermal characteristics**
###### **3.5.1 Package thermal characteristics** **Table 12. LQFP thermal characteristics [(1)]**

1. Thermal characteristics are targets based on simulation that are subject to change per device characterization.

2. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C.

3. All values need to be confirmed during device validation.

4. 1s board as per standard JEDEC (JESD51-7) in natural convection.

5. 2s2p board as per standard JEDEC (JESD51-7) in natural convection. **Table 13. LBGA256 thermal characteristics [(1)]**

1. Thermal characteristics are targets based on simulation that are subject to change per device characterization.

DocID17478 Rev 9 57/123

|Symbol|Col2|C|Parameter|Conditions(2)|Pin count|Value(3)|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|R JA|CC|D|Thermal resistance, junction-to-ambient natural convection|Single-layer board—1s|176|—|—|44.4(4)|°C/W|
||||||208|—|—|43|°C/W|
|R JA|CC|D|Thermal resistance, junction-to-ambient natural convection|Four-layer board—2s2p(5)|176|—|—|36.1|°C/W|
||||||208|—|—|33.9|°C/W|

|Symbol|Col2|C|Parameter|Conditions|Value|Unit|
|---|---|---|---|---|---|---|
|R JA|CC|—|Thermal resistance, junction-to-ambient natural convection|Single-layer board—1s|44.3|°C/W|
|||||Four-layer board—2s2p|31||


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **3.5.2 Power considerations** The average chip-junction temperature, T J, in degrees Celsius, may be calculated using Equation 1 : Equation 1 T J = T A + (P D  R  JA ) Where: T A is the ambient temperature in °C. R JA is the package junction-to-ambient thermal resistance, in °C/W. P D is the sum of P INT and P I/O (P D = P INT + P I/O ). P INT is the product of I DD and V DD, expressed in watts. This is the chip internal power. P I/O represents the power dissipation on input and output pins; user determined. Most of the time for the applications, P I/O < P INT and may be neglected. On the other hand, P I/O may be significant, if the device is configured to continuously drive external modules and/or memories. An approximate relationship between P D and T J (if P I/O is neglected) is given by: **Equation 2 P D = K / (T J + 273 °C)** Therefore, solving equations Equation 1 and Equation 2 :

**2** Equation 3 K = P D  (T A + 273 °C) + R  JA  P D Where: K is a constant for the particular part, which may be determined from Equation 3 by measuring P D (at equilibrium) for a known T A. Using this value of K, the values of P D and T J may be obtained by solving equations Equation 1 and Equation 2 iteratively for any value of T A .
##### **3.6 I/O pad electrical characteristics**
###### **3.6.1 I/O pad types** The device provides four main I/O pad types depending on the associated alternate functions:  Slow pads—These pads are the most common pads, providing a good compromise between transition time and low electromagnetic emission.  Medium pads—These pads provide transition fast enough for the serial communication channels with controlled current to reduce electromagnetic emission.  Fast pads—These pads provide maximum speed. These are used for improved Nexus debugging capability.  Input only pads—These pads are associated to ADC channels and 32 kHz low power external crystal oscillator providing low input leakage.  Low power pads—These pads are active in standby mode for wakeup source. Also, medium/slow and fast/medium pads are available in design which can be configured to behave like a slow/medium and medium/fast pads depending upon the slew-rate control.

58/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** Medium and fast pads can use slow configuration to reduce electromagnetic emission, at the cost of reducing AC performance. **3.6.2 I/O input DC characteristics** Table 14 provides input DC electrical characteristics as described in Figure 5 . **Figure 5. I/O input DC electrical characteristics definition**

V IN

V DD

V IH

V IL

PDIx = ‘1

(GPDI register of SIUL)

PDIx = ‘0’ **Table 14. I/O input DC electrical characteristics **

|Symbol|Col2|C|Parameter|Conditions(1)|Col6|Value(2)|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|V IH|SR|P|Input high level CMOS (Schmitt Trigger)|—||0.65 V DD|—|V + 0.4 DD|V|
|V IL|SR|P|Input low level CMOS (Schmitt Trigger)|—||0.3|—|0.35V DD||
|V HYS|CC|C|Input hysteresis CMOS (Schmitt Trigger)|—||0.1V DD|—|—||
|I LKG|CC|P|Digital input leakage|No injection on adjacent pin|T = 40 °C A|—|2|—|nA|
|||P|||T = 25 °C A|—|2|—||
|||D|||T = 105 °C A|—|12|500||
|||P|||T = 125 °C A|—|70|1000||
|W FI|SR|P|Width of input pulse rejected by analog filter(3)|—||—|—|40(4)|ns|
|W NFI|SR|P|Width of input pulse accepted by analog filter(3)|—||1000(4)|—|—|ns|



1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B . All values need to be confirmed during device validation.

3. Analog filters are available on all wakeup lines.

DocID17478 Rev 9 59/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx**

4. The width of input pulse in between 40 ns to 1000 ns is indeterminate. It may pass the noise or may not depending on
silicon sample to sample variation. **3.6.3 I/O output DC characteristics** The following tables provide DC characteristics for bidirectional pads:  Table 15 provides weak pull figures. Both pull-up and pull-down resistances are supported.  Table 16 provides output driver characteristics for I/O pads when in SLOW configuration.  Table 17 provides output driver characteristics for I/O pads when in MEDIUM configuration.  Table 18 provides output driver characteristics for I/O pads when in FAST configuration. **Table 15. I/O pull-up/pull-down DC electrical characteristics **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B .

3. The configuration PAD3V5 = 1 when V DD = 5 V is only a transient configuration during power-up. All pads but RESET and
Nexus output (MDOx, EVTO, MCKO) are configured in input or in high impedance state. **Table 16. SLOW configuration out p ut buffer electrical characteristics **

60/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
||I | WPU|CC|P|Weak pull-up current absolute value|V = V , V = IN IL DD 5.0 V ± 10%|PAD3V5V = 0|10|—|150|µA|
|||C|||PAD3V5V = 1(3)|10|—|250||
|||P||V = V , V = IN IL DD 3.3 V ± 10%|PAD3V5V = 1|10|—|150||
||I | WPD|CC|P|Weak pull-down current absolute value|V = V , V = IN IH DD 5.0 V ± 10%|PAD3V5V = 0|10|—|150|µA|
|||C|||PAD3V5V = 1|10|—|250||
|||P||V = V , V = IN IH DD 3.3 V ± 10%|PAD3V5V = 1|10|—|150||

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|V OH|CC|P|Output high level SLOW configuration|Push Pull|I = 3 mA, OH V = 5.0 V ± 10%, PAD3V5V = 0 DD|0.8V DD|—|—|V|
|||C|||I = 3 mA, OH V = 5.0 V ± 10%, PAD3V5V = 1(3) DD|0.8V DD|—|—||
|||P|||I = 1.5 mA, OH V = 3.3 V ± 10%, PAD3V5V = 1 DD|V 0.8 DD|—|—||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 16. SLOW confi g uration out p ut buffer electrical characteristics ( continued )**

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B .

3. The configuration PAD3V5 = 1 when V DD = 5 V is only a transient configuration during power-up. All pads but RESET and
Nexus output (MDOx, EVTO, MCKO) are configured in input or in high impedance state. **Table 17. MEDIUM configuration out p ut buffer electrical characteristics **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B .

3. The configuration PAD3V5 = 1 when V DD = 5 V is only a transient configuration during power-up. All pads but RESET and
Nexus output (MDOx, EVTO, MCKO) are configured in input or in high impedance state.

DocID17478 Rev 9 61/123

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|V OL|CC|P|Output low level SLOW configuration|Push Pull|I = 3 mA, OL V = 5.0 V ± 10%, PAD3V5V = 0 DD|—|—|0.1V DD|V|
|||C|||I = 3 mA, OL V = 5.0 V ± 10%, PAD3V5V = 1(3) DD|—|—|0.1V DD||
|||P|||I = 1.5 mA, OL V = 3.3 V ± 10%, PAD3V5V = 1 DD|—|—|0.5||

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|V OH|CC|C|Output high level MEDIUM configuration|Push Pull|I = 3 mA, OH V = 5.0 V ± 10%, DD PAD3V5V = 0|0.8V DD|—|—|V|
|||C|||I = 1.5 mA, OH V = 5.0 V ± 10%, DD PAD3V5V = 1(3)|0.8V DD|—|—||
|||C|||I = 2 mA, OH V = 3.3 V ± 10%, DD PAD3V5V = 1|V 0.8 DD|—|—||
|V OL|CC|C|Output low level MEDIUM configuration|Push Pull|I = 3 mA, OL V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|0.2V DD|V|
|||C|||I = 1.5 mA, OL V = 5.0 V ± 10%, DD PAD3V5V = 1(3)|—|—|0.1V DD||
|||C|||I = 2 mA, OL V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|0.5||


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 18. FAST confi g uration out p ut buffer electrical characteristics **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B .

3. The configuration PAD3V5 = 1 when V DD = 5 V is only a transient configuration during power-up. All pads but RESET and
Nexus outputs (MDOx, EVTO, MCKO) are configured in input or in high impedance state. **3.6.4 Output pin transition times** **Table 19. Out p ut p in transition times **

62/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|V OH|CC|P|Output high level FAST configuration|Push Pull|I = 14 mA, OH V = 5.0 V ± 10%, DD PAD3V5V = 0|0.8V DD|—|—|V|
|||C|||I = 7 mA, OH V = 5.0 V ± 10%, DD PAD3V5V = 1(3)|0.8V DD|—|—||
|||C|||I = 11 mA, OH V = 3.3 V ± 10%, DD PAD3V5V = 1|V 0.8 DD|—|—||
|V OL|CC|P|Output low level FAST configuration|Push Pull|I = 14 mA, OL V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|0.1V DD|V|
|||C|||I = 7 mA, OL V = 5.0 V ± 10%, DD PAD3V5V = 1(3)|—|—|0.1V DD||
|||C|||I = 11 mA, OL V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|0.5||

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value(3)|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|T tr|CC|D|Output transition time output pin(4)  SLOW configuration|C = 25 pF L|V = 5.0 V ± 10 %, DD PAD3V5V = 0|—|—|50|ns|
|||T||C = 50 pF L||—|—|100||
|||D||C = 100 pF L||—|—|125||
|||D||C = 25 pF L|V = 3.3 V ± 10 %, DD PAD3V5V = 1|—|—|40||
|||T||C = 50 pF L||—|—|50||
|||D||C = 100 pF L||—|—|75||
|T tr|CC|D|Output transition time output pin(4) MEDIUM configuration|C = 25 pF L|V = 5.0 V ± 10 %, DD PAD3V5V = 0 SIUL.PCRx.SRC = 1|—|—|10|ns|
|||T||C = 50 pF L||—|—|20||
|||D||C = 100 pF L||—|—|40||
|||D||C = 25 pF L|V = 3.3 V ± 10 %, DD PAD3V5V = 1 SIUL.PCRx.SRC = 1|—|—|12||
|||T||C = 50 pF L||—|—|25||
|||D||C = 100 pF L||—|—|40||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 19. Out p ut p in transition times ( continued )**

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value(3)|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|T tr|CC|D|Output transition time output pin(4) FAST configuration|C = 25 pF L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|4|ns|
|||||C = 50 pF L||—|—|6||
|||||C = 100 pF L||—|—|12||
|||||C = 25 pF L|V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|4||
|||||C = 50 pF L||—|—|7||
|||||C = 100 pF L||—|—|12||


1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B .

3. All values need to be confirmed during device validation.

4. C L includes device and package capacitances (C PKG < 5 pF). **3.6.5 I/O pad current specification** The I/O pads are distributed across the I/O supply segment. Each I/O supply is associated to a V DD /V SS_HV supply pair as described in Table 20 . Table 21 provides I/O consumption figures. In order to ensure device reliability, the average current of the I/O on a single segment should remain below the I AVGSEG maximum value. In order to ensure device functionality, the sum of the dynamic and static current of the I/O on a single segment should remain below the I DYNSEG maximum value.

1. VDD_HV_B supplies the IO voltage domain for the pins PE[12], PA[11], PA[10], PA[9], PA[8], PA[7], PE[13], PF[14], PF[15],
PG[0], PG[1], PH[3], PH[2], PH[1], PH[0], PG[12], PG[13], and PA[3].

|Col1|Table 20. I/O supplies|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Package|I/O Supplies||||||||
|LBGA256(1)|Equivalent to 208-pin LQFP segment pad distribution + G6, G11, H11, J11||||||||
|LQFP208|pin6 (V ) DD_HV_A pin7 (V ) SS_HV|pin27 (V )pi DD_HV_A n28 (V ) SS_HV|pin73 (V ) SS_HV pin75 (V ) DD_HV_A|pin101 (V ) DD_HV_A pin102 (V ) SS_HV|pin132 (V ) SS_HV pin133 (V ) DD_HV_A|pin147 (V ) SS_HV pin148 (V ) DD_HV_B|pin174 (V ) SS_HV pin175 (V ) DD_HV_A|—|
|LQFP176|pin6 (V ) DD_HV_A pin7 (V ) SS_HV|pin27 (V )pi DD_HV_A n28 (V ) SS_HV|pin57 (V ) SS_HV pin59 (V ) DD_HV_A|pin85 (V ) DD_HV_A pin86 (V ) SS_HV|pin123 (V ) SS_HV pin124 (V ) DD_HV_B|pin150 (V ) SS_HV pin151 (V ) DD_HV_A|—|—|



DocID17478 Rev 9 63/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 21. I/O consum p tion **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B .

3. All values need to be confirmed during device validation.

4. Stated maximum values represent peak consumption that lasts only a few ns during I/O transition.

64/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1),(2)|Col6|Value(3)|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|I (4) SWTSLW|C C|D|Peak I/O current for SLOW configuration|C = 25 pF L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|19.9|mA|
||||||V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|15.5||
|I (4) SWTMED|C C|D|Peak I/O current for MEDIUM configuration|C = 25 pF L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|28.8|mA|
||||||V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|16.3||
|I (4) SWTFST|C C|D|Peak I/O current for FAST configuration|C = 25 pF L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|113.5|mA|
||||||V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|52.1||
|I RMSSLW|C C|D|Root mean square I/O current for SLOW configuration|C = 25 pF, 2 MHz L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|2.22|mA|
|||||C = 25 pF, 4 MHz L||—|—|3.13||
|||||C = 100 pF, 2 MHz L||—|—|6.54||
|||||C = 25 pF, 2 MHz L|V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|1.51||
|||||C = 25 pF, 4 MHz L||—|—|2.14||
|||||C = 100 pF, 2 MHz L||—|—|4.33||
|I RMSMED|C C|D|Root mean square I/O current for MEDIUM configuration|C = 25 pF, 13 MHz L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|6.5|mA|
|||||C = 25 pF, 40 MHz L||—|—|13.32||
|||||C = 100 pF, 13 MHz L||—|—|18.26||
|||||C = 25 pF, 13 MHz L|V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|4.91||
|||||C = 25 pF, 40 MHz L||—|—|8.47||
|||||C = 100 pF, 13 MHz L||—|—|10.94||
|I RMSFST|C C|D|Root mean square I/O current for FAST configuration|C = 25 pF, 40 MHz L|V = 5.0 V ± 10%, DD PAD3V5V = 0|—|—|21.05|mA|
|||||C = 25 pF, 64 MHz L||—|—|33||
|||||C = 100 pF, 40 MHz L||—|—|55.77||
|||||C = 25 pF, 40 MHz L|V = 3.3 V ± 10%, DD PAD3V5V = 1|—|—|14||
|||||C = 25 pF, 64 MHz L||—|—|20||
|||||C = 100 pF, 40 MHz L||—|—|34.89||
|I AVGSEG|S R|D|Sum of all the static I/O current within a supply segment|V = 5.0 V ± 10%, PAD3V5V = 0 DD||—|—|70|mA|
|||||V = 3.3 V ± 10%, PAD3V5V = 1 DD||—|—|65(4)||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**
##### **3.7 RESET electrical characteristics**
###### The device implements a dedicated bidirectional RESET pin. **Figure 6. Start-up reset requirements**

**V** **DD_HV_A**

V DDMIN

RESET

V IH

V IL


device reset forced by RESET


device start-up phase

###### **Figure 7. Noise filtering on reset signal**


~~**V**~~ **RESET**

V DD

V IH

V IL

filtered by
hysteresis


filter ~~e~~ d by
lowp ~~a~~ ss filter

W FRST


filtered by
lowpass filter

W FRST


**hw_rst**

**‘1’**

**‘0’**


unknown reset

state device under hardware reset

W NFRST


DocID17478 Rev 9 65/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 22. Reset electrical characteristics **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. V DD as mentioned in the table is V DD_HV_A /V DD_HV_B . All values need to be confirmed during device validation.

3. This is a transient configuration during power-up, up to the end of reset PHASE2 (refer to the RGM module section of the
device Reference Manual).

4. C L includes device and package capacitance (C PKG < 5 pF).

5. The configuration PAD3V5 = 1 when V DD = 5 V is only transient configuration during power-up. All pads but RESET and
Nexus output (MDOx, EVTO, MCKO) are configured in input or in high impedance state.

66/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|V IH|S R|P|Input High Level CMOS (Schmitt Trigger)|—|0.65V DD|—|V + 0.4 DD|V|
|V IL|S R|P|Input low Level CMOS (Schmitt Trigger)|—|0.3|—|0.35V DD|V|
|V HYS|C C|C|Input hysteresis CMOS (Schmitt Trigger)|—|0.1V DD|—|—|V|
|V OL|C C|P|Output low level|Push Pull, I = 2 mA, OL V = 5.0 V ± 10 %, PAD3V5V = 0 DD (recommended)|—|—|0.1V DD|V|
|||||Push Pull, I = 1 mA, OL V = 5.0 V ± 10%, PAD3V5V = 1(3) DD|—|—|0.1V DD||
|||||Push Pull, I = 1 mA, OL V = 3.3 V ± 10%, PAD3V5V = 1 DD (recommended)|—|—|0.5||
|T tr|C C|D|Output transition time output pin(4) MEDIUM configuration|C = 25 pF, L V = 5.0 V ± 10%, PAD3V5V = 0 DD|—|—|10|ns|
|||||C = 50 pF, L V = 5.0 V ± 10%, PAD3V5V = 0 DD|—|—|20||
|||||C = 100 pF, L V = 5.0 V ± 10%, PAD3V5V = 0 DD|—|—|40||
|||||C = 25 pF, L V = 3.3 V ± 10%, PAD3V5V = 1 DD|—|—|12||
|||||C = 50 pF, L V = 3.3 V ± 10%, PAD3V5V = 1 DD|—|—|25||
|||||C = 100 pF, L V = 3.3 V ± 10%, PAD3V5V = 1 DD|—|—|40||
|W FRST|S R|P|Reset input filtered pulse|—|—|—|40|ns|
|W NFRS T|S R|P|Reset input not filtered pulse|—|1000|—|—|ns|
||I | WPU|C C|P|Weak pull-up current absolute value|V = 3.3 V ± 10%, PAD3V5V = 1 DD|10|—|150|µA|
|||||V = 5.0 V ± 10%, PAD3V5V = 0 DD|10|—|150||
|||||V = 5.0 V ± 10%, PAD3V5V = 1(5) DD|10|—|250||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**
##### **3.8 Power management electrical characteristics**
###### **3.8.1 Voltage regulator electrical characteristics** The device implements an internal voltage regulator to generate the low voltage core supply V DD_LV from the high voltage supply V DD_HV_A . The following supplies are involved:  HV: High voltage external power supply for voltage regulator module. This must be provided externally through V DD_HV_A power pin.  LV: Low voltage internal power supply for core, FMPLL and Flash digital logic. This is generated by the on-chip VREG with an external ballast (BCP68 NPN device). It is further split into four main domains to ensure noise isolation between critical LV modules within the device: – LV_COR: Low voltage supply for the core. It is also used to provide supply for FMPLL through double bonding. – LV_CFLA0/CFLA1: Low voltage supply for the two code Flash modules. It is shorted with LV_COR through double bonding. – LV_DFLA: Low voltage supply for data Flash module. It is shorted with LV_COR through double bonding. – LV_PLL: Low voltage supply for FMPLL. It is shorted to LV_COR through double bonding.

(4  10  f)

Off chip

NPN driver

10  f

|Col1|0 nf|Col3|Col4|
|---|---|---|---|
||VSS_LV||VDD_LV|
|||||

|VSS_LV|VDD_LV|
|---|---|

|PD0 Logic|Col2|32 KB Split|56 KB Split|
|---|---|---|---|
|||||
|||CTRL|CTRL|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|tor capacitance connection|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||PD0 (always on domain) 32 KB 56 KB 8 KB Split Split Split Logic PD0 CTRL CTRL CTRL|
||||||||VSS_LV||||
||||||||||||
||||||||||||
||||||||||||
|PD1 Switchable Domain (FMPLL, Flash)|||||||||||
||||||||||||
||||||||||||

|VDD_LV|Col2|
|---|---|
|VSS_LV||
|VRC_CTRL||
|||


**Chip Boundary**

(C DEC2 )

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|HPREG||||||
||LPVDD|sw1 (<0.1)||||
|||||||
|LPREG||||||



VDD_BV VDD_HV_A VSS_HV

HPVDD 100 nf

LPVDD

1) All VSS_LV pins must be grounded, as shown for VSS_HV pin.

DocID17478 Rev 9 67/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** The internal voltage regulator requires external bulk capacitance (C REGn ) to be connected to the device to provide a stable low voltage digital supply to the device. Also required for stability is the C DEC2 capacitor at ballast collector. This is needed to minimize sharp injection current when ballast is turning ON. Apart from the bulk capacitance, user should connect EMI/decoupling cap (C REGP ) at each V DD_LV /V SS_LV pin pair. **3.8.1.1 Recommendations**  The external NPN driver must be BCP68 type.  V DD_LV should be implemented as a power plane from the emitter of the ballast transistor.  10 F capacitors should be connected to the 4 pins closest to the outside of the package and should be evenly distributed around the package. For BGA packages, the balls should be used are D8, H14, R9, J3–one cap on each side of package. – There should be a track direct from the capacitor to this pin (pin also connects to V DD_LV plane). The tracks ESR should be less than 100 m. – The remaining V DD_LV pins (exact number will vary with package) should be decoupled with 0.1 F caps, connected to the pin as per 10 F. (see Section 3.4: Recommended operating conditions ). **3.8.2 V DD_BV options**  Option 1: V DD_BV shared with V DD_HV_A V must be star routed from V from the common source. This is to

DD_BV DD_HV_A eliminate ballast noise injection on the MCU.  Option 2: V DD_BV independent of the MCU supply V DD_BV > 2.6 V for correct functionality. The device is not monitoring this supply hence the external component must meet the 2.6 V criteria through external monitoring if required. **Table 23. Volta g e re g ulator electrical characteristics **

68/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|C REGn|S R|—|External ballast stability capacitance|—|40|—|60|F|
|R REG|S R|—|Stability capacitor equivalent serial resistance|—|—|—|0.2|W|
|C REGP|S R|—|Decoupling capacitance (Close to the pin)|V /V DD_HV_A/HV_B SS_HV pair||100|—|nF|
|||||V /V pair DD_LV SS_LV||100|—|nF|
|C DEC2|S R|—|Stability capacitance regulator supply (Close to the ballast collector)|V /V DD_BV SS_HV|10|—|40|F|
|V MREG|C C|P|Main regulator output voltage|After trimming T = 25 °C A|1.20|1.28|1.32|V|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 23. Voltage re g ulator electrical characteristics ( continued )**

1. V DD_HV_A = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. Inrush current is seen more like steps of 600 mA peak. The startup of the regulator happens in steps of 50 mV in ~25 steps
to reach ~1.2 V V DD_LV . Each step peak current is within 600 mA **3.8.3 Voltage monitor electrical characteristics** The device implements a Power-on Reset module to ensure correct power-up initialization, as well as four low voltage detectors to monitor the V DD_HV_A and the V DD_LV voltage while device is supplied:  POR monitors V DD_HV_A during the power-up phase to ensure device is maintained in a safe reset state  LVDHV3 monitors V to ensure device is reset below minimum functional

DD_HV_A supply  LVDHV5 monitors V DD_HV_A when application uses device in the 5.0 V±10 % range  LVDLVCOR monitors power domain No. 1 (PD1)  LVDLVBKP monitors power domain No. 0 (PD0). VDD_LV is same as PD0 supply. *Note: When enabled, PD2 (RAM retention) is monitored through LVD_DIGBKP.*

DocID17478 Rev 9 69/123

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|I MREG|S R|—|Main regulator current provided to V domain DD_LV|—|—|—|350|mA|
|I MREGINT|C C|D|Main regulator module current consumption|I = 200 mA MREG|—|—|2|mA|
|||||I = 0 mA MREG|—|—|1||
|V LPREG|C C|P|Low power regulator output voltage|After trimming T = 25 °C A|1.17|1.27|1.32|V|
|I LPREG|S R|—|Low power regulator current provided to V domain DD_LV|—|—|—|50|mA|
|I LPREGINT|C C|D|Low power regulator module current consumption|I = 15 mA; LPREG T = 55 °C A|—|—|600|A|
|||—||I = 0 mA; LPREG T = 55 °C A|—|20|—||
|I VREGREF|C C|D|Main LVDs and reference current consumption (low power and main regulator switched off)|T = 55 °C A|—|2|—|A|
|I VREDLVD12|C C|D|Main LVD current consumption (switch-off during standby)|T = 55 °C A|—|1|—|A|
|I DD_HV_A|C C|D|In-rush current on V during DD_BV power-up|—|—|—|600 (3)|mA|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Fi g ure 9. Low volta g e monitor vs. Reset**

V DDHV/LV

V LVDHVxH/LVxH

V LVDHVxL/LVxL

RESET **Table 24. Low volta g e monitor electrical characteristics **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.
##### **3.9 Low voltage domain power consumption**
###### Table 25 provides DC electrical characteristics for significant application modes. These values are indicative values; actual consumption depends on the application.

70/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|V PORUP|S R|P|Supply for functional POR module|—|1.0|—|5.5|V|
|V PORH|C C|P|Power-on reset threshold|—|1.5|—|2.6||
|V LVDHV3H|C C|T|LVDHV3 low voltage detector high threshold|—|2.7|—|2.85||
|V LVDHV3L|C C|T|LVDHV3 low voltage detector low threshold|—|2.6|—|2.74||
|V LVDHV5H|C C|T|LVDHV5 low voltage detector high threshold|—|4.3|—|4.5||
|V LVDHV5L|C C|T|LVDHV5 low voltage detector low threshold|—|4.2|—|4.4||
|V LVDLVCORL|C C|P|LVDLVCOR low voltage detector low threshold|T = 25 °C, A after trimming|1.08|—|1.17||
|V LVDLVBKPL|C C|P|LVDLVBKP low voltage detector low threshold||1.08|—|1.17||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 25. Low volta g e power domain electrical characteristics [(1)]**

1. Except for I DDMAX, all the current values are total current drawn from V DD_HV_A .

2. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified All temperatures are based on an
ambient temperature.

3. Target typical current consumption for the following typical operating conditions and configuration. Process = typical,
Voltage = 1.2 V.

4. Target maximum current consumption for mode observed under typical operating conditions. Process = Fast, Voltage =
1.32 V.

5. Running consumption is given on voltage regulator supply (V DDREG ). It does not include consumption linked to I/Os
toggling. This value is highly dependent on the application. The given value is thought to be a worst case value with all
cores and peripherals running, and code fetched from code flash while modify operation on-going on data flash. It is to be
noticed that this value can be significantly reduced by application: switch-off not used peripherals (default), reduce
peripheral frequency through internal prescaler, fetch from RAM most used functions, use low power mode when possible.

6. Higher current may sunk by device during power-up and standby exit. Please refer to in rush current in *Table 23* .

7. Maximum “allowed” current is package dependent.

8. Only for the “P” classification: Code fetched from RAM: Serial IPs CAN and LIN in loop back mode, DSPI as Master, PLL as
system Clock (4 x Multiplier) peripherals on (eMIOS/CTU/ADC) and running at max frequency, periodic SW/WDG timer
reset enabled. RUN current measured with typical application with accesses on both code flash and RAM.

DocID17478 Rev 9 71/123

|Symbol|Col2|C|Parameter|Conditions(2)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ(3)|Max(4)||
|I (5) DDMAX|C C|D|RUN mode maximum average current|—||—|210|300(6), (7)|mA|
|I DDRUN|C C|P|RUN mode typical average current(8)|at 120 MHz|T = 25 °C A|—|150|208(9)|mA|
|||D||at 80 MHz|T = 25 °C A|—|110(8)|150(10)|mA|
|||C||at 120 MHz|T = 125 °C A|—|180|280|mA|
|I DDHALT|C C|P|HALT mode current(11)|at 120 MHz|T = 25 °C A|—|20|27|mA|
|||C||at 120 MHz|T = 125 °C A|—|35|100|mA|
|I DDSTOP|C C|P|STOP mode current(12)|No clocks active|T = 25 °C A|—|0.4|5|mA|
|||C|||T = 125 °C A|—|16|72|mA|
|I DDSTDBY3 (96 KB RAM retained)|C C|P|STANDBY3 mode current(13)|No clocks active|T = 25 °C A|—|50|96|µA|
|||C|||T = 125 °C A|—|630|2400|µA|
|I DDSTDBY2 (64 KB RAM retained)|C C|C|STANDBY2 mode current(14)|No clocks active|T = 25 °C A|—|40|92|µA|
|||C|||T = 125 °C A|—|500|2000|µA|
|I DDSTDBY1 (8 KB RAM retained)|C C|C|STANDBY1 mode current(15)|No clocks active|T = 25 °C A|—|25|85|µA|
|||C|||T = 125 °C A|—|230|1100|µA|
|Adders in LP mode|C C|T|32 KHz OSC|—|T = 25 °C A|—|—|5|µA|
||||4–40 MHz OSC|—|T = 25 °C A|—|—|3|mA|
||||16 MHz IRC|—|T = 25 °C A|—|—|500|µA|
||||128 KHz IRC|—|T = 25 °C A|—|—|5|µA|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx**

9. Subject to change, Configuration: 1  e200z4d + 4 kbit/s Cache, 1  e200z0h (1/2 system frequency), CSE, 1  e DMA
(10 ch.), 6  FlexCAN (4  500 kbit/s, 2  125 kbit/s), 4  LINFlexD (20 kbit/s), 6  DSPI (2  2 Mbit/s, 3  4 Mbit/s,
1  10 Mbit/s), 16  Timed I/O, 16  ADC Input, 1  FlexRay (2 ch., 10 Mbit/s), 1  FEC (100 Mbit/s), 1  RTC, 4  PIT
channels, 1  SWT, 1  STM. For lower pin count packages reduce the amount of timed I/O’s and ADC channels. RUN
current measured with typical application with accesses on both code flash and RAM.

10. This value is obtained from limited sample set.

11. Data Flash Power Down. Code Flash in Low Power. SIRC 128 kHz and FIRC 16 MHz ON. 16 MHz XTAL clock. FlexCAN:
instances: 0, 1, 2 ON (clocked but no reception or transmission), instances: 4, 5, 6 clocks gated. LINFlex: instances: 0, 1, 2
ON (clocked but no reception or transmission), instance: 3-9 clocks gated. eMIOS: instance: 0 ON (16 channels on PA[0]PA[11] and PC[12]-PC[15]) with PWM 20 kHz, instance: 1 clock gated. DSPI: instance: 0 (clocked but no communication,
instance: 1-7 clocks gated). RTC/API ON. PIT ON. STM ON. ADC ON but no conversion except 2 analog watchdogs.

12. Only for the “P” classification: No clock, FIRC 16 MHz OFF, SIRC128 kHz ON, PLL OFF, HPvreg OFF, LPVreg ON. All
possible peripherals off and clock gated. Flash in power down mode.

13. Only for the “P” classification: LPreg ON, HPVreg OFF, 96 KB RAM ON, device configured for minimum consumption, all
possible modules switched-off. Measurement condition assumes T j = Ta.

14. LPreg ON, HPVreg OFF, 64 KB RAM ON, device configured for minimum consumption, all possible modules switched-off.
Measurement condition assumes T = Ta.
j

15. LPreg ON, HPVreg OFF, 8 KB RAM ON, device configured for minimum consumption, all possible modules switched OFF.
Measurement condition assumes T = Ta.
j
##### **3.10 Flash memory electrical characteristics**
###### **3.10.1 Program/Erase characteristics** Table 26 shows the code flash memory program and erase characteristics. **Table 26. Code flash memor y —Pro g ram and erase s p ecifications **

1. Typical program and erase times assume nominal supply values and operation at 25 °C. All times are subject to change
pending device characterization.

2. Initial factory condition: < 100 program/erase cycles, 25 °C, typical supply voltage.

3. The maximum program and erase times occur after the specified number of program/erase cycles. These maximum values
are characterized but not guaranteed.

4. Actual hardware programming times. This does not include software overhead.

5. It is Time between erase suspend resume and the next erase suspend request. Table 27 shows the data flash memory program and erase characteristics.

72/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Value|Col6|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
|||||Min|Typ(1)|Initial max(2)|Max(3)||
|T dwprogram|C C|C|Double word (64 bits) program time(4)|—|18|50|500|µs|
|T 16Kpperase|||16 KB block pre-program and erase time|—|200|500|5000|ms|
|T 32Kpperase|||32 KB block pre-program and erase time|—|300|600|5000|ms|
|T 128Kpperase|||128 KB block pre-program and erase time|—|600|1300|5000|ms|
|T eslat||D|Erase Suspend Latency|—|—|30|30|µs|
|t (5) ESRT||C|Erase Suspend Request Rate|20|—|—|—|ms|
|t PABT||D|Program Abort Latency|—|—|10|10|µs|
|t EAPT||D|Erase Abort Latency|—|—|30|30|µs|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 27. Data flash memor y —Pro g ram and erase s p ecifications **

|Symbol|Col2|C|Parameter|Value|Col6|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
|||||Min|Typ(1)|Initial max(2)|Max(3)||
|T wprogram|C C|C|Word (32 bits) program time(4)|—|30|70|500|µs|
|T 16Kpperase|||16 KB block pre-program and erase time|—|700|800|5000|ms|
|T eslat||D|Erase Suspend Latency|—|—|30|30|µs|
|t (5) ESRT||C|Erase Suspend Request Rate|10|—|—|—|ms|
|t PABT||D|Program Abort Latency|—|—|12|12|µs|
|t EAPT||D|Erase Abort Latency|—|—|30|30|µs|


1. Typical program and erase times assume nominal supply values and operation at 25 °C. All times are subject to change
pending device characterization.

2. Initial factory condition: < 100 program/erase cycles, 25 °C, typical supply voltage.

3. The maximum program and erase times occur after the specified number of program/erase cycles. These maximum values
are characterized but not guaranteed.

4. Actual hardware programming times. This does not include software overhead.

5. It is time between erase suspend resume and next erase suspend. **Table 28. Flash memor y module life**

1. Ambient temperature averaged over duration of application, not to exceed recommended product operating temperature
range.

|Symbol|Col2|C|Parameter|Conditions|Value|Col7|Unit|
|---|---|---|---|---|---|---|---|
||||||Min|Typ||
|P/E|CC|C|Number of program/erase cycles per block for 16 Kbyte blocks over the operating temperature range (T ) J|—|100000|100000|cycles|
||||Number of program/erase cycles per block for 32 Kbyte blocks over the operating temperature range (T ) J|—|10000|100000|cycles|
||||Number of program/erase cycles per block for 128 Kbyte blocks over the operating temperature range (T ) J|—|1000|100000|cycles|
|Retention|CC|C|Minimum data retention at 85 °C average ambient temperature(1)|Blocks with 0–1000 P/E cycles|20|—|years|
|||||Blocks with 10000 P/E cycles|10|—|years|
|||||Blocks with 100000 P/E cycles|5|—|years|



DocID17478 Rev 9 73/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** ECC circuitry provides correction of single bit faults and is used to improve further automotive reliability results. Some units will experience single bit corrections throughout the life of the product with no impact to product reliability.

1. Max speed is the maximum speed allowed including PLL frequency modulation (FM).

2. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified. **3.10.2 Flash memory power supply DC characteristics** Table 30 shows the flash memory power supply DC characteristics on external supply. **Table 30. Flash memor y p ower su pp l y DC electrical characteristics**

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = –40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. Data based on characterization results, not tested in production.

4. f CPU 120 MHz  2 % can be achieved over full temperature 125 °C ambient, 150 °C junction temperature.

74/123 DocID17478 Rev 9

|Col1|Col2|Col3|Table 29. Flash memory|read access timing(1)|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Symbol||C|Parameter|Conditions(2)||Frequency range|Unit|
|||||Code flash memory|Data flash memory|||
|f READ|CC|P|Maximum frequency for Flash reading|5 wait states|13 wait states|120 —100|MHz|
|||C||4 wait states|11 wait states|100—80||
|||D||3 wait states|9 wait states|80—64||
|||C||2 wait states|7 wait states|64—40||
|||C||1 wait states|4 wait states|40—20||
|||C||0 wait states|2 wait states|20—0||

|Symbol|Col2|Parameter|Conditions(1)|Col5|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|I (3) CFREAD|C C|Sum of the current consumption on V on read access DD_HV_A|Flash memory module read f = 120 MHz  2%(4) CPU|Code flash memory|||33|mA|
|I (3) DFREAD||||Data flash memory|||13||
|I (3) CFMOD|C C|Sum of the current consumption on V (program/erase) DD_HV_A|Program/Erase on-going while reading flash memory registers f = 120 MHz  2% (4) CPU|Code flash memory|||52|mA|
|I (3) DFMOD||||Data flash memory|||13||
|I (3) CFLPW|C C|Sum of the current consumption on V during flash DD_HV_A memory low power mode||Code flash memory|||1.1|mA|
|I (3) CFPWD|C C|Sum of the current consumption on V during flash DD_HV_A memory power down mode||Code flash memory|||150|µA|
|I (3) DFPWD||||Data flash memory|||150||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **3.10.3 Flash memory start-up/switch-off timings** **Table 31. Start-u p time/Switch-off time **

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.
##### **3.11 Electromagnetic compatibility (EMC) characteristics**
###### Susceptibility tests are performed on a sample basis during product characterization. **3.11.1 Designing hardened software to avoid noise problems** EMC characterization and optimization are performed at component level with a typical application environment and simplified MCU software. It should be noted that good EMC performance is highly dependent on the user application and the software in particular. Therefore it is recommended that the user apply EMC software optimization and pre- qualification tests in relation with the EMC level requested for the application.  Software recommendations The software flowchart must include the management of runaway conditions such as: – Corrupted program counter – Unexpected reset – Critical data corruption (control registers)  Pre-qualification trials Most of the common failures (unexpected reset and program

|Symbol|Col2|C|Parameter|Col5|Conditions (1)|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|T FLARSTEXIT|C C|D|Delay for flash memory module to exit reset mode|Code flash memory|—|—|—|125|µs|
|||||Data flash memory||—|—|||
|T FLALPEXIT|C C|T|Delay for flash memory module to exit low-power mode|Code flash memory|—|—|—|0.5||
|T FLAPDEXIT|C C|T|Delay for flash memory module to exit power-down mode|Code flash memory|—|—|—|30||
|||||Data flash memory||—|—|||
|T FLALPENTR Y|C C|T|Delay for flash memory module to enter low-power mode|Code flash memory|—|—|—|0.5|| counter corruption) can be reproduced by manually forcing a low state on the reset pin or the oscillator pins for 1 second. To complete these trials, ESD stress can be applied directly on the device. When unexpected behavior is detected, the software can be hardened to prevent unrecoverable errors occurring (see application note Software Techniques For Improving Microcontroller EMC Performance (AN1015)).

DocID17478 Rev 9 75/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **3.11.2 Electromagnetic interference (EMI)** The product is monitored in terms of emission based on a typical application. This emission test conforms to the IEC61967-1 standard, which specifies the general conditions for EMI measurements. **Table 32. EMI radiated emission measurement [(1)(2)]**

1. EMI testing and I/O port waveforms per IEC 61967-1, -2, -4.

2. For information on conducted emission and susceptibility measurement (norm IEC 61967-4), please contact your local
marketing representative.

3. All values need to be confirmed during device validation. **3.11.3 Absolute maximum ratings (electrical sensitivity)** Based on two different tests (ESD and LU) using specific measurement methods, the product is stressed in order to determine its performance in terms of electrical sensitivity. **3.11.3.1 Electrostatic discharge (ESD)** Electrostatic discharges (a positive then a negative pulse separated by 1 second) are applied to the pins of each sample according to each pin combination. The sample size depends on the number of supply pins in the device (3 parts  (n+1) supply pin). This test conforms to the AEC-Q100-002/-003/-011 standard. For more details, refer to the application note Electrostatic Discharge Sensitivity Measurement (AN1181). **Table 33. ESD absolute maximum ratin g s [(1)(2)]**

76/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|—|S R|—|Scan range|—||0.150||1000|MHz|
|f CPU|S R|—|Operating frequency|—||—|120|—|MHz|
|V DD_LV|S R|—|LV operating voltages|—||—|1.28|—|V|
|S EMI|C C|T|Peak level|V = 5 V, T = 25 °C, DD A LQFP176 package Test conforming to IEC 61967-2, f = 40 MHz/f = 120 OSC CPU MHz|No PLL frequency modulation|—|—|18|dBµV|
||||||± 2% PLL frequency modulation|—|—|14(3)|dBµV|

|Symbol|Ratings|Conditions|Class|Max value(3)|Unit|
|---|---|---|---|---|---|
|V ESD(HBM)|Electrostatic discharge voltage (Human Body Model)|T = 25 °C A conforming to AEC-Q100-002|H1C|2000|V|
|V ESD(MM)|Electrostatic discharge voltage (Machine Model)|T = 25 °C A conforming to AEC-Q100-003|M2|200||
|V ESD(CDM)|Electrostatic discharge voltage (Charged Device Model)|T = 25 °C A conforming to AEC-Q100-011|C3A|500||
|||||750 (corners)||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**

1. All ESD testing is in conformity with CDF-AEC-Q100 Stress Test Qualification for Automotive Grade Integrated Circuits.

2. A device will be defined as a failure if after exposure to ESD pulses the device no longer meets the device specification
requirements. Complete DC parametric and functional testing shall be performed per applicable device specification at
room temperature followed by hot temperature, unless specified otherwise in the device specification.

3. Data based on characterization results, not tested in production. **3.11.3.2 Static latch-up (LU)** Two complementary static tests are required on six parts to assess the latch-up performance:  A supply over-voltage is applied to each power supply pin.  A current injection is applied to each input, output and configurable I/O pin. These tests are compliant with the EIA/JESD 78 IC latch-up standard. **Table 34. Latch-u p results**
##### **3.12 Fast external crystal oscillator (4–40 MHz) electrical ** **characteristics**
###### The device provides an oscillator/resonator driver. Figure 10 describes a simple model of the internal oscillator driver and provides an example of a connection for an oscillator or a resonator. Table 35 provides the parameter description of 4 MHz to 40 MHz crystals used for the design simulations.

DocID17478 Rev 9 77/123

|Symbol|Parameter|Conditions|Class|
|---|---|---|---|
|LU|Static latch-up class|T = 125 °C A conforming to JESD 78|II level A|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 10. Crystal oscillator and resonator connection scheme**


**XTAL**

**EXTAL**


**EXTAL**

**XTAL**


**EXTAL**

**XTAL**


**R** **D**


**C1**

**C2**


**DEVICE**


**DEVICE**

###### *Note: XTAL/EXTAL must not be directly used to drive external circuits.* **Table 35. Cr y stal descri p tion**

|Nominal frequency (MHz)|NDK crystal reference|Crystal equivalent series resistance ESR |Crystal motional capacitance (C ) fF m|Crystal motional inductance (L ) mH m|Load on xtalin/xtalout C1 = C2 (pF)(1)|Shunt capacitance between xtalout and xtalin C0(2) (pF)|
|---|---|---|---|---|---|---|
|4|NX8045GB|300|2.68|591.0|21|2.93|
|8|NX5032GA|300|2.46|160.7|17|3.01|
|10||150|2.93|86.6|15|2.91|
|12||120|3.11|56.5|15|2.93|
|16||120|3.90|25.3|10|3.00|
|40|NX5032GA|50|6.18|2.56|8|3.49|


1. The values specified for C1 and C2 are the same as used in simulations. It should be ensured that the testing includes all
the parasitics (from the board, probe, crystal, etc.) as the AC / transient behavior depends upon them.

2. The value of C0 specified here includes 2 pF additional capacitance for parasitics (to be seen with bond-pads, package,
etc.).

78/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Figure 11. Fast external crystal oscillator (4 to 40 MHz) electrical characteristics**

**S_MTRANS** bit (ME_GS register)

1

0


**V** **XTAL**

V FXOSC

V FXOSCOP


1/f MXOSC


T MXOSCSU


valid internal clock

###### **Table 36. Fast external cr y stal oscillator ( 4 to 40 MHz ) electrical characteristics **

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|f FXOSC|SR|—|Fast external crystal oscillator frequency|—|4.0|—|40.0|MHz|
|g mFXOSC|CC|C|Fast external crystal oscillator transconductance|V = 3.3 V ± 10% DD|4(3)|—|20(3)|mA/V|
|||||V = 5.0 V ± 10% DD|6.5(3)|—|25(3)||
|V FXOSC|CC|T|Oscillation amplitude at EXTAL|f = 40 MHz OSC For both V = 3.3 V ± DD 10%, V = 5.0 V ± 10% DD|—|0.95|—|V|
|V FXOSCOP|CC|P|Oscillation operating point|—|—|1.8||V|
|I (4) FXOSC|CC|T|Fast external crystal oscillator consumption|V = 3.3 V ± 10%, DD f = 40 MHz OSC|—|2|2.2|mA|
|||||V = 5.0 V ± 10%, DD f = 40 MHz OSC|—|2.3|2.5||
|||||V = 3.3 V ± 10%, DD f = 16 MHz OSC|—|1.3|1.5||
|||||V = 5.0 V ± 10%, DD f = 16 MHz OSC|—|1.6|1.8||
|T FXOSCSU|CC|T|Fast external crystal oscillator start-up time|f = 40 MHz OSC For both V = 3.3 V ± DD 10%, V = 5.0 V ± 10% DD|—|—|5|ms|


DocID17478 Rev 9 79/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 36. Fast external crystal oscillator ( 4 to 40 MHz ) electrical characteristics ( continued )**

1. V DD = 3.3 V ± 10% / 5.0 V ± 10%, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. Based on ATE Cz

4. Stated values take into account only analog module consumption but not the digital contributor (clock tree and enabled
peripherals).

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|V IH|SR|P|Input high level CMOS (Schmitt Trigger)|Oscillator bypass mode|0.65V DD_ HV_A|—|V + 0.4 DD_HV_A|V|
|V IL|SR|P|Input low level CMOS (Schmitt Trigger)|Oscillator bypass mode|0.3|—|0.35V DD_HV_A|V|

##### **3.13 Slow external crystal oscillator (32 kHz) electrical ** **characteristics**
###### The device provides a low power oscillator/resonator driver. **Figure 12. Crystal oscillator and resonator connection scheme**


**OSC32K_EXTAL**

**OSC32K_XTAL**


**C1**


**OSC32K_EXTAL**

**OSC32K_XTAL**


**R** **P**


**DEVICE**


**C2** **DEVICE**

###### *Note: OSC32K_XTAL/OSC32K_EXTAL must not be directly used to drive external circuits.*

l

80/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Figure 13. Equivalent circuit of a quartz crystal**

C0

C1 Crystal C2 C m R m L m

C1 C2 **Table 37. Crystal motional characteristics [(1)]**

|Symbol|Parameter|Conditions|Value|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
||||Min|Typ|Max||
|L m|Motional inductance|—|—|11.796|—|KH|
|C m|Motional capacitance|—|—|2|—|fF|
|C1/C2|Load capacitance at OSC32K_XTAL and OSC32K_EXTAL with respect to ground(2)|—|18|—|28|pF|
|R (3) m|Motional resistance|AC coupled @ C0 = 2.85 pF(4)|—|—|65|kW|
|||AC coupled @ C0 = 4.9 pF(4)|—|—|50||
|||AC coupled @ C0 = 7.0 pF(4)|—|—|35||
|||AC coupled @ C0 = 9.0 pF(4)|—|—|30||



1. The crystal used is Epson Toyocom MC306.

2. This is the recommended range of load capacitance at OSC32K_XTAL and OSC32K_EXTAL with respect to ground. It
includes all the parasitics due to board traces, crystal and package.

3. Maximum ESR (R m ) of the crystal is 50 k

4. C0 Includes a parasitic capacitance of 2.0 pF between OSC32K_XTAL and OSC32K_EXTAL pins.

DocID17478 Rev 9 81/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 14. Slow external crystal oscillator (32 kHz) electrical characteristics**

**OSCON** bit (OSC_CTL register)

1

0


**V** **OSC32K_XTAL**

V LPXOSC32K


1/f LPXOSC32K


T LPXOSC32KSU


valid internal clock

###### **Table 38. Slow external crystal oscillator ( 32 kHz ) electrical characteristics **

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|f SXOSC|S R|—|Slow external crystal oscillator frequency|—|32|32.76 8|40|kHz|
|g mSXOSC|C C|—|Slow external crystal oscillator transconductance|V = 3.3 V ± 10%, DD|13(3)|—|33(3)|µA/V|
|||||V = 5.0 V ± 10% DD|15(3)|—|35(3)||
|V SXOSC|C C|T|Oscillation amplitude|—|1.2|1.4|1.7|V|
|I SXOSCBIAS|C C|T|Oscillation bias current|—|1.2|—|4.4|µA|
|I SXOSC|C C|T|Slow external crystal oscillator consumption|—|—|—|7|µA|
|T SXOSCSU|C C|T|Slow external crystal oscillator start-up time|—|—|—|2(4)|s|


1. V DD = 3.3 V ± 10% / 5.0 V ± 10%, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. Based on ATE CZ

4. Start-up time has been measured with EPSON TOYOCOM MC306 crystal. Variation may be seen with other crystal.

82/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**
##### **3.14 FMPLL electrical characteristics**
###### The device provides a frequency-modulated phase-locked loop (FMPLL) module to generate a fast system clock from the main oscillator driver. **Table 39. FMPLL electrical characteristics **

1. V DD = 3.3 V ± 10% / 5.0 V ± 10%, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. PLLIN clock retrieved directly from 4-40 MHz XOSC or 16 MIRC. Input characteristics are granted when oscillator is used
in functional mode. When bypass mode is used, oscillator input clock should verify f PLLIN and  PLLIN .

4. f CPU 120 + 2% MHz can be achieved at 125 °C.
##### **3.15 Fast internal RC oscillator (16 MHz) electrical characteristics**
###### The device provides a 16 MHz main internal RC oscillator. This is used as the default clock at the power-up of the device and can also be used as input to PLL. **Table 40. Fast internal RC oscillator ( 16 MHz ) electrical characteristics **

DocID17478 Rev 9 83/123

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|f PLLIN|S R|—|FMPLL reference clock(3)|—|4|—|64|MHz|
| PLLIN|S R|—|FMPLL reference clock duty cycle(3)|—|40|—|60|%|
|f PLLOUT|C C|P|FMPLL output clock frequency|—|16|—|120|MHz|
|f CPU|S R|—|System clock frequency|—|—|—|120 + 2%(4)|MHz|
|f FREE|C C|P|Free-running frequency|—|20|—|150|MHz|
|t LOCK|C C|P|FMPLL lock time|Stable oscillator (f = 16 MHz) PLLIN||40|100|µs|
|t LTJIT|C C|—|FMPLL long term jitter|f = 40 MHz (resonator), PLLIN f @ 120 MHz, 4000 cycles PLLCLK|—|—|6 (for < 1ppm)|ns|
|I PLL|C C|C|FMPLL consumption|T = 25 °C A|—|—|3|mA|

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|f FIRC|C C|P|Fast internal RC oscillator high frequency|T = 25 °C, trimmed A|—|16|—|MHz|
||S R|—||—|12||20||


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 40. Fast internal RC oscillator ( 16 MHz ) electrical characteristics ( continued )**

1. V DD = 3.3 V ± 10% / 5.0 V ± 10%, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. This does not include consumption linked to clock tree toggling and peripherals consumption when RC oscillator is ON.

84/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1)|Col6|Value(2)|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|I (3) FIRCRUN|C C|T|Fast internal RC oscillator high frequency current in running mode|T = 25 °C, trimmed A||—|—|200|µA|
|I FIRCPWD|C C|D|Fast internal RC oscillator high frequency current in power down mode|T = 25 °C A||—|—|100|nA|
|||D||T = 55 °C A||—|—|200|nA|
|||D||T = 125 °C A||—|—|1|µA|
|I FIRCSTOP|C C|T|Fast internal RC oscillator high frequency and system clock current in stop mode|T = 25 °C A|sysclk = off|—|500|—|µA|
||||||sysclk = 2 MHz|—|600|—||
||||||sysclk = 4 MHz|—|700|—||
||||||sysclk = 8 MHz|—|900|—||
||||||sysclk = 16 MHz|—|1250|—||
|T FIRCSU|C C|C|Fast internal RC oscillator start-up time|T = 55 °C A|V = 5.0 V ± DD 10%|—|—|2.0|µs|
|||—|||V = 3.3 V ± DD 10%|—|—|5||
|||—||T = A 125 °C|V = 5.0 V ± DD 10%|—|—|2.0||
|||—|||V = 3.3 V ± DD 10%|—|—|5||
| FIRCPRE|C C|C|Fast internal RC oscillator precision after software trimming of f FIRC|T = 25 °C A||1|—|+1|%|
| FIRCTRIM|C C|C|Fast internal RC oscillator trimming step|T = 25 °C A||—|1.6||%|
| FIRCVAR|C C|C|Fast internal RC oscillator variation over temperature and supply with respect to f at FIRC T = 25 °C in high-frequency A configuration|—||5|—|+5|%|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**
##### **3.16 Slow internal RC oscillator (128 kHz) electrical ** **characteristics**
###### The device provides a 128 kHz low power internal RC oscillator. This can be used as the reference clock for the RTC module. **Table 41. Slow internal RC oscillator ( 128 kHz ) electrical characteristics **

1. V DD = 3.3 V ± 10% / 5.0 V ± 10%, T A = 40 to 125 °C, unless otherwise specified.

2. All values need to be confirmed during device validation.

3. This does not include consumption linked to clock tree toggling and peripherals consumption when RC oscillator is ON.
##### **3.17 ADC electrical characteristics**
###### **3.17.1 Introduction** The device provides two Successive Approximation Register (SAR) analog-to-digital converters (10-bit and 12-bit). *Note: Due to ADC limitations, the two ADCs cannot sample a shared channel at the same time * *i.e., their sampling windows cannot overlap if a shared channel is selected. If this is done, * *neither of the ADCs can guarantee their conversion accuracies.*

DocID17478 Rev 9 85/123

|Symbol|Col2|C|Parameter|Conditions(1)|Value(2)|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|f SIRC|C C|P|Slow internal RC oscillator low frequency|T = 25 °C, trimmed A|—|128|—|kHz|
||S R|—||untrimmed, across temperatures|84|—|205||
|I (3) SIRC|C C|C|Slow internal RC oscillator low frequency current|T = 25 °C, trimmed A|—|—|5|µA|
|T SIRCSU|C C|P|Slow internal RC oscillator start- up time|T = 25 °C, V = 5.0 V ± 10% A DD|—|8|12|µs|
| SIRCPRE|C C|C|Slow internal RC oscillator precision after software trimming of f SIRC|T = 25 °C A|2|—|+2|%|
| SIRCTRIM|C C|C|Slow internal RC oscillator trimming step|—|—|2.7|—||
| SIRCVAR|C C|C|Variation in f across SIRC temperature and fluctuation in supply voltage, post trimming|—|10|—|+10|%|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 15. ADC_0 characteristic and error definitions**


Offset Error OSE


Gain Error GE


1023

1022

1021

1020

1019

1 LSB ideal = VDD_ADC / 1024

1018

(2)

code out

7

(1)

6

(1) Example of an actual transfer curve

5

(5) ( 2) The ideal transfer curve

4 (3) Differential non-linearity error (DNL)

(4) Integral non-linearity error (INL)

(4)

3 (5) Center of a step of the actual transfer curve

2 (3)

1

1 LSB (ideal)

0

V in(A) (LSB ideal )

Offset Error OSE
###### **3.17.1.1 Input impedance and ADC accuracy** To preserve the accuracy of the A/D converter, it is necessary that analog input pins have low AC impedance. Placing a capacitor with good high frequency characteristics at the input pin of the device, can be effective: the capacitor should be as large as possible, ideally infinite. This capacitor contributes to attenuating the noise present on the input pin; furthermore, it sources charge during the sampling phase, when the analog signal source is a high-impedance source. A real filter, can typically be obtained by using a series resistance with a capacitor on the input pin (simple RC Filter). The RC filtering may be limited according to the value of source impedance of the transducer or circuit supplying the analog signal to be measured. The filter at the input pins must be designed taking into account the dynamic characteristics of the input signal (bandwidth) and the equivalent input impedance of the ADC itself.

86/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** In fact a current sink contributor is represented by the charge sharing effects with the sampling capacitance: being CS and Cp 2 substantially two switched capacitances, with a frequency equal to the conversion rate of the ADC, it can be seen as a resistive path to ground. For instance, assuming a conversion rate of 1MHz, with CS+Cp 2 equal to 3pF, a resistance of 330K is obtained (Reqiv = 1 / (fc*(CS+Cp 2 )), where fc represents the conversion rate at the considered channel). To minimize the error induced by the voltage partitioning between this resistance (sampled voltage on CS+Cp 2 ) and the sum of R S + R F, the external circuit must be designed to respect the following relation **Equation 4** VA  ---------------------RS + RF  12 [--- LSB] REQ The formula above provides a constraint for external network design, in particular on resistive path. **Figure 16. Input equivalent circuit (precise channels)**

**EXTERNAL CIRCUIT** **INTERNAL CIRCUIT SCHEME**

**V** **DD**

**Channel**
**Selection** **Sampling**

**Source** **Filter** **Current Limiter**


**R** **S** **R** **F** **R** **L** **R** **SW**


**R** **AD**


**C** **P1**


**C** **P2** **C** **S**


**V** **A**


**C** **F**

R S Source Impedance

R F Filter Resistance

C F Filter Capacitance

R L Current Limiter Resistance

R SW Channel Selection Switch Impedance

R AD Sampling Switch Impedance

C P Pin Capacitance (two contributions, C P1 and C P2 )

C S Sampling Capacitance


DocID17478 Rev 9 87/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 17. Input equivalent circuit (extended channels)**

**EXTERNAL CIRCUIT** **INTERNAL CIRCUIT SCHEME**

**V** **DD**

**Channel** **Extended**

**Sampling**

**Selection** **Switch**

**Source** **Filter** **Current Limiter**


**R** **AD**


**R** **S** **R** **F** **R** **L** **R** **SW1**


**R** **SW2**


**V** **A** **C** **F** **C** **P1** **C** **P3** **C** **P2** **C** **S**

R S Source Impedance

R F Filter Resistance

C F Filter Capacitance

R L Current Limiter Resistance

R SW Channel Selection Switch Impedance (two contributions R SW1 and R SW2 )

R AD Sampling Switch Impedance

C P Pin Capacitance (three contributions, C P1, C P2 and C P3 )

C S Sampling Capacitance
###### A second aspect involving the capacitance network shall be considered. Assuming the three capacitances C F, C P1 and C P2 initially charged at the source voltage V A (refer to the equivalent circuit reported in Figure 16 ): when the sampling phase is started (A/D switch close), a charge sharing phenomena is installed. **Fi g ure 18. Transient behavior durin g sam p lin g p hase** *V CS Voltage Transient on C S*


V A

V A2

V A1

###### V < 0.5 LSB  1 < (R SW + R AD ) C S << T S

 2 = R L (C S + C P1 + C P2 )

T S *t*

###### In particular two different transient periods can be distinguished:  A first and quick charge transfer from the internal capacitance C P1 and C P2 to the sampling capacitance C S occurs (C S is supposed initially completely discharged): considering a worst case (since the time constant in reality would be faster) in which C P2 is reported in parallel to C P1 (call C P = C P1 + C P2 ), the two capacitances C P and C S are in series, and the time constant is **Equation 5**  1 =  RSW + RAD   ---------------------CPCP +  CSCS

88/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** This relation can again be simplified considering C S as an additional worst condition. In reality, transient is faster, but the A/D converter circuitry has been designed to be robust also in very worst case: the sampling time T s is always much longer than the internal time constant. **Equation 6**  1   RSW + RAD   CS « TS The charge of C P1 and C P2 is redistributed on C S,determining a new value of the voltage V A1 on the capacitance according to the following equation **Equation 7** VA1   CS + CP1 + CP2  = VA   CP1 + CP2  A second charge transfer involves also C F (that is typically bigger than the on-chip capacitance) through the resistance RL: again considering the worst case in which C P2 and C S were in parallel to C P1 (since the time constant in reality would be faster), the time constant is: **Equation 8**  2  RL   CS + CP1 + CP2  In this case, the time constant depends on the external circuit: in particular imposing that the transient is completed well before the end of sampling time T S, a constraints on R L sizing is obtained: **Equation 9** 8.5   2 = 8.5 RL    CS + CP1 + CP2   TS Of course, R L shall be sized also according to the current limitation constraints, in combination with R S (source impedance) and R F (filter resistance). Being C F definitively bigger than C P1, C P2 and C S, then the final voltage V A2 (at the end of the charge transfer transient) will be much higher than V A1 . The following equation must be respected (charge balance assuming now C S already charged at V A1 ): **Equation 10** VA2   CS + CP1 + CP2 + CF  = VA CF  + VA1   CP1 + CP2 + CS  The two transients above are not influenced by the voltage source that, due to the presence of the R F C F filter, is not able to provide the extra charge to compensate the voltage drop on C S with respect to the ideal source V A ; the time constant R F C F of the filter is very high with respect to the sampling time (T S ). The filter is typically designed to act as anti-aliasing

DocID17478 Rev 9 89/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Fi g ure 19. S p ectral re p resentation of in p ut si g nal**


*Analog Source Bandwidth (V* *A* *)*

*Noise*

f 0 *f*

*Anti-Aliasing Filter (f* *F* *= RC Filter pole)*


T C 2 R F C F *(Conversion Rate vs. Filter Pole)*

f F  f 0 *(Anti-aliasing Filtering Condition)*

2 f 0 f C *(Nyquist)*

*Sampled Signal Spectrum (f* *C* *= conversion Rate)*


f F


*f* f 0 f C *f*

###### Calling f 0 the bandwidth of the source signal (and as a consequence the cut-off frequency of the anti-aliasing filter, f F ), according to the Nyquist theorem the conversion rate f C must be at least 2f 0 ; it means that the constant time of the filter is greater than or at least equal to twice the conversion period (T C ). Again the conversion period T C is longer than the sampling time T S, which is just a portion of it, even when fixed channel continuous conversion mode is selected (fastest conversion rate at a specific channel): in conclusion it is evident that the time constant of the filter R F C F is definitively much higher than the sampling time T S, so the charge level on C S cannot be modified by the analog signal source during the time in which the sampling switch is closed. The considerations above lead to impose new constraints on the external circuit, to reduce the accuracy error due to the voltage drop on C S ; from the two charge balance equations above, it is simple to derive Equation 11 between the ideal and real sampled voltage on C S : **Equation 11** VA2 CP1 + CP2 + CF ------------ = -------------------------------------------------------- VA CP1 + CP2 + CF + CS From this formula, in the worst case (when V A is maximum, that is for instance 5 V), assuming to accept a maximum error of half a count, a constraint is evident on C F value: **Equation 12 ADC_0 (10-bit)** CF  2048 CS  **Equation 13 ADC_1 (12-bit)** CF  8192 CS 

90/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **3.17.1.2 ADC electrical characteristics** **Table 43. ADC conversion characteristics ( 10-bit ADC _ 0 )**

DocID17478 Rev 9 91/123

|Col1|Col2|Col3|Col4|Table 42. ADC input leakage current|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|Symbol||C|Parameter|Conditions||Value|||Unit|
|||||||Min|Typ|Max||
|I LKG|CC|C|Input leakage current|T = 40 °C A|No current injection on adjacent pin|—|1|—|nA|
|||C||T = 25 °C A||—|1|—||
|||C||T = 105 °C A||—|8|200||
|||P||T = 125 °C A||—|45|400||

|Symbol|Col2|C|Parameter|Conditions(1)|Value|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|V SS_ADC0|S R|—|Voltage on VSS_HV_ADC0 (ADC_0 reference) pin with respect to ground (V )(2) SS_HV|—|0.1|—|0.1|V|
|V DD_ADC0|S R|—|Voltage on VDD_HV_ADC0 pin (ADC_0 reference) with respect to ground (V ) SS_HV|—|V 0.1 DD_HV_A|—|V + 0.1 DD_HV_A|V|
|V AINx|S R|—|Analog input voltage(3)|—|V 0.1 SS_ADC0|—|V + 0.1 DD_ADC0|V|
|f ADC0|S R|—|ADC_0 analog frequency|—|6|—|32 + 2%|MHz|
|t ADC0_PU|S R|—|ADC_0 power up delay|—|—|—|1.5|µs|
|t ADC0_S|C C|T|Sample time(4)|f = 32 MHz ADC|500|—||ns|
|t ADC0_C|C C|P|Conversion time(5),(6)|f = 32 MHz ADC|0.625|—||µs|
|||||f = 30 MHz ADC|0.700|—|||
|C S|C C|D|ADC_0 input sampling capacitance|—|—|—|3|pF|
|C P1|C C|D|ADC_0 input pin capacitance 1|—|—|—|3|pF|
|C P2|C C|D|ADC_0 input pin capacitance 2|—|—|—|1|pF|
|C P3|C C|D|ADC_0 input pin capacitance 3|—|—|—|1|pF|
|R SW1|C C|D|Internal resistance of analog source|—|—|—|3|k|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 43. ADC conversion characteristics ( 10-bit ADC _ 0 ) ( continued )**

1. V DD = 3.3 V ± 10% / 5.0 V ± 10%, T A = 40 to 125 °C, unless otherwise specified.

2. Analog and digital V SS_HV must be common (to be tied together externally).

3. V AINx may exceed V SS_ADC0 and V DD_ADC0 limits, remaining on absolute maximum ratings, but the results of the
conversion will be clamped respectively to 0x000 or 0x3FF.

4. During the sample time the input capacitance C S can be charged/discharged by the external source. The internal
resistance of the analog source must allow the capacitance to reach its final voltage level within t ADC0_S . After the end of
the sample time t ADC0_S, changes of the analog input voltage have no effect on the conversion result. Values for the
sample clock t ADC0_S depend on programming.

5. This parameter does not include the sample time t ADC0_S, but only the time for determining the digital result and the time to
load the result's register with the conversion result.

6. Refer to ADC conversion table for detailed calculations.

7. PB10 should not have any current injected. It can disturb accuracy on other ADC_0 pins.

8. Total Unadjusted Error: The maximum error that occurs without adjusting Offset and Gain errors. This error is a
combination of Offset, Gain and Integral Linearity errors.

92/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|R SW2|C C|D|Internal resistance of analog source|—||—|—|2|k|
|R AD|C C|D|Internal resistance of analog source|—||—|—|2|k|
|I (7) INJ|S R|—|Input current Injection|Current injectio n on one ADC_0 input, differen t from the convert ed one|V =  DD 3.3 V ± 10%|5|—|5|mA|
||||||V =  DD 5.0 V ± 10%|5|—|5||
|| INL ||C C|T|Absolute value for integral non-linearity|No overload||—|0.5|1.5|LSB|
|| DNL ||C C|T|Absolute differential non-linearity|No overload||—|0.5|1.0|LSB|
|| OFS ||C C|T|Absolute offset error|—||—|0.5|—|LSB|
|| GNE ||C C|T|Absolute gain error|—||—|0.6|—|LSB|
|TUEP|C C|P|Total unadjusted error(8) for precise channels, input only pins|Without current injection||2|0.6|2|LSB|
|||T||With current injection||3||3||
|TUEX|C C|T|Total unadjusted error(8) for extended channel|Without current injection||3|1|3|LSB|
|||T||With current injection||4||4||


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Figure 20. ADC_1 characteristic and error definitions**


Offset Error OSE


Gain Error GE


4095

4094

4093

4092

4091
###### 1 LSB ideal = AVDD / 4096

4090

(2) code out

7

(1)

6

(1) Example of an actual transfer curve

5

(5) (2) The ideal transfer curve

(3) Differential non-linearity error (DNL)

4

(4) Integral non-linearity error (INL)

(4)

(5) Center of a step of the actual transfer curve

3

2 (3)

1

1 LSB (ideal)

0 V in(A) (LSB ideal )

Offset Error OSE

DocID17478 Rev 9 93/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 44. Conversion characteristics ( 12-bit ADC _ 1 )**

94/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions(1)|Value|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|V SS_ADC1|SR|—|Voltage on VSS_HV_ADC1 (ADC_1 reference) pin with respect to ground (V )(2) SS_HV|—|0.1||0.1|V|
|V DD_ADC1 3|SR|—|Voltage on VDD_HV_ADC1 pin (ADC_1 reference) with respect to ground (V ) SS_HV|—|V  DD_HV_A 0.1||V + 0.1 DD_HV_A|V|
|V (3), AINx (4)|SR|—|Analog input voltage(5)|—|V  SS_ADC1 0.1||V + 0.1 DD_ADC1|V|
|f ADC1|SR|—|ADC_1 analog frequency|—|8 + 2%||32 + 2%|MHz|
|t ADC1_PU|SR|—|ADC_1 power up delay|—|1.5|||µs|
|t ADC1_S|CC|T|Sample time(6) VDD=5.0 V|—|440|||ns|
||||Sample time(6) VDD=3.3 V|—|530||||
|t ADC1_C|CC|P|Conversion time(7), (8) VDD=5.0 V|f = 32 MHz ADC1|2|||µs|
||||Conversion time(7), (6) VDD =5.0 V|f = 30 MHz ADC 1|2.1||||
||||Conversion time(7), (6) VDD=3.3 V|f = 20 MHz ADC 1|3||||
||||Conversion time(7), (6) VDD =3.3 V|f = 15 MHz ADC1|3.01||||
|C S|CC|D|ADC_1 input sampling capacitance|—|5|||pF|
|C P1|CC|D|ADC_1 input pin capacitance 1|—|3|||pF|
|C P2|CC|D|ADC_1 input pin capacitance 2|—|1|||pF|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 44. Conversion characteristics ( 12-bit ADC _ 1 ) ( continued )**

1. V DD = 3.3 V ± 10 % / 5.0 V ± 10 %, T A = 40 to 125 °C, unless otherwise specified.

2. Analog and digital V SS_HV must be common (to be tied together externally).

DocID17478 Rev 9 95/123

|Symbol|Col2|C|Parameter|Conditions(1)|Col6|Value|Col8|Col9|Unit|
|---|---|---|---|---|---|---|---|---|---|
|||||||Min|Typ|Max||
|C P3|CC|D|ADC_1 input pin capacitance 3|—||1.5|||pF|
|R SW1|CC|D|Internal resistance of analog source|—||||1|k|
|R SW2|CC|D|Internal resistance of analog source|—||||2|k|
|R AD|CC|D|Internal resistance of analog source|—||||0.3|k|
|I INJ|SR|—|Input current Injection|Current injection on one ADC_1 input, different from the converte d one|V = DD 3.3 V ± 10%|5|—|5|mA|
||||||V = DD 5.0 V ± 10%|5|—|5||
|INLP|CC|T|Absolute Integral non-linearity- Precise channels|No overload|||1|3|LSB|
|INLS|CC|T|Absolute Integral non-linearity- Standard channels|No overload|||1.5|5|LSB|
|DNL|CC|T|Absolute Differential non- linearity|No overload|||0.5|1|LSB|
|OFS|CC|T|Absolute Offset error|—|||2||LSB|
|GNE|CC|T|Absolute Gain error|—|||2||LSB|
|TUEP(9)|CC|P|Total Unadjusted Error for precise channels, input only pins|Without current injection||6||6|LSB|
|||T||With current injection||8||8|LSB|
|TUES(9)|CC|T|Total Unadjusted Error for standard channel|Without current injection||10||10|LSB|
|||T||With current injection||12||12|LSB|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx**

3. PA3, PA7, PA10, PA11 and PE12 ADC_1 channels are coming from V DD_HV_B domain hence VDD_HV_ADC1 should be
within ±100 mV of VDD_HV_B when these channels are used for ADC_1.

4. VDD_HV_ADC1 can operate at 5V condition while V DD_HV_B can operate at 3.3V provided that ADC_1 channels coming
from V DD_HV_B domain are limited in max swing as V DD_HV_B .

5. V AINx may exceed V SS_ADC1 and V DD_ADC1 limits, remaining on absolute maximum ratings, but the results of the
conversion will be clamped respectively to 0x000 or 0xFFF.

6. During the sample time the input capacitance C S can be charged/discharged by the external source. The internal
resistance of the analog source must allow the capacitance to reach its final voltage level within t ADC1_S . After the end of
the sample time t ADC1_S, changes of the analog input voltage have no effect on the conversion result. Values for the
sample clock t ADC1_S depend on programming.

7. Conversion time = Bit evaluation time + Sampling time + 1 Clock cycle delay.

8. Refer to ADC conversion table for detailed calculations.

9. Total Unadjusted Error: The maximum error that occurs without adjusting Offset and Gain errors. This error is a
combination of Offset, Gain and Integral Linearity errors.
##### **3.18 Fast Ethernet Controller**
###### MII signals use CMOS signal levels compatible with devices operating at 3.3 V. Signals are not TTL compatible. They follow the CMOS electrical characteristics. **3.18.1 MII Receive Signal Timing (RXD[3:0], RX_DV, RX_ER, and RX_CLK)** The receiver functions correctly up to a RX_CLK maximum frequency of 25 MHz +1%. There is no minimum frequency requirement. In addition, the system clock frequency must exceed four times the RX_CLK frequency in 2:1 mode and two times the RX_CLK frequency in 1:1 mode. **Table 45. MII Receive Si g nal Timin g** **Figure 21. MII receive signal timing diagram**

|Spec|Characteristic|Min|Max|Unit|
|---|---|---|---|---|
|M1|RXD[3:0], RX_DV, RX_ER to RX_CLK setup|5|—|ns|
|M2|RX_CLK to RXD[3:0], RX_DV, RX_ER hold|5|—|ns|
|M3|RX_CLK pulse width high|35%|65%|RX_CLK period|
|M4|RX_CLK pulse width low|35%|65%|RX_CLK period|


M3


RX_CLK (input)

RXD[3:0] (inputs)
RX_DV
RX_ER

96/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **3.18.2 MII Transmit Signal Timing (TXD[3:0], TX_EN, TX_ER, TX_CLK)** The transmitter functions correctly up to a TX_CLK maximum frequency of 25 MHz +1%. There is no minimum frequency requirement. In addition, the system clock frequency must exceed four times the TX_CLK frequency in 2:1 mode and two times the TX_CLK frequency in 1:1 mode. The transmit outputs (TXD[3:0], TX_EN, TX_ER) can be programmed to transition from either the rising or falling edge of TX_CLK, and the timing is the same in either case. This options allows the use of non-compliant MII PHYs. Refer to the Fast Ethernet Controller (FEC) chapter of the SPC564B74 and SPC56EC74 Reference Manual for details of this option and how to enable it. **Table 46. MII transmit si g nal timin g [(1)]**

1. Output pads configured with SRE = 0b11. **Figure 22. MII transmit signal timing diagram**

|Spec|Characteristic|Min|Max|Unit|
|---|---|---|---|---|
|M5|TX_CLK to TXD[3:0], TX_EN, TX_ER invalid|5|—|ns|
|M6|TX_CLK to TXD[3:0], TX_EN, TX_ER valid|—|25|ns|
|M7|TX_CLK pulse width high|35%|65%|TX_CLK period|
|M8|TX_CLK pulse width low|35%|65%|TX_CLK period|


M7


TX_CLK (input)

TXD[3:0] (outputs)
TX_EN
TX_ER


M8

###### **3.18.3 MII Async Inputs Signal Timing (CRS and COL)** **Table 47. MII As y nc In p uts Si g nal Timin g [(1)]**

1. Output pads configured with SRE = 0b11.

DocID17478 Rev 9 97/123

|Spec|Characteristic|Min|Max|Unit|
|---|---|---|---|---|
|M9|CRS, COL minimum pulse width|1.5|—|TX_CLK period|


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 23. MII async inputs timing diagram**

CRS, COL **3.18.4 MII Serial Management Channel Timing (MDIO and MDC)** The FEC functions correctly with a maximum MDC frequency of 2.5 MHz. **Table 48. MII serial mana g ement channel timin g [(1)]**

|Spec|Characteristic|Min|Max|Unit|
|---|---|---|---|---|
|M10|MDC falling edge to MDIO output invalid (minimum propagation delay)|0|—|ns|
|M11|MDC falling edge to MDIO output valid (max prop delay)|—|25|ns|
|M12|MDIO (input) to MDC rising edge setup|28|—|ns|
|M13|MDIO (input) to MDC rising edge hold|0|—|ns|
|M14|MDC pulse width high|40%|60%|MDC period|
|M15|MDC pulse width low|40%|60%|MDC period|



1. Output pads configured with SRE = 0b11. **Figure 24. MII serial management channel timing diagram**

MDC (output)

MDIO (output)

MDIO (input)

98/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics**
##### **3.19 On-chip peripherals**
###### **3.19.1 Current consumption** **Table 49. On-chip p eri p herals current consum p tion [(1)]**

DocID17478 Rev 9 99/123

|Symbol|Col2|C|Parameter|Conditions|Col6|Value(2)|Unit|
|---|---|---|---|---|---|---|---|
|||||||Typ||
|I DD_HV_A(CAN)|CC|D|CAN (FlexCAN) supply current on V DD_HV_A|500 Kbps|Total (static + dynamic) consumption: FlexCAN in loop-back mode XTAL@8 MHz used as CAN engine clock source Message sending period is 580 µs|7.652  f + 84.73 periph|µA|
|||||125 Kbps||8.0743  f + 26.757 periph||
|I DD_HV_A(eMIOS)|CC|D|eMIOS supply current on V DD_HV_A|Static consumption: eMIOS channel OFF Global prescaler enabled||28.7  f periph||
|||||Dynamic consumption: It does not change varying the frequency (0.003 mA)||3||
|I DD_HV_A(SCI)|CC|D|SCI (LINFlex) supply current on V DD_HV_A|Total (static + dynamic) consumption: LIN mode Baudrate: 20 Kbps||4.7804  f + 30.946 periph||
|I DD_HV_A(SPI)|CC|D|SPI (DSPI) supply current on V DD_HV_A|Ballast static consumption (only clocked)||1||
|||||Ballast dynamic consumption (continuous communication): Baudrate: 2 Mbit Transmission every 8 µs Frame: 16 bits||16.3  f periph||
|I DD_HV_A(ADC)|CC|D|ADC supply current on V DD_HV_A|V = 5.5 V DD|Ballast static consumption (no conversion)|0.0409  f periph|mA|
|||||V = 5.5 V DD|Ballast dynamic consumption (continuous conversion)|0.0049  f periph||


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Table 49. On-chip p eri p herals current consum p tion [(1)]**

1. Operating conditions: T A = 25 °C, f periph = 8 MHz to 120 MHz.

2. f is in absolute value.
periph **3.19.2 DSPI characteristics** **Table 50. DSPI timin g**

100/123 DocID17478 Rev 9

|Symbol|Col2|C|Parameter|Conditions|Col6|Value(2)|Unit|
|---|---|---|---|---|---|---|---|
|||||||Typ||
|IDD_HV_ADC0|CC|D|ADC_0 supply current on V DD_HV_ADC0|V = 5.5 V DD|Analog static consumption (no conversion)|200|µA|
||||||Analog dynamic consumption (continuous conversion)|4|mA|
|IDD_HV_ADC1|CC|D|ADC_1 supply current on V DD_HV_ADC1|V = 5.5 V DD|Analog static consumption (no conversion)|300|µA|
|||||V = 5.5 V DD|Analog dynamic consumption (continuous conversion)|6|mA|
|I DD_HV(FLASH)|CC|D|CFlash + DFlash supply current on V DD_HV_ADC|V = 5.5 V DD|—|13.25|mA|
|I DD_HV(PLL)|CC|D|PLL supply current on V DD_HV|V = 5.5 V DD|—|0.0031  f periph||

|Spec|Characteristic|Symbol|Value|Col5|Unit|
|---|---|---|---|---|---|
||||Min|Max||
|1|DSPI Cycle Time|t SCK|Refer note(1)|—|ns|
|—|Internal delay between pad associated to SCK and pad associated to CSn in master mode for CSn1->0| t CSC|—|115|ns|
|—|Internal delay between pad associated to SCK and pad associated to CSn in master mode for CSn1->1| t ASC|15|—|ns|
|2|CS to SCK Delay(2)|t CSC|7|—|ns|
|3|After SCK Delay(3)|t ASC|15|—|ns|
|4|SCK Duty Cycle|t SDC|0.4  t SCK|0.6  t SCK|ns|


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 50. DSPI timin g ( continued )**

1. This value of this parameter is dependent upon the external device delays and the other parameters mentioned in this
table.

2. The maximum value is programmable in DSPI_CTAR *n* [PSSCK] and DSPI_CTAR *n* [CSSCK]. For SPC564B74 and SPC56EC74, the spec value of t CSC will be attained only if T DSPI x PSSCK x CSSCK >  t CSC .

3. The maximum value is programmable in DSPI_CTAR *n* [PASC] and DSPI_CTAR *n* [ASC]. For SPC564B74 and SPC56EC74, the spec value of t ASC will be attained only if T DSPI x PASC x ASC >  t ASC.

4. The parameter value is obtained from t SUSS and t SUO for slave.

5. This number is calculated assuming the SMPL_PT bitfield in DSPI_MCR is set to 0b00.

6. For DSPI1, the Data Hold Time for Outputs in Master (MTFE = 0) is 2 ns.

7. For DSPI1, the Data Hold Time for Outputs in Master (MTFE = 1, CPHA = 0) is 2 n.

8. For DSPI1, the Data Hold Time for Outputs in Master (MTFE = 1, CPHA = 1) is 2 ns.

|Spec|Characteristic|Symbol|Value|Col5|Unit|
|---|---|---|---|---|---|
||||Min|Max||
|—|Slave Setup Time (SS active to SCK setup time)|t SUSS|5|—|ns|
|—|Slave Hold Time (SS active to SCK hold time)|t HSS|10|—|ns|
|5|Slave Access Time (SS active to SOUT valid)(4)|t A|—|42|ns|
|6|Slave SOUT Disable Time (SS inactive to SOUT High-Z or invalid)|t DIS|—|25|ns|
|7|CSx to PCSS time|t PCSC|0|—|ns|
|8|PCSS to PCSx time|t PASC|0|—|ns|
|9|Data Setup Time for Inputs Master (MTFE = 0) Slave Master (MTFE = 1, CPHA = 0)(5) Master (MTFE = 1, CPHA = 1)|t SUI|36 5 36 36|— — — —|ns ns ns ns|
|10|Data Hold Time for Inputs Master (MTFE = 0) Slave Master (MTFE = 1, CPHA = 0)(5) Master (MTFE = 1, CPHA = 1)|t HI|0 4 0 0|— — — —|ns ns ns ns|
|11|Data Valid (after SCK edge) Master (MTFE = 0) Slave Master (MTFE = 1, CPHA = 0) Master (MTFE = 1, CPHA = 1)|t SUO|— — — —|12 37 12 12|ns ns ns ns|
|12|Data Hold Time for Outputs Master (MTFE = 0) Slave Master (MTFE = 1, CPHA = 0) Master (MTFE = 1, CPHA = 1)|t HO|0(6) 9.5 0(7) 0(8)|— — — —|ns ns ns ns|



DocID17478 Rev 9 101/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 25. DSPI classic SPI timing–master, CPHA = 0**

2 3

CSx

4 1

SCK Output

(CPOL = 0)

SCK Output

(CPOL = 1)


SIN

SOUT

CSx

SCK Output

(CPOL = 0)

SCK Output

(CPOL = 1)


First Data Data Last Dat ~~a~~

First Data Data Last Data

Note: Numbers shown reference *Table 50* .
###### **Figure 26. DSPI classic SPI timing–master, CPHA = 1**


12 11


SOUT


First Data Data Last Data

Note: Numbers shown reference *Table 50* .


102/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Figure 27. DSPI classic SPI timing–slave, CPHA = 0**

SS

SCK Input

(CPOL = 0)

SCK Input

(CPOL = 1)

Note: Numbers shown reference *Table 50* . **Figure 28. DSPI classic SPI timing–slave, CPHA = 1**

SS

SCK Input

(CPOL = 0)

SCK Input

(CPOL = 1)

5 12 6

SOUT First Data Data Last Data

Note: Numbers shown reference *Table 50* .

DocID17478 Rev 9 103/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 29. DSPI modified transfer format timing–master, CPHA = 0**

CSx

4 1

SCK Output

(CPOL = 0)

SCK Output

(CPOL = 1)


SIN

SOUT

CSx


First Data Data Last Data

12 11

First Data Data Last Data

Note: Numbers shown reference *Table 50* .
###### **Figure 30. DSPI modified transfer format timing–master, CPHA = 1**


SCK Output

(CPOL = 0)

SCK Output

(CPOL = 1)

SIN

SOUT


First Data Data Last Data

First Data Data Last Data

Note: Numbers shown reference *Table 50* .


104/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Figure 31. DSPI modified transfer format timing–slave, CPHA = 0**

SS

SCK Input

(CPOL = 0)

SCK Input

(CPOL = 1)


SOUT

SIN

SS

SCK Input

(CPOL = 0)

SCK Input

(CPOL = 1)

SOUT


First Data Data Last Data

9 10

First Data Data Last Data

Note: Numbers shown reference *Table 50* .
###### **Figure 32. DSPI modified transfer format timing–slave, CPHA = 1**

5 12 6


First Data


Data


Last Data


Note: Numbers shown reference *Table 50* .

DocID17478 Rev 9 105/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 33. DSPI PCS strobe (PCSS) timing**

7 8

PCSS

CSx

Note: Numbers shown reference *Table 50* . **3.19.3 Nexus characteristics** **Table 51. Nexus debu g p ort timin g [(1)]**

|Spec|Characteristic|Symbol|Min|Max|Unit|
|---|---|---|---|---|---|
|1|MCKO Cycle Time(2)|t MCYC|16.3|—|ns|
|2|MCKO Duty Cycle|t MDC|40|60|%|
|3|MCKO Low to MDO, MSEO, EVTO Data Valid(3)|t MDOV|–0.1|0.25|t MCYC|
|4|EVTI Pulse Width|t EVTIPW|4.0|—|t TCYC|
|5|EVTO Pulse Width|t EVTOPW|1||t MCYC|
|6|TCK Cycle Time(4)|t TCYC|40|—|ns|
|7|TCK Duty Cycle|t TDC|40|60|%|
|8|TDI, TMS Data Setup Time|t NTDIS, t NTMSS|8|—|ns|
|9|TDI, TMS Data Hold Time|t NTDIH, t NTMSH|5|—|ns|
|10|TCK Low to TDO Data Valid|t JOV|0|25|ns|



1. JTAG specifications in this table apply when used for debug functionality. All Nexus timing relative to MCKO is measured
from 50% of MCKO and 50% of the respective signal. Nexus timing specified at V DDE = 4.0 – 5.5 V, T A = T L to T H, and
C L = 30 pF with SRC = 0b11.

2. MCKO can run up to 1/2 of full system frequency. It can also run at system frequency when it is <60 MHz.

3. MDO, MSEO, and EVTO data is held valid until next MCKO low cycle.

4. The system clock frequency needs to be three times faster than the TCK frequency.

106/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Figure 34. Nexus output timing**

MCKO


MDO

MSEO

EVTO
###### EVTI


Output Data Valid

DocID17478 Rev 9 107/123


122


-----

###### **Electrical Characteristics SPC564Bxx-SPC56ECxx** **Figure 35. Nexus TDI, TMS, TDO timing**

TCK

TMS, TDI

TDO **3.19.4 JTAG characteristics** **Table 52. JTAG characteristics **

|No.|Symbol|Col3|C|Parameter|Value|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|1|t JCYC|CC|D|TCK cycle time|64|—|—|ns|
|2|t TDIS|CC|D|TDI setup time|10|—|—|ns|
|3|t TDIH|CC|D|TDI hold time|5|—|—|ns|
|4|t TMSS|CC|D|TMS setup time|10|—|—|ns|
|5|t TMSH|CC|D|TMS hold time|5|—|—|ns|
|6|t TDOV|CC|D|TCK low to TDO valid|—|—|33|ns|



108/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Electrical Characteristics** **Table 52. JTAG characteristics ( continued )** **Figure 36. Timing diagram - JTAG boundary scan**

TCK

|No.|Symbol|Col3|C|Parameter|Value|Col7|Col8|Unit|
|---|---|---|---|---|---|---|---|---|
||||||Min|Typ|Max||
|7|t TDOI|CC|D|TCK low to TDO invalid|6|—|—|ns|
|—|t TDC|CC|D|TCK Duty Cycle|40|—|60|%|
|—|t TCKRISE|CC|D|TCK Rise and Fall Times|—|—|3|ns|


DATA INPUTS

DATA OUTPUTS

DATA OUTPUTS


INPUT DATA VALID

OUTPUT DATA VALID

Note: Numbers shown reference *Table 52* .

DocID17478 Rev 9 109/123


122


-----

###### **Package characteristics SPC564Bxx-SPC56ECxx**
### **4 Package characteristics**
##### **4.1 ECOPACK [®]**
###### In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK [®] packages, depending on their level of environmental compliance. ECOPACK [®] specifications, grade definitions and product status are available at: www.st.com . ECOPACK [®] is an ST trademark.
##### **4.2 Package mechanical data**
###### **4.2.1 LQFP176 package mechanical drawing** **Figure 37. LQFP176 package mechanical drawing**


C Seating plane

A A2

A1 c

HD

D

ZD

|1|Col2|
|---|---|
||ccc C|
|||



133 88

b

45


0.25 mm

gauge plane

k


ZE


A1
L

L1

E HE

|Col1|89|Col3|
|---|---|---|
||||
|||88|


identification



44


e


1T_ME


110/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Package characteristics** **Table 53. LQFP176 mechanical data [(1)]**

1. Controlling dimension: millimeter.

2. Values in inches are converted from mm and rounded to 4 decimal digits.

3. L dimension is measured at gauge plane at 0.25 mm above the seating plane.

DocID17478 Rev 9 111/123

|Symbol|mm|Col3|Col4|inches(2)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min|Typ|Max|Min|Typ|Max|
|A|1.400||1.600|||0.063|
|A1|0.050||0.150|0.002|||
|A2|1.350||1.450|0.053||0.057|
|b|0.170||0.270|0.007||0.011|
|C|0.090||0.200|0.004||0.008|
|D|23.900||24.100|0.941||0.949|
|E|23.900||24.100|0.941||0.949|
|e||0.500|||0.020||
|HD|25.900||26.100|1.020||1.028|
|HE|25.900||26.100|1.020||1.028|
|L(3)|0.450||0.750|0.018||0.030|
|L1||1.000|||0.039||
|ZD||1.250|||0.049||
|ZE||1.250|||0.049||
|q|0 °||7 °|0 °||7 °|
|Tolerance|mm|||inches|||
|ccc|0.080|||0.0031|||


122


-----

###### **Package characteristics SPC564Bxx-SPC56ECxx** **4.2.2 LQFP208 package mechanical drawing** **Figure 38. LQFP208 mechanical drawing**

Note: Exact sha p e of each corner is o p tional.

112/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Package characteristics** **Table 54. LQFP208 mechanical data **

DocID17478 Rev 9 113/123

|Ref|mm|Col3|Col4|mm|Col6|Col7|
|---|---|---|---|---|---|---|
||Min|Typ|Max|Min|Typ|Max|
|A|||1.6|||1.6|
|A1|0.05||0.15|0.05|0.1|0.15|
|A2|1.3|1.35|1.45|1.3|1.35|1.45|
|B|0.17||0.27|0.17|0.22|0.27|
|c|0.09||0.2|0.11|0.15|0.19|
|D||30||29.8|30|30.2|
|D1||28||27.8|28|28.2|
|D3||25.5|||25.5||
|e||0.5|||0.5||
|E||30||29.8|30|30.2|
|E1||28||27.8|28|28.2|
|E3||25.5|||25.5||
|L|0.45|0.6|0.75|0.4|0.5|0.6|
|L1||1||1|||
|K|0 °|3.5 °|7.0 °|1 °|3 °|5 °|


122


-----

###### **Package characteristics SPC564Bxx-SPC56ECxx** **4.2.3 LBGA256 package mechanical drawing** **Figure 39. LBGA256 mechanical drawing**

114/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Package characteristics**

|Col1|Table 55. LBGA256 mechanical data|Col3|Col4|
|---|---|---|---|
|Ref|mm|||
||Min|Typ|Max|
|A|1.210||1.700|
|A1|0.300|||
|A2||0.300||
|A4|||0.800|
|b|0.400|0.500|0.600|
|D|16.800|17.000|17.200|
|D1||15.000||
|E|16.800|17.000|17.200|
|E1||15.000||
|e|0.900|1.000|1.100|
|Z|0.750|1.000|1.250|
|ddd|||0.200| *Note: The package is designed according to the JEDEC standard No 95-1 Section 14 dedicated to * *Ball Grid Array Package Design Guide.*

DocID17478 Rev 9 115/123


122


-----

###### **Ordering information SPC564Bxx-SPC56ECxx**
### **5 Ordering information**
###### **Figure 40. Ordering information scheme**

**Example code:**

**SPC56** **4** **C** **74** **L7** **C** **8** **E** **0** **Y**

*Product identifier* *Core* *Family* *Memory* *Package* *Temperature* *CPU Frequency* *EEPROM Options* *Conditioning*

Y = Tray
X = Tape and Reel

0 = No option
E = Ethernet

C = CSE + Ethernet

0 = NO EEPROM

E = EEPROM

8 = 80 MHz

9 = 120 MHz

B = –40 to 105 °C

C = –40 to 125 °C

L7 = LQFP176

L8 = LQFP208
B3 = LBGA256

74 = 3 MB

70 = 2 MB

64 = 1.5 MB

B = Body
C = Gateway

4 = e200z4d

E = e200z4d + e200

z0h

SPC56 = Power

Architecture in

90 nm

116/123 DocID17478 Rev 9


-----

###### **SPC564Bxx-SPC56ECxx Abbreviations**
### **Appendix A Abbreviations**
###### Table 56 lists abbreviations used but not defined elsewhere in this document.

DocID17478 Rev 9 117/123

|Col1|Table 56. Abbreviations|
|---|---|
|Abbreviation|Meaning|
|CS|Chip select|
|EVTO|Event out|
|MCKO|Message clock out|
|MDO|Message data out|
|MSEO|Message start/end out|
|MTFE|Modified timing format enable|
|SCK|Serial communications clock|
|SOUT|Serial data out|
|TBD|To be defined|
|TCK|Test clock input|
|TDI|Test data input|
|TDO|Test data output|
|TMS|Test mode select|


122


-----

###### **Revision history SPC564Bxx-SPC56ECxx**
### **Revision history**
###### Table 57 summarizes revisions to this document.

118/123 DocID17478 Rev 9

|Col1|Col2|Table 57. Revision history|
|---|---|---|
|Date|Revision|Changes|
|01-Jun-2010|1|Initial Release|
|17-Dec-2010|2|– Editing and formatting updates throughout the document. – Updated Voltage regulator capacitance connection figure. – Added a new sub-section “V Options” DD_BV – Program and erase specifications: Updated Tdwprogram TYP to 22 us Updated T128Kpperase Max to 5000 ms Added t parameter ESUS – Added recommendation in the Voltage regulator electrical characteristics section. – Added Crystal description table in Fast external crystal oscillator (4 to 140 MHz) electrical characteristics section and corrected the cross-reference to the same. – Added new sections - Pad types, System pins and functional ports – Updated TYP numbers in the Flash program and erase specifications table – Added a new table: Program and erase specifications (Data Flash) – Flash read access timing table: Added Data flash memory numbers – Flash power supply DC electrical characteristics table: Updated IDFREAD and IDFMOD values for Data flash, Removed IDFLPW parameter – Updated feature list. – SPC564Bxx and SPC56ECxx family comparison table: Updated ADC channels and added ADC footnotes. – SPC564Bxx and SPC56ECxx block diagram: Updated ADC channels and added legends. – SPC564Bxx and SPC56ECxx series block summary: Added new blocks. – Functional Port Pin Descriptions table: Added OSC32k_XTAL and OSC32k_EXTAL function at PB8 and PB9 port pins. – Electrical Characteristics: Replaced VSS with VSS_HV throughout the section. – Absolute maximum ratings, Recommended operating conditions (3.3 V) and Recommended operating conditions (5.0 V) tables: VRC_CTRL min is updated to "0". – Recommended operating conditions (3.3 V) and Recommended operating conditions (5.0 V) tables: Clarified VIN parameter, clarified footnote 2 in both tables. – LQFP thermal characteristics section: Added numbers for LQFP packages. – Low voltage power domain electrical characteristics table: Clarified footnotes based upon review comments. – Code flash memory—Program and erase specifications: Updated tESRT to 20 ms. – ADC electrical characteristics section: Replace ADC0 with ADC_0 and ADC1 with ADC_1 throughout the document. DSPI characteristics section: Replaced PCSx with CSx in all figures and tables.|


-----

###### **SPC564Bxx-SPC56ECxx Revision history**

DocID17478 Rev 9 119/123

|Col1|Col2|Table 57. Revision history (continued)|
|---|---|---|
|Date|Revision|Changes|
|28-Apr-2011|3|– Replaced VIL min from –0.4 V to –0.3 V in the following tables:  - I/O input DC electrical characteristics - Reset electrical characteristics - Fast external crystal oscillator (4 to 40 MHz) electrical characteristics – Updated Crystal oscillator and resonator connection scheme figure – Specified NPN transistor as the recommended BCP68 transistor throughout the document – Code and Data flash memory—Program and erase specifications tables: Renamed the parameter t T ESUS to eslat – Revised the footnotes in the “Functional port pin descriptions” table. – In the “System pin descriptions” table, added a footnote to the A pads regarding not using IBE. For ports PB[12–15], changed ANX to ADC0_X. – Revised the presentation of the ADC functions on the following ports: PB[4–7] PD[0–11] – ADC conversion characteristics (10-bit ADC_0) table and Conversion characteristics (12-bit ADC_1) table- Updated footnote 5 and 7 respectively for the definition of the conversion time. – Data flash memory—Program and erase specifications: Updated T to wprogram 500 µs and T to 500 µs. Corrected Teslat classsification from “C” to 16Kpperase “D”. – Code flash memory—Program and erase specifications: Corrected Teslat classification from “C” to “D”. – Flash Start-up time/Switch-off time: Changed T classification from “C” FLARSTEXIT to “D”. – Functional port pin description: Added a footnote at the PB [9] port pin. – Absolute maximum ratings table: Added footnote 1. – Low voltage power domain electrical characteristics table: Updated IDDHALT, IDDSTOP, IDDSTBY3, IDDSTDBY2, IDDSTDBY1. – Updated commercial product code structure. – Slow external crystal oscillator (32 kHz) electrical characteristics table: Updated g, V, I and I mSXOSC SXOSC SXOSCBIAS SXOSC. – FMPLL electrical characteristics table: Updated t LTJIT. – Fast internal RC oscillator (16 MHz) electrical characteristics table: Updated TFIRCSU and IFIRCPWD. – MII serial management channel timing table: Updated M12 – JTAG characteristics table: Updated t TDOV. – Low voltage monitor electrical characteristics table: Updated VLVDHV3H, VLVDHV3L, VLVDHV5H, VLVDHV5L. – DSPI electricals table: Updated spec 1, 5, 6. Updated footnote 2 and 3. Added   t, t, t, t CSC ASC SUSS HSS. – IO consumption table: Updated all parameter values.  – DSPI electricals: Updated t maxto 115 ns. CSC – Low voltage power domain electrical characteristics table: Added footnote 9. – ADC electrical characteristics: Added 2 notes above 10-bit and 12-bit conversion tables.|


122


-----

###### **Revision history SPC564Bxx-SPC56ECxx**

120/123 DocID17478 Rev 9

|Col1|Col2|Table 57. Revision history (continued)|
|---|---|---|
|Date|Revision|Changes|
|01-Dec-2011|4|– Interchanged the denominator with numerator in Equation 11 of Input impedance and ADC accuracy section – Removed the note (All ADC conversion characteristics described in the table below are applicable only for the precision channels. The data for semi-precision and extended channels is awaited and same will be subsequently updated in later revs.) in the ADC electrical characteristics section. – Table 49 (On-chip peripherals current consumption). Replaced IDD_HV_ADC with IDD_HV_ADC0 and IDD_HV_ADC1 values as per ADC specs – In Table 43, the minimum sample time of ADC0 changed to 500 at 32 MHz – In Table 43, removed the entry for sample time at 30 MHz – In Table 44, changed TUEX to TUES and INLX to INLS (Extended channels are not supported by the device. So, changed to standard channel.)|
|04-Mar-2013|5|– Updated the pins 23 and 24 of Figure 2: 176-pin LQFP configuration. – Updated unit of measure in Table 44: Conversion characteristics (12-bit ADC_1) – Modified the value to typical value in Table 49: On-chip peripherals current consumption – Added footnote to t parameter in Table 26: Code flash memory—Program ESRT and erase specifications – Added footnote to t parameter in Table 27: Data flash memory—Program ESRT and erase specifications – Updated Table 29: Flash memory read access timing. – Updated Notes 2 and Notes 3 of Table 10: Recommended operating conditions (3.3 V) and Table 11: Recommended operating conditions (5.0 V) respectively. – Updated the footnote1 of Table 10: Recommended operating conditions (3.3 V) and Table 11: Recommended operating conditions (5.0 V) – Updated V to V for C and I in Table 23: Voltage DD_HV_A DD_BV DEC2 DD_HV_A regulator electrical characteristics and deleted footnote3 – Updated the dedicated number of channels for 12-bit ADC in family comparison tables – Updated the values of f parameters and conditions of  in Table 41: SIRC, SIRCVAR Slow internal RC oscillator (128 kHz) electrical characteristics – Updated second footnote in Table 11: Recommended operating conditions (5.0 V), – Updated the value of t in Table 43: ADC conversion characteristics (10- ADC0_PU bit ADC_0) – Updated the IDD values in Table 25: Low voltage power domain electrical characteristics – Added footnote to Table 25: Low voltage power domain electrical characteristics related to current drawn from V and V DD_HV_A DD_HV_B – Updated entire Section 3.17.1.1: Input impedance and ADC accuracy – Updated the values of VLPREG in Table 23: Voltage regulator electrical characteristics. – Updated the values of V in Table 23: Voltage regulator electrical LPREG characteristics. – Added T = 25 °C, min and max values of V in Table 23: Voltage regulator A MREG electrical characteristics – Added T = 25 °C, min and max values of V in Table 23: Voltage regulator A LPREG electrical characteristics|


-----

###### **SPC564Bxx-SPC56ECxx Revision history**

DocID17478 Rev 9 121/123

|Col1|Col2|Table 57. Revision history (continued)|
|---|---|---|
|Date|Revision|Changes|
|04-Mar-2013|5 (cont.)|– Updated the min, max and typical values of V and V in LVDLVCORL LVDLVBKPL Table 24: Low voltage monitor electrical characteristics – Updated values of gmFXOSC in Table 36: Fast external crystal oscillator (4 to 40 MHz) electrical characteristics – Updated values of gmSXOSC in Table 38: Slow external crystal oscillator (32 kHz) electrical characteristics – Updated the footnote 5 for T in Table 43: ADC conversion characteristics ADC0_C (10-bit ADC_0) – Updated the footnotes of Table 25: Low voltage power domain electrical characteristics|
|17-Sep-2013|6|– Updated Disclaimer|
|28-Nov-2014|7|– Removed occurrences of 208BGA from Table 2: SPC564Bxx and SPC56ECxx family comparison. – Added PM[3] and PM[4] in the figure note 1 of Figure 4: 256-pin BGA configuration. – Added a table note inTable 20: I/O supplies. – Updated Figure 8: Voltage regulator capacitance connection and added a note in this figure. – Removed before trimming value for V, updated after trimming min value of MREG V from1.24 V to 1.20 V, updated after trimming min value of V from MREG LPREG 1.225 V to 1.17 V, updated after trimming typical value of V from1.25 V to LPREG 1.27 V and updated after trimming max value of V from1.275 V to 1.32 V LPREG in Table 23: Voltage regulator electrical characteristics. – Changed min value of V andV from 1.12 V to 1.08 V, and LVDLVCORL LVDLVBKPL removed typical value of V andV in Table 24: Low voltage LVDLVCORL LVDLVBKPL monitor electrical characteristics – Updated max values at 120 MHz for IDDRUN from 200 mA to 208 mA and from 270 mA to 280 mA; updated max value at T = 125 °C for IDDHALT from 80 mA to A 100 mA; updated max value at T = 25 °C for IDDSTOP from 1.2 mA to 5 mA and A at T = 125 °C from 60 mA to 72 mA; updated max value at T = 25 °C for A A IDDSTDBY3 from 75 µA to 96 µA and at T = 125 °C from 1200 µA to 2400 µA; A updated max value at T = 25 °C for IDDSTDBY2 from 70 µA to 92 µA and at A T = 125 °C from 1100 µA to 2000 µA; updated max value at T = 25 °C for A A IDDSTDBY1 from 65 µA to 85 µA and at T = 125 °C from 650 µA to 1100 µA; A updated 1st footnote in Table 25: Low voltage power domain electrical characteristics. – Added a footnote below Table 29: Flash memory read access timing. – Updated the formula in Eq. 11 in Section 3.17.1.1: Input impedance and ADC accuracy. – Updated legend in Figure 16: Input equivalent circuit (precise channels) – Updated min and max values for g at V = 5.0 V ± 10% from 4 mA/V to mFXOSC DD 6.5 mA/V and from 20 mA/V to 25 mA/V inTable 36: Fast external crystal oscillator (4 to 40 MHz) electrical characteristics – Added Figure 17: Input equivalent circuit (extended channels). – Updated t value to 1.5 as max and added footnote for I in Table 43: ADC0_PU INJ ADC conversion characteristics (10-bit ADC_0).|


122


-----

###### **Revision history SPC564Bxx-SPC56ECxx**

122/123 DocID17478 Rev 9

|Col1|Col2|Table 57. Revision history (continued)|
|---|---|---|
|Date|Revision|Changes|
|28-Nov-2014|7 (cont.)|– Added Category column in Table 44: Conversion characteristics (12-bit ADC_1). – Added the IDD_HV_ADC0 values in Table 49: On-chip peripherals current consumption.|
|16-Jun-2015|8|Updated Figure 37: LQFP176 package mechanical drawing and Figure 40: Ordering information scheme.|
|11-Mar-2016|9|– Added package silhouette on the cover page – Removed Figure 4: LBGA208 configuration – Removed LBGA208 column in Table 4: System pin descriptions and in Table 5: Functional port pin descriptions – Table 12: LQFP thermal characteristics: for “R ” row, changed Max value JA relating to conditions “Single-layer board—1s” and “Four-layer board—2s2p” from “TBD” to “43” and “33.9”, respectively – Removed Table 13: LBGA208 thermal characteristics – Table 13: LBGA256 thermal characteristics: for “R ” row, changed Max value JA relating to conditions “Single-layer board—1s” and “Four-layer board—2s2p” from “TBD” to “44.3” and “31”, respectively – Removed LBGA208 row in Table 20: I/O supplies – Removed Section 4.2.3: LBGA208 package mechanical drawing – In Table 25: Low voltage power domain electrical characteristics, updated notes “Only for the “P” classification: LPreg ON, HPVreg OFF, 96 KB RAM ON, device configured for...”, “LPreg ON, HPVreg OFF, 64 KB RAM ON, device configured for...”, and “LPreg ON, HPVreg OFF, 8 KB RAM ON, device configured for...” – In Table 49: On-chip peripherals current consumption, changed IDD_HV_ADC1 value from “300 × f “ to “300” periph|


-----

###### **SPC564Bxx-SPC56ECxx**


**IMPORTANT NOTICE – PLEASE READ CAREFULLY**


STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on
ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order
acknowledgement.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or
the design of Purchasers’ products.


No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. All other product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2016 STMicroelectronics – All rights reserved


DocID17478 Rev 9 123/123


123


-----

