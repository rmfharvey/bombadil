# **Modules**

# **Product Technical Specification**

## **RC76xx**

March 2025 41113440 Rev. 16


Preface

##### **Important Notice**


Information relating to this product and the application or design described herein is believed to be reliable, however
such information is provided as a guide only and Semtech assumes no liability for any errors in this document, or for
the application or design described herein.


Semtech reserves the right to make changes to the product or this document at any time without notice. Buyers
should obtain the latest relevant information before placing orders and should verify that such information is current
and complete. Semtech warrants performance of its products to the specifications applicable at the time of sale, and
all sales are made in accordance with Semtech’s standard terms and conditions of sale.


SEMTECH PRODUCTS ARE NOT DESIGNED, INTENDED, AUTHORIZED OR WARRANTED TO BE SUITABLE FOR USE
IN LIFE-SUPPORT APPLICATIONS, DEVICES OR SYSTEMS, OR IN NUCLEAR APPLICATIONS IN WHICH THE FAILURE
COULD BE REASONABLY EXPECTED TO RESULT IN PERSONAL INJURY, LOSS OF LIFE OR SEVERE PROPERTY OR

ENVIRONMENTAL DAMAGE. INCLUSION OF SEMTECH PRODUCTS IN SUCH APPLICATIONS IS UNDERSTOOD TO BE


UNDERTAKEN SOLELY AT THE CUSTOMER’S OWN RISK. Should a customer purchase or use Semtech products for
any such unauthorized application, the customer shall indemnify and hold Semtech and its officers, employees,
subsidiaries, affiliates, and distributors harmless against all claims, costs damages and attorney fees which could
arise.


The Semtech name and logo are registered trademarks of the Semtech Corporation. All other trademarks and trade
names mentioned may be marks and names of Semtech or their respective companies. Semtech reserves the right
to make changes to, or discontinue any products described in this document without further notice. Semtech makes
no warranty, representation or guarantee, express or implied, regarding the suitability of its products for any
particular purpose. All rights reserved.

##### **Wireless Communications**


Due to the nature of wireless communications, transmission and reception of data can never be guaranteed. Data
may be delayed, corrupted (i.e., have errors) or be totally lost. The Semtech product should not be used in situations
where failure to transmit or receive data could result in damage of any kind to the user or any other party, including
but not limited to personal injury, death, or loss of property. Semtech accepts no responsibility for damages of any
kind resulting from delays or errors in data transmitted or received using the Semtech product, or for failure of the
Semtech product to transmit or receive such data.

##### **Safety**


Do not operate the Semtech product in areas where blasting is in progress, where explosive atmospheres may be
present, near medical equipment, near life support equipment, or near any equipment which may be susceptible to
any form of radio interference. In such areas, the Semtech product should be powered off.

##### **Qualcomm Licenses**


Semtech's cellular modules are sold subject to certain notices and restrictions regarding patent licenses from
Qualcomm Incorporated. These notices and restrictions are available at www.sierrawireless.com/qualcommnotices.


Rev. 16 March 2025 2 41113440


Product Technical Specification

##### **Sierra Wireless**


Semtech Corporation purchased Sierra Wireless in January 2023. The Sierra Wireless brand is gradually being
phased out. During the phase-out period, references to both “Semtech” and “Sierra Wireless” may appear in product
documentation.







|Contact Information|Col2|
|---|---|
|Sales information and technical support,<br>including warranty and returns|Web: sierrawireless.com/company/contact-us<br>Global toll-free number: 1-877-687-7795<br>6:00 am to 5:00 pm PST|
|Corporate and product information|Web:sierrawireless.com|

##### **Revision History**







|Revision<br>Number|Release Date|Changes|
|---|---|---|
|1.0|November 08, 2019|Creation|
|2.0|January 03, 2020|Baseband and other software-related modifications|
|2.1|January 22, 2020|**•**<br>Modify the current consumption from 15uA to TBD<br>**•**<br>Added FCC ID|
|2.2|February 05, 2020|**•**<br>Updated Transmit Band and Receive Band columns in Table1-3<br>**•**<br>Removed SDIO information<br>**•**<br>Changed PSM mode values to TBD on Table 3-9|
|3.0|June 22, 2020|Updates on Functional Specifications, Technical Specifications, Interface Details, Routing<br>Constraints and Recommendations, Pinout, and Acronyms|
|3.1|July 06, 2020|Minor edits on Table1-3|
|3.2|July 07, 2020|Updated Figure 3-4 and Figure 3-5|
|4.0|September 01, 2020|**•**<br>Updates on Functional Specifications, Technical Specifications, Interface Details,<br>Routing Constraints and Recommendations, Pad, and Acronyms<br>**•**<br>Added RC7630 specifications<br>**•**<br>Added Japan Regulatory approval|
|5.0|November 04, 2020|**•**<br>Updates on Functional Specifications, Technical Specifications, Interface Details,<br>Routing Constraints and Recommendations, Pad, and Acronyms<br>**•**<br>Added Industry Canada Statement|
|5.1|November 05, 2020|**•**<br>Additional minor edits|
|6.0|January 12, 2021|**•**<br>Added internal devic16e frequencies<br>**•**<br>Additional minor edits|


Rev. 16 March 2025 3 41113440


Preface







|Revision<br>Number|Release Date|Changes|
|---|---|---|
|6.1|February 23, 2021|**•**<br>Updated PCM mode timings|
|6.2|February 24, 2021|**•**<br>Removed information about GSM support for RC7630 series|
|7.0|May 07, 2021|**•**<br>Added new note under Introduction|
|8.0|September 22, 2021|**•**<br>Updated Table 3-11, Updated section 9.5.1, Added new note under VGPIO, and other<br>minor edits|
|9.0|April 20, 2022|**•**<br>Added add RC7612, RC7612-1 (Limited Availability)<br>**•**<br>Added Support Band tables for RC7612, RC7612-1|
|10.0|July 2022|**•**<br>Updates on Technical Specifications|
|11.0|August 2022|**•**<br>Added back the following sections:<br>**•** Software and Tools<br>**•** Reliability Specification<br>**•** Customization<br>**•** Testing<br>**•** References<br>**•** Abbreviations|
|12|January 2023|**•**<br>Updated Figure 4-2<br>**•**<br>Added product markings for NCC, JPA/JRF and KCC on Product Marking|
|13|June 2023|**•**<br>Updated footnote e on Table 4-6<br>**•**<br>Updated WAKE_ON_WWAN description<br>**•**<br>Updated Figure 4-6<br>**•**<br>Modified assertion time for POWER_ON_N<br>**•**<br>Modified assertion time for POWER_ON_N in Power State Transitions|
|14|September 2024|**•**<br>Updated Table 3-1<br>**•**<br>Updated Under-Voltage Lockout (UVLO)<br>**•**<br>Updated POWER_ON_N<br>**•**<br>Updated Reset Signals (RESET_IN_N and RESET_OUT_N)<br>**•**<br>Updated the document format to the new Semtech template<br>**•**<br>Updated Approvals chapter to Regulatory Compliance and Industry Certifications<br>**•**<br>Updated Important Notes and added a note under Power Saving Mode (PSM).<br>**•**<br>Added footnote b to Table 4-3<br>**•**<br>Added footnote l to Table 10-1<br>**•**<br>Added note under UART.<br>**•**<br>Added note under UIM Interface.|


Rev. 16 March 2025 4 41113440


Product Technical Specification







|Revision<br>Number|Release Date|Changes|
|---|---|---|
|15|December 2024|**•**<br>Added Table 1-5: RC7630J band configuration<br>**•**<br>Updated Table 1-1: Supported Networks and Voice Capability for RC7630J<br>**•**<br>Added RC7630J in Figure 2-1: Architecture Overview<br>**•**<br>Updated 2.2 Telecom Features<br>**•**<br>Added RC7630J in Table 3-14: Supported RF Band<br>**•**<br>Added Table 3-18: RC7630J Conducted Tx Max Output Power Tolerances—LTE<br>**•**<br>Added Table 3-22: RC7630J Conducted Rx Sensitivity—LTE Bands<br>**•**<br>Added RC7630J in 4.7.2 eSIM / UIM2 Interface<br>**•**<br>Updated Table 10-1: Pin Definitions<br>**•**<br>Added Table 12-7: Test Settings—RC7630J LTE Transmission Path<br>**•**<br>Added Table 12-14: Test Settings — RC7630J LTE Receive Path<br>**•**<br>Updated Chapter 9 as Legal Information and added RC7630J<br>**•**<br>Added RC7630J under Japan Radio and Telecom Approval (pending final regulatory<br>approval)|
|16|March 2025|**•**<br>Updated 8. Reliability Specification|


Rev. 16 March 2025 5 41113440


#### **Contents**

Important Notice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2


Wireless Communications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2


Safety. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2


Qualcomm Licenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2


Sierra Wireless . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


Contact Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


Revision History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


**1: Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12**


1.1 General Features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


1.2 Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


1.3 Common Flexible Form Factor (CF3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


1.4 Physical Dimensions and Connection Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


**2: Functional Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19**


2.1 Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


2.2 Telecom Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

2.2.1 Network Technology Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2.2.2 Modem Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


2.3 Multi-Core Processing Capabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


**3: Technical Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26**


3.1 Environmental . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26


3.2 Power Supply Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

3.2.1 Under-Voltage Lockout (UVLO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

3.2.2 Sudden Power Loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

3.2.3 Power Consumption States. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

3.2.4 Power Saving Mode (PSM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3.2.5 Active State to PSM Transition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.2.6 Extended Discontinuous Reception (eDRX) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.2.7 Current Consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


3.3 RF. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43


Rev. 16 March 2025 6 41113440


DocTitleHeader


3.3.1 Supported RF Bands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

3.3.2 LTE RF Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3.3.3 GSM / GPRS / EDGE RF Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

3.3.4 WCDMA RF Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

3.3.5 WWAN Antenna Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51


3.4 GNSS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

3.4.1 Characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

3.4.2 GNSS Antenna Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

3.4.3 Antenna Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56


3.5 Electrical Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

3.5.1 Absolute Maximum Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

3.5.2 Digital I/O Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

3.5.3 Internal Devices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61


3.6 Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

3.6.1 Application Core . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

3.6.2 Embedded Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

3.6.3 Recovery Mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

3.6.4 Secure Boot / Secure Debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64


3.7 Mechanical Drawing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65


3.8 Mechanical Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66


**4: Interfaces Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67**


4.1 POWER_ON_N . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

4.1.1 Power-up Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

4.1.2 Software-Initiated Power Down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69


4.2 Emergency Power Off . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69


4.3 POWER_ON_N, RESET_IN_N, AT!POWERDOWN Use Cases . . . . . . . . . . . . . . . . . . . . . . . . 69


4.4 Tx Power Control. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70


4.5 USB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70


4.6 UART. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71


4.7 UIM Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

4.7.1 External UIM1 Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

4.7.2 eSIM / UIM2 Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74


Rev. 16 March 2025 7 41113440


Contents


4.7.3 External SIM Switch Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74


4.8 General Purpose Input / Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76


4.9 GPIO4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

4.9.1 SIM Detect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

4.9.2 General Purpose Input / Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77


4.10 GPIO6. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

4.10.1 SIM Switching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

4.10.2 General Purpose Input / Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

4.10.3 RESET_OUT_N. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


4.11 Wakeup Interrupt (Sleep State) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


4.12 Wakeup Events (PSM). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79


4.13 I2C Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

4.13.1 Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80


4.14 VGPIO. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80


4.15 Reset Signals (RESET_IN_N and RESET_OUT_N). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81


4.16 ADC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83


4.17 Digital Audio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

4.17.1 PCM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

4.17.2 I2S. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95


4.18 SPI Bus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

4.18.1 Configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

4.18.2 Waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96


4.20 TP1 (Boot Pin) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98


4.21 Temperature Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98


4.22 Test Pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100


4.23 Antenna Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101


4.24 Indication Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

4.24.1 Tx Activity Indicator (TX_ON) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

4.24.2 WWAN_LED_N . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.24.3 WAKE_ON_WWAN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.24.4 Ring Indicator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

4.24.5 SAFE_PWR_REMOVE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104


Rev. 16 March 2025 8 41113440


DocTitleHeader


4.25 DR_SYNC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105


4.26 W_DISABLE_N — Wireless Disable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105


**5: Routing Constraints and Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107**


5.1 General Rules and Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107


5.2 Power Supply . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107


5.3 Antenna . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

5.3.1 OTA Considerations when Developing Products with an Integrated Antenna. . . . 108


5.4 PCB Layout Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

5.4.1 General Design Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

5.4.2 Specific Design Rules to Support TRP Performances . . . . . . . . . . . . . . . . . . . . . . . . . . 110

5.4.3 Specific Design Rules to Support TIS Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111


5.5 PCB Specifications for the Application Board. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111


5.6 Recommended PCB Land Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111


5.7 Routing Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

5.7.1 Power Supply. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

5.7.2 UIM Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

5.7.3 RF Routing Recommendations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

5.7.4 USB Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116


5.8 Thermal Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117


5.9 EMC and ESD Recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117


5.10 Mechanical Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118


5.11 Signal Reference Schematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

5.11.1 UIM Holder. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

5.11.2 USB. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120


**6: Software and Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121**


6.1 Support Tools. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121


6.2 SED (Smart Error Detection) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121


6.3 Firmware Upgrade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121


6.4 Operating System Upgrade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121


6.5 Product Marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122


Rev. 16 March 2025 9 41113440


Contents


**7: Debug and Assembly Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123**


7.1 Testing Assistance Provided by Semtech . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


7.2 Integration Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


7.3 IOT / Operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


7.4 Module Testing Recommendations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


7.5 Serial Link Access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123


7.6 RF Output Accessibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124


7.7 USB Debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124


**8: Reliability Specification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125**


8.1 Functional / Performance Tests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125


8.2 Aging Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

8.2.1 High Temperature Operating Life Test. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

8.2.2 Humidity Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

8.2.3 Thermal Shock Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125


8.3 Characterization Tests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

8.3.1 Electrostatic Discharge Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

8.3.2 Low Temperature Cold Start Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

8.3.3 Electrostatic Discharge Component Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

8.3.4 Unprotected Free Fall Drop Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

8.3.5 Component Solder Wettability Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126


**9: Legal Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127**


9.1 Regulatory and Industry Approvals/ Certifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127


9.2 Compliance Acceptance and Certification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127


9.3 Certification Compliance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127

9.3.1 Important Compliance Information for North American Users. . . . . . . . . . . . . . . . . . 127

9.3.2 Japan Radio and Telecom Approval. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130


**10: Pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131**


10.1 Pin Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131


10.2 Pin Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131


Rev. 16 March 2025 10 41113440


DocTitleHeader


**11: Customization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140**


**12: Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141**


12.1 Certification Testing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141


12.2 Production Testing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141


12.3 Functional Production Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

12.3.1 Suggested Production Tests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

12.3.2 Production Test Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142


12.4 UMTS (WCDMA/GSM) RF Transmission Path Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144


12.5 LTE RF Transmission Path Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146


12.6 UMTS (WCDMA/GSM) RF Receive Path Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149


12.7 LTE RF Receive Path Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152


12.8 GNSS RF Receive Path Test. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154


**A: Appendix. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156**


A.1 Web Site Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156


A.2 Reference Documents. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156


A.3 Abbreviations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156


Rev. 16 March 2025 11 41113440


## **1**


### **1: Introduction**

This document defines the high-level product features and illustrates the interfaces for the Semtech RC76xx
Embedded Modules. It covers the hardware aspects of the product series, including electrical and mechanical.


_Note: Semtech modules are shipped factory-programmed, with industry or mobile operator approved firmware, according to the specific_
_SKU ordered. Periodically, newer firmware versions become available and can include new features, bug fixes, or critical security updates._
_Semtech strongly recommends that customers establish their own production capability for updating module firmware on their_
_assembled end platform, in the event that a newer firmware must be installed before deployment. Semtech also recommends customers_
_design their products to support post-deployment FOTA upgrades using the AirVantage cloud platform._

##### **1.1 General Features**


The Semtech R76xx is an industrial-grade LGA 239-pad embedded module. Its wireless modem provides voice and
data connectivity on the networks listed in Table 1-1.


**Table 1-1: Supported Networks and Voice Capability**























|Variant|Network|Network Voice Support|LTE Category|
|---|---|---|---|
|RC7611|LTE|VoLTE|Cat4|
|RC7611-1|RC7611-1|RC7611-1|Cat1|
|RC7612a|LTE<br>UMTS (DC-HSPA+, HSPA+, HSPA,<br>WCDMA)|NA (Data only)|Cat4|
|RC7612-1a|RC7612-1a|RC7612-1a|Cat1|
|RC7620|LTE<br>UMTS (DC-HSPA+, HSPA+, HSPA,<br>WCDMA)<br>GSM/GPRS/EDGE|Circuit switch voice<br>+ VoLTE|Cat4|
|RC7620-1|RC7620-1|RC7620-1|Cat1|
|RC7630|LTE|VoLTE|Cat4|
|RC7630-1|RC7630-1|RC7630-1|Cat1|
|RC7630Ja|RC7630Ja|RC7630Ja|Cat4|


a. Limited Availability


To simplify cellular connectivity, the Semtech RC76xx has been designed to support Ready-To-Connect. To learn
more about Ready-To-Connect capabilities and to know which variant already supports this feature, please get in
touch with your Semtech sales representative.


GNSS functionality is available as a SKU-dependent feature.


Rev. 16 March 2025 12 41113440


Product Technical Specification


In addition to modem features, the Semtech RC76xx embeds several cores for maximum flexibility and security for
embedded software execution, including:

**•**
A Telecom Core that natively manages 4G modem features


The following tables detail supported RF bands/connectivity.


**Table 1-2: RC7611 and RC7611-1 Supported Bands / Connectivity**






|Technology|RF Band|Transmit Band (Tx) (MHz)|Receive Band (Rx) (MHz)|Notes|
|---|---|---|---|---|
|LTE|B2|1850–1910|1930–1990|MIMOa and<br>diversity|
|LTE|B4|1710–1755|2110–2155|2110–2155|
|LTE|B5|824–849|869–894|869–894|
|LTE|B12|699–716|729–746|729–746|
|LTE|B13|777–787|746–756|746–756|
|LTE|B14|788–798|758–768|758–768|
|LTE|B25|1850–1915|1930–1995|1930–1995|
|LTE|B26|814–849|859–894|859–894|
|LTE|B66|1710–1780|2110-2200|2110-2200|
|LTE|B71|663–698|617–652|617–652|
|GNSSb|GPS||1575.42 ± 1.023||
|GNSSb|GLONASS||1597–1606||
|GNSSb|Galileo||1575.42 ± 2.046||
|GNSSb|BeiDou||1561.098 ± 2.046||



a. Downlink MIMO 2x2

b. GNSS support is SKU-dependent.


**Table 1-3: RC7620 and RC7620-1 Supported Bands/Connectivity**

|Technology|RF Band|Transmit Band (Tx) (MHz)|Receive Band (Rx) (MHz)|Notes|
|---|---|---|---|---|
|LTE|B1|1920–1980|2110–2170|MIMOa and<br>diversity|
|LTE|B3|1710–1785|1805–1880|1805–1880|
|LTE|B7|2500–2570|2620–2690|2620–2690|
|LTE|B8|880–915|925–960|925–960|
|LTE|B20|832–862|791–821|791–821|
|LTE|B28|703–748|758–803|758–803|
|UMTS|B1|1920 – 1980|2110–2170|Diversity|
|UMTS|B8|880–915|925–960|925–960|
|GSM/GPRS/EDGE|E-GSM 900|880–915|925–960||
|GSM/GPRS/EDGE|DCS 1800|1710–1785|1805–1880||



Rev. 16 March 2025 13 41113440


Introduction


**Table 1-3: RC7620 and RC7620-1 Supported Bands/Connectivity (Continued)**

|Technology|RF Band|Transmit Band (Tx) (MHz)|Receive Band (Rx) (MHz)|Notes|
|---|---|---|---|---|
|GNSSb|GPS||1575.42 ± 1.023||
|GNSSb|GLONASS||1597–1606||
|GNSSb|Galileo||1575.42 ± 2.046||
|GNSSb|BeiDou||1561.098 ± 2.046||



a. Downlink MIMO 2x2
b. GNSS support is SKU-dependent.


**Table 1-4: RC7630 and RC7630-1 Supported Bands/Connectivity**



|Technology|RF Band|Transmit Band (Tx) (MHz)|Receive Band (Rx) (MHz)|Notes|
|---|---|---|---|---|
|LTE|B1|1920–1980|2110–2170|MIMOa and<br>diversity|
|LTE|B3|1710–1785|1805–1880|1805–1880|
|LTE|B5|824–849|869–894|869–894|
|LTE|B7|2500–2570|2620–2690|2620–2690|
|LTE|B8|880–915|925–960|925–960|
|LTE|B18|815–830|860–875|860–875|
|LTE|B19|830–845|875–890|875–890|
|LTE|B21|1447.9–1462.9|1495.9–1510.9|1495.9–1510.9|
|GNSSb|GPS||1575.42 ± 1.023||
|GNSSb|GLONASS||1597–1606||
|GNSSb|Galileo||1575.42 ± 2.046||
|GNSSb|BeiDou||1561.098 ± 2.046||
|GNSSb|QZSS||1575.42 ± 1.023||


a. Downlink MIMO 2x2





b. GNSS support is SKU-dependent.


Rev. 16 March 2025 14 41113440


Product Technical Specification


**Table 1-5: RC7630J** **[a]** **Supported Bands/Connectivity**



|Technology|RF Band|Transmit Band (Tx) (MHz)|Receive Band (Rx) (MHz)|Notes|
|---|---|---|---|---|
|LTE|B1|1920–1980|2110–2170|MIMOb and<br>diversity|
|LTE|B3|1710–1785|1805–1880|1805–1880|
|LTE|B5|824–849|869–894|869–894|
|LTE|B18|815–830|860–875|860–875|
|LTE|B19|830–845|875–890|875–890|
|GNSSc|GPS||1575.42 ± 1.023||
|GNSSc|GLONASS||1597–1606||
|GNSSc|Galileo||1575.42 ± 2.046||
|GNSSc|BeiDou||1561.098 ± 2.046||
|GNSSc|QZSS||1575.42 ± 1.023||


a. Limited availability.

b. Downlink MIMO 2x2





c. GNSS support is SKU-dependent.


**Table 1-6: RC7612 and RC7612-1 Supported Bands / Connectivity (Limited Availability)**



|Technology|RF Band|Transmit Band (Tx) (MHz)|Receive Band (Rx) (MHz)|Notes|
|---|---|---|---|---|
|LTE|B2|1850–1910|1930–1990|MIMOa and<br>diversity|
|LTE|B4|1710–1755|2110–2155|2110–2155|
|LTE|B5|824–849|869–894|869–894|
|LTE|B12|699–716|729–746|729–746|
|LTE|B13|777–787|746–756|746–756|
|UMTS|B2|1850-1910|1930-1990||
|UMTS|B4|1710–1755|2110-2155||
|UMTS|B5|824–849|869–894||
|GNSSb|GPS||1575.42 ± 1.023||
|GNSSb|GLONASS||1597–1606||
|GNSSb|Galileo||1575.42 ± 2.046||
|GNSSb|BeiDou||1561.098 ± 2.046||


a. Downlink MIMO 2x2





b. GNSS support is SKU-dependent.


Rev. 16 March 2025 15 41113440


Introduction

##### **1.2 Interfaces**


The Semtech RC76xx provides the following interfaces and peripheral connectivity:

**•** UIM interface—See UIM Interface

**·** eSIM—See eSIM / UIM2 Interface

**•**
VBAT_RF/VBAT_BB power supply— See Power Supply Ratings

**•** RF—See RF

**•** GNSS (RF_GNSS)—See GNSS

**•** ON/OFF control:

**·**
POWER_ON_N—See POWER_ON_N

**·**
Reset signals—See Reset Signals (RESET_IN_N and RESET_OUT_N)

**•** USB 2.0—See USB

**•** UART serial links—See UART

**•** GPIOs—See General Purpose Input / Output

**•** I [2] C—See I2C Interface

**•** 1.8V voltage reference— See VGPIO

**•** ADCs—See ADC

**•** Digital audio (PCM/I [2] S)— See Digital Audio

**•** SPI bus—See SPI Bus

**•** Antenna control—See Antenna Control

**•** System clock outputs—See Clock

**•** Test pins—See Test Pins

**•**
Tx Activity Indicator (TX_ON)—See Tx Activity Indicator (TX_ON)

##### **1.3 Common Flexible Form Factor (CF3)**


The Semtech RC76xx belongs to the Common Flexible Form Factor (CF3) family of WWAN modules. These modules
share the same mechanical dimensions (same width and length with varying thicknesses) and footprint. The CF3
form factor provides a unique solution to a series of problems faced commonly in the WWAN module space as it:

**•**
Accommodates multiple radio technologies and band groupings

**•**
Supports bit-pipe (Essential Module Series) and value-add (Smart Module Series) solutions

**•**
Offers electrical and functional compatibility

##### **1.4 Physical Dimensions and Connection Interface**


The Semtech RC76xx module is a compact, robust, fully shielded and labeled (laser-etched) module with the
dimensions noted in Table 1-7.


**Table 1-7: Module Dimensions** **[a]**

|Parameter|Nominal|Tolerance|Units|
|---|---|---|---|
|Length|23.00|±0.10|mm|
|Width|22.00|±0.10|mm|
|Thickness|2.50|±0.20|mm|
|Weight|2.6|±1.0|g|



a. Dimensions are accurate as of the release date of this document.


Rev. 16 March 2025 16 41113440


Product Technical Specification


The Semtech RC76xx module is an LGA form factor device. All electrical and mechanical connections are made
through the 238 Land Grid Array (LGA) pads on the bottom side of the PCB. (See Figure 10-1 for details.)


**Pad 1**


_Figure 1-1: RC76 Series Module Bottom View_


_Figure 1-2: RC76 Series Shield View_


Rev. 16 March 2025 17 41113440


Introduction


The 239 pads have the following distribution:


**Table 1-8: LGA Pad Types**

|Pad Type / Quantity|Col2|Dimensions|Pitch|
|---|---|---|---|
|Signal Pads|66 inner pads|1.0x0.5 mm|0.8 mm|
|Signal Pads|91 outer pads|91 outer pads|91 outer pads|
|Test Points|9 test points|0.8 mm (diameter)|1.20 mm|
|Ground Pads|64 inner pads|1.0x1.0 mm|1.83 mm/1.48 mm|
|Ground Pads|4 inner corner pads|1.0x1.0 mm|-|
|Ground Pads|4 outer corner pads|1.0x0.9 mm|-|
|Polarity Mark|1 polarity mark (Ground)|1.0 mm (diameter)|-|



Rev. 16 March 2025 18 41113440


## **2**


### **2: Functional Specifications**

##### **2.1 Architecture**

The following figure presents an overview of the Semtech RC76xx module’s internal architecture and external
interfaces.





































_Figure 2-1: RC7611, RC7611-1, RC7612*, RC7612-1*, RC7630, RC7630-1, RC7630J* Architecture Overview_


- Limited availability


Rev. 16 March 2025 19 41113440


Functional Specifications




















|WTR_FB|Col2|
|---|---|
|All GSM TX<br>~~All GSM TX~~|All GSM TX<br>~~All GSM TX~~|
|All band PRIMARY RX<br>~~All bands TX~~<br>D<br>Power<br>Amplifier|UPLEXER|











_Figure 2-2: RC7620, RC7620-1 Architecture Overview_

##### **2.2 Telecom Features**













Table 2-1 summarizes the Semtech RC76xx module’s capabilities offered through the Telecom core.


**Table 2-1: Module Capabilities**

|Feature|Description|
|---|---|
|Electrical|3.2–4.3V supply voltage (VBAT_BB, VBAT_RF):<br>**•**<br>Single supply, VBAT_BB tied to VBAT_RF<br>_or_<br>**•**<br>Dual supplies, single supply each for VBAT_BB and VBAT_RF|
|Voice (Digital Audio)|**•**<br>PCM/I2S digital audio interface<br>**•**<br>Supports Enhanced Full Rate (EFR), Full Rate (FR), Half Rate (HR), and both Narrow-Band<br>and Wide-band Adaptive Multirate (AMR-NB and AMR-WB) vocoders<br>**•**<br>MO and MT calling<br>**•**<br>Echo cancellation and noise reduction<br>**•**<br>Emergency calls (112, 110, 911, etc.)<br>**•**<br>Incoming call notification<br>**•**<br>DTMF generation<br>**•**<br>Internal codec driver for WM8944|



Rev. 16 March 2025 20 41113440


Product Technical Specification


**Table 2-1: Module Capabilities (Continued)**






|Feature|Description|
|---|---|
|SMS|**•**<br>SMS MO and MT<br>**•**<br>CS and PS support<br>**•**<br>SMS saving to UIM card or ME storage<br>**•**<br>SMS reading from UIM card or ME storage<br>**•**<br>SMS sorting<br>**•**<br>SMS concatenation<br>**•**<br>SMS Status Report<br>**•**<br>SMS replacement support<br>**•**<br>SMS storing rules (support of**AT+CNMI**, **AT+CNMA**)|
|Supplementary<br>services|**•**<br>Call Barring<br>**•**<br>Call Forwarding<br>**•**<br>Call Hold<br>**•**<br>Caller ID<br>**•**<br>Call Waiting<br>**•**<br>Multi-party service<br>**•**<br>USSD<br>**•**<br>Automatic answer|


###### **2.2.1 Network Technology Specifications**

**2.2.1.1 LTE Specifications**


The following table describes LTE specifications for Semtech RC76xx modules.


**Table 2-2: Supported LTE Specifications**

|Standard|Feature Description|
|---|---|
|R13|**•**<br>eDRX (Extended Discontinuous Reception) to extend battery life in devices that do not require<br>frequent network access<br>**•**<br>PSM (Power Saving Mode) to reduce power consumption|



Rev. 16 March 2025 21 41113440


Functional Specifications


**Table 2-2: Supported LTE Specifications (Continued)**







|Standard|Feature Description|
|---|---|
|R10|**•**<br>Release 10 mandatory LTE features<br>**•**<br>RC76xx Data rates:<br>**·**<br>Cat 1 FDD (up to 10 Mbps downlink, 5 Mbps uplink)<br>**·**<br>Cat 4 FDD (up to 150 Mbps downlink, 50 Mbps uplink)<br>**•**<br>1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz and 20 MHz RF bandwidth<br>**•**<br>IPv6, QoS<br>**•**<br>NAS & RRC standalone security<br>**•**<br>Commercial Mobile Alert System (CMAS)<br>**•**<br>ETWS (Earthquake Tsunami Warning System) notification<br>**•**<br>Inter-frequency/bandwidth mobility<br>**•**<br>DRX cycle while in:<br>**·**<br>Connected mode<br>**·**<br>Idle mode<br>**•**<br>UE IRAT support for Self Organizing Networks and Automatic Neighbor Relation (SON AR)|
|System<br>Determination|**•**<br>Frequency Scan and System Selection within LTE<br>**•**<br>LTE BPLMN support<br>**•**<br>LTE Connected mode OOS<br>**•**<br>System selection across RATs, Standalone Security, Dedicated EPS Bearer Management and<br>Dormancy<br>**•**<br>256 UPLMN and 256 OPLMN entries in UIM support<br>**•**<br>Carrier Specific BSR Requirements|
|Data|**•**<br>Data call throttling<br>**•**<br>Default IPv4 bearer activation at attach/IPv4 data call<br>**•**<br>NW and UE initiated QoS<br>**•**<br>Dual IP and IPv4/IPv6 continuity<br>**•**<br>IPv4/IPv6 session continuity<br>**•**<br>W/G IP session continuity<br>**•**<br>Emergency services—LTE NAS Support for Control Plane LTE Positioning Protocol|


**2.2.1.2 GSM / GPRS / EDGE Specifications**


The following table describes GSM/GPRS/EDGE specifications for Semtech RC7620 modules.


**Table 2-3: Supported GSM Specifications**

|Standard|Feature Description|
|---|---|
|GPRS|Packet-switched data:<br>**•**<br>DTM (simple class A) operation<br>**•**<br>GPRS Multislot class 10 (with backoffa)—Four Rx slots (maximum), two Tx slots (maximum), five active<br>slots total<br>**•**<br>Coding schemes—CS1–CS4<br>**•**<br>GEA1, GEA2, and GEA3 ciphering<br>**•**<br>WCDMA/GERAN system selection|



Rev. 16 March 2025 22 41113440


Product Technical Specification


**Table 2-3: Supported GSM Specifications (Continued)**

|Standard|Feature Description|
|---|---|
|EDGE|**•**<br>E2 power class for 8 PSK<br>**•**<br>DTM (simple class A), multislot class 12<br>**•**<br>EGPRS—Multislot class 12 (with backoffa)—Four Rx slots (maximum), four Tx slots (maximum), five<br>active slots total<br>**•**<br>Coding schemes—MCS1–MCS9<br>**•**<br>BEP reporting<br>**•**<br>SRB loopback and test modes A and B<br>**•**<br>8-bit and 11-bit RACH<br>**•**<br>PBCCH support<br>**•**<br>One-phase/two-phase access procedures<br>**•**<br>Link adaptation and IR<br>**•**<br>NACC, extended UL TBF<br>**•**<br>PFC/PFI (Packet Flow Context/Packet Flow Identifier) support - allows identity tagging of RLC blocks to<br>identify separate QoS streams at the radio link layer<br>**•**<br>GPRS/EDGE MSC12-EDA - permits allocation of more than two uplink timeslots for GPRS/EDGE<br>**•**<br>Enh DL RLC/MAC Segmentation - permits reception of MAC control messages that exceed one radio<br>block capacity in length<br>**•**<br>Enhanced Ext UL TBF - dummy block transmission is punctured for current saving purposes<br>**•**<br>2G PS handover - packet-switched equivalent of CS handover to ensure faster cell change and improved<br>throughput<br>**•**<br>WCDMA/GERAN<br>**•**<br>Band Scan: Run-time Configurable RRC Band Scan Order<br>**•**<br>Power and Network Optimizations: Frame Early Termination for Power Optimization<br>**•**<br>Protocols: MRAB-Pack-1 Enhancements - reduces multi-RAB call drops<br>**•**<br>GPRS/EDGE - Class 33 (296 kbps downlink, 236.8 kbps uplink)<br>**•**<br>CSD (Circuit-switched data bearers)<br>**•**<br>Release 4 GERAN Feature Package 1<br>**•**<br>SAIC / DARP Phase 1|
|EDGE|**•**<br>Latency reduction<br>**•**<br>Repeated FACCH, Repeated SACCH<br>**•**<br>A-GPS support<br>**•**<br>GPRS ROHC<br>**•**<br>Enhanced Operator Name String (EONS)<br>**•**<br>Enhanced Network Selection (ENS)|



a. Backoff is firmware dependent. 2G power backoff level is 3dB at the maximum power level as per 3GPP standards.


Rev. 16 March 2025 23 41113440


Functional Specifications


**2.2.1.3 WCDMA Specifications**


The following table describes WCDMA specifications for Semtech RC7620, RC7612*, RC7612-1* modules.


**Table 2-4: Supported WCDMA Specification**

|Standard|Feature Description|
|---|---|
|R99|**•**<br>All modes and data rates for WCDMA FDD, with the following restrictions:<br>**·**<br>The downlink supports the following specifications:<br>**·**<br>Up to four physical channels, including the broadcast channel (BCH), if present<br>**·**<br>Up to three dedicated physical channels (DPCHs)<br>**·**<br>Spreading factor (SF) range support from 4 to 256<br>**·**<br>The uplink supports the following specifications:<br>**·**<br>One physical channel, eight TrCH, and 16 TrBks starting at any frame boundary<br>**·**<br>A maximum data rate of 384 kbps<br>**·**<br>Full SF range support from 4 to 256<br>**•**<br>PS data rates of 384 kbps DL and 384 kbps UL|
|R8 HSDPA|**•**<br>PS data speeds up to 42 Mbps (UE category 24) on the downlink<br>**•**<br>HS-DSCH (HS-SCCH, HS-PDSCH, and HS-DPCCH)<br>**•**<br>Maximum of 15 HS-PDSCH channels, both QPSK and 16 QAM modulation<br>**•**<br>Support for 3GPP-defined features:<br>**·**<br>R99 transport channels<br>**·**<br>Maximum of four simultaneous HS-SCCH channels<br>**·**<br>CQI and ACK/NACK on HS-DPCCH channel<br>**·**<br>All incremental redundancy versions for HARQ<br>**·**<br>Configurable support for power classes 3 or 4, per TS 25.101<br>**·**<br>TFC selection limitation on UL factoring in transmissions on the HS-DPCCH, per TS 25.133<br>**•**<br>Switching between HS-PDSCH and DPCH channel resources, as directed by the network<br>**•**<br>Network activation of compressed mode by SF/2 or HLS on the DPCH for conducting inter-frequency or<br>inter-radio access technology (RAT) measurements when the HS-DSCH is active|
|R8 HSDPA|**•**<br>STTD on both associated DPCH and HS-DSCH simultaneously<br>**•**<br>CLTD mode 1 on the DPCH when the HS-PDSCH is active<br>**•**<br>STTD on HS-SCCH when STTD or CLTD mode 1 are configured on the associated DPCH<br>**•**<br>SCH-IC support<br>**•**<br>HS-DSCH DRX support|



Rev. 16 March 2025 24 41113440


Product Technical Specification


**Table 2-4: Supported WCDMA Specification (Continued)**

|Standard|Feature Description|
|---|---|
|R6 HSUPA|**•**<br>E-DCH data rates of up to 5.76 Mbps for 2 ms TTI (UE category 6) uplink<br>**•**<br>Support for 3GPP-defined features:<br>**·**<br>E-AGCH, E-RGCH, and E-HICH channels for downlink; E-RGCH and E-HICH supports serving and non-<br>serving radio links, with up to four radio links in the E-DCH active set<br>**·**<br>All HARQ incremental redundancy versions and maximum number of HARQ retransmissions<br>**·**<br>Uplink E-DCH channel with support for up to four E-DPDCH channels<br>**·**<br>HSUPA channels run simultaneously with R99 and HSDPA channels<br>**•**<br>STTD on all HSUPA downlink channels<br>**•**<br>CLTD mode 1 on HS-PDSCH and DPCH along with HSUPA channels<br>**•**<br>Switch between HSUPA channels and DPCH channel resources, as directed by the network<br>**•**<br>Handover using compressed mode with simultaneous E-DCH and HS-DSCH interactive, background,<br>and streaming QoS classes<br>**•**<br>CSD fallback<br>**•**<br>DPCCH DTX support|



*Limited Availability

###### **2.2.2 Modem Specifications**


**Table 2-5: Supported Modem Specifications**

|Standard|Feature Description|
|---|---|
|Data|**•**<br>IPHC protocol as RFC 2509<br>**•**<br>Stateless DHCPv4 protocol to get P-CSCF and DNS addresses<br>**•**<br>IPv4/IPv6<br>**•**<br>Dual IP on single QMAP PDN<br>**•**<br>Multi-QMAP PDN Data Call|


##### **2.3 Multi-Core Processing Capabilities**


The Semtech RC76xx is a powerful multiple-core system that includes:

**•**
One QDSP6 core, embedding Telecom firmware with integrated cellular voice, VoLTE, data and wireless Internet
connectivity

**•**
One Cortex A7 core entirely dedicated to Semtech Proprietary application and natively provided with ThreadX
operating system


Rev. 16 March 2025 25 41113440


## **3**


### **3: Technical Specifications**

##### **3.1 Environmental**

The environmental specifications for operation and storage of the Semtech RC76xx are defined in Table 3-1.


**Table 3-1: Environmental Specifications**

|Parameter|Range|Operating Class|
|---|---|---|
|Ambient Operating Temperature|-30°C to +70°C|Class A (Operational, 3GPP compliant)|
|Ambient Operating Temperature|-40°C to +85°C|Class B (Operational, non-3GPP<br>compliant)|
|Ambient Storage Temperature|-40°C to +85°C|-|
|Ambient Humidity|85% or less|-|



Class A is defined as the operating temperature range within which the device:

**•**
Shall exhibit normal function during and after environmental exposure.

**•**
Shall meet the minimum requirements of 3GPP or appropriate wireless standards.


Class B is defined as the operating temperature range within which the device:

**•**
Shall remain fully functional during and after environmental exposure

**•**
Shall exhibit the ability to establish any of the device’s supported call modes (SMS, Data, and emergency calls) at
all times even when one or more environmental constraint exceeds the specified tolerance.

**•**
Unless otherwise stated, full performance should return to normal after the excessive constraint(s) have been
removed.

##### **3.2 Power Supply Ratings**


The Semtech RC76xx operates using DC power supplied via the VBAT_RF and VBAT_BB signals. Power supply
options are:

**•**
A single regulated DC power supply (3.7V nominal)

**•**
Two regulated DC power supplies (3.7V nominal), one each for VBAT_BB and VBAT_RF


**Table 3-2: Power Supply Pins**

|Pin|Name|Direction|Function|Notes|
|---|---|---|---|---|
|63, 158|VBAT_BB|Input|Baseband power supply|63—Must be used<br>158—Optional|
|61, 62, 157|VBAT_RF|Input|RF power supply|61/62—Must be used<br>157—Optional|



Rev. 16 March 2025 26 41113440


Product Technical Specification


**Table 3-3: Operating Conditions**










|Parameter|Col2|Min|Typ|Max|Units|Notes|
|---|---|---|---|---|---|---|
|Power supply voltagea,b|Power supply voltagea,b|3.2|3.7|4.3|V|Must be within min/max values over all<br>operating conditions (including voltage<br>ripple, drop, and transient).|
|Power supply ripple|Power supply ripple|-|-|100|mVpp|SeeFigure 3-1.|
|Extended power supply voltagec|Extended power supply voltagec|3.0|3.7|4.3|V|To enable this operating condition, use<br>AT!PCVOLTLIMITS for voltage monitoring.<br>Refer to the RC76xx AT Command<br>Reference Guide for more details.|
|Power supply voltage drop|Power supply voltage drop|-|-|250|mVpp|SeeFigure 3-1 andFigure 3-2.|
|Power supply voltage transient<br>(overshoot/undershoot)|Power supply voltage transient<br>(overshoot/undershoot)|-|-|300|mVpp|SeeFigure 3-1.|
|Output current ratingd|LTE,<br>UMTS|1.0|1.5|-|A|**•**<br>Typical value varies and depends on<br>output power, band, and operating<br>voltage. SeeCurrent Consumption for<br>values measured under normal<br>operating conditions.<br>**•**<br>Max value measured over 100 µs<br>period.|
|Output current ratingd|GSM|2.2|3.0|3.0|A|A|



a. Power supply voltage outside the required range may affect call quality (dropped calls, data transfer errors, etc.)
b. For Absolute Maximum Ratings, see Table 3-34.
c. VBAT from 3.0-3.2V is functional (3GPP performance is not guaranteed) but the power source must be sufficient, and the impedance
of power source/power path should be as low as possible to reduce the voltage drop.
d. These values include a margin. For information on current consumption, see Current Consumption.


Customer should characterize the ripple, drop, and transient response (overshoot/undershoot) of the power supply
delivery system at the module input under full transmit power in Semtech RC76xx modules. To minimize voltage
variation, add suitable capacitors to the supply line as close as possible to the module—depending on the power
supply design, these capacitors may range from tens to several thousand µ F.


_Figure 3-1: Power Supply Characteristics_


Rev. 16 March 2025 27 41113440


Technical Specifications


_Figure 3-2: Common and Separate Power Supply Examples_

###### **3.2.1 Under-Voltage Lockout (UVLO)**


The power management section of the Semtech RC76xx includes an under-voltage lockout circuit that monitors
supply and shuts down when VBAT_BB falls below the threshold.


_Figure 3-3: Under-Voltage Lockout (UVLO) Diagram_


_Note: Due to under-voltage lockout, which causes the PMIC to shutdown directly, the device is powered down._


The Semtech RC76xx will power down by PMIC directly and remain off until VBAT_BB returns to the valid range and
the ON/OFF signal is active.


Rev. 16 March 2025 28 41113440


Product Technical Specification


_Note: If the device experiences six consecutive UVLO events less than 45 seconds apart (approximately) and a host-initiated power down_
_or reset has not occurred, the device enters a mode in which only the DM port enumerates on the USB._


**Table 3-4: UVLO Specifications**

|Parameter|Min|Typ|Max|Units|
|---|---|---|---|---|
|Threshold voltage, falling|2.225|2.4|2.80|V|
|Threshold voltage, accuracy|-5|-|+5|%|
|Hysteresis|-|425|-|mV|
|UVLO detection interval|-|1.0|-|s|


###### **3.2.2 Sudden Power Loss**


Any sudden power loss of the embedded module during operating mode will increase the EFS crash risk, even in the
power on or power down sequence. It is strongly recommended to remove the power only after the module is in
power down mode.

###### **3.2.3 Power Consumption States**


The Semtech RC76xx has four basic power states: Active, Sleep, Power Saving Mode (PSM), and Off. As the module
transitions between power states, the range of available device functionality adjusts appropriately, as described in
Table 3-5 and Figure 3-4.


In the Active state, the module is ON with the application processor running. In Sleep state, the processor suspends
its activity, reducing power consumption. The Active state has more than one power mode to reduce power
consumption. Power Saving Mode (PSM; network-dependent) may be enabled to achieve the lowest possible
average power consumption.


**Table 3-5: Supported Power States**

|State|Description|
|---|---|
|Active|Module is fully powered (ThreadX runs in theApplication Core; modem is on) and operating in one of the<br>following modes:<br>**•**<br>Full function (WWAN radio active; GNSS radio can be turned on/off)—Highest power<br>consumption.<br>**•**<br>Idle mode (WWAN radio on; Module registered on network, but no active connection; GNSS radio<br>can be turned on/off)<br>**•**<br>Airplane mode (WWAN radio off; GNSS radio can be active if allowed by PRI)<br>**•**<br>eDRX (Extended Discontinuous Reception)—eDRX mode provides a ‘flexible sleep’ for the modem,<br>which significantly reduces energy consumption. For eDRX details, seeExtended Discontinuous<br>Reception (eDRX).|
|Sleep|**•**<br>Lower power consumption than Active state, but higher than PSM.<br>**•**<br>Application Core is sleeping; modem is in DRX/eDRX. The processor monitors signals (triggers) that<br>can ‘wake’ the module—seeWakeup Interrupt (Sleep State) for details.<br>Sleep state can be entered based on USB-SS (if USB is connected to the module), UART_DTR,<br>wake_lock(), configured GPIOs, and QMI exchanges from the modem.|



Rev. 16 March 2025 29 41113440


Technical Specifications



**Table 3-5: Supported Power States (Continued)**







|State|Description|
|---|---|
|PSM (Power Saving<br>Mode)|3GPP Release 12 introduced network support of PSM. PSM allows the module to negotiate, with the<br>network, an extended period during which registration context with the network is retained while the<br>module is unreachable. During the negotiated period, the module enters a very low-power dormant<br>state.<br>After the specified period, the modem and application processors boot up and the module sends a TAU<br>(Tracking Area Update) to the network.<br>After sending the TAU, the module remains active to allow any pending data to be exchanged with the<br>network. Then, after a negotiated period of inactivity, the module automatically returns to PSM to<br>repeat the cycle.<br>For PSM details, seePower Saving Mode (PSM).<br>When the 3GPP PSM feature is accepted by the network, (seePower Saving Mode (PSM)), the RC76<br>module will directly enter into the PSM power state. The module cannot remain in another power state<br>other than PSM when the PSM 3GPP feature is accepted by the network.|
|OFF (VBATT_ON)|Module is OFF (VBATT is ON):<br>**·**<br>Active state (POWER_ON_N is asserted) - This is a low level signal to turn on the module.<br>**·**<br>POWER_ON_N is de-asserted - The module is not turned on but consumes 6uA.|


**Table 3-6: PSM Wakeup Sources**

|Type|Description|
|---|---|
|TAU timer|Periodic TAU—PSM Cycle Timer (T3412)<br>Configurable timer specifying PSM sleep duration. Applies to PSM only.|
|Wakeup timer|Derived from TAU timer (value is automatically set slightly shorter than TAU timer to ensure module boot<br>completes before TAU timer expires)|
|RESET_IN_N|Resets the module with POWER_ON_N ON.<br>_Note: If RESET_IN_N is used when POWER_ON_N is OFF, an emergency power off occurs—seeEmergency Power_<br>_Off_|
|POWER_ON_N|Wakes the module when asserted (transitions from OFF to ON).|



Figure 3-4 illustrates the current consumption requirements of the different power states and the possible
transitions between power states. For specific values, see Current Consumption


_Note: Illustration not to scale. Values are based on the RC7611. Refer to Current Consumption for specific consumption values per_

_variant._


Rev. 16 March 2025 30 41113440


Product Technical Specification



1000













OFF POWER_ON_N OFF Airplane Idle USB activeAirplane: USB activeIdle: On call



Power States*
OFF OFF PSM Sleep Active
(VBATT_ON)



_Figure 3-4: Overview of Current Consumption and Power States_


_Note: *Refer to Table 3-5_


**RC76xx**





















~~P~~ O ~~WE~~ R_ ~~ON~~ _N a ~~s~~ s ~~e~~ rte ~~d~~ o ~~v~~ er 7s ~~(~~ fro ~~m~~ “ ~~O~~ F ~~F~~ ” ~~m~~ o ~~d~~ e)


**Note: VBATT = VBAT_BB and VBAT_RF**


_Figure 3-5: Power State Transitions_


Rev. 16 March 2025 31 41113440


Technical Specifications

###### **3.2.4 Power Saving Mode (PSM)**


Power Saving Mode (PSM) is a 3GPP feature that allows the RC76xx to minimize power consumption by registering
on a PSM-supporting LTE network, entering a very low power ‘dormant’ state for a pre-configured duration (via a
periodic TAU (Tracking Area Update) timer), and then booting up for a short period to transmit/receive data, before
re-entering PSM. During the dormant period, the module remains unreachable by the network until woken by a
configured wakeup source (POWER_ON_N, RESET_IN_N) or the expiry of the periodic TAU timer.


_Note: When using PSM, the POWER_ON_N signal must be floating. If this signal is grounded, it will automatically trigger a wake. When_
_the PSM mode is activated, the VGPIO voltage is switched off and I/O pins states are undefined. Once the module is woken up, the VGPIO_
_is switched on again and the I/O pin states return to the states they had before entering PSM. To avoid extra power-consumption, the_
_host should place the signals connected to the module in high impedance or floating._





















|1. User enables LTE PSM. Module transmits TAU and exchanges data with network|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Module<br>registered on<br>network<br>1. User enables LTE PSM.<br>2. Module requests user-specified TAU-timer period.<br>3. Network responds with actual TAU-timer period to use.<br>4. Module enters and stays in idle mode until idle mode<br>  remains uninterrupted for the Active timer duration.<br>Wake event:<br>  - TAU timer expires<br>Power<br>up<br>Data<br>Tx<br>Idle window — Module waits for Rx<br>Module returns to<br>dormant state,<br>LTE PSM cycle repeats<br>exchanges data with network<br>Power<br>off<br>Module enters LTE PSM<br>(Dormant, very low<br>power)<br>Power<br>off|Module<br>registered on<br>network<br>1. User enables LTE PSM.<br>2. Module requests user-specified TAU-timer period.<br>3. Network responds with actual TAU-timer period to use.<br>4. Module enters and stays in idle mode until idle mode<br>  remains uninterrupted for the Active timer duration.<br>Wake event:<br>  - TAU timer expires<br>Power<br>up<br>Data<br>Tx<br>Idle window — Module waits for Rx<br>Module returns to<br>dormant state,<br>LTE PSM cycle repeats<br>exchanges data with network<br>Power<br>off<br>Module enters LTE PSM<br>(Dormant, very low<br>power)<br>Power<br>off|Module<br>registered on<br>network<br>1. User enables LTE PSM.<br>2. Module requests user-specified TAU-timer period.<br>3. Network responds with actual TAU-timer period to use.<br>4. Module enters and stays in idle mode until idle mode<br>  remains uninterrupted for the Active timer duration.<br>Wake event:<br>  - TAU timer expires<br>Power<br>up<br>Data<br>Tx<br>Idle window — Module waits for Rx<br>Module returns to<br>dormant state,<br>LTE PSM cycle repeats<br>exchanges data with network<br>Power<br>off<br>Module enters LTE PSM<br>(Dormant, very low<br>power)<br>Power<br>off|Module<br>registered on<br>network<br>1. User enables LTE PSM.<br>2. Module requests user-specified TAU-timer period.<br>3. Network responds with actual TAU-timer period to use.<br>4. Module enters and stays in idle mode until idle mode<br>  remains uninterrupted for the Active timer duration.<br>Wake event:<br>  - TAU timer expires<br>Power<br>up<br>Data<br>Tx<br>Idle window — Module waits for Rx<br>Module returns to<br>dormant state,<br>LTE PSM cycle repeats<br>exchanges data with network<br>Power<br>off<br>Module enters LTE PSM<br>(Dormant, very low<br>power)<br>Power<br>off|Module<br>registered on<br>network<br>1. User enables LTE PSM.<br>2. Module requests user-specified TAU-timer period.<br>3. Network responds with actual TAU-timer period to use.<br>4. Module enters and stays in idle mode until idle mode<br>  remains uninterrupted for the Active timer duration.<br>Wake event:<br>  - TAU timer expires<br>Power<br>up<br>Data<br>Tx<br>Idle window — Module waits for Rx<br>Module returns to<br>dormant state,<br>LTE PSM cycle repeats<br>exchanges data with network<br>Power<br>off<br>Module enters LTE PSM<br>(Dormant, very low<br>power)<br>Power<br>off|
|Module<br>registered on<br>network<br>1. User enables LTE PSM.<br>2. Module requests user-specified TAU-timer period.<br>3. Network responds with actual TAU-timer period to use.<br>4. Module enters and stays in idle mode until idle mode<br>  remains uninterrupted for the Active timer duration.<br>Wake event:<br>  - TAU timer expires<br>Power<br>up<br>Data<br>Tx<br>Idle window — Module waits for Rx<br>Module returns to<br>dormant state,<br>LTE PSM cycle repeats<br>exchanges data with network<br>Power<br>off<br>Module enters LTE PSM<br>(Dormant, very low<br>power)<br>Power<br>off|||||
||~~Periodic TAU (T3412)~~<br>Active Timer<br>(T3324)|||Tim|
||~~Periodic TAU (T3412)~~<br>Active Timer<br>(T3324)|TAU<br>procedure|TAU<br>procedure|TAU<br>procedure|
||||||
||~~PSM Cycle~~||||


_Figure 3-6: PSM Example (Simplified)_







Typical candidates for PSM are systems (such as monitors and sensors) that:

**•**
Require long battery life (low power consumption)

**•**
Tolerate very long latency for mobile-terminated SMS/data

**•** Do not use mobile-terminated voice

**•**
Send and/or receive data infrequently and periodically (e.g. on a given schedule of once every few hours, days,
weeks, etc.)


For example, a module connected to a sensor can be configured to:

**·**
Wake periodically to transmit collected data to a server or network entity.

**·**
Wait a short (configured) period of time to receive transmissions (e.g 60 seconds) and then return to its
dormant state.


Table 3-6 on page 30 describes the available triggers for waking an RC76xx from PSM. These triggers are configured
using the methods described in Table 3-7.


Rev. 16 March 2025 32 41113440


Product Technical Specification


**Table 3-7: PSM-Related Application User Commands/Interfaces**







|Type|Command/Interfacea|Description|Col4|
|---|---|---|---|
|AT|**+CPSMS**|3GPP-defined command (3GPP TS27.007 Release 12) that allows direct control of<br>all LTE PSM parameters, and is useful for advanced users wanting to test/<br>experiment with different options. This command is limited to networks that<br>support PSM.<br>It is not expected that every user must be fully versed in the details of PSM to take<br>advantage of its capabilities.<br>Use this command to:<br>**•**<br>Enable/disable LTE PSM.<br>**•**<br>Configure Period TAU timer (T3412) with a requested maximum duration of<br>the dormant period.<br>**•**<br>Configure Active timer (T3324) with a requested ‘idle mode time’ (the duration<br>the module remains idle before going dormant)<br>**•**<br>This command follows the 3GPP TS 27.007, Release 12 specification, with<br>exceptions noted for certain parameters.<br>_Note: The requested timer values are negotiated with the network and the final_<br>_negotiated values take effect immediately, then persist across power cycles (e.g. after a_<br>_power cycle, the settings will be used during network attach)._|3GPP-defined command (3GPP TS27.007 Release 12) that allows direct control of<br>all LTE PSM parameters, and is useful for advanced users wanting to test/<br>experiment with different options. This command is limited to networks that<br>support PSM.<br>It is not expected that every user must be fully versed in the details of PSM to take<br>advantage of its capabilities.<br>Use this command to:<br>**•**<br>Enable/disable LTE PSM.<br>**•**<br>Configure Period TAU timer (T3412) with a requested maximum duration of<br>the dormant period.<br>**•**<br>Configure Active timer (T3324) with a requested ‘idle mode time’ (the duration<br>the module remains idle before going dormant)<br>**•**<br>This command follows the 3GPP TS 27.007, Release 12 specification, with<br>exceptions noted for certain parameters.<br>_Note: The requested timer values are negotiated with the network and the final_<br>_negotiated values take effect immediately, then persist across power cycles (e.g. after a_<br>_power cycle, the settings will be used during network attach)._|
|AT|**!POWERMODE**|Custom Semtech command that allows application developers to enable<br>PSM without the complexity of the AT+CPSMS syntax|Custom Semtech command that allows application developers to enable<br>PSM without the complexity of the AT+CPSMS syntax|
|AT|**!POWERWAKE**|Custom Semtech command used to configure PSM timers (TAU time, active<br>time) in seconds. Note that only timer values supported by the 3GPP standard are<br>allowed.|Custom Semtech command used to configure PSM timers (TAU time, active<br>time) in seconds. Note that only timer values supported by the 3GPP standard are<br>allowed.|
|AT|_Note: AT!POWERWAKE (configuration of PSM timers) should be used with AT!POWERMODE (activation of the PSM_<br>_feature). Using these proprietary SWI commands is equivalent to using the 3GPPP AT+CPSMS command. AT+CPSMS will_<br>_automatically change settings in AT!POWERMODE / AT!POWERWAKE and vice versa. As soon as the network accepts the_<br>_PSM feature based on these command settings, the PSM power state will be activated in the RC76 module (see_<br>_Table 3-5 for details)._|_Note: AT!POWERWAKE (configuration of PSM timers) should be used with AT!POWERMODE (activation of the PSM_<br>_feature). Using these proprietary SWI commands is equivalent to using the 3GPPP AT+CPSMS command. AT+CPSMS will_<br>_automatically change settings in AT!POWERMODE / AT!POWERWAKE and vice versa. As soon as the network accepts the_<br>_PSM feature based on these command settings, the PSM power state will be activated in the RC76 module (see_<br>_Table 3-5 for details)._|_Note: AT!POWERWAKE (configuration of PSM timers) should be used with AT!POWERMODE (activation of the PSM_<br>_feature). Using these proprietary SWI commands is equivalent to using the 3GPPP AT+CPSMS command. AT+CPSMS will_<br>_automatically change settings in AT!POWERMODE / AT!POWERWAKE and vice versa. As soon as the network accepts the_<br>_PSM feature based on these command settings, the PSM power state will be activated in the RC76 module (see_<br>_Table 3-5 for details)._|


a. [For AT command details, refer to RC76xx AT Command Reference, available at http://source.sierrawireless.com.](http://source.sierrawireless.com)


**PSM Process Example**


The following example describes how the module uses PSM (as shown in Figure 3-4):


**1.** Module registers on an LTE network.


**2.** User enables PSM via AT command or API library function, specifying the desired TAU timer and Active timer
periods, and optional wakeup sources.


**3.** Module submits the PSM request (including desired TAU timer) to the network.


**4.** Network responds and indicates whether PSM is supported and (if it is) indicates the actual TAU timer to use.


Rev. 16 March 2025 33 41113440


Technical Specifications


**5.** If the network supports PSM:


**a.** Module enters idle mode (waiting for Rx from network).


**b.** When module has remained idle for the Active timer period, module powers off (except for maintaining
timer and interrupts) and enters PSM.


**c.** Module remains in PSM for the specified period or until a configured trigger (POWER_ON_N, RESET_IN_N)
wakes it.


_Note: If traffic must be transmitted when the module is in the sleep portion of the cycle, the module can initiate data/SMS/voice session_
_immediately._


**d.** Module powers up before TAU timer expires, then transmits TAU and/or exchanges data with network.


**e.** Module enters idle mode and cycle repeats.


_Note: When the module is powered up, the PSM request can be re-issued with different timers and triggers to adjust the PSM behavior._
_These new settings take effect immediately._


**Important Notes:**

**•**
Carefully select the PSM Periodic-TAU timer and Active Time values to match the intended use case(s) for the
module:

**·**
Periodic TAU PSM Cycle timer (T3412)—Note that while the module is dormant (for the duration of this
timer, unless woken by POWER_ON_N or RESET_IN_N), it will be completely unreachable by the network.

**·**
Active Time (Idle mode time after transmission (T3324))—Make sure to set the Active timer high enough to
provide appropriate delay-tolerance for mobile-terminated/network-originated transmissions to be received.

**•**
When using multiple devices, consider scheduling the modules to wake at different times so that the network
does not get flooded by all modules waking and transmitting simultaneously.


_Note: RC76xx series modules do not support waking up via ADC or GPIO in PSM state._

###### **3.2.5 Active State to PSM Transition**


If the module will be used in situations where it needs to be active very infrequently (for example, in a remote
monitoring station that must transmit data periodically—e.g. on a regular schedule ranging from days to weeks or
more), PSM may be used to reduce power consumption much more than is possible in Sleep state. Refer to
Figure 3-4 for transition conditions. If the module does not enter PSM, the request must be explicitly repeated—the
module will not attempt to enter PSM automatically.

###### **3.2.6 Extended Discontinuous Reception (eDRX)**


The RC76xx supports eDRX, which is a ‘flexible sleep’ active mode that allows for longer sleep duration (T I-eDRX ) and
a significant decrease in power consumption compared to regular DRX (T I-DRX ).


Rev. 16 March 2025 34 41113440


Product Technical Specification



Page received,















_Figure 3-7: eDRX Example (Simplified)_


Specifically, the RC76xx supports eDRX, which extend the DRX cycle (the paging cycle comprised of a paging window
during which the module is awake and able to receive or transmit on the network, and a sleep period during which
the network cannot wake the module) by increasing the sleep duration beyond the DRX maximum of 2.56 seconds:

**•**
I-eDRX (Idle mode eDRX)—The sleep duration of the DRX cycle can be set up to 44 minutes for LTE-M.


_Note: If traffic must be transmitted when the module is in the sleep portion of the cycle, the module can initiate data/SMS/voice session_
_immediately._


Rev. 16 March 2025 35 41113440


Technical Specifications


Table 3-8 describes the available methods for configuring eDRX.


**Table 3-8: eDRX-Related Commands** **[a]**

|Type|Command|Description|
|---|---|---|
|AT|**+CEDRXS**|Enable/disable eDRX, and configure related settings|
|AT|**+CEDRXRDP**|Display current eDRX settings|



a. [For AT command details, refer to RC76xx AT Command Reference, available at http://source.sierrawireless.com.](http://source.sierrawireless.com)


**3.2.6.1 eDRX Process Example**


**•**
Use the AT+CEDRXS command to configure the desired eDRX behavior.

**•**
During the network attachment process:

**·**
eDRX request and settings are sent to the network

**·**
Network responds and indicates whether eDRX is supported for the connection and may adjust the eDRX
parameters.

**•**
If eDRX is supported by the network:

**·**
While in active mode (connected), the sleep duration is used if supported, otherwise the regular DRX sleep
duration is used.

**·**
While in idle mode, the I-eDRX sleep duration is used if supported, otherwise the network uses the standard
LTE I-DRX value.


**Important Notes:**


**•**
The sleep duration must be carefully selected to match the intended use case(s) for the module. While the
module is asleep, it will be unreachable by the network. The duration should provide appropriate delaytolerance for mobile-terminated / network-originated transmissions to be received.

**•**
Due to the extended sleep time compared to regular DRX, eDRX is not suitable for most mobile-terminated
voice connections.

**•**
Network-side store and forward is supported — Packets will be stored until the module is reachable.

###### **3.2.7 Current Consumption**


The following tables describe the Semtech RC76xx module’s current consumption under various power states.
Typical values are measured at nominal supply voltage, nominal ambient temperature, and with a conducted 50 Ω
load on the antenna port.


Rev. 16 March 2025 36 41113440


Product Technical Specification


_Note: All current consumption values are tested on the Sierra Development Kit._


**Table 3-9: RC7611, RC7611-1 Current Consumption Values**





























|Power State|Parameter|Col3|Min.a|Typ.a|Max.b|Units|
|---|---|---|---|---|---|---|
|Active|Active|Active|Active|Active|Active|Active|
|LTE Data transferc|B2|B2|210d|700e|980e|mA|
|LTE Data transferc|B4|B4|210d|710e|1000e|mA|
|LTE Data transferc|B5|B5|190d|570e|700e|mA|
|LTE Data transferc|B12|B12|190d|610e|700e|mA|
|LTE Data transferc|B13|B13|190d|680e|800e|mA|
|LTE Data transferc|B14|B14|190d|700e|800e|mA|
|LTE Data transferc|B25|B25|210d|720e|980e|mA|
|LTE Data transferc|B26|B26|190d|580e|700e|mA|
|LTE Data transferc|B66|B66|220d|700e|1000e|mA|
|LTE Data transferc|B71|B71|190d|600e|700e|mA|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB active|25|26|39|mA|
|Airplane modef|Radio off|USB active|25|25|36|mA|
|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB-SS|1.7|1.8|6|mA|
|Idle—LTE eDRXg|Period: 40.96 sec|USB-SS|1.5|1.8|4|mA|
|Airplane modef|Radio off|USB-SS|1|1.3|4|mA|
|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|
|PSM Dormant|Non-active|Non-active|7|10|20|uA|
|OFF (VBATT_ON)|Non-active|Non-active|3|6|10|uA|
|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|
|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|23|25|35|mA|
|Tracking (Registered)|Tracking (Registered)|Tracking (Registered)|23|25|35|mA|


a. Input 3.7V, normal temperature

b. Input 3.4V, 70 [o] C

c. Bandwidth 10 MHz, UP/DL RB=50, enable throughput, modulation:QPSK

d. Tx min.


e. Tx max.

f. Radio is turned off and all interfaces setting are default without any external control connection.

g. eDRX test condition: eDRX setting: at+cedrxs=1,4,"0011", eDRX period = 40.96 sec, PTW = 5.12 sec, DRX cycle = 64 ms, For details
on AT commands, see Semtech RC76xx AT Command Reference.


Rev. 16 March 2025 37 41113440


Technical Specifications


h. GNSS current consumption values are for the GNSS radio only. For total consumption, add the GNSS value to the consumption for the
mode being used.


**Table 3-10: RC7620, RC7620-1 Current Consumption Values**
























|Power State|Parameter|Min.a|Typ.a|Max.b|Units|
|---|---|---|---|---|---|
|Active|Active|Active|Active|Active|Active|
|GSM/GPRS/EDGE<br>data transfer|E-GSM 900|160c|600d|2160d,e<br>1020d,f|mA|
|GSM/GPRS/EDGE<br>data transfer|DCS 1800|150c|560d|1278d,e<br>665f|mA|
|HSDPA data<br>transferg|B1|180c|803d|1140d|mA|
|HSDPA data<br>transferg|B8|150c|550d|840d|mA|
|LTE Data transferh|B1|240c|790d|850d|mA|
|LTE Data transferh|B3|240c|740d|900d|mA|
|LTE Data transferh|B7|300c|770d|980d|mA|
|LTE Data transferh|B8|210c|620d|700d|mA|
|LTE Data transferh|B20|210c|750d|850d|mA|
|LTE Data transferh|B28|210c|670d|710d|mA|
|Idle—GSM/<br>GPRS/EDGE|**•**<br>Registered<br>**•**<br>MFRM=9<br>**•**<br>USB active|25|25|36|mA|
|Idle—WCDMA|**•**<br>Registered<br>**•**<br>DRX=8<br>**•**<br>USB active|25|25|36|mA|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256<br>**•**<br>USB active|25|26|39|mA|
|Airplane modei|**•**<br>Radio off<br>**•**<br>USB active|25|25|36|mA|
|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep|
|Idle—GSM/<br>GPRS/EDGE|**•**<br>Registered<br>**•**<br>MFRM=9<br>**•**<br>USB-SS|1.7|1.8|4|mA|
|Idle—WCDMA|**•**<br>Registered<br>**•**<br>DRX=8<br>**•**<br>USB-SS|1.6|1.8|4|mA|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256<br>**•**<br>USB-SS|1.7|1.8|6|mA|



Rev. 16 March 2025 38 41113440


Product Technical Specification


**Table 3-10: RC7620, RC7620-1 Current Consumption Values (Continued)**













|Power State|Parameter|Min.a|Typ.a|Max.b|Units|
|---|---|---|---|---|---|
|Idle—LTE eDRXj|**•**<br>Period = 40.96<br>sec<br>**•**<br>USB-SS|1.5|1.8|4|mA|
|Airplane modei|**•**<br>Radio off<br>**•**<br>USB-SS|1|1.3|4|mA|
|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|
|PSM Dormant|Non-active|7|10|20|uA|
|OFF (VBATT_ON)|Non-active|3|6|10|uA|
|GNSSk|GNSSk|GNSSk|GNSSk|GNSSk|GNSSk|
|GNSS|Acquisition (Airplane<br>mode, cold start)|23|25|35|mA|
|GNSS|Tracking (Registered)|23|25|35|mA|


a. Input 3.7V, normal temperature
b. Input 3.4V, 70 [o] C
c. Tx min.

d. Tx max.
e. At GSM conducted 4 slot max Tx output power, measured at peak current on supported DC range.
f. At GSM conducted 4 slot max TX output power, measured at average current on supported DC range.
g. At WCDMA conducted max Tx output power. (see Table 3-33)
h. Bandwidth 10 MHz, UP/DL RB=50, enable throughput, modulation:QPSK
i. Radio is turned off and all interfaces setting are default without any external control connection.
j. eDRX test condition: eDRX setting: at+cedrxs=1,4,"0011", eDRX period = 40.96 sec, PTW = 5.12 sec, DRX cycle = 64 ms, For details
on AT commands, see Semtech RC76xx AT Command Reference.
k. GNSS current consumption values are for the GNSS radio only. For total consumption, add the GNSS value to the consumption for the
mode being used.


Rev. 16 March 2025 39 41113440


Technical Specifications



**Table 3-11: RC7630, RC7630-1 Current Consumption Values**

































|Power State|Parameter|Col3|Min.a|Typ.a|Max.b|Unit|
|---|---|---|---|---|---|---|
|Active|Active|Active|Active|Active|Active||
|LTE Data transferc|B1|B1|691d|743e|891e|mA|
|LTE Data transferc|B3|B3|650d|697e|802e|mA|
|LTE Data transferc|B5|B5|665d|712e|758e|mA|
|LTE Data transferc|B7|B7|700d|744e|804e|mA|
|LTE Data transferc|B8|B8|669d|718e|813e|mA|
|LTE Data transferc|B18|B18|693d|738e|869e|mA|
|LTE Data transferc|B19|B19|676d|725e|836e|mA|
|LTE Data transferc|B21|B21|507d|558e|661e|mA|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB active|25|26|39|mA|
|Airplane modef|Radio off|USB active|25|25|36|mA|
|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep||
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB-SS|1.7|1.8|6|mA|
|Idle—LTE eDRXg|Period: 40.96 sec|USB-SS|1.5|1.8|4|mA|
|Airplane modef|Radio off|USB-SS|1|1.3|4|mA|
|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode||
|PSM Dormant|Non-active|Non-active|7|10|20|uA|
|OFF (VBATT_ON)|Non-active|Non-active|3|6|10|uA|
|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh||
|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|23|25|35|mA|
|Tracking (Registered)|Tracking (Registered)|Tracking (Registered)|23|25|35|mA|


a. Input 3.7V, normal temperature

b. Input 3.4V, 70 [o] C

c. Bandwidth 10 MHz, UP/DL RB=50, enable throughput, modulation: QPSK

d. Tx min.


e. Tx max.

f. Radio is turned off and all interfaces setting are default without any external control connection.

g. eDRX test condition: eDRX setting: at+cedrxs=1,4,"0011", eDRX period = 40.96 sec, PTW = 5.12 sec, DRX cycle = 64 ms, For details
on AT commands, see Semtech RC76xx AT Command Reference.

h. GNSS current consumption values are for the GNSS radio only. For total consumption, add the GNSS value to the consumption for the
mode being used.


Rev. 16 March 2025 40 41113440


Product Technical Specification


**Table 3-12: RC7630J** **[a]** **Current Consumption Values**

































|Power State|Parameter|Col3|Min.b|Typ.b|Max.c|Unit|
|---|---|---|---|---|---|---|
|Active|Active|Active|Active|Active|Active||
|LTE Data transferd|B1|B1|691e|743f|891e|mA|
||B3|B3|650d|697e|802e|mA|
||B5|B5|665d|712e|758e|mA|
||B18|B18|693d|738e|869e|mA|
||B19|B19|676d|725e|836e|mA|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB active|25|26|39|mA|
|Airplane modeg|Radio off|USB active|25|25|36|mA|
|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep||
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB-SS|1.7|1.8|6|mA|
|Idle—LTE eDRXh|Period: 40.96 sec|USB-SS|1.5|1.8|4|mA|
|Airplane modef|Radio off|USB-SS|1|1.3|4|mA|
|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode||
|PSM Dormant|Non-active|Non-active|7|10|20|uA|
|OFF (VBATT_ON)|Non-active|Non-active|3|6|10|uA|
|GNSSi|GNSSi|GNSSi|GNSSi|GNSSi|GNSSi||
|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|23|25|35|mA|
|Tracking (Registered)|Tracking (Registered)|Tracking (Registered)|23|25|35|mA|


a. Limited availability.

b. Input 3.7V, normal temperature

c. Input 3.4V, 70 [o] C

d. Bandwidth 10 MHz, UP/DL RB=50, enable throughput, modulation: QPSK

e. Tx min.


f. Tx max.

g. Radio is turned off and all interfaces setting are default without any external control connection.

h. eDRX test condition: eDRX setting: at+cedrxs=1,4,"0011", eDRX period = 40.96 sec, PTW = 5.12 sec, DRX cycle = 64 ms, For details
on AT commands, see Semtech RC76xx AT Command Reference.

i. GNSS current consumption values are for the GNSS radio only. For total consumption, add the GNSS value to the consumption for the
mode being used.


Rev. 16 March 2025 41 41113440


Technical Specifications


**Table 3-13: RC7612, RC7612-1 Current Consumption Values (Limited Availability)**



























|Power State|Parameter|Col3|Min.a|Typ.a|Max.b|Units|
|---|---|---|---|---|---|---|
|Active|Active|Active|Active|Active|Active|Active|
|LTE Data<br>transferc|B2|B2|210d|700e|980e|mA|
|LTE Data<br>transferc|B4|B4|210d|710e|1000e|mA|
|LTE Data<br>transferc|B5|B5|190d|570e|700e|mA|
|LTE Data<br>transferc|B12|B12|190d|610e|700e|mA|
|LTE Data<br>transferc|B13|B13|190d|680e|800e|mA|
|HSDPA Data<br>transfer|B2|B2|240|720|1000|mA|
|HSDPA Data<br>transfer|B4|B4|250|740|1100|mA|
|HSDPA Data<br>transfer|B5|B5|210|600|720|mA|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB active|25|26|39|mA|
|Idle—HSDPA|**•**<br>Registered<br>**•**<br>DRX=8|USB active|25|25|36|mA|
|Airplane modef|Radio off|USB active|25|25|36|mA|
|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep|Sleep|
|Idle—LTE|**•**<br>Registered<br>**•**<br>Paging cycle=256|USB-SS|1.7|1.8|6|mA|
|Idle—HSDPA|**•**<br>Registered<br>**•**<br>DRX=8|USB active|1.6|1.8|4|mA|
|Idle—LTE<br>eDRXg|Period: 40.96 sec|USB-SS|1.5|1.8|4|mA|
|Airplane modef|Radio off|USB-SS|1|1.3|4|mA|
|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|Low Power Mode|
|PSM Dormant|Non-active|Non-active|7|10|20|uA|
|OFF (VBATT_ON)|Non-active|Non-active|3|6|10|uA|
|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|GNSSh|
|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|Acquisition (Airplane mode, cold start)|23|25|35|mA|
|Tracking (Registered)|Tracking (Registered)|Tracking (Registered)|23|25|35|mA|


a. Input 3.7V, normal temperature

b. Input 3.4V, 70 [o] C

c. Bandwidth 10 MHz, UP/DL RB=50, enable throughput, modulation:QPSK

d. Tx min.


e. Tx max.

f. Radio is turned off and all interfaces setting are default without any external control connection.


Rev. 16 March 2025 42 41113440


Product Technical Specification


g. eDRX test condition: eDRX setting: at+cedrxs=1,4,"0011", eDRX period = 40.96 sec, PTW = 5.12 sec, DRX cycle = 64 ms, For details
on AT commands, see Semtech RC76xx AT Command Reference.
h. GNSS current consumption values are for the GNSS radio only. For total consumption, add the GNSS value to the consumption for the
mode being used.

##### **3.3 RF**


This section presents the module’s WWAN RF interface, and defines the specifications for the LTE interface.


_Note: RF sensitivity values presented in this section are for soldered-down modules. Sensitivity values decrease for modules installed in_
_snap-in sockets, which might prevent the module from meeting 3GPP minimum specifications._


Semtech RC76xx is designed to be compliant with 3GPP Release 13 standards; refer to Network Technology
Specifications.


Rev. 16 March 2025 43 41113440


Technical Specifications


###### **3.3.1 Supported RF Bands**

**Table 3-14: Supported RF Band**





|RAT|Band|RC7612a|RC7612-1a|RC7630|RC7630-1|RC7630Ja|RC7620|RC7620-1|RC7611|RC7611-1|
|---|---|---|---|---|---|---|---|---|---|---|
|LTE|Category|4|1|4|1|4|4|1|4|1|
|LTE|B1|||Y|Y|Y|Y|Y|||
|LTE|B2|Y|Y||||||Y|Y|
|LTE|B3|||Y|Y|Y|Y|Y|||
|LTE|B4|Y|Y||||||Y|Y|
|LTE|B5|Y|Y|Y|Y|Y|||Y|Y|
|LTE|B7|||Y|Y||Y|Y|||
|LTE|B8|||Y|Y||Y|Y|||
|LTE|B12|Y|Y||||||Y|Y|
|LTE|B13|Y|Y||||||Y|Y|
|LTE|B14||||||||Y|Y|
|LTE|B18|||Y|Y|Y|||||
|LTE|B19|||Y|Y|Y|||||
|LTE|B20||||||Y|Y|||
|LTE|B21|||Y|Y||||||
|LTE|B25||||||||Y|Y|
|LTE|B26||||||||Y|Y|
|LTE|B28||||||Y|Y|||
|LTE|B66||||||||Y|Y|
|LTE|B71||||||||Y|Y|
|UMTS|B1||||||Y|Y|||
|UMTS|B2|Y|Y||||||||
|UMTS|B4|Y|Y||||||||
|UMTS|B5|Y|Y||||||||
|UMTS|B8||||||Y|Y|||
|GSM/GPRS/EDGE|E-GSM 900||||||Y|Y|||
|GSM/GPRS/EDGE|DCS 1800||||||Y|Y|||


Rev. 16 March 2025 44 41113440


Product Technical Specification


**Table 3-14: Supported RF Band (Continued)**

|RAT|Band|RC7612a|RC7612-1a|RC7630|RC7630-1|RC7630Ja|RC7620|RC7620-1|RC7611|RC7611-1|
|---|---|---|---|---|---|---|---|---|---|---|
|GNSS|GPS|Yb|Yb|Yb|Yb|Yb|Yb|Yb|Y b|Y b|
|GNSS|GLONASS|GLONASS|GLONASS|GLONASS|GLONASS|GLONASS|GLONASS|GLONASS|GLONASS|GLONASS|
|GNSS|Galileo|Galileo|Galileo|Galileo|Galileo|Galileo|Galileo|Galileo|Galileo|Galileo|
|GNSS|BeiDou|BeiDou|BeiDou|BeiDou|BeiDou|BeiDou|BeiDou|BeiDou|BeiDou|BeiDou|
|GNSS|QZSS|||Y|Y|Y|||||



a. Limited Availability
b. SKU-dependent

###### **3.3.2 LTE RF Interface**


This section presents the LTE RF specification for Semtech RC76xx modules.


**3.3.2.1 Tx Output Power**


The module’s LTE maximum transmitter output power is specified in Table 3-15.


**Table 3-15: RC7611, RC7611-1, RC7612** **[a]** **, RC7612-1** **[a]** **Conducted Tx Max Output Power Tolerances—**
**LTE** **[b]**

|RF Band|Operating Condition|Min|Typ|Max|Units|Notes|
|---|---|---|---|---|---|---|
|B2|Normal (25°C)|21|23|24|dBm|Power class 3|
|B4|Normal (25°C)|21|23|24|dBm|Power class 3|
|B5|Normal (25°C)|21|23|24|dBm|Power class 3|
|B12|Normal (25°C)|21|23|24|dBm|Power class 3|
|B13|Normal (25°C)|21|23|24|dBm|Power class 3|
|B14|Normal (25°C)|21|23|24|dBm|Power class 3|
|B25|Normal (25°C)|21|23|24|dBm|Power class 3|
|B26|Normal (25°C)|21|23|24|dBm|Power class 3|
|B66|Normal (25°C)|21|23|24|dBm|Power class 3|
|B71|Normal (25°C)|21|23|24|dBm|Power class 3|



a. Limited Availability
b. Stated typical power tolerance satisfies 3GPP TS 36.521-1 requirements for normal (25°C).


Rev. 16 March 2025 45 41113440


Technical Specifications


**Table 3-16: RC7620, RC7620-1 Conducted Tx Max Output Power Tolerances—LTE** **[a]**

|RF Band|Operating Condition|Min|Typ|Max|Units|Notes|
|---|---|---|---|---|---|---|
|B1|Normal (25°C)|21|23|24|dBm|Power class 3|
|B3|Normal (25°C)|21|23|24|dBm|Power class 3|
|B7|Normal (25°C)|21|23|24|dBm|Power class 3|
|B8|Normal (25°C)|21|23|24|dBm|Power class 3|
|B20|Normal (25°C)|21|23|24|dBm|Power class 3|
|B28|Normal (25°C)|21|23|24|dBm|Power class 3|



a. Stated typical power tolerance satisfies 3GPP TS 36.521-1 requirements for normal (25°C).


**Table 3-17: RC7630, RC7630-1 Conducted Tx Max Output Power Tolerances—LTE** **[a]**

|RF Band|Operating Condition|Min|Typ|Max|Units|Notes|
|---|---|---|---|---|---|---|
|B1|Normal (25°C)|21|23|24|dBm|Power class 3|
|B3|Normal (25°C)|21|23|24|dBm|Power class 3|
|B5|Normal (25°C)|21|23|24|dBm|Power class 3|
|B7|Normal (25°C)|21|23|24|dBm|Power class 3|
|B8|Normal (25°C)|21|23|24|dBm|Power class 3|
|B18|Normal (25°C)|21|23|24|dBm|Power class 3|
|B19|Normal (25°C)|21|23|24|dBm|Power class 3|
|B21|Normal (25°C)|21|23|24|dBm|Power class 3|



a. Stated typical power tolerance satisfies 3GPP TS 36.521-1 requirements for normal (25°C).


Rev. 16 March 2025 46 41113440


Product Technical Specification


**Table 3-18: RC7630J** **[a,b]** **Conducted Tx Max Output Power Tolerances—LTE**

|RF Band|Operating Condition|Min|Typ|Max|Units|Notes|
|---|---|---|---|---|---|---|
|B1|Normal (25°C)|21|23|24|dBm|Power class 3|
|B3|Normal (25°C)|21|23|24|dBm|Power class 3|
|B5|Normal (25°C)|21|23|24|dBm|Power class 3|
|B18|Normal (25°C)|21|23|24|dBm|Power class 3|
|B19|Normal (25°C)|21|23|24|dBm|Power class 3|



a. Stated typical power tolerance satisfies 3GPP TS 36.521-1 requirements for normal (25°C).
b. Limited availability.


**3.3.2.2 Rx Sensitivity**


The module’s LTE receiver sensitivity is specified in the following tables.


**Table 3-19: RC7611, RC7611-1, RC7612** **[a]** **, RC7612-1** **[a]** **Conducted Rx Sensitivity—LTE Bands** **[b]**





















|LTE Bands|Col2|+25°C (dBm)<br>Primary Secondary SIMO<br>(Typical) (Typical) (Typical)|Col4|Col5|Class A (dBm)<br>Primary Secondary SIMO<br>(Typical) (Typical) (Typical)|Col7|Col8|SIMO<br>(Worst<br>case)c|
|---|---|---|---|---|---|---|---|---|
|B2|Full RB<br>BW: 10 MHzd|-98|-98|-100|-97|-97.5|-99.5|-94.3|
|B4|B4|-98|-97.5|-99.5|-97|-96.5|-98.5|-96.3|
|B5|B5|-99|-98|-100.5|-98|-97|-99.5|-94.3|
|B12|B12|-97|-96|-99|-96|-95.5|-98|-93.3|
|B13|B13|-97.5|-95|-99|-96|-94|-98|-93.3|
|B14|B14|-96.5|-97|-99.5|-96.5|-96|-98.5|-93.3|
|B25|B25|-98|-98|-100|-97|-97.5|-99.5|-92.8|
|B26|B26|-99|-98|-100.5|-98|-97|-99.5|-93.8|
|B66|B66|-98|-98|-100|-97|-97|-99|-95.8|
|B71|B71|-98|-97.5|-100|-96.5|-97|-99|-93.5|


a. Limited Availability
b. RF sensitivity values are for soldered-down modules.

c. Per 3GPP specification.

d. Sensitivity values scale with bandwidth: x_MHz_Sensitivity = 10_MHz_Sensitivity - 10×log(10 MHz/x_MHz)
Note: Bandwidth support is dependent on firmware version


Rev. 16 March 2025 47 41113440


**Table 3-20: RC7620, RC7620-1 Conducted Rx Sensitivity—LTE Bands** **[a]**



Technical Specifications





















|LTE Bands|Col2|+25°C (dBm)<br>Primary Secondary SIMO<br>(Typ.) (Typ.) (Typ.)|Col4|Col5|Class A (dBm)<br>Primary Secondary SIMO<br>(Typ.) (Typ.) (Typ.)|Col7|Col8|SIMO (Worst case)b|
|---|---|---|---|---|---|---|---|---|
|B1|Full RB<br>BW: 10<br>MHzc|-97.5|-96.5|-100|-96.5|-96|-99|-96.3|
|B3|B3|-97|-97|-100|-96.5|-97|-99|-93.3|
|B7|B7|-95|-96|-99|-94.5|-95|-98|-94.3|
|B8|B8|-98|-97|-100|-97.5|-96|-99|-93.3|
|B20|B20|-97|-96|-99|-97|-95|-99|-93.3|
|B28|B28|-96|-93|-98.5|-95.5|-92|-98|-94.8|


a. RF sensitivity values are for soldered-down modules.

b. Per 3GPP specification.

c. Sensitivity values scale with bandwidth: x_MHz_Sensitivity = 10_MHz_Sensitivity - 10×log(10 MHz/x_MHz)
Note: Bandwidth support is dependent on firmware version


**Table 3-21: RC7630, RC7630-1 Conducted Rx Sensitivity—LTE Bands** **[a]**

























|LTE Bands|Col2|+25°C (dBm)<br>Primary Secondary SIMO<br>(Typical) (Typical) (Typical)|Col4|Col5|Class A (dBm)<br>Primary Secondary SIMO<br>(Typical) (Typical) (Typical)|Col7|Col8|SIMO<br>(Worst case)b|
|---|---|---|---|---|---|---|---|---|
|B1|Full RB<br>BW:<br>10 MHzc|-98.5|-97.5|-101|-97|-96.5|-100|-96.3|
|B3|B3|-98.5|-98|-100.5|-97.5|-96.5|-99.5|-93.3|
|B5|B5|-98.5|-99|-101|-97|-97|-100|-94.3|
|B7|B7|-97|-97|-99|-96|-96|-98|-94.3|
|B8|B8|-98.5|-99|-101|-97.5|-98|-100|-93.3|
|B18|B18|-98.5|-99|-101|-97.5|-98|-100|-96.3|
|B19|B19|-98.5|-99|-101|-97.5|-98|-100|-96.3|
|B21|B21|-98.5|-100|-101|-97|-99|-100|-96.3|


a. RF sensitivity values are for soldered-down modules.

b. Per 3GPP specification

c. Sensitivity values scale with bandwidth: x_MHz_Sensitivity = 10_MHz_Sensitivity - 10×log(10 MHz/x_MHz)
Note: Bandwidth support is dependent on firmware version.


Rev. 16 March 2025 48 41113440


Product Technical Specification


**Table 3-22: RC7630J** **[a]** **Conducted Rx Sensitivity—LTE Bands** **[b]**

























|LTE Bands|Col2|+25°C (dBm)<br>Primary Secondary SIMO<br>(Typical) (Typical) (Typical)|Col4|Col5|Class A (dBm)<br>Primary Secondary SIMO<br>(Typical) (Typical) (Typical)|Col7|Col8|SIMO<br>(Worst case)c|
|---|---|---|---|---|---|---|---|---|
|B1|Full RB<br>BW:<br>10 MHzd|-98.5|-97.5|-101|-97|-96.5|-100|-96.3|
|B3|B3|-98.5|-98|-100.5|-97.5|-96.5|-99.5|-93.3|
|B5|B5|-98.5|-99|-101|-97|-97|-100|-94.3|
|B18|B18|-98.5|-99|-101|-97.5|-98|-100|-96.3|
|B19|B19|-98.5|-99|-101|-97.5|-98|-100|-96.3|


a. Limited availability.
b. RF sensitivity values are for soldered-down modules.

c. Per 3GPP specification

d. Sensitivity values scale with bandwidth: x_MHz_Sensitivity = 10_MHz_Sensitivity - 10×log(10 MHz/x_MHz)
Note: Bandwidth support is dependent on firmware version.

###### **3.3.3 GSM / GPRS / EDGE RF Interface**


This section presents the GSM / GPRS / EDGE RF specifications for Semtech RC7620 modules.


**3.3.3.1 GSM / GPRS / EDGE Tx Output Power**


**Table 3-23: Conducted Tx Max Output Power Tolerances—GSM / GPRS / EDGE** **[a]**

|RF Band|Min|Typ|Max|Units|Notes|
|---|---|---|---|---|---|
|E-GSM 900|31|33|34|dBm|GMSK mode (Class 4; 2 W, 33 dBm)|
|E-GSM 900|24.5|27|29.5|dBm|8PSK mode (Class E2; 0.5 W, 27 dBm)|
|DCS 1800|28|30|31|dBm|GMSK (Class 1; 1W, 30 dBm)|
|DCS 1800|23.5|26|28.5|dBm|8PSK (Class E2; 0.4W, 26 dBm)|



a. Stated power tolerance satisfy 3GPP TS 51.010-1 requirements for normal (25°C) conditions.


Rev. 16 March 2025 49 41113440


Technical Specifications



**3.3.3.2 GSM / GPRS / EDGE Rx Sensitivity**


**Table 3-24: Conducted Rx Sensitivity—GSM / GPRS / EDGE Bands** **[a]**







|Col1|@ +25°C (dBm)b|@ Class A (dBm)c|
|---|---|---|
|E-GSM 900|-109|-108|
|DCS 1800|-109|-108|


a. Stated power tolerance satisfy 3GPP TS 51.010-1 requirements for normal (25°C) and Class A (extreme) conditions.

b. Typical value

c. Typical value, tested at Class A extreme condition

###### **3.3.4 WCDMA RF Interface**


This section presents the WCDMA RF specification for Semtech RC76xx modules.


**3.3.4.1 WCDMA Tx Output Power**


The module’s WCDMA maximum transmitter output power is specified in the following table.


**Table 3-25: RC7612, RC7612-1 Conducted Tx Max Output Power Tolerances—WCDMA**







|RF Band|Min|Typa|Max|Units|Notes|
|---|---|---|---|---|---|
|B2|21.5|23|24|dBm|Power class 3 bis|
|B4|21.5|23|24|dBm|Power class 3 bis|
|B5|21.5|23|24|dBm|Power class 3 bis|


a. Stated typical power tolerance satisfies 3GPP TS 34.121-1 requirements for normal (25°C) conditions.


**Table 3-26: RC7620, RC7620-1 Conducted Tx Max Output Power Tolerances—WCDMA**







|RF Band|Min|Typa|Max|Units|Notes|
|---|---|---|---|---|---|
|B1|21.5|23|24|dBm|Power class 3 bis|
|B8|21.5|23|24|dBm|Power class 3 bis|


a. Stated typical power tolerance satisfies 3GPP TS 34.121-1 requirements for normal (25°C) conditions.


Rev. 16 March 2025 50 41113440


Product Technical Specification


**3.3.4.2 RC76xx WCDMA Rx Sensitivity (Limited Availability)**


The module’s WCDMA receiver sensitivity is specified in the following table.


**Table 3-27: RC7612, RC7612-1 Conducted Rx Sensitivity—WCDMA Bands** **[a,b]**















|Band|+25°C<br>Primary Secondary<br>(dBm)c (dBm)c|Col3|Class A<br>Primary Secondary<br>(dBm)d (dBm)d|Col5|Standard Limit<br>(dBm)|Notes|
|---|---|---|---|---|---|---|
|B2|-109|-109|-109|-109|-104|CS 0.1% BER 12.2<br>kbps Reference<br>Measurement<br>Channel|
|B4|-110|-110|-110|-110|-106|-106|
|B5|-110|-109|-109|-109|-104|-104|


a. Stated sensitivity values satisfy 3GPP TS 34.121-1 V8.10.0 requirements for normal (25°C) and Class A (extreme) conditions.
b. RF sensitivity values are for soldered-down modules

c. Typical value.

d. Typical value, tested at Class A extreme temperature.


**Table 3-28: RC7620, RC7620-1 Conducted Rx Sensitivity—WCDMA Bands** **[a,b]**















|Band|+25°C<br>Primary Secondary<br>(dBm)c (dBm)c|Col3|Class A<br>Primary Secondary<br>(dBm)d (dBm)d|Col5|Standard Limit<br>(dBm)|Notes|
|---|---|---|---|---|---|---|
|B1|-108|-108|-107|-107|-106|CS 0.1% BER 12.2<br>kbps Reference<br>Measurement<br>Channel|
|B8|-110|-109|-109|-109|-103|-103|


a. Stated sensitivity values satisfy 3GPP TS 34.121-1 V8.10.0 requirements for normal (25°C) and Class A (extreme) conditions.
b. RF sensitivity values are for soldered-down modules

c. Typical value.

d. Typical value, tested at Class A extreme temperature.

###### **3.3.5 WWAN Antenna Interface**


The following table defines the WWAN antenna interfaces of the Semtech RC76xx modules.


**Table 3-29: WWAN Antenna Interface Pins**

|Pin #|Signal name|Direction|Function|
|---|---|---|---|
|30|GND||Diversity Antenna Ground|
|31|RF_DIV|Input|Diversity Antenna Interface|
|32|GND||Diversity Antenna Ground|
|48|GND||Primary Antenna Ground|
|49|RF_MAIN|Input/Output|Primary Antenna Interface|
|50|GND||Primary Antenna Ground|



Rev. 16 March 2025 51 41113440


Technical Specifications


**Table 3-29: WWAN Antenna Interface Pins (Continued)**

|Pin #|Signal name|Direction|Function|
|---|---|---|---|
|111|GND||Diversity Antenna Ground|
|113|GND||Diversity Antenna Ground|
|136|GND||Primary Antenna Ground|
|139|GND||Primary Antenna Ground|



_Note: For the routing of ground and RF signal, see Figure 5-4 and Figure 5-5._


**3.3.5.1 WWAN Antenna Recommendations**


Table 3-30 defines the key characteristics to consider for antenna selection.


**Table 3-30: Antenna Recommendations** **[a]**









|Parameter|Col2|Recommendations|Notes|
|---|---|---|---|
|Antenna system|Antenna system|External multi-band antenna system|Dual WWAN antennas for diversity (Antenna 1/<br>Antenna 2)b|
|Operating<br>bands|RC7611,<br>RC7611-1|617– 798 MHz|Operating bands depend on the module’s supported<br>bands/modes.|
|Operating<br>bands|RC7611,<br>RC7611-1|814 – 894 MHz|814 – 894 MHz|
|Operating<br>bands|RC7611,<br>RC7611-1|1710 – 2200 MHz|1710 – 2200 MHz|
|Operating<br>bands|RC7620,<br>RC7620-1|703 – 960 MHz|703 – 960 MHz|
|Operating<br>bands|RC7620,<br>RC7620-1|1710 – 1980 MHz|1710 – 1980 MHz|
|Operating<br>bands|RC7620,<br>RC7620-1|2110 – 2170 MHz|2110 – 2170 MHz|
|Operating<br>bands|RC7620,<br>RC7620-1|2500 – 2690 MHz|2500 – 2690 MHz|
|Operating<br>bands|RC7630,<br>RC7630-1|815 – 960 MHz|815 – 960 MHz|
|Operating<br>bands|RC7630,<br>RC7630-1|1710 – 2170 MHz|1710 – 2170 MHz|
|Operating<br>bands|RC7630,<br>RC7630-1|1447 – 1511 MHz|1447 – 1511 MHz|
|Operating<br>bands|RC7630,<br>RC7630-1|2500 – 2690 MHz|2500 – 2690 MHz|
|Operating<br>bands|RC7630Jc|815-894 MHz|815-894 MHz|
|Operating<br>bands|RC7630Jc|1710-2170 MHz|1710-2170 MHz|
|Operating<br>bands|RC7612,<br>RC7612-1c|617– 798 MHz|617– 798 MHz|
|Operating<br>bands|RC7612,<br>RC7612-1c|814 – 894 MHz|814 – 894 MHz|
|Operating<br>bands|RC7612,<br>RC7612-1c|1710 – 2200 MHz|1710 – 2200 MHz|


Rev. 16 March 2025 52 41113440


Product Technical Specification


**Table 3-30: Antenna Recommendations** **[a]** **(Continued)**






|Parameter|Col2|Recommendations|Notes|
|---|---|---|---|
|VSWR|VSWR|< 2.5:1 (worst case)|**•**<br>On all bands including band edges<br>**•**<br>Applies to both antennas|
|Total radiated efficiency|Total radiated efficiency|> 50% on all bands|**•**<br>Measured at the RF connector.<br>**•**<br>Applies to both antennas<br>**•**<br>Includes mismatch losses, losses in the<br>matching circuit, and antenna losses, excluding<br>cable loss.<br>**•**<br>Semtech recommends using antenna efficiency<br>as the primary parameter for evaluating the<br>antenna system.<br>**•**<br>Peak gain is not a good indication of antenna<br>performance when integrated with a host device<br>(the antenna does not provide omnidirectional<br>gain patterns). Peak gain can be affected by<br>antenna size, location, design type, etc.—the<br>antenna gain pattern remains fixed unless one<br>or more of these parameters change.|
|Radiation patterns|Radiation patterns|Nominally omnidirectional radiation<br>pattern in azimuth plane.||
|Envelope<br>correlation<br>coefficient<br>between<br>Antenna 1<br>and<br>Antenna 2||**•**<br>< 0.4 on B5 Rx (869–894 MHz),<br>B12 Rx (729–746 MHz), B13 Rx<br>(746–756 MHz), B14 Rx (758–768<br>MHz), B26 Rx (859–894 MHz) and<br>B71 Rx (617–652 MHz)<br>**•**<br>< 0.2 on B2 Rx (1930–1990 MHz),<br>B4 Rx (2110–2155 MHz), B25 Rx<br>(1930–1995 MHz) and B66 Rx<br>(2110–2200 MHz)||
|Mean<br>Effective<br>Gain (MEG)|| -3 dBi||
|Mean<br>Effective<br>Gain<br>Imbalance—<br>Antenna 1<br>and<br>Antenna 2<br>(MEG1 /<br>MEG2)||< 6 dB for diversity operation||
|Maximum<br>antenna gain||Must not exceed antenna gains due to<br>RF exposure and ERP/EIRP limits, as<br>listed in the module’s FCC grant.||



Rev. 16 March 2025 53 41113440


Technical Specifications



**Table 3-30: Antenna Recommendations** **[a]** **(Continued)**










|Parameter|Col2|Recommendations|Notes|
|---|---|---|---|
|Isolation<br>between<br>Antenna 1<br>and<br>Antenna 2<br>(S21)||> 10 dB|**•**<br>If antennas can be moved, test all positions for<br>both antennas.<br>**•**<br>Unless otherwise specified, this isolation<br>requirement must be maintained for optimum<br>operation.<br>**•**<br>Make sure all other wireless devices (Bluetooth<br>or WLAN antennas, etc.) are turned OFF to avoid<br>interference.|
|Maximum<br>voltage<br>applied to<br>antenna||6.3 VDC||
|Power<br>handling||> 1 W on all bands<br>> 2 W RF power on low bands|**•**<br>Measure power endurance over 4 hours<br>(estimated talk time) using a 2 W CW signal—<br>set the CW test signal frequency to the middle<br>of the PCS Tx band (1880 MHz for PCS).<br>**•**<br>Visually inspect device to ensure there is no<br>damage to the antenna structure and matching<br>components.<br>**•**<br>VSWR/TIS/TRP measurements taken before<br>and after this test must show similar results.|



a. These worst-case VSWR figures for the transmitter bands may not guarantee RSE levels to be within regulatory limits. The device
alone meets all regulatory emissions limits when tested into a cabled (conducted) 50 Ω system. With antenna designs with up to
2.5:1 VSWR or worse, the radiated emissions could exceed limits. The antenna system may need to be tuned in order to meet the RSE
limits as the complex match between the module and antenna can cause unwanted levels of emissions. Tuning may include antenna
pattern changes, phase/delay adjustment, passive component matching.
b. Antenna 1—Primary (RF_MAIN), Antenna 2—Secondary (RF_DIV) (Diversity)
c. Limited availability.

##### **3.4 GNSS**


The Semtech RC76xx includes Global Navigation Satellite System (GNSS) capabilities via the QUALCOMM IZat™
Gen8C Engine (formerly gpsOne), capable of operation in assisted and standalone GNSS modes (GPS/Galileo/
GLONASS/BeiDou/QZSS).


_Note: The Semtech RC76xx modules are not affected by the 6 April 2019 rollover. Software modifications extend the GPS rollover date to_

_12 December 2032._


Rev. 16 March 2025 54 41113440


Product Technical Specification

###### **3.4.1 Characteristics**


The GNSS implementation supports GPS L1, Galileo E1, BeiDou-B1 and GLONASS L1 FDMA operation.


**Table 3-31: GNSS Characteristics** **[a]**













|Parameter|Col2|Value|
|---|---|---|
|Sensitivityb|Standalone or MS-based tracking sensitivity|-160 dBm|
|Sensitivityb|Cold start acquisition sensitivity|-145 dBm|
|Sensitivityb|MS-assisted acquisition sensitivity|-158 dBm|
|Accuracy in open sky (1 Hz tracking)|Accuracy in open sky (1 Hz tracking)|< 2 m CEP-50|
|Satellite channels availablec|Acquisition|118|
|Satellite channels availablec|Simultaneous tracking|40|
|Support for predicted orbits|Support for predicted orbits|Yes|
|Predicted orbit CEP-50 accuracy|Predicted orbit CEP-50 accuracy|5 m|
|Standalone Time To First Fix (TTFF)|Hot|1 s|
|Standalone Time To First Fix (TTFF)|Warm|29 s|
|Standalone Time To First Fix (TTFF)|Cold|32 s|
|Altitude (max)|Altitude (max)|18,288 m (60,000 ft)|
|Velocity (max)|Velocity (max)|1,852 km/h (1150.8 mph)|
|Acceleration (max)|Acceleration (max)|20 m/s2|
|GNSS message protocols|GNSS message protocols|NMEA|
|Recommended signal power for GPS input|Recommended signal power for GPS input|Below -120 dBm|
|Maximum allowed GPS input|Maximum allowed GPS input|-116 dBm<br>(if noise figure < 3 is achieved)|


a. Acquisition / tracking sensitivity performance figures in conducted mode assume a 2.5 dB noise figure.

b. GNSS sensitivity may degrade for modules installed in snap-in sockets.

c. Resources are dynamically assigned and not constellation-specific.

###### **3.4.2 GNSS Antenna Interface**


The GNSS antenna interface is defined in Table 3-32.


**Table 3-32: GNSS Antenna Interface Pads**

|Pad|Name|Directiona|Function|
|---|---|---|---|
|37|GND||GNSS Antenna Ground|
|38|RF_GNSS|Input|GNSS Antenna Interface|
|39|GND||GNSS Antenna Ground|



Rev. 16 March 2025 55 41113440


Technical Specifications


**Table 3-32: GNSS Antenna Interface Pads (Continued)**

|Pad|Name|Directiona|Function|
|---|---|---|---|
|125|GND||GNSS Antenna Ground|
|128|GND||GNSS Antenna Ground|



a. Signal direction with respect to the module.


_Note: For the routing of ground and RF signal, see Figure 5-4 and Figure 5-5._

###### **3.4.3 Antenna Recommendations**


Table 3-33 defines the key characteristics to consider for antenna selection.


**Table 3-33: GNSS Standalone Antenna Recommendations** **[a]**






















|Parameter|Recommendations|Notes|
|---|---|---|
|Frequency range|**•**<br>Wide-band GPS, Galileo, GLONASS, and<br>BeiDou: 1559–1606 MHz recom-<br>mended<br>**•**<br>Narrow-band GPS: 1575.42 MHz ±<br>2.046 MHz minimum||
|Field of view (FOV)b|**•**<br>Omni-directional in azimuth<br>**•**<br>-45 to +90 in elevation||
|Polarization (average Gv/Gh)|> 0 dB|Vertical linear polarization is sufficient.|
|Free space average gain<br>(Gv+Gh) over FOV|> -6 dBi (preferably > -3 dBi)|Gv and Gh are measured and averaged over -<br>45 to +90 in elevation, and ±180 in<br>azimuth.|
|Gain|**•**<br>Maximum gain and uniform coverage in<br>the high elevation angle and zenith.<br>**•**<br>Gain in azimuth plane is not desired.||
|Average 3D gain|> -5 dBi||
|Isolation between GNSS and RF<br>Antenna|> 20 dB in all uplink bands||
|Typical VSWR|< 2.5:1||
|Polarization|Any other than LHCP (left-hand circular<br>polarized) is acceptable.|Type of antenna and polarization (RHCP/<br>linear) to be implemented is a matter of<br>consideration based on specific end<br>application.|
|Maximum voltage applied to<br>antenna|6.3 VDC||
|700 MHz harmonicb,c|< -56 dBm (input jammer 787.76 MHz at -<br>25 dBm and measure the harmonic tone at<br>1575.42 MHz)|This specification is for B13 and B14<br>coexistence.|



Rev. 16 March 2025 56 41113440


Product Technical Specification


**Table 3-33: GNSS Standalone Antenna Recommendations** **[a]** **(Continued)**







|Parameter|Recommendations|Notes|
|---|---|---|
|IIP2b,c|> 45 dBm (Input jammers at 824.6 MHz with<br>level -25 dBm and 2400 MHz with level<br>-32 dBm and measure output IM2 at<br>1575.4 MHz)|Out of band|
|IIP3b,c|> 2 dBm (Input jammers at 1712.7 MHz with<br>level -20 dBm and 1850 MHz with level<br>-65 dBm and measure output IM3 at<br>1575.4 MHz)|Out of band|
|Input 1 dB power compression<br>pointb,c|> -10 dBm||
|Out of band rejection for an active antenna|Out of band rejection for an active antenna|Out of band rejection for an active antenna|
|663–716 MHz|> 50 dB||
|777–798 MHz|> 50 dB||
|814–915 MHz|> 40 dB|50 dB is preferred|
|925–960 MHz|> 30 dB|50 dB is preferred|
|1427–1463 MHz|> 35 dB||
|1710–1785 MHz|> 35 dB||
|1850–1980 MHz|> 40 dB||
|2010–2025 MHz|> 40 dB||
|2305–2315 MHz|> 40 dB||
|2401–2483 MHz|> 40 dB||
|2500–2570 MHz|> 35 dB||


a. All values are preliminary and subject to change.
b. Noise figure: < 2dB, System gain: [14-17dB].


c. For the LNA used by an active antenna

##### **3.5 Electrical Specifications**


This section provides details of key electrical specifications.

###### **3.5.1 Absolute Maximum Ratings**


**Warning:** _If these parameters are exceeded, even momentarily, damage may occur to the device. In addition, extended application of_
_Absolute Maximum Rating conditions to the device may reduce device reliability._


Rev. 16 March 2025 57 41113440


Technical Specifications


_Note: Operation above the maximum specified operating voltage (see Table 3-3) is not recommended, and specified typical performance_
_or functional operation of the device is neither implied nor guaranteed._







|Table 3-34: Absolute Maximum Ratings|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Parameter**|**Parameter**|**Min**|**Typ**|**Max**|**Units**|
|**Power supply voltages**|**Power supply voltages**|**Power supply voltages**|**Power supply voltages**|**Power supply voltages**|**Power supply voltages**|
|VBAT_BB|Power Supply Input|0|-|6.0|V|
|VBAT_RF|Power Supply Input|0|-|5.5|V|
|VDD_Px (low-voltage (1.8V) operation)|Digital pad circuits|-0.5|-|2.3|V|
|VDD_Px (high-voltage (2.85V) operation)|Digital pad circuits|-0.5|-|3.35|V|
|**USB signal pins**|**USB signal pins**|**USB signal pins**|**USB signal pins**|**USB signal pins**|**USB signal pins**|
|USB_D+|High-speed USB data plus|-|-|3.6|V|
|USB_D-|High-speed USB data minus|-|-|3.6|V|
|USB_VBUS|High-speed USB bus voltage|-|-|5.25|V|
|**Thermal conditions**|**Thermal conditions**|**Thermal conditions**|**Thermal conditions**|**Thermal conditions**|**Thermal conditions**|
|TS|Storage temperature|-40||85|°C|
|TJ|Junction temperaturea|-|-|100|°C|
|**Maximum voltage applied to antenna interface pins**|**Maximum voltage applied to antenna interface pins**|**Maximum voltage applied to antenna interface pins**|**Maximum voltage applied to antenna interface pins**|**Maximum voltage applied to antenna interface pins**|**Maximum voltage applied to antenna interface pins**|
|VANT|RF_MAIN|-||6.3|Vdc|
|VANT|RF_DIV|-||6.3|Vdc|
|VANT|RF_GNSS|-||6.3|Vdc|
|**ESD ratings**|**ESD ratings**|**ESD ratings**|**ESD ratings**|**ESD ratings**|**ESD ratings**|
|SeeEMC and ESD Recommendations.|SeeEMC and ESD Recommendations.|SeeEMC and ESD Recommendations.|SeeEMC and ESD Recommendations.|SeeEMC and ESD Recommendations.|SeeEMC and ESD Recommendations.|


a. Refer to APN 2174283 Semtech - RC76xx - Thermal Model

###### **3.5.2 Digital I/O Characteristics**


The I/O characteristics for supported digital interfaces are described in:

**•** Table 3-35—GPIOs, UART, ANT_CNTL, TX_ON, PCM/I [2] S, SPI, I2C,
W_DISABLE_N, TP1, WAKE_ON_WWAN, and DR_SYNC signals

**•** Table 3-36—GPIO8 and GPIO28

**•** Table 3-37—UIM signals


Rev. 16 March 2025 58 41113440


Product Technical Specification


**•** Table 3-38 — GPIO6, SAFE_PWR_REMOVE, Clocks


**Table 3-35: Digital I/O Characteristics — V** **DD_IO** **= 1.80 V (nominal)**







|Parameter|Col2|Notes|Min|Max|Units|
|---|---|---|---|---|---|
|VIH|High level input voltage|CMOS/Schmitt|0.65 × VDD_IO|VDD_IO+ 0.3|V|
|VIL|Low level input voltage|CMOS/Schmitt|-0.3|0.35 × VDD_IO|V|
|VSHYS|Schmitt hysteresis voltage||100|-|mV|
|VOH|High level output voltage|CMOS, at pin-rated drive strength|VDD_IO- 0.45|VDD_IO|V|
|VOL|Low level output voltage|CMOS, at pin-rated drive strength|0|0.45|V|
|RP|Pull up/down resistance||55|390|kΩ|
|RK|Keeper resistance||30|150|kΩ|
|IIH|Input high leakage currenta|No pull-down|-|1|uA|
|IIL|Input low leakage currentb|No pull-up|-1|-|uA|
|CIN|Input capacitancec||-|5|pF|
|IPIN|Current per pin||-|16|mA|


a. Pin voltage = V DD_IO . For keeper pins, pin voltage = V DD_IO   - 0.45.

b. Pin voltage = GND and supply = V DD_IO . For keeper pins, pin voltage = 0.45 V and supply = V DD_IO

c. Input capacitance is guaranteed by design.


**Table 3-36: GPIO8 and GPIO28 Digital I/O Characteristics — V** **DD_IO** **= 1.80 V (nominal)**









|Parameter|Col2|Notes|Min|Max|Units|
|---|---|---|---|---|---|
|VIH|High level input voltage|CMOS/Schmitt|0.65 × VDD_IO|VDD_IO+ 0.3|V|
|VIL|Low level input voltage|CMOS/Schmitt|-0.3|0.35 × VDD_IO|V|
|VSHYS|Schmitt hysteresis voltage||165|-|mV|
|VOH|High level output voltage|CMOS, at pin-rated drive strength|0.8x VDD_IO|VDD_IO|V|
|VOL|Low level output voltage|CMOS, at pin-rated drive strength|0|0.2x VDD_IO|V|
|RP|Pull up/down resistance||10|50|kΩ|
|RK|Keeper resistance||10|50|kΩ|
|IIH|Input high leakage currenta|No pull-down|-|1|uA|
|IIL|Input low leakage currentb|No pull-up|-1|-|uA|
|IPIN|Current per pin||-|16|mA|
|CIN|Input capacitancec||-|5|pF|


a. Pin voltage = V DD_IO

b. Pin voltage = GND and supply = V DD_IO

c. Input capacitance is guaranteed by design.





Rev. 16 March 2025 59 41113440


Technical Specifications


**Table 3-37: UIM Characteristics — Dual-voltage V** **UIM_IO** **= 1.80 V or 2.85 V (nominal)**












|Parameter|Col2|Notes|Min|Max|Units|
|---|---|---|---|---|---|
|Common to UIM dual-voltage pads (1.8 V / 2.85 V)|Common to UIM dual-voltage pads (1.8 V / 2.85 V)|Common to UIM dual-voltage pads (1.8 V / 2.85 V)|Common to UIM dual-voltage pads (1.8 V / 2.85 V)|Common to UIM dual-voltage pads (1.8 V / 2.85 V)|Common to UIM dual-voltage pads (1.8 V / 2.85 V)|
|VIH|High level input voltage|CMOS/Schmitt|0.7 × VUIM_IO|VUIM_IO + 0.3|V|
|VIL|Low level input voltage|CMOS/Schmitt|-0.3|0.2 × VUIM_IO|V|
|VSHYS|Schmitt hysteresis voltage||100|-|mV|
|VOH|High level output voltage|CMOS, at pin-rated drive strength|0.8 × VUIM_IO|VUIM_IO|V|
|VOL|Low level output voltage|CMOS, at pin-rated drive strength|0|0.4|V|
|RP|Pull resistance|Pull-up and pull-down|10|100|kΩ|
|RK|Keeper resistance||10|100|kΩ|
|CI/O|I/O capacitancea||-|5|pF|
|Common to UIM pads at 2.85 V only|Common to UIM pads at 2.85 V only|Common to UIM pads at 2.85 V only|Common to UIM pads at 2.85 V only|Common to UIM pads at 2.85 V only|Common to UIM pads at 2.85 V only|
|IIH|Input high leakage currentb|No pull-down|-|10|uA|
|IIL|Input low leakage currentc|No pull-up|-10|-|uA|
|Common to UIM pads at 1.8 V only|Common to UIM pads at 1.8 V only|Common to UIM pads at 1.8 V only|Common to UIM pads at 1.8 V only|Common to UIM pads at 1.8 V only|Common to UIM pads at 1.8 V only|
|IIH|Input high leakage currentb|No pull-down|-|2|uA|
|IIL|Input low leakage currentc|No pull-up|-2|-|uA|



a. Input capacitance is guaranteed by design.

b. Pin voltage = V UIM_IO

c. Pin voltage = GND and supply = V UIM_IO


**Table 3-38: GPIO6, SAFE_PWR_REMOVE, Clocks — V** **DD_IO** **= 1.80 V (nominal)**

|Parameter|Col2|Notes|Min|Max|Units|
|---|---|---|---|---|---|
|VIH|High-level input voltage|CMOS/Schmitt|0.65 x VDD_IO|VDD_IO+0.3|V|
|VIL|Low-level input voltage|CMOS/Schmitt|-0.3|0.35 x VDD_IO|V|
|VSHYS|Schmitt hysteresis voltage||15|-|mV|
|IL|Input leakage currenta|VDD_IO= max, VIN = 0 V to VDD_IO|-0.20|+0.20|uA|
|VOH|High-level output voltage|IOUT= IOH|VDD_IO- 0.45|VDD_IO|V|
|VOL|Low-level output voltage|IOUT= IOL|0|0.45|V|
|IOH<br>c|High-level output current|VOUT= VOH|0.15|0.9|mA|
|IOL<br>c|Low-level output current|VOUT= VOL|0.15|0.9|mA|
|IOH_XO|High-level output current|XO digital clock outputs only|6|-|mA|
|IOL_XO|Low-level output current|XO digital clock outputs only|-|-6|mA|



Rev. 16 March 2025 60 41113440


Product Technical Specification


**Table 3-38: GPIO6, SAFE_PWR_REMOVE, Clocks — V** **DD_IO** **= 1.80 V (nominal) (Continued)**

|Parameter|Col2|Notes|Min|Max|Units|
|---|---|---|---|---|---|
|CIN|Input capacitanceb||-|5|pF|
|IIN<br>c|Input current|Internal pull-up|-|30|mA|
|IIN<br>c|Input current|Internal pull-downd|-|10|uA|



a. The GPIO6 pin complies with the input leakage specification only when configured as a digital input.
b. Input capacitance is guaranteed by design.
c. For GPIO6 only.
d. The default status of the internal pull down is 10 Ω A.

###### **3.5.3 Internal Devices**


Table 3-39 summarizes the frequencies generated within the Semtech RC76xx. This table is provided for reference
only to the device integrator.


**Table 3-39: Internal Device Frequencies**







|Subsystem / Feature|Frequency|Units|
|---|---|---|
|Real Time Clock|32.768|kHz|
|PCM Audio Interface (PCM Master Mode)|256 / 512 / 1024 / 2048 / 4096|kHz|
|I2C Interface|100|kHz|
|PMIC power supplies switching frequency|1.6|MHz|
|Fundamental clock|19.2|MHz|
|PLL|**•**<br>PLL0: 800.0000<br>**•**<br>PLL1: 614.4000<br>**•**<br>PLL2: 480.0000<br>**•**<br>PLL3: 600.6000<br>**•**<br>PLL4: 576.0000<br>**•**<br>PLL5: 691.2000<br>**•**<br>PLL6: Varies (1.2 GHz max)|MHz|
|SPI|38|MHz|
|USB|480|Mb/s|

##### **3.6 Processing**

###### **3.6.1 Application Core**

The Application Core is based on a Cortex A7 32-bit RISC architecture core. It has the following main characteristics:

**•**
Up to 1.3 GHz operation

**•** Cache:

**·**
L1: Instruction (32 kB) and Data (32 kB)

**·** L2: 256 kB


Rev. 16 March 2025 61 41113440


Technical Specifications


Refer to Interfaces Specifications for the list of interfaces supported by this core.

###### **3.6.2 Embedded Memory**


The Semtech RC76xx module includes Flash and RAM embedded memory as detailed in Table 3-40.


Refer to the latest customer release note for any changes regarding embedded memory.


**Table 3-40: Embedded Memory Details**

|Type|Details|Size|
|---|---|---|
|Flash|Total|128 MB|
|Flash|Reserved for Application processor|8 MB|
|Flash|Minimum number of write cycles|100, 000|
|RAM|Total|128 MB|
|RAM|Reserved for Application processor|40 MB|



The application processor memory is dedicated to the ThreadX platform, including Semtech Proprietary Applications.


**3.6.2.1 Flash Memory**


Flash memory is partitioned for use by various elements. Partition APPS can be used by the ThreadX firmware,
framework and application. The remaining partitions are reserved for internal use.


**Table 3-41: Flash Memory Partitions**


Rev. 16 March 2025 62 41113440


Product Technical Specification


**Table 3-41: Flash Memory Partitions (Continued)**


Rev. 16 March 2025 63 41113440


Technical Specifications


Follow these instructions to display partition sizes and to determine whether a customer firmware will fit:


**1.** Connect to the RC module.


**2.** Use **Trace32 command** . Partition sizes are listed in the ‘Start block’ and ‘Limit’ columns.


**3.** When building an image, use the **swicwe** command to display the sizes of the image components to ensure
that they can fit in the associated partitions. For example:

###### **3.6.3 Recovery Mechanism**


The Semtech RC76xx has the capability to automatically detect and recover from various corruption scenarios (for
example, corruption may occur when power is abruptly removed from the module).


A backup of the configuration stored in the file system is created before the RC76xx leaves the Semtech factory. The
file system backup can be updated at customer factories using **AT!NVBACKUP** . If a file system corruption is
detected, the stored backups are checked and the most recent backup is automatically restored.


To avoid the potential for memory corruption, make sure to always follow the proper power off procedure before
removing power from the module. (Figure 4-2 illustrates the signal timing details for powering off the module.)

###### **3.6.4 Secure Boot / Secure Debug**


Semtech RC76xx modules incorporate the following permanently enabled features to enhance device security:


Secure Boot—Ensures only firmware images signed by Semtech can be loaded and run on the RC76xx modules.
Specifically, Secure Boot applies to the following firmware components: system boot loader, carrier configuration,
and telecom FW.


Secure Debug—Disables debug features such as RAM dump collection and JTAG access to the module.


[For additional details, refer to application notes available on: http://source.sierrawireless.com](https://source.sierrawireless.com/)


Rev. 16 March 2025 64 41113440


Product Technical Specification

##### **3.7 Mechanical Drawing**


The Semtech RC76xx module’s LGA footprint is a 239-pad array of copper pads (see Physical Dimensions and
Connection Interface). The following drawing illustrates the device footprint and dimensions.


_Figure 3-8: Mechanical Drawing 1_


_Figure 3-9: Mechanical Drawing 2_


Rev. 16 March 2025 65 41113440


Technical Specifications

##### **3.8 Mechanical Specifications**


The following table describes additional mechanical specifications for the Semtech RC76xx module.


**Table 3-42: Mechanical Specifications**

|Specification|Value|Notes|
|---|---|---|
|Clamping force|20 psi|Maximum clamping force on module over entire shield surface.|



Rev. 16 March 2025 66 41113440


## **4**


### **4: Interfaces Specifications**

This section describes the interfaces supported by the Semtech RC76xx embedded module and provides specific
voltage, timing, and circuit recommendations for each interface.

##### **4.1 POWER_ON_N**


The Semtech RC76xx module requires a low level signal (POWER_ON_N) that is used to switch the module ON or
OFF.


The POWER_ON_N signal is internally pulled-up which signal level about 0.8V. An open collector or open drain
transistor or equivalent should be used to ground the signal when necessary to power on the module. To avoid any
damage or abnormal power on signal, do not design any external pull up circuit on this pin.


_Figure 4-1: POWER_ON_N_


To turn the module ON:


Power the module (VBATT on) and connect POWER_ON_N to ground for at least 200 ms and not more than ~7s.


_Note: If POWER_ON_N remains connected to the GND for more than ~7s, the module will start and turn off once POWER_ON_N is_

_released._


To turn the module OFF:


Send the AT command, AT!powerdown to turn off module. To avoid any boot issue, turn off the module by pressing
the power key or use the AT command to run a graceful shutdown process. While the module is in an active power
state mode, asserting POWER_ON_N to low over 1s will turn the module OFF. Table 4-1 describes the
POWER_ON_N signal's characteristics.


**Table 4-1: POWER_ON_N Electrical Characteristics** **[a]**

|Parameter|Min|Typ|Max|Units|
|---|---|---|---|---|
|Input Voltage—Low||-|0.35|V|
|Internal pull-up resistor|150|200|250|kΩ|



a. When floating, voltage will be approximately 800 mV.


Rev. 16 March 2025 67 41113440


Interfaces Specifications

###### **4.1.1 Power-up Sequence**


**4.1.1.1 Power On / Off Timing**


The host should not drive any signals to the module until the VGPIO raises up (approximately 100 ms after power
ups). Before reaching the “Active” state, signals on the host port must be set to “floating, high impedance, or input
pull-down”. This setting also applies when the module is in reset mode, during a firmware update, or during a
power-off sequence. The host must consider this signal setting when designing the module interface.


Figure 4-2 describes the timing sequence for powering the module on and off.











VBAT_BB / High
VBAT_RF Low


0.8V





POWER_ON_N


SAFE_PWR_REMOVE


VGPIO


USB_D+
(Single enumeration)


Host Signals
(GPIOs and Interfaces)



Low


High


Low


High


Low


High


Low


High


Low








|BATT applied POWER_ON_N low|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|Disconnected|Off|Power-on<br>Sequence|Power-on<br>Sequence|Active|Active|Power-off<br>Sequence|Power-off<br>Sequence|Off|Disconnected|
|||||||||t_pwr_remo||
||Assertion<br>time|Assertion<br>time|Assertion<br>time|Initiate power-off using<br>software commanda<br>de-asserted<br>>= 1s||||||
||Assertion<br>time|Assertion<br>time|Assertion<br>time|Initiate power-off using<br>software commanda<br>de-asserted<br>>= 1s|||||ve|
||Assertion<br>time|Assertion<br>time||||||||
||Assertion<br>time|Assertion<br>time|Assertion<br>time|Assertion<br>time||||||
||Assertion<br>time|Assertion<br>time|Assertion<br>time|Assertion<br>time||||||
||Assertion<br>time|Assertion<br>time|Assertion<br>time|Assertion<br>time||||||
|||t_pwr_on_seq|t_pwr_on_seq|||||||
|||t_pwr_on_seq|t_pwr_on_seq|||||||
|||||||||||
|||||||t_pwr_off_seq<br>b|t_pwr_off_seq<br>b|t_pwr_off_seq<br>b|t_pwr_off_seq<br>b|
||b|b|b|b|b|b|b|b||
||b|b|b|||||||
|||||||||||



_Figure 4-2: Signal Timing (POWER_ON_N, and USB Enumeration)_


**a.** After the **AT!POWERDOWN** command, the host should ensure that all of the I/O connected to the module
are actually either into HighZ, floating, or input pull-down, before the VGPIO switches off.


**b.** When the module is not on active status, the host should ensure that all of the I/O connected to the module

are actually either into HighZ, floating, or input pull-down.


**Table 4-2: POWER_ON_N Timing Parameters**












|Parameter|Typical|Maximum|Units|
|---|---|---|---|
|t_pwr_on_seq|7|24a|s|
|t_pwr_off_seq|0.4–5.5|6|s|
|t_pwr_remove|13|-|ms|
|POWER_ON_N assertion timeb|200 ms|7000 s||



a. Value is based on disabled custom parameter “BOOTQUIETDISABLE”. Note that there will be an increase in value if this custom
parameter is enabled.

b. Assertion time is the time required to keep POWER_ON_N at LOW level to ensure the module can be powered ON successfully.


Rev. 16 March 2025 68 41113440


Product Technical Specification


**4.1.1.2 USB Enumeration**


The unit supports single USB enumeration with the host. Enumeration starts within (maximum) t_pwr_on_seq
seconds of power-on.

###### **4.1.2 Software-Initiated Power Down**


To power down the module via software:


**1.** Initiate the power down process using **AT!POWERDOWN** .


**2.** Monitor VGPIO and SAFE_PWR_REMOVE.


**3.** When VGPIO and SAFE_PWR_REMOVE are on the low level, remove power.


_Note:_

**•** _If the VGPIO cannot be monitored from the design interface, measure the delay time (pulse from SAFE_PWR_REMOVE to VGPIO_
_must = 0, refer to Figure 4-33 for details) and include this information in the firmware to ensure that power can be removed safely._

**•** _It is highly recommended to run a graceful shutdown using the AT command:_ _**AT!POWERDOWN**_ _to enable powering down rather_
_than cutting off the power directly. This avoids flash/MCP/Memory write-back fail causing flip issues._

##### **4.2 Emergency Power Off**


The module can be switched off by controlling the RESET_IN_N pin. This must only be used in emergency situations
if the system freezes (not responding to commands).


To perform an emergency power off:


**1.** De-assert POWER_ON_N.


**2.** While POWER_ON_N is de-asserted, assert RESET_IN_N (logic low) for at least 8 s. This immediately powers
down the module.

##### **4.3 POWER_ON_N, RESET_IN_N, AT!POWERDOWN Use Cases**


Table 4-3 lists the behavior of the RC76xx depending on POWER_ON_N, RESET_IN_N and **AT!POWERDOWN** use

cases.


**Table 4-3: POWER_ON_N, RESET_IN_N and AT!POWERDOWN Use Cases**






|Use Case|Col2|Behavior|
|---|---|---|
|POWER_ON_N|VBATT is applied then POWER_ON_N is asserted|Turns ON|
|POWER_ON_N|POWER_ON_N is asserted then VBATT is applied|Turns ON|
|RESET_IN_Na|POWER_ON_N is left asserted then RESET_IN_N is asserted|Resets|
|RESET_IN_Na|POWER_ON_N is de-asserted then RESET_IN_N is asserted|Resets|
|RESET_IN_Na|POWER_ON_N is de-asserted then RESET_IN_N is asserted with a<br>long pulse (>8 sec)|Emergency OFF|



Rev. 16 March 2025 69 41113440


Interfaces Specifications


**Table 4-3: POWER_ON_N, RESET_IN_N and AT!POWERDOWN Use Cases (Continued)**

|Use Case|Col2|Behavior|
|---|---|---|
|**AT!POWERDOWNb**|POWER_ON_N is asserted then the power OFF command is sent|Restarts|
|**AT!POWERDOWNb**|POWER_ON_N is de-asserted then the power OFF command is sent|Turns OFF|



a. This pin should only be used for emergencies such as when the module stops responding to AT commands.
b. It is highly recommended to use graceful shutdown using AT command: AT!POWERDOWN to power down the module rather than
cutting the power directly. This prevents flash/MCP/Memory write back fail that results to a flip issue.

##### **4.4 Tx Power Control**


The module’s Tx power limit may be controlled using the following methods:

**•** SAR backoff AT commands (see document RC76xx AT Command Reference):

**· !SARSTATEDFLT** — Set (or report) the default SAR backoff state that the device uses when it powers up.
This setting is persistent across power cycles and overrides any PRI setting.

**· !SARSTATE** — Set (or report) the current SAR backoff state (override the default state). This change in state
is non-persistent across power cycles.

**· !SARBACKOFF** — Set (or report) the maximum Tx power limit for a specific band / technology / state combination.

**•** GPIO control via **!SARGPIO** command (see RC76xx AT Command Reference)—Set an unallocated external
GPIO to control SAR.

##### **4.5 USB**


The Semtech RC76xx implements a high-speed USB 2.0 Interface, which conforms to _Universal Serial Bus_
_Specification, Revision 2.0._


_Note: It is recommended to make the USB interface accessible through test points._


**Table 4-4: USB Pin Descriptions**

|Pin|Signal Name|Direction|Function|
|---|---|---|---|
|12|USB_D-|Input/Output|Differential data interface negative|
|13|USB_D+|Input/Output|Differential data interface positive|
|16|USB_VBUS|Input|USB supply voltage|



Rev. 16 March 2025 70 41113440


Product Technical Specification


**Table 4-5: USB_VBUS Characteristic**

|USB|Col2|Value|Units|
|---|---|---|---|
|USB_VBUS|Voltage range|4.75 - 5.25<br>or VBAT_BB|V|
|USB_VBUS|Maximum Current Drawn|1|mA|
|USB_VBUS|Maximum Input Capacitance<br>(Min ESR = 50 mΩ)|10|µF|



_**​**_



_**​**_



_**​**_



_**​**_



_Note: The USB interface has routing constraints. For details, refer to USB Interface._

##### **4.6 UART**


_**​**_



_**​**_



The Semtech RC76xx provides two UART interfaces:

**•**
UART1 (primary UART)—8-wire interface

**•**
UART2 (secondary UART)—4-wire interface (only for internal Semtech debug)


The UART interfaces are used for data communication between the module and a PC or host processor. These
interfaces comply with the RS-232 interface.

**•**
UART1 support baud rate: 2400 bps, 4800 bps, 19200 bps, 38400 bps, 57600 bps, 115200 bps, 230400 bps,
921600 bps, 4 Mbps

**•**
UART2 support baud rate: 115200 bps


Flow control is managed using the UART_RTS and UART_CTS signals.


Table 4-6 describes the signals used for UART1 and UART2.


_Note:_

**•** _UART signals are named with respect to the host device, and directions are listed with respect to the module. For example,_
_UART1_RX is an output from the module to the host. WIFI coex and 8-wire UART concurrency is not supported._

**•** _If there is no pull up setting on host side, or to avoid any unclear signal level when host side is in low power mode, it is recommended_
_to reserve a pull up resistor design on UART_RX and UART_TX pins. The typical resistor value is 100k_ Ω _. This value depends on appli-_
_cation and used hardware. For further information, contact a Semtech FAE_ _**​**_ _._


Rev. 16 March 2025 71 41113440


**Table 4-6: UART Pins**





Interfaces Specifications






























|Pin|Interface|Namea|Directionb|Function|Reset<br>State|If<br>Unused|Notes|
|---|---|---|---|---|---|---|---|
|2|UART1|UART1_RIc|Output|Ring Indicator<br>Signal incoming<br>calls (voice and<br>data), SMS, etc.|Pull Down|Leave<br>open|Do not install<br>external pull-up on<br>this pin, otherwise<br>the module will not<br>boot.|
|3|3|UART1_RTSd|Input|Ready To Send,<br>Flow Control|Pull Down||Highly<br>Recommended|
|4|4|UART1_CTSd|Output|Clear To Send,<br>Flow Control|Pull Down||Highly<br>Recommended|
|5|5|UART1_TXd|Input|Transmit Data|Pull Down||Highly<br>Recommended|
|6|6|UART1_RXd|Output|Receive Data|Pull Down||Highly<br>Recommended|
|7|7|UART1_DTRe|Input<br>(active low)|Data terminal<br>ready<br>Prevents the<br>RC76xx from<br>entering sleep<br>mode, switches<br>between data<br>mode and<br>command mode,<br>and wakes the<br>module.|Pull Down|Leave<br>open||
|8|8|UART1_DCD|Output|Data Carrier Detect<br>Signal data<br>connection in<br>progress|Pull Down|Leave<br>open|Do not install<br>external pull-up on<br>this pin, otherwise<br>the module will not<br>boot.|
|9|9|UART1_DSR|Output|Data Set Ready<br>Signal UART<br>interface is ON|Pull Down|Leave<br>open|Do not install<br>external pull-up on<br>this pin, otherwise<br>the module will not<br>boot.|
|96|UART2f,d|UART2_TX|Input|Transmit data|Pull Down||Highly<br>Recommended|
|97|97|UART2_RX|Output|Receive data|Pull Down||Highly<br>Recommended|
|98|98|UART2_RTS|Input|Ready To Send,<br>flow control|Pull Down||Highly<br>Recommended|
|99|99|UART2_CTS|Output|Clear To Send, flow<br>control|Pull Down||Highly<br>Recommended|



a. Signals are named with respect to the host device. For example, UART1_RX is the signal used by the host to receive data from the
module.


Rev. 16 March 2025 72 41113440


Product Technical Specification


b. Signal direction with respect to the module. For example, UART1_RX is an output from the module to the host.
c. RI can be used independently and supports the following AT commands: AT+WWAKESET and AT+WRID.
d. Must be accessible through 0 ohm resistors. Test points are highly recommended at module side.
e. Pin is ‘wakeable’. Can be used to trigger the module to wake up from sleep state. See Wakeup Interrupt (Sleep State) for details.The
pin will be floating when KSLEEP=0 and will be pull-up when KSLEEP=1 or 2. For details on KSLEEP, see the RC76xx AT Command
Guide.
f. For Semtech debug purposes.

##### **4.7 UIM Interface**


The Semtech RC76xx has two physical UIM interfaces:

**•** UIM1—this interface allows control of 1.8V or 2.85V UIMs. For RC7611, RC7611-1, RC7612, RC7612-1,
RC7620, RC7620-1, RC7630, RC7630-1, and RC7630J* it also supports single or external dual SIMs. For usage
details, see Figure 4-3 and Figure 4-4.

**•**
UIM2—this interface is used to control the following:

**·**
For RC7611, RC7611-1, RC7620, RC7620-1, RC7630, RC7630-1, RC7630J*: this interface is used to control
an eSIM on selected variants.

**·**
For RC7612 and RC7612-1 (Limited Availability): this interface allows control of 1.8V or 2.85V UIMs.


_Note:_

**•** _* Limited availability._

**•** _UIM1 and UIM2 cannot be activated simultaneously (DSSS).External UIM1 Interface._

**•** _UIM interface is compliant with ETSI TS 102 221 V12.0.0 (2014-12) Class B and Class C._

###### **4.7.1 External UIM1 Interface**


The following table describes the signals used for UIM1.


**Table 4-7: UIM1 Interface Pins**



















|Pin|Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|26|UIM1_VCC|Output|Supply output|Leave open|
|27|UIM1_CLK|Output|Clock|Leave open|
|28|UIM1_DATA|Input/Output|Data connection|Leave open|
|29|UIM1_RESET_N|Output|Reset|Leave open|
|64|UIM1_SIMA_DETb|Input|Detect UIM|Leave open|
|65|UIM1_SIMB_DET/GPIO4|Input|Detect UIMB|Leave open|
|65|UIM2_DETc/GPIO4|UIM2_DETc/GPIO4|Detect UIM2|Detect UIM2|
|46|Ext_SIM_switch/GPIO6|Output|Switch between UIMA and UIMB|Leave open|


a. Signal direction with respect to the module. Examples: UIM1_SIMA_DET (pin 64) is an input to the module from the host; UIM1_RESET_N (pin 29) is an output from the module to the host.

b. Pin is ‘wakeable’. Can be used to trigger the module to wake up from sleep mode.See Wakeup Interrupt (Sleep State) for details.

c. Limited Availability for RC7612, RC7612-1.


Rev. 16 March 2025 73 41113440


Interfaces Specifications



The UIM2 interface is included with RC7612 and RC7612-1. (Limited Availability).


**Table 4-8: External UIM2 Interface**












|Pin|Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|55|UIM2_VCC|Output|Supply output|Leave open|
|56|UIM2_DATA|Input/Output|Data connection|Data connection|
|57|UIM2_RESET_N|Output|Reset|Reset|
|58|UIM2_CLK|Output|Clock|Clock|
|65|UIM1_SIMB_DET/GPIO4|Input|Detect UIMB|Detect UIMB|
|65|UIM2_DETb,c/GPIO4|UIM2_DETb,c/GPIO4|Detect UIM2|Detect UIM2|



a. Signal direction with respect to the module. Examples: UIM1_SIMA_DET (pin 64) is an input to the module from the host; UIM1_RESET_N (pin 29) is an output from the module to the host.

b. Pin is ‘wakeable’. Can be used to trigger the module to wake up from sleep mode.See Wakeup Interrupt (Sleep State) for details.
c. Limited Availability for RC7612, RC7612-1 only.

###### **4.7.2 eSIM / UIM2 Interface**


**4.7.2.1 For RC7611, RC7620, RC7630, and RC7630J***


For RC7611, RC7620, RC7630, and RC7630J*, whether an embedded eSIM is provided or not, UIM2 signals are not
available externally.


Selection of active SIM between UIM1 (external SIM) and UIM2 (eSIM) is possible using AT commands AT!UIMS and
AT!CUSTOM=“UIMAUTOSWITCH”. Refer to document [1] AirPrime RC76xx AT Command Reference for more details
regarding these commands.


When UIM2 is deselected, the eSIM component is unpowered.


_*Limited availability_


**4.7.2.2 For RC7612 and RC7612-1**


For RC7612 and RC7612-1 (Limited Availability), UIM2 is available. Selecting an active SIM between UIM1 (external
SIM) and UIM2 (external UIM2) is possible using AT commands. Refer to document [1] AirPrime RC76xx AT
Command Reference for more details regarding these commands.

###### **4.7.3 External SIM Switch Configuration**


_Note: for RC7611, RC7612, RC7620, RC7630, and RC7630J* only_


The UIM1 interface can be used with either a single external SIM, or with two external SIMs, using an external
switch. The external switch is controlled by GPIO6 (pin 46), and GPIO4 is used to detect the second external SIM.


An external PU should be provided on the UIM1_SIMB_DET.


_* Limited availability_


Rev. 16 March 2025 74 41113440


Product Technical Specification


_Figure 4-3: Single External SIM Configuration_


_Note: Figure 4-3 illustrates the recommended implementation of a single external SIM configuration. For a detailed UIM schematic, see_
_Figure 5-8._


_Figure 4-4: Dual External SIM Configuration_


_Note: Figure 4-4 illustrates the recommended implementation of a dual external SIM configuration. For a detailed external SIM schematic,_
_see Figure 5-9._


Supports two external SIM and signal switching using GPIO6, while SIM B is detected by GPIO4. See GPIO6 and
GPIO4 for details.


Rev. 16 March 2025 75 41113440


Interfaces Specifications

##### **4.8 General Purpose Input / Output**


The Semtech RC76xx defines several GPIOs for customer use, as described in Table 4-9. For electrical specifications,
see Table 3-35 and Table 3-36.


_Note: There should not be any voltage applied to the GPIOs when the module is off or resetting.._


**Table 4-9: GPIO Pin Description**















|Pin|Signal Name|Edge Wakeable|Default State|Function|If Unused|
|---|---|---|---|---|---|
|10|GPIO2a|Yes|PDb|General purpose I/O|Leave open|
|40|GPIO7|Yes|Yes|Yes|Yes|
|41|GPIO8|||||
|44|GPIO13|Yes|Yes|Yes|Yes|
|46|GPIO6c|Yes|Yes|Yes|Yes|
|65|GPIO4d|||||
|101|GPIO35|Yes|Yes|Yes|Yes|
|104|GPIO32|||||
|105|GPIO33|||||
|109|GPIO42a|Yes|Yes|Yes|Yes|
|147|GPIO21a|Yes|Yes|Yes|Yes|
|148|GPIO22|Yes|Yes|Yes|Yes|
|149|GPIO23|||||
|150|GPIO24|Yes|Yes|Yes|Yes|
|153|GPIO28e|||||
|154|GPIO29e|||||
|155|GPIO30e|||||
|156|GPIO31e|||||
|159|GPIO25|||||


a. Pin is ‘wakeable’. Can be used to trigger the module to wake up from sleep mode. See Wakeup Interrupt (Sleep State) for details.

b. Internal configuration of all GPIOs—internal input pull-down.

c. See GPIO6.


d. See GPIO4.


e. This pin is available for use when configured using **AT+WIOCFG** .


Rev. 16 March 2025 76 41113440


Product Technical Specification

##### **4.9 GPIO4**


GPIO4 can be used for two different functions as described below.

###### **4.9.1 SIM Detect**


GPIO4 can provide a detect function to the external UIM2 to detect the physical presence of a UIM card in the UIM
holder. The signal needs an external pull-up resistor on it.


The UIM detect signal transitions:

**•**
When a UIM is inserted—high (logic 0 to logic 1)

**•**
When a UIM is removed—low (logic 1 to logic 0)


To use this pin for SIM detect, enable the feature using:


**1.** AT!CUSTOM="EXTUIMSWITCHEN",1


**2.** AT+KSIMSEL=2


**3.** Reboot the module.

###### **4.9.2 General Purpose Input / Output**


To configure this pin as a GPIO:


**1.** Disable external SIM detect feature using AT!UNLOCK=”A710”.


**2.** Use AT+CUSTOM=”UIM2ENABLE”,0.


**3.** Reboot the module.


**4.** Configure GPIO4 using AT+WIOCFG=4,4.


**5.** The default GPIO state is a digital input pull-down function.

##### **4.10 GPIO6**


GPIO6 can be used for three different functions as described below. Refer to the RC76xx AT Command Reference for
AT command details to configure GPIO6.

###### **4.10.1 SIM Switching**


To use this pin for fast SIM switching, enable the feature using AT!CUSTOM="EXTUIMSWITCHEN",1.

###### **4.10.2 General Purpose Input / Output**


To configure this pin as a GPIO:


**1.** Disable external SIM switch feature using AT!CUSTOM="EXTUIMSWITCHEN",0.


**2.** Configure GPIO6 using AT+WIOCFG=6,4.


**3.** Reboot the module.


**4.** The default GPIO state is a digital input with 10 µA pull-down function.


Rev. 16 March 2025 77 41113440


Interfaces Specifications

###### **4.10.3 RESET_OUT_N**


This pin can be used to provide a signal that will hold peripheral devices (such as a USB hub, I [2] C device, etc.) in reset
until the power-up sequence is complete.


To configure this pin as Reset:


**1.** Disable external SIM switch feature using **AT!CUSTOM="EXTUIMSWITCHEN",0** .


**2.** Configure GPIO6 using **AT+WIOCFG=6,0** .


_Note: For details, refer to the Semtech RC76xx AT Command Reference guide._


**3.** Reboot the module.


When the module is:

**•**
In reset or powering up—this pin is held low to put peripheral devices in reset. Once the power-on sequence is
complete, this pin will be turned high to take the peripherals out from reset.

**•**
In PSM—this pin will keep its previous status.


For timing details between RESET_IN_N and RESET_OUT_N, see Reset Signals (RESET_IN_N and RESET_OUT_N).

##### **4.11 Wakeup Interrupt (Sleep State)**


The following pins can be used to wake the device when it is in Sleep state:

**•** GPIO2

**•** GPIO21

**•** GPIO42

**•** UART1_DTR

**•** UIM1_SIMA_DET

**•** UIM1_SIMB_DET


The GPIO pins can be configured as a wakeup source by using the AT+WIOCFG command (see RC76xx AT Command
Reference).


If the device firmware is monitoring these pins while the device is in sleep mode, any transition on these pins will
wake the device.


_Note: These signals wake the device when it is in Sleep state. If the device is in PSM, it is woken by configured wakeup triggers—see_
_Wakeup Events (PSM) for details._


Rev. 16 March 2025 78 41113440


Product Technical Specification

##### **4.12 Wakeup Events (PSM)**


The following signals/sources can be used to wake the device from PSM:


**Table 4-10: PSM Wakeup Signals/Sources**

|Signal Configuration|Signal|
|---|---|
|Configurable|Timer|
|Always enabled|POWER_ON_N|
|Always enable|RESET_IN_N|



_Note: These signals wake the device only when it is in PSM. If the device is in Sleep state, it can be woken using the signals described in_
_Wakeup Interrupt (Sleep State)._


For PSM details, see Table 3-5.

##### **4.13 I [2] C Interface**


The Semtech RC76xx module provides one I [2] C (Inter-Integrated Circuit) dedicated serial port (bus interface) based
on I2C Bus Specification, Version 5.0, October 2012.


The interface uses the pins indicated in Table 4-11.


**Table 4-11: I** **[2]** **C Interface Pins**

|Pin|Signal Name|Direction|Function|If Unused|Reset State|
|---|---|---|---|---|---|
|1|I2C1_CLK|Input/Output|I2C Clock|Leave open|Internal pull-down|
|66|I2C1_DATA|Input/Output|I2C Data|Leave open|Internal pull-down|



This implementation of the I [2] C interface includes the following characteristics:

**•**
Supported voltage—1.8 V

**•**
Standard-mode interface—data transfer rates up to 100 kbit/s

**•**
Master mode operation only—the module always operates as the master

**•** I [2] C signals are implemented internally as open drain outputs (per the I [2] C specification) with 2.2 k Ω pull-up
resistors to VGPIO (see Figure 4-5).


_Note: I_ _[2]_ _C slave address 0x1A is reserved for internal use._


For I [2] C bus details, including I2C bus waveform and timing details, refer to the I2C Bus Specification.


Rev. 16 March 2025 79 41113440


Interfaces Specifications

###### **4.13.1 Application**



|Embedded Module<br>2.2K 2.2K|VGPIO<br>I2C1_CLK|
|---|---|
|Embedded Module<br>2.2K<br>2.2K|I2C1_DATA|


_Figure 4-5: Example of I_ _[2]_ _C Bus Application_

##### **4.14 VGPIO**





The Semtech RC76xx utilizes 1.8V logic, provided via the VGPIO (GPIO voltage output) pin.


**Table 4-12: VGPIO Reference Pin**







|Pin|Signal Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|45|VGPIO|Output|GPIO voltage output|Leave open|


a. Signal direction with respect to the module—VGPIO (pin 45) is an output from the module to the host.


**Table 4-13: VGPIO Electrical Characteristics**

|Parameter|Min|Typ|Max|Unit|Remarks|
|---|---|---|---|---|---|
|Voltage level|1.7|1.8|1.9|V|Applies to active mode and sleep mode|
|Current capability|-|-|50|mA|Power Management support up to 50 mA output|



The VGPIO voltage is available when the module is switched ON, and can be used to:

**•**
Pull up signals such as I/Os

**•**
Supply external digital transistors driving LEDs

**•**
Act as a voltage reference for the ADC interfaces

**•**
Supply external circuitry. Make sure you do not exceed the maximum current capability. Use an external
regulator if a higher consumption is required.


Rev. 16 March 2025 80 41113440


Product Technical Specification


_Note: VGPIO is at a high level (1.8V) when the module is in active or sleep mode. VGPIO is off (high impedance), when the module is in_
_PSM or in off mode. Signal referenced to VGPIO are as follows (signals power group is VGPIO):_

**•** _Internal pull down (FW setting) signals:_
_overshoot voltage: 50mV,_

**•** _No-pull signals:_
_overshoot voltage: 50 mV,_

**•** _Internal pull up (FW setting) signals:_
_Same situation with VGPIO_

##### **4.15 Reset Signals (RESET_IN_N and RESET_OUT_N)**


The Semtech RC76xx provides an interface to allow an external application to reset the module (RESET_IN_N) and
reset the peripheral device (RESET_OUT_N).


_Note: Using RESET_IN_N to reset the module could result in memory corruption if used inappropriately. This signal should only be used if_
_the module has become unresponsive and it is not possible to perform a power cycle. Adding a test point is recommended._


**Table 4-14: RESET Pins**







|Pin|Signal Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|11|RESET_IN_N|Input|External Reset Input|Leave open|
|46 (GPIO6)|RESET_OUT_N|Output|Peripheral devices reset|Leave open|


a. Signal direction with respect to the module—RESET_IN_N (pin 11) is an input to the module from the host.


The RESET_IN_N signal is internally pulled-up with 40k Ω . An open collector or open drain transistor or equivalent
should be used to ground the signal, when necessary, to reset the module. To avoid any damage or abnormal reset
signal, do not design any external pull up circuit on this pin.


To avoid any damage or abnormal reset signal, please do not design any external pull up circuit on this pin.


Rev. 16 March 2025 81 41113440


Interfaces Specifications


_Figure 4-6: RESET_IN_N_


To reset the module, a low level pulse must be applied on the RESET_IN_N pin. This will immediately restart the
module.


The RESET_IN_N signal will reset the registers of the CPU and reset the RAM memory as well, for the next power

on.


**Table 4-15: Reset Timing**







|Symbol|Parameter|Min|Typ|Max|
|---|---|---|---|---|
|Trdet|Duration of RESET_IN_N signal before firmware detects it (debounce<br>timer)|-|32 ms|-|
|Trlen1|Duration RESET_IN_N asserted|42 ms|-|-|
|Trlen2|Duration RESET_OUT_N asserted|420 ms|-|-|
|Trdel1|Delay between minimum Reset duration and internal reset generated|18 ms|-|-|
|Tduration|Duration time from RESET_IN_N falling edge to RESET_OUT_N|50 ms|-|-|


_Figure 4-7: Reset timing when RESET_IN_N < Trdel1_


Rev. 16 March 2025 82 41113440


Product Technical Specification


_Figure 4-8: Reset timing when RESET_IN_N is held low_

##### **4.16 ADC**


The Semtech RC76xx provides two general purpose ADC (Analog to Digital Converter) inputs, as described
Table 4-16 and Table 4-17.


**Table 4-16: ADC Interface Pins**







|Pin|Signal Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|24|ADC1|Input|Analog to Digital Converter|Leave open or Ground|
|25|ADC0|Input|Analog to Digital Converter|Leave open or Ground|


a. Signal direction with respect to the module. Example: ADC1 (pin 24) is an input to the module from the host.


**Table 4-17: ADC Interface Characteristics**

|Parameter|Value|Units|
|---|---|---|
|Full-scale voltage level|0.1–1.7|V|
|Resolution|15|bit|
|Sample rate|2.4|MHz|
|Voltage error|8 (Typ), 16 (Max)|mV|


##### **4.17 Digital Audio**


The Semtech RC76xx provides a 4-wire digital audio interface that can be configured as either PCM (Pulse Code
Modulation) or I [2] S (Inter-IC Sound).


Table 4-18 describes the audio interface signals.


Rev. 16 March 2025 83 41113440


_Note: Audio availability is firmware-dependent._


**Table 4-18: PCM / I** **[2]** **S Interface Signals**



Interfaces Specifications


















|Pin|Signal name|Directiona|Function|Reset State|If Unused|
|---|---|---|---|---|---|
|33|PCM_OUT|Output|PCM Data Out<br>The frame “data out” relies on the<br>selected configuration mode.|Pull Down|Leave open|
|33|I2S_OUT|Output|I2S Data Out<br>The frame “data out” relies on the<br>selected configuration mode.|Pull Down|Pull Down|
|34|PCM_IN|Input|PCM Data In<br>The frame “data in” relies on the selected<br>configuration mode.|Pull Down|Leave open|
|34|I2S_IN|Input|I2S Data In<br>The frame “data in” relies on the selected<br>configuration mode.|Pull Down|Pull Down|
|35|PCM_SYNC|Input/Output in Primary<br>mode|PCM Sync<br>The frame synchronization signal delivers<br>an 16 kHz frequency pulse that<br>synchronizes the frame data in and the<br>frame data out.|Pull Down|Leave open|
|35|I2S_WS|Output|I2S Word Select<br>The word select clock indicates which<br>channel is currently being transmitted<br>(low cycle indicates left audio channel,<br>high cycle indicates right audio channel).|Pull Down|Pull Down|
|36|PCM_CLK|Input/Output in Primary<br>mode|PCM Clock<br>The frame bit clock signal controls data<br>transfer with the audio peripheral.|Pull High|Leave open|
|36|I2S_CLK|Output|I2S Clock<br>The frame bit clock signal controls data<br>transfer with the audio peripheral.|Pull High|Pull High|



a. Signal direction with respect to the module. Examples: PCM_IN (pin 34) is an input to the module from the host; PCM_OUT (pin 33) is
an output from the module to the host.

###### **4.17.1 PCM**


Table 4-19 defines the PCM interface configuration.Data Format


**Table 4-19: PCM Interface Configurations**

|Element|PCM|
|---|---|
|Slot configuration|Slot-based|
|Sync type|Long|



Rev. 16 March 2025 84 41113440


Product Technical Specification


**Table 4-19: PCM Interface Configurations (Continued)**

|Element|PCM|
|---|---|
|Clock (Master)|512 KHz|
|Data formats|16-bit linear|
|Mode|Master|



**4.17.1.1 Data Format**


The PCM data is 16 kHz and 16 bits with the following PDM (Pulse-density modulation) bit format:

**•** PCM_DIN—SDDD DDDD DDDD DDVV

**•** PCM_DOUT—SDDD DDDD DDDD DDVV


Where:

**•**
S—Signed bit

**•** D—Data

**•**
V—Volume padding


**4.17.1.2 Timing**


The following table and drawings illustrate PCM signals timing when operating in PCM mode.


**Table 4-20: PCM Mode Timing** **[a]**

|Parameter|Description|Min|Typ|Max|Units|
|---|---|---|---|---|---|
|t(auxsync)|PCM_SYNC cycle time|-|62.5|-|us|
|t(auxsynca)|PCM_SYNC high time|-|31.2|-|us|
|t(auxsyncd)|PCM_SYNC low time|-|31.2|-|us|
|frequency(SYNC)|Data formats|-|16|-|kHz|
|frequency(CLK)|Clock (Master)|-|515|-|kHz|
|t(auxclk)|PCM_CLK cycle time|-|1.94|-|us|
|t(auxclkh)|PCM_CLK high time|-|975|-|ns|
|t(auxclkl)|PCM_CLK low time|-|975|-|ns|
|t(suauxsync)|PCM_SYNC setup time high before falling edge of PCM_CLK|-|0|-|ns|
|t(hauxsync)|PCM_SYNC hold time after PCM_CLK rising|-|996|-|ns|
|t(suauxdin)|PCM_IN setup time before falling edge of PCM_CLK|-|975|-|ns|
|t(hauxdin)|PCM_IN hold time after falling edge of PCM_CLK|-|994|-|ns|
|t(pauxdout)|Delay from PCM_CLK rising to PCM_OUT valid|-|0|-|ns|



a. Maximum PCM clock rate is 512 kHz.


Rev. 16 March 2025 85 41113440


Interfaces Specifications


**PC Sync Timings**


_Figure 4-9: t(sync)_


_Figure 4-10: t(synch)_


Rev. 16 March 2025 86 41113440


Product Technical Specification


_Figure 4-11: t(syncl)_


Rev. 16 March 2025 87 41113440


Interfaces Specifications


**PCM Codec to Device Timings**


_Figure 4-12: t(clk)_


_Figure 4-13: t(clkh)_


Rev. 16 March 2025 88 41113440


Product Technical Specification


_Figure 4-14: t(clkl)_


_Figure 4-15: t(hauxsync)_


Rev. 16 March 2025 89 41113440


Interfaces Specifications


_Figure 4-16: t(hdin)_


_Figure 4-17: t(sudin)_


Rev. 16 March 2025 90 41113440


Product Technical Specification


_Figure 4-18: t(susync)_


**Device to PCM Codec Timings**


_Figure 4-19: t(clk)_


Rev. 16 March 2025 91 41113440


Interfaces Specifications


_Figure 4-20: t(clkh)_


_Figure 4-21: t(clkl)_


Rev. 16 March 2025 92 41113440


Product Technical Specification


_Figure 4-22: t(hauxsync)_


_Figure 4-23: t(pauxdout)L_


Rev. 16 March 2025 93 41113440


Interfaces Specifications


_Figure 4-24: t(pauxdout)R_


_Figure 4-25: t(susync)_


Rev. 16 March 2025 94 41113440


Product Technical Specification

###### **4.17.2 I [2] S**


The I [2] S interface can be used to transfer serial digital audio to or from an external stereo DAC/ADC and supports the
following features:

**•**
Mode: Master (Slave mode is not supported)

**•**
Sampling rate: 16 kHz

**•**
Bits per frame: 16

**•** Bit clock: 512 kHz


V(hi) = 2.0 V



SCK


SD and WS
(transmitter)


SD and WS
(receiver)


_Figure 4-26: I_ _[2]_ _S Transmitter Timing_


**Table 4-21: I** **[2]** **S Interface Timing** **[a]**



V(lo) = 0.8 V







|Parameter|Description|Min|Typ|Max|Units|
|---|---|---|---|---|---|
||Frequency|-|-|12.288|MHz|
|T|Clock period|81.380|-|-|ns|
|t(hc)|Clock high|0.45×T|-|0.55×T|ns|
|t(lc)|Clock low|0.45×T|-|0.55×T|ns|
|t(sr)|SD and WS input setup time|16.276|-|-|ns|
|t(hr)|SD and WS input hold time|0|-|-|ns|
|t(dtr)|SD and WS output delay|-|-|65.100|ns|
|t(htr)|SD and WS output hold time|0|-|-|ns|


a. Load capacitance is 10–40 pF


Rev. 16 March 2025 95 41113440


Interfaces Specifications


##### **4.18 SPI Bus**

The Semtech RC76xx module provides one 4-wire serial peripheral interfaces (SPI1).


The following features are available on the SPI bus:

**•**
Mode: Master (Slave mode is not supported)

**•**
SPI speed from 960 kbps to 25 Mbps in master mode operation

**•** 4-wire interface

**•**
4 to 32 bits data length

**•**
38 MHz clock frequency


Table 4-22 describes the SPI interface pins.


**Table 4-22: SPI Pin Descriptions**










|Pin|Signal Name|Directiona|Description|Reset State|I/O<br>Type|
|---|---|---|---|---|---|
|51|SPI1_MRDY|Output|SPI Master Ready|Internal Pull-<br>Down|1V8|
|52|SPI1_MISO|Input|SPI Master Input/Slave Output<br>(output from slave)|SPI Master Input/Slave Output<br>(output from slave)|SPI Master Input/Slave Output<br>(output from slave)|
|53|SPI1_CLK|Output|SPI serial clock<br>(output from Master)|SPI serial clock<br>(output from Master)|SPI serial clock<br>(output from Master)|
|54|SPI1_MOSI|Output|SPI Master Output/Slave Input<br>(output from master)|SPI Master Output/Slave Input<br>(output from master)|SPI Master Output/Slave Input<br>(output from master)|



a. Signal direction with respect to module. Examples: SPI1_MISO (pin 52) is an input to the module from the host; SPI1_CLK (pin 53) is
an output from the module to the host.

###### **4.18.1 Configuration**


**Table 4-23: SPI Configuration**

|Operation|Max Speed|SPI-Mode|Duplex|4-wire Type|
|---|---|---|---|---|
|Master|25 Mb/s|0,1,2,3|Full|**•**<br>SCLK (SPI1_CLK)<br>**•**<br>MOSI (SPI1_MOSI)<br>**•**<br>MISO (SPI1_MISO)<br>**•**<br>SS (SPI1_MRDY)|


###### **4.18.2 Waveforms**


The following figure shows waveforms for SPI transfer using a 4-wire configuration.
_Figure 4-27: 4-Wire Configuration SPI Transfer_


**Table 4-24: SPI Master Timing Characteristics (@38 MHz)**

|Parameter|Col2|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|SPI clock frequency|SPI clock frequency|-|-|38|MHz|
|Ta|SPI clock period|20.0|-|-|ns|



Rev. 16 March 2025 96 41113440


Product Technical Specification


**SPI_MRDY**


**SPI_CLK**


**SPI_MOSI**


**SPI_MISO**











Notes:

                                              - SPI_CS_N to SPI_CLK timing is fixed at 1 clock period

                                              - 50% clock duty cycle shown, but not a requirement

                                                  - t(mov) will be negative if output transitions before the clock rising edge


**Table 4-24: SPI Master Timing Characteristics (@38 MHz) (Continued)**

|Parameter|Col2|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|t(ch)|Clock high|9.0|-|-|ns|
|t(cl)|Clock low|9.0|-|-|ns|
|t(mov)|Master output valid|-5.0|-|-5.0|ns|
|t(mis)|Master input setup|5.0|-|-|ns|
|t(mih)|Master input hold|1.0|-|-|ns|



a. Minimum clock period includes 1% jitter of the maximum frequency

###### **4.18.3 Application**









_Figure 4-28: Example of 4-wire SPI Bus Application_

##### **4.19 Clock**


The Semtech RC76xx supports two digital clock interfaces that are connected directly from the PMIC.


Rev. 16 March 2025 97 41113440


Interfaces Specifications


Table 4-25 describes the clock interface pins.


**Table 4-25: Clock Interface Pin Descriptions**

|Pin|Signal Name|I/O|I/O Type|Description|If Unused|
|---|---|---|---|---|---|
|22|SYS_CLK|Output|1.8V|19.2 MHz digital clock output|Leave open|
|23|SLEEP_CLK|Output|1.8V|32.768 kHz digital clock output|Leave open|


##### **4.20 TP1 (Boot Pin)**


The TP1 pin (boot pin) can be used for two primary purposes:

**•**
The pin can be used to force the module to enter boot-loader mode on power-up—Connect the pin to a control
mechanism (for example, a button, switch, or jumper) on the host platform, and use this mechanism to assert
(drive low) the TP1 pin on power-up. The boot loader monitors the TP1 pin and when it detects a low signal,
prevents normal power-up and prepares to download firmware via the DM port.

When the module has restarted and entered boot-loader mode, make sure to de-assert the TP1 pin. When the
firmware download finishes, the module reboots automatically and the de-asserted pin allows the module to
boot normally.

**•**
If not connected to a control mechanism, at minimum the pin should be connected to a test point on the host
platform, for use by Semtech in RMA debugging.


_Note: Firmware downloads also occur using software tools available on_
_[http://source.sierrawireless.com or over the air using an AirVantage server.](http://source.sierrawireless.com)_


**Table 4-26: TP1 Pin Description**

|Pin|Name|Direction|Function|If Unused|
|---|---|---|---|---|
|47|TP1|Input|Device recovery (boot load)|Mandatory test point|


##### **4.21 Temperature Monitoring**


The Semtech RC76xx provides internal temperature monitoring of the module’s baseband thermistor, as detailed
below in Figure 4-29 and Table 4-27.


The temperature state can be queried directly, and unsolicited notifications of temperature state transitions can be
received by using:

**•** **AT!PCTEMP** —Display the current temperature state (normal, hi or low warning, hi or low critical).

**•** **AT+WUSLMSK** —Enable unsolicited notifications for **!PCTEMP**, to be received over the AT port whenever the
state changes.


Rev. 16 March 2025 98 41113440


Product Technical Specification













_Figure 4-29: Temperature Monitoring State Machine_


**Table 4-27: Temperature Monitoring States**







|State|Description|Threshold|Default<br>Temp<br>Value (C)a|Functionality|
|---|---|---|---|---|
|Normal|PA thermistor is between|TEMP_HI_NORM|+100|Class A|
|Normal|PA thermistor is between|TEMP_LO_NORM|-40|Class B|
|High Temperature Warning|PA thermistor has exceeded|TEMP_HI_WARN|+105|Class B|
|High Temperature Critical|PA thermistor has exceeded|TEMP_HI_CRIT|+110|Low Power Mode|
|Low Temperature Critical|PA thermistor has descended past|TEMP_LO_CRIT|-45|Low Power Mode|


a. Junction (PA thermistor) temperature


To restore full operation, the PA thermistor’s temperature reading must be within the normal or high temperature
warning state thresholds.


Rev. 16 March 2025 99 41113440


Interfaces Specifications

##### **4.22 Test Pins**


Semtech requires test points on the customer application for Semtech RMA and debug service.


**Table 4-28: Mandatory Test Pins**

|Pin|Name|Function|If Unused|
|---|---|---|---|
|236|J1|Test point|Mandatory test point|
|237|J2|Test point|Mandatory test point|
|238|J3|Test point|Mandatory test point|
|239|J4|Test point|Mandatory test point|
|240|J5|Test point|Mandatory test point|
|241|J6|Test point|Mandatory test point|
|242|J7|Test point|Mandatory test point|
|243|J8|Test point|Mandatory test point|
|244|J9|Test point|Mandatory test point|



**Table 4-29: Recommended Test Pins**







|Pin|Name|Function|If Unused|
|---|---|---|---|
|3|UART1_RTS|UART1|Strongly recommended (almost mandatory) for debug purposes|
|4|UART1_CTS|UART1|Strongly recommended (almost mandatory) for debug purposes|
|5|UART1_TX|UART1|Strongly recommended (almost mandatory) for debug purposes|
|6|UART1_RX|UART1|Strongly recommended (almost mandatory) for debug purposes|
|11|RESET_IN_N|Control signal|Adding a test point is recommended|
|12|USB_D-|USB|Strongly recommended (almost mandatory) for debug purposes|
|13|USB_D+|USB|Strongly recommended (almost mandatory) for debug purposes|
|16|USB_VBUS|USB|Strongly recommended (almost mandatory) for debug purposes|
|26|UIM1_VCC|UIM1|Recommended|
|27|UIM1_CLK|UIM1|Recommended|
|28|UIM1_DATA|UIM1|Recommended|
|29|UIM1_RESET_N|UIM1|Recommended|
|45|VGPIO|Voltage reference|Strongly recommended (almost mandatory) for debug purposes|
|46|Ext_SIM_switchg / GPIO6<br>/ RESET_OUT_N|UIM1|Recommended|
|47|TP1 (Boot pin)|Control Signal|Should be connected to a test point|


Rev. 16 March 2025 100 41113440


Product Technical Specification


**Table 4-29: Recommended Test Pins (Continued)**

|Pin|Name|Function|If Unused|
|---|---|---|---|
|59|POWER_ON_N|Control Signal|Strongly recommended (almost mandatory) for debug purposes|
|64|UIM1_SIMA_DET|UIM1|Recommended|
|65|UIM1_SIMB_DET / GPIO4|UIM1|Recommended|
|96|UART2_TX|UART2|Recommended|
|97|UART2_RX|UART2|Recommended|
|98|UART2_RTS|UART2|Recommended|
|99|UART2_CTS|UART2|Recommended|
|151|W_DISABLE_N|Control Signal|Recommended|


##### **4.23 Antenna Control**


The Semtech RC76xx provides four output signals that can be used for host designs that incorporate tunable
antennas.


_Note:_

**•** _It is the responsibility of developers of host designs to evaluate the performance of tunable antennas that use these signals for_
_neighbor cell measurements, Inter-RAT handovers, etc. Semtech does not guarantee ANT_CNTLx signal timing._

**•** _Antenna control signals support is optional._

**•** _These pins can be configured for use as GPIOs using_ **+WIOCFG** _._


**Table 4-30: Antenna Control Signals**











|Pin|Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|153|ANT_CNTL0|Output|Customer-defined external switch<br>control for tunable antennas|Leave open|
|154|ANT_CNTL1|Output||Leave open|
|155|ANT_CNTL2|Output||Leave open|
|156|ANT_CNTL3|Output||Leave open|


a. Signal direction with respect to module. Examples: ANT_CNTL0 (pin 153) is an output from the module to the host.


To tune the antenna:


**1.** Enable band selection, which is required to tune the antennas for specific bands:
**AT!CUSTOM=”BANDSELEN”,1**

Note that this setting is persistent unless disabled by issuing
**AT!CUSTOM=”BANDSELEN”,0** .


**2.** Drive the antenna control signals high or low, as required, for a specific band: **AT!ANTSEL=<band>,**
**<gpio1>, <gpio2>, <gpio3>[, <gpio4>]**

See RC76xx AT Command Reference for details.

Note that <gpio1>–<gpio4> correspond to ANT_CTRL0–ANTCTRL3.


Rev. 16 March 2025 101 41113440


Interfaces Specifications

##### **4.24 Indication Interfaces**


The Semtech RC76xx provides several indication interfaces that deliver notifications when specific events occur.
These interfaces include:

**•**
Tx Activity Indicator (TX_ON)

**•** WWAN_LED_N

**•** WAKE_ON_WWAN

**•**
Ring Indicator

**•** SAFE_PWR_REMOVE

###### **4.24.1 Tx Activity Indicator (TX_ON)**


The Semtech RC76xx provides a digital output signal to indicate the occurrence of Tx activity.


**Table 4-31: Tx Activity Indicator States**







|Pin|Signal Name|Directiona|I/O Type|Module State|Signal State|
|---|---|---|---|---|---|
|60|TX_ON|Output|1.8V|During Tx activity|High|
|60|TX_ON|Output|1.8V|No Tx|Low|


a. Signal direction with respect to module—TX_ON (pin 60) is an output from the module to the host.


**Table 4-32: Tx Activity Indicator Characteristics**








|Parameter|Min.|Max.|
|---|---|---|
|Tadvance|64.8 ms (LTE)<br>20 ms (3G) / 150 us (2G)|-|
|Tdelay|-|33.8 ms(LTE)<br>800 ms (3G) / 50 us (2G)|



TX_ON


VBAT_RF







|N|Col2|
|---|---|
|||
|_RF<br>T advance|_RF<br>T advance|
|_RF<br>T advance||


_Figure 4-30: TX_ON State During Transmission_


Rev. 16 March 2025 102 41113440


Product Technical Specification

###### **4.24.2 WWAN_LED_N**


The Semtech RC76xx provides a LED control output signal pad.


**Table 4-33: LED Interface Pin**



|Pin|Signal Name|Direction|Voltage / Current|Function|If Unused|
|---|---|---|---|---|---|
|106|WWAN_LED_N|Output|**•**<br>Voltage (max)=Typical output range: 0.3 to<br>VBAT_BB<br>**•**<br>Maximum current sink capability=40 mA|LED driver control|Leave open|

###### **4.24.3 WAKE_ON_WWAN**

_Note: Host support for WAKE_ON_WWAN signal is optional._





The Semtech RC76xx drives WAKE_ON_WWAN high to wake the host when it receives specific events such as
incoming SMS or incoming data packets. This pin can be configured by using **AT!CUSTOM** command with the option:
**WAKEHOSTEN** . For details, please see the RC76xx AT Command Reference Guide.


See Figure 4-31 for a recommended implementation.

|Control|WAKE_ON_WWAN|
|---|---|
|Control||



Embedded Module


_Figure 4-31: Recommended WAKE_ON_WWAN Connection_


_Note: WAKE_ON_WAN for incoming data packets is based on the host driver QMI event registration (using_
_QMI_WDS_SET_EVENT_REPORT). For Linux Host, the WDS event reporting indicator must be enabled by the Linux SDK application (for_
_example, MBPL SDK application). This will ensure that this pin is triggered._

###### **4.24.4 Ring Indicator**


The ring indicator (UART1_RI) may be used to notify an external application of several events such as an incoming
call, timer expiration, or incoming SMS. The Semtech RC76xx pulses the signal low when an event occurs. It can be
used independently from the UART1 interface.


**Table 4-34: Ring Duration Time**

|Parameter|Time|
|---|---|
|Pulse width|50 ms|



Rev. 16 March 2025 103 41113440


Interfaces Specifications


_Note: The pulse width duration is based on the current FW setting and can be configured using the AT command: AT+WRID._


_Figure 4-32: UART1_RI_


**Table 4-35: UART1_RI Pin**







|Pin|Name|Directiona|Function|If unused|
|---|---|---|---|---|
|2|UART1_RI|Output|**•**<br>Ring Indicator<br>**•**<br>Signal incoming calls (voice and data), SMS,<br>etc.|Leave open|


a. Signal direction with respect to the module—UART1_RI (pin 2) is an output from the module to the host.


**Important:** Do not install an external pull-up on this pin, otherwise the module will not boot.


_Note:_

**•** _Pin status is in internal pull-down when the module boots or resets._

**•** _RI supports events which toggle the RI signal. This pin can be configured using the AT+WWAKESET AT command._

###### **4.24.5 SAFE_PWR_REMOVE**





The SAFE_PWR_REMOVE signal is provided by Semtech RC76xx to indicate to the host device that the main power
supply (VBATT) can be safely turned off after a positive pulse.


**Table 4-36: SAFE_PWR_REMOVE Duration Time**

|Parameter|Time|
|---|---|
|Pulse width|13.26 ms|
|Duration time from the falling edge of SAFE_PWR_REMOVE signal to VGPIO off|7.8 ms|



_Note:_

**•** _All host interfaces connected to the module must be disabled (high Z or pull-down) before turning off VBATT. This prevents leakages_
_and bad power on sequences._

**•** _Consider the VGPIO discharge time (depends on the load on the host equipment) before switching off VBATT._


Rev. 16 March 2025 104 41113440


Product Technical Specification


_Figure 4-33: SAFE_PWR_REMOVE_

##### **4.25 DR_SYNC**


The Semtech RC76xx provides DR_SYNC, an output used for GPS dead reckoning synchronization. The module
pulses the DR_SYNC signal once every integer GPS second. While position fixes are occurring, the DR_SYNC pulse is
aligned precisely with the GPS time. When a position fix cannot be made (for example, when a vehicle has entered a
tunnel), the module continues to pulse the DR_SYNC signal every second while the level of uncertainty of the GPS
time is low. When the uncertainty level is high, the module stops pulsing the signal.


**Table 4-37: DR_SYNC Pin Details**







|Pin|Signal Name|Directiona|Function|If Unused|
|---|---|---|---|---|
|42|DR_SYNC|Output|GPS dead reckoning sync signal|Leave open|


a. Signal direction with respect to the module—DR_SYNC (pin 42) is an output from the module to the host.


_Pin status is in internal pull-down when the module boots or resets._

##### **4.26 W_DISABLE_N — Wireless Disable**


_Note: Host support for wireless disable signals is optional._


The host device uses W_DISABLE_N (pin 151) to enable / disable the WWAN or radio modem. When disabled, the
modem cannot transmit or receive information. Letting this signal float high allows the module to operate normally.
The pin has an internal pull-up resistor. See Figure 4-34 for a recommended implementation.


When integrating with your host device, keep the following in mind:

**•**
The signal is an input to the module and should be driven LOW only for its active state (controlling the power
state); otherwise it should be floating (or high impedance). It should never be driven to a logic high level. The
module has an internal pull-up resistor to an internal 1.8V rail, so if the signal is floating or (high impedance),
then the radio is on.


Rev. 16 March 2025 105 41113440


Interfaces Specifications


**•**
If the host never needs to assert this power state control to the module, leave this signal unconnected from the
host interface.







Host


_Figure 4-34: Recommended Wireless Disable Connection_





Rev. 16 March 2025 106 41113440


## **5**


### **5: Routing Constraints and Recommendations**

This section describes general routing constraints and recommendations for the Semtech RC76xx module.


_Note: This is a non-exhaustive list of suggested design guidelines. The developer is responsible for deciding whether to implement these_
_guidelines._

##### **5.1 General Rules and Recommendations**


Clock and other high-frequency digital signals (e.g. serial buses) should be routed as far as possible from the
module’s analog signals.


If the application design makes it possible, all analog signals should be separated from digital signals by a ground
trace on the PCB.


_Note: Avoid routing any signals under the module on the application board._

##### **5.2 Power Supply**


When designing the power supply, make sure that VBAT_BB/VBAT_RF meet the requirements listed in Power
Supply Ratings.


Careful attention should be paid to the following:

**•**
Power supply noise—PFM systems should be avoided; Low ripple, linear regulation or PWM converters are
preferred for low noise.

**•**
High switching load capability to deliver high current peaks in a short time (for TDMA frames—RC7620 and
RC7620-1 only). For details about the input capacitor, see Power Supply

**•**
Power supply and power tracks design must support peak currents with an acceptable voltage drop that
guarantees the minimum required VBATT value.

**•** Voltage applied on VBATT signal pads must never exceed the voltage range defined in Power Supply Ratings,
otherwise the module’s power amplifier and GPS chipset may be severely damaged.

**•**
A weakly-designed (not robust) power supply could affect EMC performance, the radiated spurious emission
(RSE), and the phase error and frequency error.

##### **5.3 Antenna**


Semtech strongly recommends working with an antenna manufacturer either to develop an antenna adapted to the
application, or to adapt an existing solution to the application. Refer to Table 3-30


For information on routing constraints for the RF circuit, see RF Routing Recommendations.


Rev. 16 March 2025 107 41113440


Routing Constraints and Recommendations

###### **5.3.1 OTA Considerations when Developing Products with an Integrated** **Antenna**


Developing a product with an integrated antenna is challenging considering RF design and performances; difficulty
increases with the level of integration. Smaller product size implies:

**•**
The smaller the antenna, the more challenging to reach the expected antenna efficiency.

**•**
Large RF TX signal level radiated by the antenna can be captured by nonlinear devices and create, by rectification, a high level of unwanted harmonics.

**•**
As much as the distance between the antenna and electronic devices (including the module and other application related hardware) decreases, coupling to clocks and DC/DC switchers harmonics and wide band noise
sources generated by high speed digital signals increases. Such a coupling may create receiver desensitization
from the resulting noise generated at the receiver frequency bands.


It is essential to take into account appropriate design rules when developing new products and to evaluate OTA
performances at an early stage of product integration:

**•**
TRP (Total Radiated Power): To verify the antenna efficiency at TX frequency bands and compliance to spurious
emission requirements.

**•**
TIS (Total Isotropic Sensitivity): To verify the antenna efficiency at RX frequency bands and evaluate the
presence of noise generated into supported frequency bands subject to cause receiver desensitization.

##### **5.4 PCB Layout Recommendations**

###### **5.4.1 General Design Rules**


**•**
Application board should be designed in such a way that provides a plain GND connection on the whole surface
located under the module area. A matrix of high density vias should be implemented to connect the top layer (in
contact to the module LGA ground pads) to other GND layers. Such implementation aims to reduce noise interference, spurious radiation and improve heat dissipation spreading heat through the PCB surface and layers.

**•**
To reduce coupling between antenna and other signals and improve EMC, the top and bottom layers of the PCB
should be covered by solid GND plan as much as possible.

**•**
Good PCB grounding is essential; use ground planes that are as wide as possible and link the different GND
planes from each layers using regularly spaced via holes. The maximum recommended distance between two
consecutive vias.


Rev. 16 March 2025 108 41113440


Product Technical Specification


**•**
Particularly, via should be present all around the PCB edge to block any unwanted EMI emitted from the internal
layers. Usually power planes are not recommended. We recommend a distributed power supply instead.


**•**
Sensitive signals should be shielded by routing them into inner layers (to prevent them from radiating) and
sensitive components can be shielded. The top and bottom ground plans connected together with vias ensures
all sensitive traces are shielded well. This significantly reduces coupling between antenna and other signals and
improves EMI and EMC performances.

**•**
When it is not possible to route a signal trace into inner layers, top and bottom layers can be used for short
distance connections (i.e. connections between adjacent pads).

**•**
It is good practice during the design phase to anticipate and reserve area for shield cans.

**•**
The module’s power supply needs decoupling capacitors to filter out noise to prevent it from reaching the
module. It could cause instabilities in the RF output in the transmitter, resulting in undesired interference and
spurious radiations. In the receiver, it increases packet error and reduces sensitivity.

**•**
Place a decoupling capacitor (10–33pF is recommended) as close to the power supply pin of the module as
possible.

**•**
Use as many vias as possible to build a ground fence around the RF stripline and microstrip line to isolate it from
other signals.

**•**
In some specific cases, like impedance controlled lines and RF connection pads and antenna pads, sufficient
keep out distance between RF signals and GND should be implemented to prevent impedance mismatch from
parasitic capacitance load.


Rev. 16 March 2025 109 41113440


Routing Constraints and Recommendations

###### **5.4.2 Specific Design Rules to Support TRP Performances**


**•**
Prevent neighboring components from being interfered by TX radiated RF energy to prevent them from generating harmonics through non-linear behavior such as saturation or rectification. The mandatory maximum
radiated harmonics level for R&TTE/PTCRB certification is below -30dBm and can be very easily failed with
inappropriate design.


**•**
When possible, add 10-47pF in parallel of each fast rectifier diode to prevent generating harmonics (due to the
TX signal detection).


**•**
With an antenna located close to circuitry using active devices, shielding may be needed to reach enough
isolation.


Rev. 16 March 2025 110 41113440


Product Technical Specification

###### **5.4.3 Specific Design Rules to Support TIS Performance**


**•**
High speed digital signal (such as DC/DC converters, system clock, CPU and Memory bus, USB and other high
speed interfaces) should be routed on inner layers and located as far as possible from RF signals and antenna.

**•**
Good practice for interferences prevention is to add decoupling capacitors (10–33pF recommended) every
10mm on all top and bottom power lines longer than 10mm.

**•**
With an antenna located close to circuitry using active devices or noisy signals, shielding may be needed to
reach enough isolation.

##### **5.5 PCB Specifications for the Application Board**


Digital and sensitive signals (such as audio, UIM, clocks, high speed interface) should be routed on the inner layers
and separated from each other by GND tracks regularly punctured with vias (or microvias). Routing sensitive signals
close to noisy signals could result in noise being coupled.


The clocks (SYS_CLK and SLEEP_CLK) should use a 50 Ohm controlled impedance trace and the length must be as
short as possible.

##### **5.6 Recommended PCB Land Pattern**


Refer to document RC76xx Customer Process Guidelines, available at
[http://source.sierrawireless.com.](http://source.sierrawireless.com)

##### **5.7 Routing Constraints**

###### **5.7.1 Power Supply**


_Note: The recommended output current capability for the power supply on Table 3-3 on page 28 includes margin._


If the following design recommendations are not followed, phase error (peak) and power loss could occur.

**•**
The trace widths of the power supplies (VBAT_BB and VBAT_RF) should be as wide as possible to minimize
voltage drops and reduce electromagnetic interference risks.


Rev. 16 March 2025 111 41113440


Routing Constraints and Recommendations


_Figure 5-1: Power Supply Routing Example_


_Note: Figure 5-1 shows separate traces for VBAT_BB and VBAT_RF. If VBAT_BB and VBAT_RF share a single power supply, these traces_

_should be connected._


_Note: For optimal decoupling, place the capacitors on the underside of the board, directly under the pins._


**•** Input capacitors (2×47 μ F) are required close to the module.

**•**
Attention should be paid to the ground trace or the ground plane on the application board for the power supply
that supplies the module. The ground trace or ground plane, as well as the VBATT trace, must be able to support
current peaks.

**•**
If the ground trace between the module and the power supply is a copper plane, make sure it is a solid plane.

**•** Design routing to make sure total line impedance does not exceed 10 m Ω @ 217 Hz.


_Note: 2G GSM communications use intermittent burst signals with a period of 4.615 ms (217 Hz)_


**5.7.1.1 Ground Plane Connection**


The Semtech RC76xx requires a solid, central ground plane (with solder mask defined pads) located directly under
the module. This will:

**•**
Ensure high current signal returns

**•**
Provide heat dissipation under higher operating temperatures


The ground plane should be connected (with vias) to the reference ground layer of the application board.


Do not use a separate GND for the antennas. Connections to GND from the Semtech RC76xx module should be
flooded plane using thermal reliefs to ensure reliable solder joints.


Rev. 16 March 2025 112 41113440


Product Technical Specification

###### **5.7.2 UIM Interface**


**•**
Tracks between the module and the UIM socket should be as short as possible and routed on inner layers.
Maximum recommended length is 10 cm.

**•**
The ESD must be placed near the UIM holder

**•**
ESD protection is mandatory on the UIM lines unless:

**·**
An external eSIM is being used, or

**·**
There is no physical access to the UIM.

**•**
The decoupling capacitor(s) should be placed as close as possible to the UIM card connector for the UIM1_VCC
signal.

###### **5.7.3 RF Routing Recommendations**


For radiofrequency signals, the following recommendations shall be taken into consideration on PCB layout:

**•**
For each antenna interface (RF_MAIN, RF_DIV, RF_GNSS), the related GND pads should be considered as an
integrated part of the radio input/output (refer to Figure 5-4 example).Reference ground of the RF traces shall
be a solid integrated plane.

**•**
The use of a CBCPW (Conductor-Backed Coplanar Waveguide) is strongly recommended for lower insertion loss,
better impedance matching stability and no additional loss due to the use of vias required by the Stripline
structure.


The CBCPW must be surrounded by GND planes evenly punched by GND vias:


_Figure 5-2: Conductor-Backed Coplanar Waveguide (CBCPW) design_


**•**
The distance between two adjacent vias should be ≤ the quarter wavelength / 10 of the highest frequency
carrier.

**•**
The CBCPW design for RF trace must be used for better isolation, and the coplanar clearance (G, below) from the
trace to the ground should be at least the trace width (W) and at least twice the height (H). This reduces the
parasitic capacitance, which potentially alters the trace impedance and increases the losses.


Rev. 16 March 2025 113 41113440


Routing Constraints and Recommendations


_Figure 5-3: Coplanar Clearance example_


_Note: The figure above shows several internal ground layers cut out, which may not be necessary for every application._


**•**
As far as possible and in order to avoid impedance breaks, choose a track width at least equal size of the
component pad connected to it.


_Figure 5-4: Track width and component pad_


**•**
Because a part of the RF track is routed under the module, the RF track width shall be slightly reduced before
going under the module for considering the metallic mass of the module. Thus, under the module, the structure
of the RF line becomes a stripline.

**•**
Anticipate a copper keep-out under the RF pads to reduce stray capacitance losses.


Rev. 16 March 2025 114 41113440


Product Technical Specification


_Figure 5-5: RF Tracks Routing_


Rev. 16 March 2025 115 41113440


Routing Constraints and Recommendations


**•**
All RF traces must be well isolated to other “noise” circuits such as USB, PCIe, external XO, DC power supply, etc.

**•**
Edge mount RF connectors are strongly suggested for better impedance matching.


_Figure 5-6: RF Connector_


**•**
Different layers routing design with vias transition is not recommended as they will introduce more RF losses.

**•** Do not use right angle RF tracks. A 90 [o ] mitered bend is recommended:


_Figure 5-7: RF tracks - Example of optimally 90_ _[o]_ _mitered bend routing_

###### **5.7.4 USB Interface**


When the USB interface is externally accessible, ESD protection is required on the USB_VBUS, USB_D+, and
USB_D- signals.


HS-USB guidelines:

**•**
Up to 480 Mbps data rate.

**•** 90 Ω differential, ± 10% trace impedance.

**•**
Differential data pair matching < 3.8 mm (150 mils).

**•**
Other comments and guidelines:

**·**
External components should be located near the USB connector.

**·**
Relatively fast edge rates, so they should be routed away from sensitive circuits and signals (RF, system
clock).

**·**
VBUS trace width must be sized depending on the length of VBUS and the expected current.

**·**
Loading on the USB DP/DM lines could cause USB receiver sensitivity issues. Perform USB electrical tests
(eye diagram and receiver sensitivity) to ensure proper USB functionality.

**·** It is not recommended to install series switches on the USB lines.

**·**
Trace width and trace spacing for DP and DM based on impedance calculator. Avoid discontinuity. The trace
width should be equal from source to destination. Keep impedance constant.

**·**
Avoid having multiple vias. Vias are a source of discontinuity, which can cause signal reflection.

**·**
Avoid crossing different power plane if possible for USB signals. This caused an unpredictable return path
current and cause a signal quality issue.


Rev. 16 March 2025 116 41113440


Product Technical Specification


**·**
Avoid stubs. A common routing mistake is to create a stub by connecting a component on the DP or DM
traces.

**·**
Adding test points on USB traces must comply with radio frequency signal routing rules to avoid degradation
of USB signal quality.

**·**
The USB power supplies should have wider traces and not narrow traces, which cause IR drop. This affects the
jitter performance of the USB signal.

##### **5.8 Thermal Considerations**


When transmitting, the Semtech RC76xx can generate significant amounts of heat (due to the internal Power
Amplifier) that must be dissipated in the host device for safety and performance reasons.


The amount of thermal dissipation required depends on the following factors:

**•**
Supply voltage—Maximum power dissipation for these modules can be up to 3 W at voltage supply limits.

**•**
Usage—Typical power dissipation values depend on the location within the host, amount of data transferred,
etc.


To enhance heat dissipation:

**•** Maximize airflow over / around the module

**•**
Locate the module away from other components that generate heat

**•**
Ensure the module is connected to a solid ground plane

##### **5.9 EMC and ESD Recommendations**


EMC tests must be performed on the application as soon as possible to detect any potential problems.


When designing, special attention should be paid to:

**•**
Possible spurious emissions radiated by the application to the RF receiver in the receiver band

**•**
ESD protection—Typically, ESD protection is mandatory for externally accessible signals, including:

**·**
VBAT_RF/VBAT_BB

**·**
UIM (if accessible from outside)

**·** Serial link

**·** USB

**·** Antennas

**•**
Length of the UIM interface lines (preferably <10 cm)

**•**
Ground plane: Semtech recommends a common ground plane for analog/digital/RF grounds


_Note: The Semtech RC76xx does not include any protection against over-voltage._


The host device must provide adequate ESD protection on digital circuits and antenna ports as detailed in the
following table.


Rev. 16 March 2025 117 41113440


Routing Constraints and Recommendations


_Note: The level of protection required depends on your application._


**Table 5-1: ESD Specifications** **[a]**







|Category|Connection|Specification|
|---|---|---|
|Operational|**•**<br>RF ports<br>**•**<br>UIM connector<br>**•**<br>USB connector<br>**•**<br>UART connector|IEC-61000-4-2 - Level (Electrostatic Discharge Immunity Test)<br>**•**<br>± 6kV Contact<br>**•**<br>± 8kV Air|
|Non-operational|Host connector interface|Unless otherwise specified:<br>**•**<br>JESD22-A114 ± 1kV Human Body Model<br>**•**<br>JESD22-A115 ± 100V Machine Model<br>**•**<br>JESD22-C101C ± 500V Charged Device Model|


a. ESD protection is highly recommended at the point where the UIM contacts are exposed, and for any other signals that would be subjected to ESD by the user.

##### **5.10 Mechanical Integration**


Attention should be paid to:

**•**
Antenna cable integration (bending, length, position, etc)

**•**
Pads of the Semtech RC76xx to be soldered to the ground plane

**•**
Ensuring proper board layout

**•**
Providing sufficient space around the module for heat dissipation

##### **5.11 Signal Reference Schematics**

###### **5.11.1 UIM Holder**


Figure 5-8 illustrates the recommended implementation of a UIM holder.


Rev. 16 March 2025 118 41113440


Product Technical Specification














|UIM1_VCC<br>UIM1_RESET_N<br>UIM1_CLK<br>RC76xx<br>GND<br>UIM1_DATA<br>UIM1_SIMA_DET|Col2|Col3|Col4|Col5|Col6|Col7|C1<br>C2<br>C3<br>UIM Holder<br>C5<br>C7<br>SW_1<br>SW_2|
|---|---|---|---|---|---|---|---|
|<br>**RC76xx**<br>**UIM1_VCC**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**GND**<br>**UIM1_SIMA_DET**<br>**UIM1_RESET_N**|||**100nF** <br>**1nF**<br>**4.7µF**<br>**DNI**|**100nF** <br>**1nF**<br>**4.7µF**<br>**DNI**|**ESD**|**ESD**|**ESD**|
|<br>**RC76xx**<br>**UIM1_VCC**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**GND**<br>**UIM1_SIMA_DET**<br>**UIM1_RESET_N**|||**RCLK **|||||
|<br>**RC76xx**<br>**UIM1_VCC**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**GND**<br>**UIM1_SIMA_DET**<br>**UIM1_RESET_N**|**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**|**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**|**ESD suppressor**<br>**diode array**<br> <br>(e.g. DALC208SC6)<br> <br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**|**ESD suppressor**<br>**diode array**<br> <br>(e.g. DALC208SC6)<br> <br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**|**NC**|**NC**|**NC**|
|<br>**RC76xx**<br>**UIM1_VCC**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**GND**<br>**UIM1_SIMA_DET**<br>**UIM1_RESET_N**||||||||
|<br>**RC76xx**<br>**UIM1_VCC**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**GND**<br>**UIM1_SIMA_DET**<br>**UIM1_RESET_N**||||||**ESD**|**SW_2**|
|<br>**RC76xx**<br>**UIM1_VCC**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**GND**<br>**UIM1_SIMA_DET**<br>**UIM1_RESET_N**||||||||



_Figure 5-8: Recommended Single UIM Holder Implementation_


The UIM1 Detect signal (UIM1_SIMA_DET) is used to detect the physical presence of a UIM card in the UIM holder.
The signal has a 470 k Ω pull-up internal to the module. It should be set to GND when a UIM is not present. The UIM
Detect signal transitions:

**•**
When a UIM is inserted—high (logic 0 to logic 1)

**•**
When a UIM is removed—low (logic 1 to logic 0)


The capacitor and the two resistors, RCLK and RDATA, should be added as placeholders to compensate for potential
layout issues. UIM1_DATA trace should be routed away from the UIM1_CLK trace. Keep the distance between the
module and the UIM holder as short as possible.


All signals near the UIM holder must be ESD-protected.


An ESD device specifically designed for UIM cards is recommended for the UIM1 VCC, RESET_N, CLK, and DATA
signals (for example, STMicroelectronics DALC208SC6). For UIM1_SIMA_DET a low leakage ESD suppressor should
be selected.


This schematic also applies to the external UIM2 of RC7612 and RC7612-1 (Limited Availability).


Rev. 16 March 2025 119 41113440


**Analog switch**

(e.g. FSA2567MPX)



Routing Constraints and Recommendations








|Col1|Col2|Col3|Col4|Col5|C1<br>C2<br>C3<br>UIM Holder 1<br>C5<br>C7<br>SW_1<br>SW_2|
|---|---|---|---|---|---|
||**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**|**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**|**ESD**|**ESD**|**ESD**|
||**RCLK **|||||
||**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**|**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**|**NC**|**NC**|**NC**|
|||||||
|||||**ESD**|**SW_2**|
















|UIM1_VCC C1<br>4.7µF 100nF 1nF ESD<br>DNI<br>UIM1_RESET_N C2<br>RCLK<br>UIM1_CLK C3<br>0<br>VGPIO RDATA<br>15k<br>DNI ESD suppressor<br>RC76xx diode array UIM Holder 1<br>R 2D 9.E 4T k  (e.g. DALC208SC6)<br>DNI NC<br>GND C5<br>UIM1_DATA C7<br>SW_1<br>UIM1_SIMA D_ET<br>Ext _SIM_Switch ESD<br>(GPIO6) SW_2<br>UIM1_SIMB_DET<br>(GPIO4)<br>C1<br>4.7µF 100nF 1nF ESD<br>DNI<br>C2<br>RCLK<br>C3<br>0<br>VGPIO RDATA<br>15k<br>DNI ESD suppressor<br>diode array UIM Holder 2<br>R 2D 9.E 4T k  (e.g. DALC208SC6)<br>DNI NC<br>C5<br>C7<br>SW_1<br>ESD<br>SW_2|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**UIM Holder  2**<br>**C1**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**|
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**|**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**|**ESD**|**ESD**|**ESD**|
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RCLK **|||||
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**|**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**|**NC**|**NC**|**NC**|
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|||||||
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|||||**ESD**|**SW_2**|
|**RC76xx**<br>**UIM1_VCC**<br>**UIM1_RESET_N**<br>**UIM1_CLK**<br>**UIM1_DATA**<br>**UIM Holder  1**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**UIM1_SIMA _DET**<br>**GND**<br>**RCLK **<br>**0** <br>**NC**<br>**RDATA **<br>**15k** <br>**DNI**<br>**Ext _SIM_Switch**<br>**(GPIO6)**<br>**UIM Holder  2**<br>**C1**<br>**100n**~~**F **~~<br>**1nF**<br>**4.7µF**<br>**DNI**<br>**ESD**<br>**ESD suppressor**<br>**diode array**<br>(e.g. DALC208SC6)<br> <br>**ESD**<br>**C2**<br>**C3**<br>**C5**<br>**C7**<br>**SW_1**<br>**SW_2**<br>**RCLK **<br>**0** <br>**NC**<br>**UIM1_SIMB_DET**<br>**(GPIO4)**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**RDATA **<br>**15k** <br>**DNI**<br>**RDET **<br>**29.4k** <br>**DNI**<br>**VGPIO**<br>**VGPIO**|||||||



_Figure 5-9: External SIM schematic for RC7611, RC7620, RC7630, and RC7630J*_

_* Limited availability_

###### **5.11.2 USB**


_Figure 5-10: USB Inteface_


Rev. 16 March 2025 120 41113440


## **6**


### **6: Software and Tools**

##### **6.1 Support Tools**

The Semtech RC76xx is compatible with Semtech’ SwiLogPlus trace tool that allows users to send error logs to
Semtech.

##### **6.2 SED (Smart Error Detection)**


The Semtech RC76xx uses a form of SED to track premature module resets. In such cases, the module automatically
forces a pause in boot-and-hold mode at power-on to accept an expected firmware download to resolve the
problem.


**1.** Module tracks consecutive resets within 30 seconds of power-on.


**2.** After a sixth consecutive reset, the module waits in boot-and-hold mode (up to 30 seconds) for a firmware
download to resolve the power-cycle problem.


A RAM dump tool that can be used to help isolate the cause of premature resets is available from Semtech. Contact
your Semtech account representative for assistance.

##### **6.3 Firmware Upgrade**


Firmware upgrades are downloaded to the embedded module over the USB interface or over the air via Semtech’
AVMS (AirVantage Management System). Contact your Semtech account representative for assistance.

##### **6.4 Operating System Upgrade**


The Semtech RC76xx module’s operating system is stored in flash memory and can be easily upgraded.


**Tip:** _To follow regular changes in the 3GPP standard and to offer a state-of-the-art operating system, Semtech recommends that the_
_application designed around an embedded module (or embedded module based product) should allow easy operating system upgrades on_
_the embedded module via the recommended firmware download protocol. Therefore, the application shall either allow a direct access to_
_the embedded module USB interface through an external connector or implement any mechanism allowing the embedded module_
_operating system to be downloaded._


Rev. 16 March 2025 121 41113440


Software and Tools

##### **6.5 Product Marking**


_Figure 6-1: Unit Product Marking—Laser-etched, Typical Representation_


_Note: The figure above is not to scale. Contents will vary by SKU._


The product marking is laser-etched and may contain:

**•** Product identification (Model name, serial number)

**•** IMEI or MEID number and barcode

**•**
Fabrication country

**•**
Required regulatory markings (NCC, KCC, CE logo, Japan approval mark, FCC ID, IC certification number, etc., as
appropriate)

**•** Pin 1 indicator


_Note: The Semtech RC76xx supports OEM partner specific product marking requirements._


Rev. 16 March 2025 122 41113440


## **7**


### **7: Debug and Assembly Considerations**

##### **7.1 Testing Assistance Provided by Semtech**

Semtech offers optional professional services based assistance to OEMs with regulatory approvals.

##### **7.2 Integration Requirements**


When integrating the Semtech RC76xx, the following items must be addressed:

**•**
Mounting—Effect on temperature, shock, and vibration performance

**•**
Power supply—Impact on battery drain and possible RF interference

**•**
Antenna location and type—Impact on RF performance

**•**
Regulatory approvals—As described in Approval

**•**
Service provisioning—Manufacturing process


Semtech provides guidelines for successful module integration with the document suite and offers integration
support services as necessary.

##### **7.3 IOT / Operator**


Interoperability and Operator/Carrier testing of the finished system is the responsibility of the OEM. The test
process will be determined with the chosen network operator(s) and will be dependent upon your business
relationship with them, as well as the product's application and sales channel strategy.


Semtech offers assistance to OEMs with the testing process, if required.

##### **7.4 Module Testing Recommendations**


When testing your integration design:

**•**
Test to your worst case operating environment conditions (temperature and voltage)

**•**
Test using worst case operation (transmitter on 100% duty cycle, maximum power)

**•** Monitor the module’s junction temperature using **AT!PATEMP** . This command polls a thermistor located near
the module’s power amplifier (typically the hottest spot on the module).


_Note: Make sure that your system design provides sufficient cooling for the integrated module. The RF shield temperature should not be_
_exposed to an ambient temperature greater than 85°C to prevent damage to the module's components._

##### **7.5 Serial Link Access**


Direct access to the UART1 serial link is very useful for:

**•**
Testability operations

**•**
Accessing the module’s console for debugging


Refer to the following figure for a level shifter implementation that allows UART1 serial link access.


Rev. 16 March 2025 123 41113440


Debug and Assembly Considerations


_Figure 7-1: UART Application sample_

##### **7.6 RF Output Accessibility**


During the integration phase of the Semtech RC76xx, it can be helpful to connect the module to a simulator to check
critical RF TX parameters and power behavior for supported RATs.


Although the module has been certified, some parameters may have degraded if some basic precautions have not
been followed (poor power supply, for example). This may not affect the functionality of the product, but the product
may not comply with 3GPP specifications.


The following TX parameters can be checked using a Radio Communication tester:

**•**
Phase & Frequency Error

**•**
Output Power and Burst Time

**•**
Output Spectrum (Modulation and Switching)


The following are available typical Radio Communication testers:

**•** Rohde & Schwarz: CMU200, CMW500

**•**
Keysight (formerly Agilent): 8960

**•** Anritsu: MD8475


Because of the high prices associated with Radio Communication testers and the necessary RF know-how to
perform simulations, customers can check their applications in the Semtech laboratories. Contact the Semtech
support team for more information.

##### **7.7 USB Debug**


The USB interface is also used to collect traces for debug purposes. It is highly recommended to reserve test points
for collecting trace when USB is not used. Refer to USB for additional interface description.


Rev. 16 March 2025 124 41113440


## **8**


### **8: Reliability Specification**

##### **8.1 Functional / Performance Tests**


**•**
Operating Condition: Powered

**•**
Test Temperature: Class A and Class B

##### **8.2 Aging Tests**

###### **8.2.1 High Temperature Operating Life Test**


**•**
Standard: IEC 60068-2-2, Test B: Dry heat

**•**
Test Temperature: 85°C

**•**
Operating Condition: 45 minutes Max Tx/15 minutes Idle

**•**
Duration: 20 days

###### **8.2.2 Humidity Test**


**•**
Standard: IEC 60068-2-78, Test Cab: Damp heat, steady state

**•**
Test Temperature: 85°C

**•**
Relative Humidity: 85%

**•**
Operating Condition: 15 minutes Idle/15 minutes Off

**•**
Duration: 10 days

###### **8.2.3 Thermal Shock Test**


**•**
Standard: IEC 60068-2-14, Test N: Change of temperature

**•**
Test Temperature: -40°C to 85°C

**•**
Temperature Transition Time: < 30 seconds

**•** Dwell Time: 10 minutes

**•**
Operating Condition: Unpowered

**•**
Duration: 300 cycles

##### **8.3 Characterization Tests**

###### **8.3.1 Electrostatic Discharge Test**


**•**
Standard: IEC 61000-4-2: Testing and measurement techniques—Electrostatic discharge Immunity test

**•**
Operating Condition: Powered

**•**
Air Voltage: ±2kV, ±4kV, ±8kV

**•**
Contact Voltage: ±2kV, ±4kV, ±6kV


Rev. 16 March 2025 125 41113440


Reliability Specification

###### **8.3.2 Low Temperature Cold Start Test**


**•** Standard: IEC 60068-2-1, Test A: Cold

**•**
Test Temperature: -40°C

**•**
Operating Condition: 30 minutes Off/5 minutes Idle

**•**
Duration: 5 days

###### **8.3.3 Electrostatic Discharge Component Test**


**•**
Standard: ANSI/ESDA/JEDEC JS-001, ESDA/JEDEC Joint Standard for Electrostatic Discharge Sensitivity Testing,
Human Body Model (HBM)—Component Level

**•**
Standard: ANSI/ESDA/JEDEC JS-002, ESDA/JEDEC Joint Standard for Electrostatic Discharge Sensitivity Testing,
Charged Device Model (CDM)—Device Level

**•** CDM: 500 V

**•** HBM: 2000 V

**•**
Operating Condition: Powered

###### **8.3.4 Unprotected Free Fall Drop Test**


**•**
Standard: IEC 60068-2-31, Test Ec: Rough handling shocks, primarily for equipment-type specimens

**•**
Number of Drops: 1 drop per direction (±X, ±Y, ±Z), 6 directions

**•**
Surface Type: Un-protected drops onto concrete

**•**
Drop Height: 1 meter

**•**
Operating Condition: Unpowered

###### **8.3.5 Component Solder Wettability Test**


**•**
Standard: IPC/EAC J-STD-002, Solder Wettability Tests for Component Leads, Terminations, Lugs, Terminals
and Wires

**•**
Surface Mount Process Simulation Test (Preconditioning 16 hours ±30minutes dry bake)

**•**
Operating Condition: Unpowered


Rev. 16 March 2025 126 41113440


## **9**


### **9: Legal Information**

This chapter describes the current certification status of the RC7611, RC7611-1, RC7612, RC7612-1, RC7620,
RC7620-1, RC7630, RC7630-1, and RC7630J* modules collectively referred to as the RC76xx series modules or
RC76xx module. Certifications in other countries may be attained upon customer request — contact your Semtech
account representative for details.


Additional testing and certification may be required for the host product with an embedded RC76xx series module
and are the responsibility of the OEM. Semtech offers professional services-based assistance to OEMs with the
testing and certification process, if required.


_* Limited availability_

##### **9.1 Regulatory and Industry Approvals/ Certifications**


The RC76xx Series modules are designed to meet, and upon commercial release, will meet the requirements of the
following regulatory bodies and regulations, where applicable:

**•** Federal Communications Commission (FCC) of the United States

**•**
The Certification and Engineering Bureau of Industry Canada (IC)

**•**
(HL7810) The National Communications Commission (NCC) of Taiwan, Republic of China

**•**
Regulatory Compliance Mark (RCM), Electrical Regulatory Authorities Council (Australia and New Zealand)

**•**
Radio Equipment Directive (RED) of the European Union

**•**
Ministry of Internal Affairs and Communications (MIC) of Japan


Upon commercial release, the following industry certifications will have been obtained, where applicable:

**•** GCF

**•** PTCRB


Additional certifications and details on specific country approvals may be obtained upon customer request —
contact your Semtech account representative for details.

##### **9.2 Compliance Acceptance and Certification**


Final regulatory and operator certification requires regulatory agency testing and approval with the fully integrated
UE host device incorporating the Semtech RC76xx module.


The OEM host device and, in particular, the OEM antenna design and implementation will affect the final product
functionality, RF performance, and certification test results.


_Note: Tests that require features not supported by the Semtech RC76xx (as defined by this document) are not supported._

##### **9.3 Certification Compliance**

###### **9.3.1 Important Compliance Information for North American Users**


The Semtech RC7611, RC7611-1, RC7612, and RC7612-1 modules have been granted modular approval for mobile
applications. Integrators may use these modules in their final products without additional FCC/IC certification if they
meet the following conditions. Otherwise, additional FCC/IC approvals must be obtained.


Rev. 16 March 2025 127 41113440


Legal Information


**1.** The end product must follow the RF trace routing recommendations on RF Routing Recommendations.


**2.** At least 20 cm separation distance between the antenna and the user’s body must be maintained at all times.


**3.** To comply with FCC regulations limiting both maximum RF output power and human exposure to RF radiation,
the maximum antenna gain including cable loss in a mobile-only exposure condition must not exceed the limits
stipulated in Table 9-1.


**Table 9-1: Antenna Gain Specifications**






|Device|Technology|Band|Frequency (MHz)|Maximum Antenna Gain (dBi)|
|---|---|---|---|---|
|RC7611,<br>RC7611-1|LTE|2|1850–1910|6|
|RC7611,<br>RC7611-1|LTE|4|1710–1755|6|
|RC7611,<br>RC7611-1|LTE|5|824–849|6|
|RC7611,<br>RC7611-1|LTE|12|699–716|6|
|RC7611,<br>RC7611-1|LTE|13|777–787|6|
|RC7611,<br>RC7611-1|LTE|14|788–798|6|
|RC7611,<br>RC7611-1|LTE|25|1850–1915|6|
|RC7611,<br>RC7611-1|LTE|26|814–849|6|
|RC7611,<br>RC7611-1|LTE|66|1710–1780|6|
|RC7611,<br>RC7611-1|LTE|71|663–698|6|
|RC7612,<br>RC7612-1|LTE|Band 2|1850–1910|6|
|RC7612,<br>RC7612-1|LTE|Band 4|1710–1755|6|
|RC7612,<br>RC7612-1|LTE|Band 5|824–849|6|
|RC7612,<br>RC7612-1|LTE|Band 12|699–716|6|
|RC7612,<br>RC7612-1|LTE|Band 13|777–787|6|
|RC7612,<br>RC7612-1|UMTS|Band II|1850–1910|6|
|RC7612,<br>RC7612-1|UMTS|Band IV|1710–1755|6|
|RC7612,<br>RC7612-1|UMTS|Band V|824–849|6|



**4.** The Semtech RC7611, RC7611-1, RC7612, and RC7612-1 may transmit simultaneously with other collocated
radio transmitters within a host device, provided the following conditions are met:

**·**
Each collocated radio transmitter has been certified by FCC/IC for mobile application.


Rev. 16 March 2025 128 41113440


Product Technical Specification


**·**
At least 20 cm separation distance between the antennas of the collocated transmitters and the user’s body
must be maintained at all times.

**·** The radiated power of a collocated transmitter must not exceed the EIRP limit stipulated in Table 9-2.


**Table 9-2: Collocated Radio Transmitter Specifications**






|Device|Technology|Frequency (MHz)|EIRP Limit (dBm)|
|---|---|---|---|
|Collocated<br>transmittersa|WLAN|2400–2500|25|
|Collocated<br>transmittersa|WLAN|5150–5850|27|
|Collocated<br>transmittersa|WiMAX|2300–2400|25|
|Collocated<br>transmittersa|WiMAX|2500–2700|25|
|Collocated<br>transmittersa|WiMAX|3300–3800|25|
|Collocated<br>transmittersa|BT|2400–2500|15|



a. Valid collocated transmitter combinations: WLAN+BT; WiMAX+BT.
(WLAN+WiMAX+BT is not permitted.)


**5.** A label must be affixed to the outside of the end product into which the Semtech RC7611, RC7611-1, RC7612,
or RC7612-1 is incorporated, with a statement similar to the following:

**·**
**(RC7611/RC7611-1) This device contains FCC ID:**
**N7NRC76B / IC: 2417C-RC76B**

**·**
**(RC7612/RC7612-1) This device contains FCC ID:**
**N7NRC76C / IC: 2417C-RC76C**


**6.** A user manual with the end product must clearly indicate the operating requirements and conditions that must
be observed to ensure compliance with current FCC/IC RF exposure guidelines.


The end product with an embedded RC7612 or RC7611 may also need to pass the FCC Part 15 unintentional
emission testing requirements and be properly authorized per FCC Part 15.


_Note: If this module is intended for use in a portable device, you are responsible for separate approval to satisfy the SAR requirements of_

_FCC Part 2.1093 and IC RSS-102._


**9.3.1.1 Industry Canada Statement**


This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following
two conditions:


(1) this device may not cause interference, and


(2) this device must accept any interference, including interference that may cause undesired operation of the
device.


This module is intended for OEM integrator. The OEM integrator is responsible for the compliance to all the rules
that apply to the product into which this certified RF module is integrated. Additional testing and certification may be
necessary when multiple modules are used.


This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This
equipment should be installed and operated with minimum distance 20 cm between the radiator and your body.


Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence.
L'exploitation est autorisée aux deux conditions suivantes :


Rev. 16 March 2025 129 41113440


Legal Information


(1) l'appareil ne doit pas produire de brouillage, et


(2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible
d'en compromettre le fonctionnement.


L'intégrateur OEM doit être conscient de ne pas fournir des informations à l'utilisateur final quant à la façon
d'installer ou de supprimer ce module RF dans le manuel de l'utilisateur du produit final qui intègre ce module. Le
manuel de l'utilisateur final doit inclure toutes les informations réglementaires requises et avertissements comme
indiqué dans ce manuel.


Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non
contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 20 cm de distance entre la source de
rayonnement et votre corps.

###### **9.3.2 Japan Radio and Telecom Approval**


The RC76xx Series modules have been granted Japan radio and telecom approvals with the approval numbers
shown below.

**•** RC7630 and RC7630-1:


**•** RC7630J*:


_*Limited availability_


Rev. 16 March 2025 130 41113440


## **10**


### **10: Pinout**

The system interface of the Semtech RC76xx is through the LGA pattern on the bottom of the PCB.


Semtech RC76xx pins are divided into three functional categories:

**•**
Core functions and associated pins—Cover all the mandatory features for M2M connectivity and will be
available by default across all CF3 family of modules. These Core functions are always available and always at
the same physical pin locations. A customer platform using only these functions and associated pins is
guaranteed to be forward and/or backward compatible with the next generation of CF3 modules.

**•**
Extension functions and associated pins—Bring additional capabilities to the customer. Whenever an Extension
function is available on a module, it is always at the same pin location.

**•**
Custom functions and associated pins—These are module-specific and make use of specific chipset functions
and I/Os.

**Warning:** _Custom features should be used with caution as there is no guarantee that the custom functions available on a given module_
_will be available on other CF3 modules._


Pins marked as "Leave open" or "Reserved" should not be used or connected.

##### **10.1 Pin Configuration**


Figure 10-1 illustrates the pin configuration of the RC76xx series module.



































|168 167 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71<br>96 166<br>244 243 242 241 240 239 238 237 236 Polarity<br>97 Mark 165<br>98 164<br>68 67 99 163 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1<br>100 19 66 162<br>192 193 194 195 196 197 198 171<br>101 20 65 161<br>102 21 64 160<br>191 214 215 216 217 218 199 172<br>103 22 63 159<br>104 23 190 213 228 229 230 219 200 173 62 158<br>105 24 61 157<br>106 25 189 212 227 234 231 220 201 174 60 156<br>107 26 59 155<br>108 27 188 211 226 233 232 221 202 175 58 154<br>109 28 57 153<br>110 29 187 210 225 224 223 222 203 176 56 152<br>111 30 55 151<br>186 209 208 207 206 205 204 177<br>31 54 150<br>113 32 53 149<br>185 184 183 182 181 180 179 178<br>114 33 52 148<br>115 147<br>69 70 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51<br>116 146<br>117 145<br>118 144<br>169 170 119 120 121 122 123 124 125 128 129 130 131 132 133 134 135 136 139 140 141 142 143|Col2|
|---|---|
|169<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>139<br>140<br>141<br>142<br>143<br>136<br>170<br>168<br>95<br>94<br>93<br>92<br>91<br>90<br>89<br>86<br>85<br>84<br>83<br>82<br>81<br>80<br>79<br>75<br>74<br>73<br>72<br>71<br>78<br>77<br>76<br>88<br>87<br>167<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>164<br>165<br>166<br>161<br>162<br>163<br>151<br>152<br>118<br>117<br>116<br>115<br>114<br>113<br>109<br>108<br>107<br>106<br>105<br>104<br>103<br>102<br>98<br>97<br>96<br>101<br>100<br>99<br>111<br>110<br>33<br>32<br>31<br>30<br>29<br>28<br>27<br>26<br>25<br>24<br>23<br>22<br>21<br>20<br>19<br>69<br>70<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>68<br>67<br>18<br>17<br>16<br>15<br>14<br>13<br>12<br>11<br>10<br>9<br>8<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>185<br>192<br>191<br>190<br>189<br>188<br>187<br>186<br>184<br>193<br>214<br>213<br>212<br>211<br>210<br>209<br>183<br>194<br>215<br>228<br>227<br>226<br>225<br>208<br>182<br>195<br>216<br>229<br>234<br>233<br>224<br>207<br>181<br>196<br>217<br>230<br>231<br>232<br>223<br>206<br>180<br>197<br>218<br>219<br>220<br>221<br>222<br>205<br>179<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>178<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>244<br>236<br>243<br>242<br>241<br>240<br>239<br>238<br>237<br>Polarity<br>Mark|Core pin<br>Extensio<br>Reserve<br>Ground|


_Figure 10-1: Pin Configuration (Top View, Through Module)_

##### **10.2 Pin Description**


Table 10-1 on page 132 lists detailed information for the LGA pins.



Rev. 16 March 2025 131 41113440


Pinout


_Note: Some pin numbers (112, 126, 127, 137, 138, 235) do not appear in this table because there are no corresponding pads on the_

_module’s PCB._


**Table 10-1: Pin Definitions**




















|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|1|I2C1_CLK|I2C|I/O|1.8V|PU||Leave open|I2C clock|Core|
|2|UART1_RIc,d|UART1|O|1.8V||L|Leave open|UART1 Ring<br>indicator|Core|
|2|UART1_RIc,d|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|
|3|UART1_RTSc|UART1|I|1.8V|PD|L|Leave open|UART1 Request to<br>send|Core|
|4|UART1_CTSc|UART1|O|1.8V||L|Leave open|UART1 Clear to<br>send|Core|
|5|UART1_TXc|UART1|I|1.8V|PD|L|Leave open|UART1 Transmit<br>data|Core|
|6|UART1_RXc|UART1|O|1.8V|||Leave open|UART1 Receive<br>data|Core|
|7|UART1_DTRc,e,l|UART1|I|1.8V|PD|L|Leave open|UART1 Data<br>terminal ready|Core|
|8|UART1_DCDc,d|UART1|O|1.8V||L|Leave open|UART1 Data carrier<br>detect|Core|
|8|UART1_DCDc,d|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|
|9|UART1_DSRc,d|UART1|O|1.8V||L|Leave open|UART1 Data set<br>ready|Core|
|9|UART1_DSRc,d|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|_Note: Do not install external pull-up on this pin, otherwise the module will not boot._|
|10|GPIO2e|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|11|RESET_IN_N|Control signal|I|1.8V|PU|L|Leave open|Input reset signal|Core|
|12|USB_D-|USB|I/O||||Leave open|USB Data negative|Core|
|13|USB_D+|USB|I/O||||Leave open|USB Data positive|Core|
|14|Reserved|No<br>Connection|||||See<br>footnotef||Extension|
|15|Reserved|No<br>Connection|||||See<br>footnotef||Extension|



Rev. 16 March 2025 132 41113440


Product Technical Specification


**Table 10-1: Pin Definitions (Continued)**









































|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|16|USB_VBUS|USB|I|5V or<br>VBAT_BB|||Optional<br>connection<br>(If USB<br>interface is<br>required<br>then<br>connect to<br>USB_VBUS<br>or, if<br>unavailable,<br>VBAT_BB;<br>otherwise,<br>leave open.)|USB power supply|Core|
|17–<br>20|Reserved|No<br>Connection|||||See<br>footnotef||Extension|
|21|Reserved|No<br>Connection|||||See<br>footnotef||Extension|
|22|SYS_CLK|Clock|O|1.8V|||Leave open|19.2 MHz digital<br>clock output|Extension|
|23|SLEEP_CLK|Clock|O|1.8V|||Leave open|32.768 kHz digital<br>clock output|Extension|
|24|ADC1|ADC|AI|0.1V - 1.7V|||Leave open|Analog to digital<br>conversion|Core|
|25|ADC0|ADC|AI|0.1V - 1.7V|||Leave open|Analog to digital<br>conversion|Core|
|26|UIM1_VCC|UIM1|Power<br>Output|1.8V /<br>2.85V|||Mandatory<br>connection|UIM1 Power supply|Core|
|27|UIM1_CLK|UIM1|O|1.8V /<br>2.85V|||Mandatory<br>connection|UIM1 Clock|Core|
|28|UIM1_DATA|UIM1|I/O|1.8V /<br>2.85V|||Mandatory<br>connection|UIM1 Data|Core|
|29|UIM1_RESET_N|UIM1|O|1.8V /<br>2.85V||L|Mandatory<br>connection|UIM1 Reset|Core|
|30|GND|Ground|0V|0V|||Mandatory<br>connection|Diversity antenna<br>ground|Extension|
|31|RF_DIV|RF|AI||||Mandatory<br>connection|Diversity antenna|Extension|
|32|GND|Ground|0V|0V|||Mandatory<br>connection|Diversity antenna<br>ground|Extension|
|33|PCM_OUT|PCM|O|1.8V|||Leave open|PCM data out|Core|
|33|I2S_OUT|I2S|O|1.8V|||Leave open|I2S data out|I2S data out|
|34|PCM_IN|PCM|I|1.8V|PD||Leave open|PCM data in|Core|
|34|I2S_IN|I2S|I|1.8V|PD||Leave open|I2S data in|I2S data in|
|35|PCM_SYNC|PCM|O|1.8V|||Leave open|PCM sync|Core|
|35|I2S_WS|I2S|O|1.8V|||Leave open|I2S word select|I2S word select|


Rev. 16 March 2025 133 41113440


**Table 10-1: Pin Definitions (Continued)**





Pinout




























































|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|36|PCM_CLK|PCM|O|1.8V|||Leave open|PCM clock|Core|
|36|I2S_CLK|I2S|O|1.8V|||Leave open|I2S clock|I2S clock|
|37|GND|Ground|0V|0V|||Mandatory<br>connection|GNSS antenna<br>ground|Core|
|38|RF_GNSS|RF|AI||||Leave open|RF GNSS input|Extension|
|39|GND|Ground|0V|0V|||Mandatory<br>connection|GNSS antenna<br>ground|Core|
|40|GPIO7|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|41|GPIO8|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|42|DR_SYNC|GPS|O|1.8V|||Leave open|GPS dead reckoning<br>sync|Extension|
|43|EXT_GPS_LNA_EN|GPS|O|1.8V||H|Leave open|External GNSS LNA<br>enable|Extension|
|44|GPIO13|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|45|VGPIO|Voltage<br>reference|Power<br>Output|1.8V|||Leave open|GPIO voltage<br>output|Core|
|46|Ext_SIM_switchg|O|I|1.8V|||Leave open|External SIM switch|Core|
|46|GPIO6|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|46|RESET_OUT_N|Control<br>Signal|O|1.8V|||Leave open|Reset output signal|Core|
|47|TP1<br>(Boot pin)|Control<br>Signal|I|1.8V||L|Mandatory<br>test point|Test point 1<br>0—Download<br>mode<br>Open—Normal<br>mode|Extension|
|48|GND|Ground|0V|0V|||Mandatory<br>connection|Main antenna<br>ground|Core|
|49|RF_MAIN|RF|AI, AO||||Mandatory<br>connection|Main RF antenna|Core|
|50|GND|Ground|0V|0V|||Mandatory<br>connection|Main antenna<br>ground|Core|
|51|SPI1_MRDY|SPI1|O|1.8V|||Leave open|SPI Master Ready|Core|
|52|SPI1_MISO|SPI1|I|1.8V|PD||Leave open|SPI Master Input/<br>Slave Output<br>(output from slave)|Core|
|53|SPI1_CLK|SPI1|O|1.8V|||Leave open|SPI serial clock<br>(output from<br>Master)|Core|



Rev. 16 March 2025 134 41113440


Product Technical Specification


**Table 10-1: Pin Definitions (Continued)**











































|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|54|SPI1_MOSI|SPI1|O|1.8V|||Leave open|SPI Master Output/<br>Slave Input (output<br>from master)|Core|
|55|Reservedj|No<br>Connection|||||See footnotef|See footnotef|Core|
|55|UIM2_VCCk|UIM2|Power<br>Output|1.8V /<br>2.85V|||Leave open|UIM1 Power|UIM1 Power|
|56|Reservedj|No<br>Connection|||||See footnotef|See footnotef|Core|
|56|UIM2_DATAk|UIM2|I/O|1.8V /<br>2.85V|||Leave|UIM1|UIM1|
|57|Reservedj|No<br>Connection|||||See footnotef|See footnotef|Core|
|57|UIM2_RESET_Nk|UIM2|O|1.8V /<br>2.85V|||Leave|UIM1|UIM1|
|58|Reservedj|No<br>Connection|||||See footnotef|See footnotef|Core|
|58|UIM2_CLKk|UIM2|O|1.8V /<br>2.85V|||Leave open|UIM1 Clock|UIM1 Clock|
|59|POWER_ON_N|Control<br>Signal|I|0.8V|PU|L|Mandatory<br>connection|Power On control<br>signal|Core|
|60|TX_ON|Indication|O|1.8V||H|Leave open|Tx activity indicator|Extension|
|61|VBAT_RF|Power|Power<br>Input|3.2V (min)<br>3.7V (typ)<br>4.3V (max)|||Mandatory<br>connection|RF power supply<br>(seePower Supply<br>Ratings)|Core|
|62|VBAT_RF|Power|Power<br>Input|3.2V (min)<br>3.7V (typ)<br>4.3V (max)|||Mandatory<br>connection|RF power supply<br>(seePower Supply<br>Ratings)|Core|
|63|VBAT_BB|Power|Power<br>Input|3.2V (min)<br>3.7V (typ)<br>4.3V (max)|||Mandatory<br>connection|Baseband power<br>supply (seePower<br>Supply Ratings)|Core|
|64|UIM1_SIMA_DETe|UIM1|I|1.8V|PU|H|Mandatory<br>connection|Detect UIM1<br>insertion/removal.<br>(Pin must be open<br>to detect the UIM,<br>or grounded if no<br>UIM is present.)|Core|
|65|UIM1_SIMB_DETe|UIM1|I|1.8V|PU|H|Leave open|Detect UIM1_SIMB<br>insertion / removal<br>/ General purpose I/<br>O|Extension|
|65|GPIO4f|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|66|I2C1_Data|I2C|I/O|1.8V|PU||Leave open|I2C data|Core|


Rev. 16 March 2025 135 41113440


**Table 10-1: Pin Definitions (Continued)**





Pinout










































|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|67–<br>70|GND|Ground|0V|0V|||Mandatory<br>connection|Ground|Core|
|71–<br>90|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|91|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|92|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|93|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|94|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|95|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|96|UART2_TXc|UART2|I|1.8V|PD|L|Leave open|UART2 Transmit<br>data|Extension|
|97|UART2_RXc|UART2|O|1.8V|PD|L|Leave open|UART2 Receive<br>data|Extension|
|98|UART2_RTSc|UART2|I|1.8V|PD||Leave open|UART2 Request To<br>Send|Extension|
|99|UART2_CTSc|UART2|O|1.8V|||Leave open|UART2 Clear To<br>Send|Extension|
|100|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|101|GPIO35|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|102|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|103|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|104|GPIO32|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|105|GPIO33|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|106|WWAN_LED_N|Indication|O|VBAT_BBg||L|Leave open|LED driver control|Extension|
|107|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|108|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|109|GPIO42e|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|



Rev. 16 March 2025 136 41113440


Product Technical Specification


**Table 10-1: Pin Definitions (Continued)**




































































|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|110|WAKE_ON_WWAN|Indication|O|1.8V||H|Leave open|Driven high to wake<br>the host when<br>specific events<br>occur.|Extension|
|111|GND|Ground|0V|0V|||Mandatory<br>connection|Diversity antenna<br>ground|Core|
|113|GND|Ground|0V|0V|||Mandatory<br>connection|Diversity antenna<br>ground|Core|
|114–<br>124|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|125|GND|Ground|0V|0V|||Mandatory<br>connection|GNSS antenna<br>ground|Core|
|128|GND|Ground|0V|0V|||Mandatory<br>connection|GNSS antenna<br>ground|Core|
|129–<br>135|Reserved|No<br>Connection|||||See footnotef.|See footnotef.|Reserved|
|136|GND|Ground|0V|0V|||Mandatory<br>connection|Main antenna<br>ground|Core|
|139|GND|Ground|0V|0V|||Mandatory<br>connection|Main antenna<br>ground|Core|
|140–<br>146|Reserved|No<br>Connection|||||See footnotef.|See footnotef.|Reserved|
|147|GPIO21e|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|148|GPIO22|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|149|GPIO23|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|150|GPIO24|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|151|W_DISABLE_N|Control<br>Signal|I|1.8V|PU|L|Leave open|Wireless disable<br>(main RF radio)|Core|
|152|SAFE_PWR_REMO<br>VE|Indication|O|1.8V||H|Leave open|Indicate to host<br>that Main DC power<br>can be removed|Extension|
|153|ANT_CNTL0|Antenna<br>control|O|1.8V|||Leave open|Antenna<br>control|Extension|
|153|GPIO28h|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|154|ANT_CNTL1|Antenna<br>control|O|1.8V|||Leave open|Antenna<br>control|Extension|
|154|GPIO29h|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|



Rev. 16 March 2025 137 41113440


**Table 10-1: Pin Definitions (Continued)**





Pinout








































|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|155|ANT_CNTL2|Antenna<br>control|O|1.8V|||Leave open|Antenna<br>control|Extension|
|155|GPIO30h|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|156|ANT_CNTL3|Antenna<br>control|O|1.8V|||Leave open|Antenna control|Extension|
|156|GPIO31h|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Extension|
|157|VBAT_RF|Power|Power<br>Input|3.2V (min)<br>3.7V (typ)<br>4.3V (max)|||Optional<br>connection|RF power supply<br>(seePower Supply<br>Ratings)|Core|
|158|VBAT_BB|Power|Power<br>Input|3.2V (min)<br>3.7V (typ)<br>4.3V (max)|||Optional<br>connection|Baseband power<br>supply (seePower<br>Supply Ratings)|Core|
|159|GPIO25|GPIO|I/O|1.8V|PD||Leave open|General purpose I/<br>O|Core|
|160|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|161|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|162|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|163|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|164|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|165|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|166|Reserved|No<br>Connection|||||See<br>footnotef||Reserved|
|167–<br>234|GND|Ground|0V|0V|||Mandatory<br>connection|Ground|Core|
|236|J1i|||1.8V||L|Mandatory<br>test point|Test point|Extension|
|237|J2i|||1.8V|||Mandatory<br>test point|Test point|Extension|
|238|J3i|||1.8V|||Mandatory<br>test point|Test point|Extension|
|239|J4i|||1.8V|||Mandatory<br>test point|Test point|Extension|
|240|J5i|||1.8V||L|Mandatory<br>test point|Test point|Extension|



Rev. 16 March 2025 138 41113440


Product Technical Specification


**Table 10-1: Pin Definitions (Continued)**









|Pin|Signal Name|Group|I/Oa|Voltage|PU/<br>PD in<br>active<br>statusb|Active|If<br>Unused|Function|Type|
|---|---|---|---|---|---|---|---|---|---|
|241|J6i|||1.8V|||Mandatory<br>test point|Test point|Extension|
|242|J7i|||1.8V|||Mandatory<br>test point|Test point|Extension|
|243|J8i|||1.8V|||Mandatory<br>test point|Test point|Extension|
|244|J9i|||1.8Vj|||Mandatory<br>test pointk|Test pointl|Extension|


a. Signal direction with respect to the module. Examples: PCM_OUT (pin 33) is an output from the module to the host; PCM_IN (pin 34)
is an input to the module from the host.
b. NP—No Pull; PD—Pull Down; PU—Pull Up (in default/active normal mode)
c. (UART signals only) Signals are named with respect to the host device. For example, UART1_RX is the signal used by the host to
receive data from the module.
d. Do not install external pull-up on this pin, otherwise the module will not boot.
e. Pin is ‘wakeable’. Can be used to trigger the module to wake up from Sleep mode. See Wakeup Interrupt (Sleep State) for details.
f. Pins are connected internally, but are reserved for future use. Leave them unconnected to ensure compatibility with other Semtech
CF3 modules.
g. Refer to GPIO6 for functional details.
h. This pin is available for use when configured using **AT+WIOCFG** .
i. Accessibility restricted to soldered-down modules. Not available for socket-mounted modules.
j. For RC7611, RC7620, RC7630, and RC7630J* (* Limited availability).
k. Limited Availability for RC7612, RC7612-1.
l. The pin (UART1_DTR) will be floating when KSLEEP=0 and will pull-up when KSLEEP=1 or 2. For details on KSLEEP, see the RC76xx
AT command guide.


**Table 10-2: RF Pin Information**

|Signal name|Pin #|Description|
|---|---|---|
|RF_DIV|31|Diversity input|
|RF_GNSSa|38|RF GNSS input|
|RF_MAIN|49|Main RF port (input/output)|



a. Support is SKU-dependent.


**Table 10-3: Supply Pin Information**

|Signal name|Pin #|Description|
|---|---|---|
|VBAT_RF|61, 62, 157|RF power supply|
|VBAT_BB|63, 158|Baseband power supply|
|USB_VBUS|16|Connected to USB_VBUS (5V) or (if unavailable) VBAT_BB|



Rev. 16 March 2025 139 41113440


## **11**


### **11: Customization**

Subject to commercial terms, Semtech can supply custom-configured modems to facilitate a carrier's network and
performance requirements. Semtech also offers a standard configuration for each country.


Custom configurations are entered into a selector spreadsheet that Sierra supplies. A unique part number is
assigned to each custom configuration to facilitate customer ordering.


**Table 11-1: Customizable Features**







|Name|Description|Default|
|---|---|---|
|Display of IMSI|Display of International Mobile Subscriber Identity via<br>**AT+CIMI** command|Display enabled|
|UART baud rate|Default UART speed|115200 bps|
|UART enabled|Defines whether UART port is enabled by default or not|UART enabled|


Rev. 16 March 2025 140 41113440


## **12**


### **12: Testing**

##### **12.1 Certification Testing**

_Note: Typically, certification testing of your device with the integrated module is required one time only._


The Semtech RC76xx module has been certified as described in Compliance Acceptance and Certification.


When you produce a host device with a Semtech Semtech embedded module, you must obtain certifications for the
final product from appropriate regulatory bodies in the jurisdictions where it will be distributed.


The following are _some_ of the regulatory bodies from which you may require certification—it is your responsibility
to make sure that you obtain all necessary certifications for your product from these or other groups:

**•** [FCC (Federal Communications Commission—www.fcc.gov)](http://www.fcc.gov)

**•** [GCF (Global Certification Forum—www.globalcertificationforum.org) outside of North America](http://www.globalcertificationforum.org)

**•** [PTCRB (PCS Type Certification Review Board—www.ptcrb.com) in North America](http://www.ptcrb.com)

##### **12.2 Production Testing**


_Note: Production testing typically continues for the life of the product._


Production testing ensures that, for each assembled device, the module is installed correctly (I/O signals are passed
between the host and module), and the antenna is connected and performing to specifications (RF tests).


Typical items to test include:

**•**
Host connectivity

**•** Baseband (host/module connectors)

**•**
RF assembly (Tx and/or Rx, as appropriate)

**•**
Network availability

**•**
Host/device configuration issues


_Note: The number and types of tests to perform are_ _**your**_ _decision—the tests listed in this section are guidelines only. Make sure that the_
_tests you perform exercise functionality to the degree that_ _**your**_ _situation requires._


Use an appropriate test station and use AT commands to control the integrated module.


_Note: Your test location must be protected from ESD to avoid interference with the module and antenna(s), assuming that your test_
_computer is in a disassembled state._
_Also, consider using an RF shielding box—local government regulations may prohibit unauthorized transmissions._


_Note: The tests described in this chapter are done using a Linux O/S (e.g. Ubuntu 12.04)._


Rev. 16 March 2025 141 41113440


Testing

##### **12.3 Functional Production Test**


This section presents a suggested procedure for performing a basic manual functional test on a laboratory bench
using an Semtech RC76xx module and a hardware development kit. When you have become familiar with the testing
method, use it to develop your own automated production testing procedures.

###### **12.3.1 Suggested Production Tests**


Consider the following tests when you design your production test procedures for devices with the module installed.

**•** Visual check of the module’s connectors and RF assemblies

**•**
Module is operational

**•** USB connection is functional

**•** LED is functional

**•** Power on/off

**•** Firmware revision check

**•**
Rx tests on main and auxiliary paths

**•** Tx test

###### **12.3.2 Production Test Procedure**


The following is a suggested test plan—you must decide which tests are appropriate for your product. You may
wish to add additional tests that more fully exercise the capabilities of your product.


Using an appropriate test station, and referring to the appropriate AT command references:


**1.** Visually inspect the module for obvious defects (such as tainted or damaged shields) before installing it in the
test station.


**2.** Ensure that the module is powered off (no voltage on VBAT_BB/VBAT_RF) before beginning your tests.


**3.** Determine whether any USB devices are currently connected to the computer:


**a.** Open a shell window and enter the command ls /dev/tty/USB* .


**b.** Record the ttyUSB _n_ values that are returned; these are the currently connected USB devices. If the
command returns “no such file or directory”, there are no devices currently connected.


**4.** Provide power to the module (voltage on VBAT_BB/VBAT_RF).


**5.** Test POWER_ON_N—Turn on the module by driving POWER_ON_N low, as shown in Figure 4-2.


**6.** Test USB functionality—Check for USB enumeration.

Enter the command ls /dev/tty/USB* and then record and compare the results with those from Step 3. If there
are any new ttyUSB _n_ devices, then the modem has enumerated successfully. (The AT port is usually the _last_ new
device.)


**7.** Make sure your modem is connected and running, and then establish contact with the module:

Use a terminal emulation/communications program such as minicom to connect over the device handle for AT
commands (see listings in Step 6):


_Note: If the command “minicom” is not found, then use a different program, or download minicom and repeat this step. See Downloading_
_and Configuring minicom for Linux Systems on page 143 for details._


**a.** Start minicom:

**·** First use of the modem: From the command line, type minicom -s . (The ‘-s’ switch shows the configuration
menu.)


Rev. 16 March 2025 142 41113440


Product Technical Specification


**·**
Subsequent uses: From the command line, type minicom. (The ‘-s’ switch is assumed.)


The minicom configuration details appear and the message OK appears when the connection is established.


**8.** Display the firmware version using **ATI.**


**9.** Unlock the extended AT command set with **AT!ENTERCND=”<password>”** .


_Note: Use_ _**AT!ENTERCND?**_ _to check command syntax which is SKU-dependent._


**10.** Test the LED—Visually confirm that the LED turns on and off using:

**AT!LEDTEST=0,1** (LED on)

**AT!LEDTEST=0,0** (LED off)


**11.** Put the module in diagnostic/factory test mode using **AT!DAFTMACT** :


**12.** Communicate with the SIM using **AT+CPIN** or **AT+CIMI** .


**13.** Test RF transmission, if desired.

**·** For LTE, see LTE RF Transmission Path Test on page 146.

**·**
For UMTS, see UMTS (WCDMA/GSM) RF Transmission Path Test on page 144


**14.** Test RF reception, if desired.

**·** For LTE, see LTE RF Receive Path Test on page 152.

**·**
For UMTS, see See UMTS (WCDMA/GSM) RF Receive Path Test on page 149.


**15.** Test standalone GNSS functionality. See GNSS RF Receive Path Test on page 154.


**16.** Remove power from the module.


**12.3.2.1 Downloading and Configuring minicom for Linux Systems**


_Note: This procedure is for Ubuntu systems. If you are using a different Linux distribution, use the appropriate commands for your system_

_to download minicom._


To download and configure minicom in a Ubuntu system:


_Note: To install minicom, you must have root access, or be included in the sudoers list._


**1.** Download and install minicom by entering **sudo apt-get install minicom** .


**2.** When prompted, enter your user password to begin the download and installation. When minicom is installed,
the shell prompt appears.


**3.** Configure minicom to communicate with your modem. Start minicom with command **minicom -s** .


**4.** Use the down-arrow key to select the Serial port setup option.


Rev. 16 March 2025 143 41113440


Testing


**5.** Refer to Step 6 on page 142 to identify the device file handle (/dev/ttyUSBn) used for AT commands.


**6.** Indicate the file handle to use for AT commands—Enter A and then replace the serial device string with the AT
file handle.


**7.** Press Enter twice.


**8.** Use the down-arrow key to select Save setup as dfl .


**9.** Select Exit .

##### **12.4 UMTS (WCDMA/GSM) RF Transmission Path Test**


**Important:** _As of the publication date of this document, the test procedure described is to be considered preliminary, pending imple-_
_mentation of some commands in a future firmware upgrade._


_Note: This procedure is performed in Step 13 of the Production Test Procedure on page 142_


The suggested test procedure that follows uses the parameters in the following tables.


**Table 12-1: Test Settings—RC7620 UMTS Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Tx Channela|
|---|---|---|---|---|
|2100 MHz|B1|1950.0|9|9750|
|900 MHz|B8|897.6|29|2788|



a. Channel values shown are at the center of the corresponding bands.


**Table 12-2: Test Settings—RC7620 2G Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Tx Channela|
|---|---|---|---|---|
|900 MHz|E-GSM 900|897.4|10|37|
|1800 MHz|DCS 1800|1747.8|11|700|



a. Channel values shown are at the center of the corresponding bands


**Table 12-3: Test Settings—RC7612 UMTS Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Tx Channel|
|---|---|---|---|---|
|1900 MHz|B2|1880|16|9400|
|AWS-1|B4|1732.6|28|1413|
|850 MHz|B5|836.6|22|4183|



_Note: This procedure describes steps using the “Power Meter: Gigatronics 8651a (with option 12 and Power Sensor 80701A)._


Rev. 16 March 2025 144 41113440


Product Technical Specification


To test the DUT’s transmitter path:


**1.** Set up the power meter:


**a.** Make sure the meter has been given sufficient time to warm up, if necessary, to enable it to take accurate
measurements.


**b.** Zero-calibrate the meter.


**c.** Enable MAP mode.


**2.** Prepare the DUT using the following AT commands:


**a.** **AT!ENTERCND="<password>"** (Unlock extended AT command set.)


**b.** **AT!DAFTMACT** (Enter test mode.)


**c.** **AT!DASBAND=<bandValue>** (Set frequency band, e.g. 34 for LTE B1.)


**d.** **AT!DALSTXBW=3** (Set Tx bandwidth to 10 MHz.)


**e.** **AT!DALSRXBW=3** (Set Rx bandwidth to 10 MHz.)


**f.** **AT!DASCHAN=<channel>** (Set modem channel, e.g. 18300 for LTE B1.)


**g.** **AT!DALSTXMOD=0** (Set Tx modulation type to QPSK.)


**h.** **AT!DALSWAVEFORM=1,12,0,19** (Set the Tx waveform characteristics. Make sure to set the correct
resource block allocation (2nd parameter) appropriately. For example, 12 is used to produce max power—
refer to 3GPP 36.521 table for Maximum Power Reduction (MPR) for Power Class 3 for more information.)


**i.** **AT!DALSNSVAL=1** (Set the LTE NS (Net Sig) value.)


**j.** **AT!DASTXON** (Turn on the transmitter. Note that the trans- mitter will put out the last power level that
was programmed.)


**k.** **AT!DALSTXPWR=1,10** (Begin transmitting at requested power level.)


**l.** Take the measurement.


**m.** Repeat Step k with different power levels if desired.


**n.** **AT!DALSTXPWR=0,0** (Reduce Tx power to 0, so next time trans- mitter is turned on, it will come on with
0 dBm power.)


**o.** **AT!DASTXOFF** (Turn off the transmitter.)


**3.** Test limits—Run ten or more good DUTs through this test procedure to obtain a nominal output power value.

**·**
Apply a tolerance of + 5 to 6 dB to each measurement (assuming a good setup design).

**·**
Monitor these limits during mass-production ramp-up to determine if further adjustments are needed.


Rev. 16 March 2025 145 41113440


Testing


_Note: The module has a nominal output power of +23 dBm +1 dB in LTE mode. However, the value measured by the power meter is_
_significantly influenced (beyond the stated +1 dB output power tolerance) by the test setup (host RF cabling loss, antenna efficiency and_
_pattern, test antenna efficiency and pattern, and choice of shield box). When doing the same test over the air in an RF chamber, values are_
_likely to be significantly lower._

##### **12.5 LTE RF Transmission Path Test**


**Important:** _As of the publication date of this document, the test procedure described is to be considered preliminary, pending imple-_
_mentation of some commands in a future firmware upgrade._


_Note: This procedure segment is performed in Step 13 of the Production Test Procedure on page 142._


The suggested test procedure that follows uses the parameters in the following tables.


**Table 12-4: Test Settings — RC7611, RC7612 LTE Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Channela|
|---|---|---|---|---|
|1900 MHz|B2|1880.0|43|18900|
|1700 MHz|B4|1732.4|42|20175|
|850 MHz|B5|836.5|45|20525|
|700 MHz|B12|707.5|50|23095|
|700 MHz|B13|782.0|36|23230|
|700 MHz|B14|793.0|51|23330|
|1900 MHz|B25|1882.5|61|26365|
|850 MHz|B26|831.5|62|26865|
|1700 MHz|B66|1745.0|83|132322|
|600 MHz|B71|680.5|97|133297|



a. Channel value used by the **!DASCHAN** command ( **!DASCHAN** uses uplink (Tx) channel at the center of the corresponding band, for
both Tx and Rx testing)


**Table 12-5: Test Settings—RC7620 LTE Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Channela|
|---|---|---|---|---|
|2100 MHz|B1|1950.0|34|18300|
|1800 MHz|B3|1747.5|44|19575|
|2600 MHz|B7|2535.0|35|21100|
|900 MHz|B8|897.5|47|21625|



Rev. 16 March 2025 146 41113440


Product Technical Specification


**Table 12-5: Test Settings—RC7620 LTE Transmission Path (Continued)**

|Band|Col2|Frequency (MHz)|Band ID|Channela|
|---|---|---|---|---|
|800 MHz|B20|847.0|56|24300|
|700 MHz|B28|725.5|64|27435|



a. Channel value used by the !DASCHAN command (!DASCHAN uses uplink (Tx) channel at the center of the corresponding band, for both
Tx and Rx testing.)


**Table 12-6: Test Settings—RC7630 LTE Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Channela|
|---|---|---|---|---|
|2100 MHz|B1|1950.0|34|18300|
|1800 MHz|B3|1747.5|44|19575|
|850 MHz|B5|836.5|45|20525|
|2600 MHz|B7|2535|35|21100|
|900 MHz|B8|897.5|47|21625|
|800 MHz|B18|822.5|54|23925|
|800 MHz|B19|837.5|55|24075|
|1500 MHz|B21|1455.5|57|24525|



a. Channel value used by the !DASCHAN command (!DASCHAN uses uplink (Tx) channel at the center of the corresponding band, for both
Tx and Rx testing.)


**Table 12-7: Test Settings—RC7630J** **[a]** **LTE Transmission Path**

|Band|Col2|Frequency (MHz)|Band ID|Channelb|
|---|---|---|---|---|
|2100 MHz|B1|1950.0|34|18300|
|1800 MHz|B3|1747.5|44|19575|
|850 MHz|B5|836.5|45|20525|
|800 MHz|B18|822.5|54|23925|
|800 MHz|B19|837.5|55|24075|



a. Limited availability.

b. Channel value used by the !DASCHAN command (!DASCHAN uses uplink (Tx) channel at the center of the corresponding band, for both
Tx and Rx testing.)


Rev. 16 March 2025 147 41113440


Testing


To test the DUT’s transmitter path:


_Note: This procedure describes steps using the "Power Meter: Gigatronics 8651A” (with Option 12 and Power Sensor 80701A)._


**1.** Set up the power meter:


**a.** Make sure the meter has been given sufficient time to warm up, if necessary, to enable it to take accurate
measurements.


**b.** Zero-calibrate the meter.


**c.** Enable MAP mode.


**2.** Prepare the DUT using the following AT commands (adjusting the band, channel, bandwidth, modulation, RB
allocation, NS, and power level as necessary):


**a.** **AT!ENTERCND=”<password>”** (Unlock extended AT command set.)


**b.** **AT!DAFTMACT** (Enter test mode.)

**c.** **AT!DASBAND=<bandValue>** (Set frequency band (e.g. 34 for LTE B1.))


See table Table 12-4 on page 146 for appropriate <bandValue> values.
**d.** **AT!DALSTXBW=3** (Set Tx bandwidth to 10 MHz.)
**e.** **AT!DALSRXBW=3** (Set Rx bandwidth to 10 MHz.)
**f.** **AT!DASCHAN=<channel>** (Set modem channel (e.g. 18300 for LTE B1).)


See tables Table 12-4 on page 146 for appropriate <channel> values.
**g.** **AT!DALSTXMOD=0** (Set Tx modulation type to QPSK.)
**h.** **AT!DALSWAVEFORM=1,12,0,19** (Set the Tx waveform characteristics. Make sure to set the
correct resource block allocation (2nd parameter) appropriately.
For example, 12 is used to produce max power—refer to
3GPP 36.521 table for Maximum Power Reduction (MPR) for
Power Class 3 for more information.)


**i.** **AT!DALSNSVAL=1** (Set the LTE NS (Net Sig) value.)


**j.** **AT!DASTXON** (Turn on the transmitter. Note that the transmitter will put out the
last power level that was programmed.)


**k.** **AT!DALSTXPWR=1,10** (Begin transmitting at requested power level.)


**l.** Take the measurement.


**m.** Repeat Step k with different power levels if desired.


**n.** **AT!DALSTXPWR=0,0** (Reduce Tx power to 0, so next time transmitter is turned on, it will
come on with 0 dBm power.)


**o.** **AT!DASTXOFF** (Turn off the transmitter.)


Rev. 16 March 2025 148 41113440


Product Technical Specification


**3.** Test limits—Run ten or more good DUTs through this test procedure to obtain a nominal output power value.

**·** Apply a tolerance of  5 to 6 dB to each measurement (assuming a good setup design).

**·**
Monitor these limits during mass-production ramp-up to determine if further adjustments are needed.


_Note: The module has a nominal output power of +23 dBm_  _1 dB in LTE mode. However, the value measured by the power meter is_
_significantly influenced (beyond the stated_  _1 dB output power tolerance) by the test setup (host RF cabling loss, antenna efficiency and_
_pattern, test antenna efficiency and pattern, and choice of shield box)._


_Note: When doing the same test over the air in an RF chamber, values are likely to be significantly lower._

##### **12.6 UMTS (WCDMA/GSM) RF Receive Path Test**


_Note: This procedure segment is performed in Step 14 of the Production Test Procedure on page 142._


The suggested test procedure that follows uses the parameters in the following tables.


**Table 12-8: Test Settings—RC7620 UMTS Receive Path**







|Band|Col2|Frequencya (MHz)|Band ID|Rx Channelb|
|---|---|---|---|---|
|2100 MHz|B1|2141.2|9|10700|
|900 MHz|B8|943.8|29|3013|


a. Receive frequencies shown are 1.2 MHz offset from center.

b. Channel values shown are at the center of the corresponding bands.


**Table 12-9: Test Settings—RC7620 2G Receive Path**







|Band|Col2|Frequencya (MHz)|Band ID|Rx Channelb|
|---|---|---|---|---|
|900 MHz|E-GSM 900|942.467|10|37|
|1800 MHz|DCS 1800|1842.867|11|700|


a. Receive frequencies shown are 67 KHz offset from center.

b. Channel values shown are at the center of the corresponding bands.


**Table 12-10: Test Settings—RC7612 UMTS Receive Path**







|Band|Col2|Frequencya (MHz)|Band ID|Rx Channelb|
|---|---|---|---|---|
|1900MHz|B2|1960|16|9800|
|AWS-1|B4|2132.6|28|1638|
|850MHz|B5|881.6|22|4408|


a. Receive frequencies shown are 67 KHz offset from center.

b. Channel values shown are at the center of the corresponding bands.


Rev. 16 March 2025 149 41113440


Testing


To test the DUT’s receive path:


_Note: This procedure describes steps using the Agilent 8648C signal generator—the Rohde & Schwarz SML03 is shown for reference_
_only._


**1.** Set up the signal generator:


Rev. 16 March 2025 150 41113440


Product Technical Specification


**a.** Set the amplitude to:

**·**
-80 dBm (WCDMA mode)

**·**
-60 dBm (GSM mode)


**b.** Set the frequency for the band being tested. See Table 12-8 and Table 12-9 for frequency values.


**2.** Set up the DUT:


**a.** **AT!ENTERCND=”<password>”** (Unlock extended AT command set.)
**b.** **AT!DAFTMACT** (Put modem into factory test mode.)
**c.** **AT!DASBAND=<band>** (Set frequency band.)


See Table 12-8 and Table 12-9for <band> values

**d.** **AT!DASCHAN=<channel>** (Set modem channel)

**·** See Table 12-8 and Table 12-9 for <channel> values

**e.** **AT!DASLNAGAIN=0** (Set the LNA to maximum gain.)
**f.** **AT!DAWGAVGAGC=9400,0** (WCDMA mode: For PCS1900, channel 9400 as an example.)
**g.** GSM mode:


**i.** **AT!DAGSRXBURST=0** (Set to receive bursted mode.)


**ii.** **AT!DAGGAVGRSSI=190,0** (For channel 190, for example)


**3.** Test limits—Run ten or more good DUTs through this test procedure to obtain a nominal received power value.

**·** Apply a tolerance of  5 to 6 dB to each measurement (assuming a good setup design).

**·**
Make sure the measurement is made at a high enough level that it is not influenced by DUT-generated and
ambient noise.

**·**
The Signal Generator power level can be adjusted and new limits found if the radiated test needs greater
signal strength.

**·**
Monitor these limits during mass-production ramp-up to determine if further adjustments are needed.


_Note: The value measured from the DUT is significantly influenced by the test setup and DUT design (host RF cabling loss, antenna_
_efficiency and pattern, test antenna efficiency and pattern, and choice of shield box)._


**4.** Test diversity paths:


**a.** Set up the signal generator as in Step a.


**b.** Set up the DUT:


**i.** **AT!ENTERCND=”<password>”** Unlock extended AT command set.)


**ii.** **AT!DAFTMACT** Put modem into factory test mode.)


**iii.** **AT!DASBAND=<band>** (Set frequency band.)

**•** See Table 12-8 and Table 12-9for <band> values


**iv.** **AT!DAWSSCHAIN=1** (Enable the secondary chain.)


**v.** **AT!DASCHAN=<channel>** ( Set modem channel)

**•** See Table 12-8 and Table 12-9 for <channel> values


**vi.** **AT!DASLNAGAIN=0** (Set the LNA to maximum gain.)


**vii. AT!DAWGAVGAGC=9400,0,1** ( The ‘1’ indicates tge diversity path used.)


**c.** Test the limits as in Step 3.


Rev. 16 March 2025 151 41113440


Testing


##### **12.7 LTE RF Receive Path Test**

_Note: This procedure segment is performed in Step 14 of the Production Test Procedure on page 142._


The suggested test procedure that follows uses the parameters in the following tables.


**Table 12-11: Test Settings — RC7611, RC7612 LTE Receive Path**







|Band|Col2|Frequencya (MHz)|Band ID|Channelb|
|---|---|---|---|---|
|1900 MHz|B2|1962.00|43|18900|
|1700 MHz|B4|2134.50|42|20175|
|850 MHz|B5|883.50|45|20525|
|700 MHz|B12|739.50|50|23095|
|780 MHz|B13|753.00|36|23230|
|700 MHz|B14|763.0|51|23330|
|1900 MHz|B25|1964.5|61|26365|
|850 MHz|B26|878.5|62|26865|
|1700 MHz|B66|2157|83|132322|
|600 MHz|B71|635.5|97|133297|


a. Receive frequencies shown are 2 MHz offset from center

b. Channel value used by the **!DASCHAN** command ( **!DASCHAN** uses uplink (Tx) channel at the center of the corresponding band, for
both Tx and Rx testing)


**Table 12-12: Test Settings — RC7620 LTE Receive Path**







|Band|Col2|Frequencya (MHz)|Band ID|Channelb|
|---|---|---|---|---|
|2100 MHz|B1|2142.00|34|18300|
|1800 MHz|B3|1844.5|44|19575|
|2600 MHz|B7|2657.00|35|21100|
|900 MHz|B8|944.5|47|21625|
|800 MHz|B20|808.00|56|24300|
|700 MHz|B28|782.5|64|27435|


a. Receive frequencies shown are 2 MHz offset from center

b. Channel values shown are at the center of the corresponding bands.


Rev. 16 March 2025 152 41113440


Product Technical Specification


**Table 12-13: Test Settings — RC7630 LTE Receive Path**





|Band|Col2|Frequencya (MHz)|Band ID|Channelb|
|---|---|---|---|---|
|2100 MHz|B1|2142|34|18300|
|1800 MHz|B3|1844.5|44|19575|
|850 MHz|B5|883.5|45|20525|
|2600 MHz|B7|2657|35|21100|
|900 MHz|B8|944.5|47|21625|
|800 MHz|B18|869.5|54|23925|
|800 MHz|B19|884.5|55|24075|
|1500 MHz|B21|1505.5|57|24525|


a. Receive frequencies shown are 2 MHz offset from center.

b. Channel values shown are at the center of the corresponding bands.


**Table 12-14: Test Settings — RC7630J** **[a]** **LTE Receive Path**







|Band|Col2|Frequencyb (MHz)|Band ID|Channelc|
|---|---|---|---|---|
|2100 MHz|B1|2142|34|18300|
|1800 MHz|B3|1844.5|44|19575|
|850 MHz|B5|883.5|45|20525|
|800 MHz|B18|869.5|54|23925|
|800 MHz|B19|884.5|55|24075|


a. Limited availability.

b. Receive frequencies shown are 2 MHz offset from center.

c. Channel values shown are at the center of the corresponding bands.


To test the DUT’s receive path (or diversity path, while connected to the diversity antenna):


_Note: This procedure describes steps using the Agilent 8648C signal generator—the Rohde & Schwarz SML03 is shown for reference_
_only._


Rev. 16 March 2025 153 41113440


Testing


**1.** Set up the signal generator:


**a.** Set the amplitude to -70 dBm


**b.** Set the frequency for the band being tested. See Table 12-11 on page 152 for frequency values.


**2.** Set up the DUT:


**a.** **AT!ENTERCND=”<password>”** (Unlock extended AT command set.)
**b.** **AT!DAFTMACT** (Put modem into factory test mode.)
**c.** **AT!DASBAND=<band>** (Set frequency band.)


See tables Table 12-11 on page 152 for <band> values
**d.** **AT!DALSRXBW=2** (Set Rx LTE bandwidth to 5MHz.)
**e.** **AT!DALSTXBW=2** (Set Tx LTE bandwidth to 5MHz.)
**f.** **AT!DASCHAN=<channel>** (Set modem channel)

**·** See tables Table 12-11 on page 152 for <channel> values


**g.** **AT!DALGAVGAGC=<channel>,0** (Get averaged Rx AGC)

**·** See tables Table 12-11 on page 152 for <channel> values


**3.** Test limits—Run ten or more good DUTs through this test procedure to obtain a nominal received power value.

**·** Apply a tolerance of  5 to 6 dB to each measurement (assuming a good setup design).

**·**
Make sure the measurement is made at a high enough level that it is not influenced by DUT-generated and
ambient noise.

**·**
The Signal Generator power level can be adjusted and new limits found if the radiated test needs greater
signal strength.

**·**
Monitor these limits during mass-production ramp-up to determine if further adjustments are needed.


_Note: The value measured from the DUT is significantly influenced by the test setup and DUT design (host RF cabling loss, antenna_
_efficiency and pattern, test antenna efficiency and pattern, and choice of shield box)._

##### **12.8 GNSS RF Receive Path Test**


The GNSS receive path uses the dedicated GNSS connector.


To test the GNSS receive path:


**1.** Inject a carrier signal at -110dBm, frequency 1575.52 MHz into the GNSS Rx path at the connector. (Note that
this frequency is 100 kHz higher than the actual GPS L1 center frequency.)


Rev. 16 March 2025 154 41113440


Product Technical Specification


**2.** Test the signal carrier-to-noise level at the GNSS receiver:


**a.** **AT!ENTERCND=”<password>”** (Unlock extended AT command set.)


**b.** **AT!DAFTMACT** (Put modem into factory test mode.)


**c.** **AT!DACGPSTESTMODE=1** (Start CGPS diagnostic task.)


**d.** **AT!DACGPSSTANDALONE=1** (Enter standalone RF mode.)


**e.** **AT!DACGPSMASKON** (Enable log mask.)


**f.** **AT!DACGPSCTON** (Return signal-to-noise and frequency measurements.)


**g.** Repeat **AT!DACGPSCTON** five to ten times to ensure the measurements are repeatable and stable.


**3.** Leave the RF connection to the embedded module intact, and turn off the signal generator.


**4.** Take several more **!DACGPSCTON** readings. This will demonstrate a 'bad' signal in order to set limits for testing,
if needed. This frequency offset should fall outside of the guidelines in the note below, which indicates that the
CtoN result is invalid.


**5.** (Optional) Turn the signal generator on again, and reduce the level to -120dBm. Take more **!DACGPSCTON**
readings and use these as a reference for what a marginal/poor signal would be.


_Note: The response to_ _**AT!DACGPSCTON**_ _for a good connection should show CtoN within 58 +/- 5dB and Freq (frequency offset) within_

_100000 Hz +/- 5000 Hz._


Rev. 16 March 2025 155 41113440


## **A**
### **A: Appendix**

For more details, several references can be consulted, as detailed below.

##### **A.1 Web Site Support**


[Check http://source.sierrawireless.com for the latest documentation available.](http://source.sierrawireless.com)

##### **A.2 Reference Documents**


**[1]** RC76xx AT Command Reference

Reference number: 41113566


**[2]** RC76xx Scalability Guide

Reference number: 41113646


**[3]** RC76xx Customer Process Guidelines

Reference number: 41113573


**[4]** Inter-Chip USB Supplement to the USB 2.0 Specification Revision 1.0


**[5]** I [2] C Bus Specification, Version 5.0, October 2012

Reference: Phillips Semiconductor document number 9398 393 40011

##### **A.3 Abbreviations**






|Acronym or Term|Definition|
|---|---|
|3GPP|3rd Generation Partnership Project|
|8PSK|Octagonal Phase Shift Keying|
|ADC|Analog to Digital Converter|
|AF|Audio-Frequency|
|API|Application Programming Interface|
|AT|Attention (prefix for modem commands)|
|BeiDou|BeiDou Navigation Satellite System<br>A Chinese system that uses a series of satellites in geostationary and middle earth orbits to<br>provide navigational data.|
|BER|Bit Error Rate—A measure of receive sensitivity|
|BLER|Block Error Rate|
|Bluetooth|Wireless protocol for data exchange over short distances|
|CEP<br>CEP-##|Circular Error Probability—Measure of GPS horizontal accuracy indicating the radius of a circle<br>around the actual position that contains 50% of GPS measurements.<br>CEP-##—Radius of circle containing ##% of GPS measurements (e.g. CEP-90 indicates 90% of<br>measurements contained within circle)|



Rev. 16 March 2025 156 41113440


DocTitleHeader

|Acronym or Term|Definition|
|---|---|
|CF3|Common Flexible Form Factor|
|CLK|Clock|
|CMOS|Complementary Metal Oxide Semiconductor|
|CPU|Central Processing Unit|
|CQI|Channel Quality Indication|
|CS|Circuit-Switched|
|CS|Coding Scheme|
|CTS|Clear To Send|
|CW|Continuous waveform|
|DAC|Digital to Analog Converter|
|dB|Decibel = 10 x log10 (P1/P2)<br>_P1 is calculated power; P2 is reference power_<br>Decibel = 20 x log10 (V1/V2)<br>_V1 is calculated voltage, V2 is reference voltage_|
|dBm|A logarithmic (base 10) measure of relative power (dB for decibels); relative to milliwatts (m). A<br>dBm value will be 30 units (1000 times) larger (less negative) than a dBW value, because of the<br>difference in scale (milliwatts vs. watts).|
|DC|Direct Current|
|DCD|Data Carrier Detect|
|DCS|Digital Cellular System<br>A cellular communication infrastructure that uses the 1.8 GHz radio spectrum.|
|DL|Downlink (network to mobile)|
|DRX|Discontinuous Reception|
|DSR|Data Set Ready|
|DSSS|Dual SIM Single Standby|
|DTR|Data Terminal Ready|
|eDRX|Extended Discontinuous Reception|
|E-GSM|Extended GSM|
|EDGE|Enhance Data rates for GSM Evolution|
|EFR|Enhanced Full Rate|
|EGPRS|Enhance GPRS|
|EIRP|Effective (or Equivalent) Isotropic Radiated Power|
|EMC|Electromagnetic Compatibility|
|EN|Enable|



Rev. 16 March 2025 157 41113440


|Acronym or Term|Definition|
|---|---|
|ERP|Effective Radiated Power|
|ESD|Electrostatic Discharges|
|eSIM|Embedded SIM|
|ETSI|European Telecommunications Standards Institute|
|FCC|Federal Communications Commission<br>The U.S. federal agency that is responsible for interstate and foreign communications. The FCC<br>regulates commercial and private radio spectrum management, sets rates for communications<br>services, determines standards for equipment, and controls broadcast licensing. Consult<br>www.fcc.gov.|
|FDD|Frequency Division Duplex|
|FDMA|Frequency Division Multiple Access|
|firmware|Software stored in ROM or EEPROM; essential programs that remain even when the system is<br>turned off. Firmware is easier to change than hardware but more permanent than software<br>stored on disk.|
|FOV|Field Of View|
|FR|Full Rate|
|FSN|Factory Serial Number—A unique serial number assigned to the module during manufacturing.|
|Galileo|A European system that uses a series of satellites in middle earth orbit to provide navigational<br>data.|
|GCF|Global Certification Forum|
|GLONASS|Global Navigation Satellite System—A Russian system that uses a series of 24 satellites in<br>middle circular orbit to provide navigational data.|
|GMSK|Gaussian Minimum Shift Keying modulation|
|GND|Ground|
|GNSS|Global Navigation Satellite Systems (GPS, GLONASS, BeiDou, Galileo, and QZSS)|
|GPIO|General Purpose Input Output|
|GPRS|General Packet Radio Service|
|GPS|Global Positioning System<br>An American system that uses a series of 24 satellites in middle circular orbit to provide<br>navigational data.|
|GSM|Global System for Mobile communications|
|Hi Z|High impedance (Z)|
|Host|The device into which an embedded module is integrated|
|HR|Half Rate|
|HSDPA|High Speed Downlink Packet Access|
|HSUPA|High Speed Uplink Packet Access|


Rev. 16 March 2025 158 41113440


DocTitleHeader







|Acronym or Term|Definition|
|---|---|
|Hz|Hertz = 1 cycle/second|
|I/O|Input/Output|
|IC<br>IC|Industry Canada|
|IC<br>IC|Integrated Circuit|
|I-eDRX|Idle mode eDRX|
|IMEI|International Mobile Equipment Identity|
|IMS|IP Multimedia Subsystem—Architectural framework for delivering IP multimedia services.|
|inrush current|Peak current drawn when a device is connected or powered on|
|IOT|Interoperability Testing|
|IS|Interim Standard.<br>After receiving industry consensus, the TIA forwards the standard to ANSI for approval.|
|ISIM|IMS Subscriber Identity Module.|
|LED|Light Emitting Diode.<br>A semiconductor diode that emits visible or infrared light.|
|LGA|Land Grid Array|
|LHCP|Left-Hand Circular Polarized|
|LNA|Low noise Amplifier|
|LTE|Long Term Evolution—a high-performance air interface for cellular mobile communication<br>systems.|
|MAX|Maximum|
|MCS|Modulation and Coding Scheme|
|MHz|Megahertz = 106 Hz|
|MIC|Microphone|
|MIMO|Multiple Input Multiple Output—wireless antenna technology that uses multiple antennas at<br>both transmitter and receiver side. This improves performance.|
|MIN|Minimum|
|MO|Mobile Originated|
|MT|Mobile Terminated|
|N/A|Not Applicable|
|NMEA|National Marine Electronics Association|
|NOM|Nominal|
|OEM|Original Equipment Manufacturer—a company that manufactures a product and sells it to a<br>reseller.|
|OTA|Over the Air Technology|


Rev. 16 March 2025 159 41113440


|Acronym or Term|Definition|
|---|---|
|PA|Power Amplifier|
|packet|A short, fixed-length block of data, including a header, that is transmitted as a unit in a<br>communications network.|
|PBCCH|Packet Broadcast Control Channel|
|PC|Personal Computer|
|PCB|Printed Circuit Board|
|PCL|Power Control Level|
|PCS|Personal Communication System<br>A cellular communication infrastructure that uses the 1.9 GHz radio spectrum.|
|PDN|Packet Data Network|
|PFM|Power Frequency Modulation|
|PLL|Phase Lock Loop|
|PMIC|Power Management Integrated Circuit|
|PSM|Power Saving Mode|
|PSS|Primary synchronization signal|
|PST|Product Support Tools|
|PTCRB|PCS Type Certification Review Board|
|PWM|Pulse Width Modulation|
|QAM|Quadrature Amplitude Modulation.<br>This form of modulation uses amplitude, frequency, and phase to transfer data on the carrier<br>wave.|
|QPSK|Quadrature Phase-Shift Keying|
|QZSS|Quasi-Zenith Satellite System|
|R2C|Ready-To-Connect|
|RAM|Random Access Memory|
|RAT|Radio Access Technology|
|RF|Radio Frequency|
|RHCP|Right Hand Circular Polarization|
|RI|Ring Indicator|
|RSE|Radiated Spurious Emissions|
|RSSI|Received Signal Strength Indication|
|RST|Reset|
|RTC|Real Time Clock|


Rev. 16 March 2025 160 41113440


DocTitleHeader

|Acronym or Term|Definition|
|---|---|
|RTS|Request To Send|
|RX|Receive|
|SCLK|Serial Clock|
|SED|Smart Error Detection|
|Sensitivity (Audio)|Measure of lowest power signal that the receiver can measure.|
|Sensitivity (RF)|Measure of lowest power signal at the receiver input that can provide a prescribed BER/BLER/<br>SNR value at the receiver output.|
|SIM|Subscriber Identity Module.|
|SIMO|Single Input Multiple Output—Wireless antenna technology that uses multiple antennas at the<br>receiver side and one antenna at the source (transmitter).|
|SKU|Stock Keeping Unit—identifies an inventory item: a unique code, consisting of numbers or letters<br>and numbers, assigned to a product by a retailer for purposes of identification and inventory<br>control.|
|SMS|Short Message Service|
|SNR|Signal-to-Noise Ratio|
|SPI|Serial Peripheral Interface|
|SPK|Speaker|
|SW|Software|
|TBC|To Be Confirmed|
|TBD|To Be Determined|
|TDD|Time Division Duplex|
|TIA/EIA|Telecommunications Industry Association / Electronics Industry Association.<br>A standards setting trade organization, whose members provide communications and<br>information technology products, systems, distribution services and professional services in the<br>United States and around the world. Consultwww.tiaonline.org.|
|TIS|Total Isotropic Sensitivity|
|TP|Test Point|
|TRP|Total Radiated Power|
|TX|Transmit|
|TYP|Typical|
|UART|Universal Asynchronous Receiver-Transmitter|
|UE|User Equipment|
|UICC|Universal Integrated Circuit Card|
|UIM|User Identity Module. Generic term used in this document to refer to UICC, where the application<br>on the UICC (USIM, ISIM, CSIM, etc.) varies depending on the provider of the card.|



Rev. 16 March 2025 161 41113440


|Acronym or Term|Definition|
|---|---|
|UL|Uplink (mobile to network)|
|UMTS|Universal Mobile Telecommunications System|
|USB|Universal Serial Bus|
|USB-SS|USB Selective Suspend/USB not enumerated|
|USIM|Universal Subscriber Identity Module (UMTS)|
|USSD|Unstructured Supplementary Services Data|
|UTRA|UMTS Terrestrial Radio Access|
|VBATT|VBATT is a virtual signal that represents both VBAT_BB and VBAT_RF|
|VBAT_BB|Baseband power supply|
|VBAT_RF|RF power supply|
|VCC|Supply voltage|
|VSWR|Voltage Standing Wave Ratio|
|WCDMA|Wideband Code Division Multiple Access (also referred to as UMTS)|
|WLAN|Wireless Local Area Network|
|WWAN|Wireless Wide Area Network|
|ZIF|Zero Intermediate Frequency|


Rev. 16 March 2025 162 41113440


