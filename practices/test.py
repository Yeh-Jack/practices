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
