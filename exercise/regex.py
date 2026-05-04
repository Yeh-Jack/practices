import re

text = "123456DEFAB89CDEFG ABCDE12,345 XYZ12345"
pattern1 = re.compile(r"^.{2}|[XY]{2}")
print(" ".join(pattern1.findall(text)))

pattern2 = re.compile(r"\b[A-C]{3}|[X-Z]{3}[12]{2}")
print(" ".join(pattern2.findall(text)))

pattern3 = re.compile(r"\d{2}[D-F]{3}|B[89]{2}..|[C-E]{3}\d{2}")
print(" ".join(pattern3.findall(text)))
