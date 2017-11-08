from PIL import Image
import sys

import pyocr
import pyocr.builders

import sys

tools = pyocr.get_available_tools()

if len(tools) == 0:
    print("Not found OCR tool")
    sys.exit(1)

tool = tools[0]
print("Will use tool: '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: '%s'" % ", ".join(langs))
print("Will use lang '%s'" % ("chi_sim"))

txt = tool.image_to_string(
    Image.open('images/jjj.jpg'),
    lang='chi_sim',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print(txt)
