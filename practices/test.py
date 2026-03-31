SKIP_ONE_LINE = "\n\n"

# Basic mathmatical calculation.
PI = 3.14159
r = 5
area = PI * r * r

print(
    "r = %d\tarea of the circle = %f\ndimension = %d\tlength = %f"
    % (r, area, 2 * r, 2 * PI * r)
)
print("PI = %s\tr = %s\tarea = %s" % (type(PI), type(r), type(area)), end=SKIP_ONE_LINE)

# # Input and output.
# inp = input("Input a value : ")
# inpVal = eval(inp)
# print(
#     "Your input is %s, and type of your input is %s.\nDigit : %f"
#     % (inp, type(inpVal), inpVal)
# )

# Reverse a string.
string = "Hello world!"
print(string[::-1], end=SKIP_ONE_LINE)

# String mainuplation.
parts = string.split()
print(f"type of parts = {type(parts)}, parts = {parts}")

join = "_".join(parts)
print(f"Joined string = {join}", end=SKIP_ONE_LINE)

org = "Hello"
to = "Hi,"
print(f"Replace '{org}' by '{to}' -> {string.replace(org, to)}", end=SKIP_ONE_LINE)

# String encoding and decoding.
string = "一二三四五 on the original Unicode."
utf8 = string.encode()
big5 = string.encode(encoding="big5")
print(f"Original string = [{string}]")
print(f"Encode it to UTF-8 = {utf8}")
print(f"Encode it to BIG-5 = {big5}")
print(f"Decode UTF-8 to UTF-8 = {utf8.decode(encoding="utf8")}")
# UnicodeDecodeError: codec can't decode
# print(f"Decode UTF-8 to BIG-5 = {utf8.decode(encoding="big5")}")
# print(f"Decode BIG-5 to UTF-8 = {big5.decode(encoding="utf8")}")
print(f"Decode BIG-5 to BIG-5 = {big5.decode(encoding="big5")}", end=SKIP_ONE_LINE)

# Numeric testing.
nums = ["77", " 77", "７７", "七七", "77.77", "+77.77", "-77"]
for num in nums:
    print(
        f"Testing .. [{num}] ->\tisDigital = {num.isdigit()}\tisDecimal = {num.isdecimal()}\tisNumeric = {num.isnumeric()}"
    )
print()

# Control flow.
score = eval(input("Please input a score : "))
if score < 0 or score > 100:
    print(f"Invalid score number [{score}].")
elif score >= 90:
    print(f"[{score}] is excellent.")
elif score >= 80:
    print(f"[{score}] is great.")
elif score >= 70:
    print(f"[{score}] is good.")
elif score >= 60:
    print(f"[{score}] is fine.")
else:
    print(f"[{score}] is unsatisfied.")
