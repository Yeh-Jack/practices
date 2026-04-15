# --- Read XML file.
import os, random
import xml.etree.ElementTree as ET

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

path = "./data/xml/"
root = ET.parse(path + "宜蘭縣停車場.xml").getroot()

for row in root.findall("row_item"):
    data = []
    for col in ["名稱", "編號", "小車位總數", "小車位剩餘數"]:
        data.append(row.find(col).text)
    print(f"{data[0]}({data[1]})\t小車位數 = {data[3]} / {data[2]}")

    # --- Append a tag with attributes to the row.
    # Method 1: by Element()
    grade = ET.Element("grade", {"team": "apple", "level": "2"})
    grade.text = "A"
    row.append(grade)
    #  Method 2: by SubElement()
    ET.SubElement(row, "score", {"max": "120", "min": "60"}).text = str(
        random.randint(50, 120)
    )
    for tag in row.iter():
        print(f"\t{tag.tag} = {tag.text}")
