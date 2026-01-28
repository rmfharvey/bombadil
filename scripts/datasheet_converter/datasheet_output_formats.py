import os
from bombadil.utils.datasheet_parser.datasheet_converter import MicroDatasheetConverter, DatasheetConverter
from bombadil import global_logger

logger = global_logger


dir_names = [
    # ("spc56ec74", MicroDatasheetConverter),
    # ("stm32f103", MicroDatasheetConverter),
    # ("stm32g431c6", MicroDatasheetConverter),
    # ("stm32g474", MicroDatasheetConverter),
    # ("stm32h730", MicroDatasheetConverter),
    # ("stm32h723", MicroDatasheetConverter),
    ("stm32h743", MicroDatasheetConverter),
    # ("tps1htc30", DatasheetConverter),
    # ("bq25756", DatasheetConverter),
    # ("rc7611_old", DatasheetConverter),
    # ("vnf1048f", DatasheetConverter),
    # ("icm-20948", DatasheetConverter),
    # ("ncv78703", DatasheetConverter),
    # ("tps92520", DatasheetConverter),
    # ("dp83tg720", DatasheetConverter),
]

_root = os.path.dirname(__file__)

for dir_name, cls in dir_names:
    dir_path = os.path.join(_root, dir_name)

    src_contents = {fn: os.path.join(dir_path, fn) for fn in os.listdir(dir_path)}
    ds_pdf = src_contents.get("datasheet.pdf")
    ds_md = src_contents.get("datasheet.md")

    ds = ds_md if ds_md else ds_pdf

    ds = cls(source_path=ds, output_directory=dir_path)
    ds.update_config(os.path.join(dir_path, "datasheet.json"))
    # ds.save_config(os.path.join(dir_path, "datasheet.json"))
    print()
print()
