# Datasheet Ingester Memory

## JSON Schema Patterns
- No `example_datasheet.json` files exist in the repo; use existing `datasheet.json` files as reference
- Good references: `lmr38025sdrrr` (buck regulator), `tps22917dbvr` (load switch), `bq25756` (charger with I2C)
- `high_level.device_type` uses strings like "REGULATOR_BUCK", "HIGH_SIDE_DRIVER", "OSCILLATOR"
- `high_level.serial_busses` uses strings like "I2C", "PMBus"
- Pins with multiple pin numbers: use comma-separated string e.g. "1, 2, 3, 34"
- NC pins with different pin numbers: use unique keys like "NC_8", "NC_9", "NC_10"
- `serial_bus.registers` follows PMBus/I2C command map with address, type, data_format, default_value, description, fields

## Device-Type Specific Patterns
- **EEPROM devices**: Use `serial_bus.memory_organization` for size/page/endurance info, `serial_bus.slave_address` for I2C addressing, `serial_bus.write_operations`/`read_operations` for protocol details. `serial_bus.registers` is empty `{}` since EEPROMs are pure memory (no control registers). Device type string: "EEPROM"
- CAT24C01/02/04/08/16: shared onsemi datasheet family. CAT24C16 uses all address bits internally (no external A0/A1/A2); pins 1-3 are NC. Slave address range 0x50-0x57 for block selection.
- **USB-to-UART bridges** (e.g., FTDI FT231X): No traditional serial bus registers. MTP memory configured over USB via FT_PROG utility. `serial_bus` is empty `{}`. Device type: "USB_TO_UART". QFN package has exposed pad (pin 21) for ground/thermal.
- For devices with dual GND pins, use unique keys like "GND_3", "GND_13" with pin_id matching the pin number.
- **Power monitors (INA family)**: Use `ina236aiddfr` as gold reference for INA2xx family. INA238 adds VBUS pin, temp sensor, CONVDLY, SLOWALERT vs INA236. Device type: "POWER_MONITOR". POWER register is 24-bit. Reset values from header e.g. "[reset = FB68h]". Note INA238 register addresses skip 3,9,10 (reserved).

## Manufacturer URL Patterns
- **Vishay**: `https://www.vishay.com/docs/{doc_number}/{part_family}.pdf` (e.g., 77863/sic450_sic451_sic453.pdf)
- **TI**: `https://www.ti.com/lit/ds/symlink/{part}.pdf`
- **onsemi**: `https://www.onsemi.com/pdf/datasheet/{family}-d.pdf` (e.g., cat24c01-d.pdf covers CAT24C02/04/08/16); also try `https://www.onsemi.com/download/data-sheet/pdf/{family}-d.pdf`
- **FTDI**: `https://ftdichip.com/wp-content/uploads/2021/10/DS_{part_family}.pdf` (e.g., DS_FT231X.pdf)
- **Analog Devices (ADI/Linear)**: `https://www.analog.com/media/en/technical-documentation/data-sheets/{part_family}.pdf` (e.g., ltc4372-4373.pdf, ltc7890.pdf). Note: analog.com blocks default Python requests User-Agent; must use browser-like User-Agent header. Standard requests.get() with default UA returns empty or error.
- **Realtek**: Not hosted on realtek.com for public download. Use GitHub repos (e.g., `https://github.com/libc0607/Realtek_switch_hacking/raw/files/{part}_Datasheet.pdf`) or LCSC (`https://datasheet.lcsc.com/lcsc/...`). LCSC URLs often block plain requests.get() without headers.

## Conversion Notes
- pymupdf4llm works well for most datasheets; tables are converted to markdown pipe format
- Vishay datasheets: pin tables parse cleanly, PMBus command tables are readable but verbose
- SiC45x family (SiC450/451/453): shared datasheet, 34-pin MLP package, PMBus 1.3, ~66 registers
- onsemi CAT24Cxx datasheets: pin tables and electrical characteristics parse cleanly; timing diagrams render as fragmented text (not useful for parsing)
- **Ideal diode controllers** (LTC4372, LM5050): Use `lm5050` as reference. Device type: "IDEAL_DIODE_CONTROLLER". No serial bus. `serial_bus` contains a note string. Include `application_info` with mosfet_selection_guidelines, design_configurations. LTC4372 has DD (DFN) and MS8 (MSOP) packages; DFN has exposed pad (pin 9, optional GND). LTC4372/LTC4373 share a datasheet.
- **Oscillators** (LTC6908): Device type: "OSCILLATOR". No serial bus; `serial_bus.registers` is empty `{}`. Three-state MOD pin (GND/FLOAT/V+) for SSFM config. DCB package pin order: SET(1), V+(2), GND(3), OUT1(4), OUT2(5), MOD(6), EXPOSED_PAD(7). LTC6908-1 = complementary outputs, LTC6908-2 = quadrature outputs.
- **I/O Expanders** (TCA9535): Device type: "IO_EXPANDER". Use `serial_bus` with type/base_address/address_pins/address_range/max_clock_frequency_kHz. Registers are simple 8-bit per-port (input/output/polarity/config). Fields are individual bits (64 total for 16-bit expander). Pin numbers use TSSOP-24 (PW) package pinout. TCA9535 has no internal pull-ups (unlike TCA9555). I2C base address 0x20, 3 hardware address pins (A0-A2).
- **DC-DC controllers** (LTC7890): Device type: "CONTROLLER_BUCK". No serial bus; `serial_bus.registers` is empty `{}`. Split gate drivers (TGUP/TGDN/BGUP/BGDN) have absolute max warning: "Do not apply a voltage or current source; capacitive loads only." GaN FET controllers have smart bootstrap and dead time control pins. Pin count can be high (40-pin QFN with exposed pad = 41 pins).
- **Ethernet switches** (RTL8367S): Device type: "ETHERNET_SWITCH". 128-pin LQFP. Multi-function pins with GPIO/RGMII/MII/SPI/UART overlays -- use composite key names (e.g. "GPIO01_RG2_TXD3"). Serial bus is PCS PHY registers (IEEE 802.3 standard registers 0-15) accessed via SMI/MDIO. Strapping pins configure EEPROM mode, 8051 enable, SPI flash, EEE, PHY enable, management interface selection. Internal switching regulator (EN_SWR/LX/HV_SWR) generates 1.1V from 3.3V. 40 MDI pins across 5 PHY ports (8 per port: 4 differential pairs).
- **Battery chargers** (BQ25756): Device type: "CHARGER_BUCK_BOOST". Register keys use decimal address strings ("0", "2", "6" etc.). Register fields stored as list (not dict) in `serial_bus.fields`. Registers have: address, bit_width, init_value, name, description, optional read_only. Fields have: name, description, register_location (list of {register_address, reg_start_bit, reg_end_bit, field_start_bit, field_end_bit}), optional reserved, digital_physical_map. 42 registers, 182 fields, 37 pins. VQFN-36 package with exposed thermal pad (pin 37). I2C address 0x6B. Reset values stored as decimal integers (e.g., 0x0010 stored as 16).
