#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "xmltodict",
# ]
# ///

from pathlib import Path
import xmltodict
import json

here = Path(__file__).parent
xml_file = here / "063_PFB1/course/course.xml"
json_file = here / "course.json"
json_file.write_text(json.dumps(xmltodict.parse(xml_file.read_text()), indent=4))
print(f"Json written to {json_file=}")
