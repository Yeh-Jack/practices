# Basic mathmatical calculation.
PI = 3.14159
r = 5
area = PI * r * r

print(
    "r = %d\tarea of the circle = %f\ndimension = %d\tlength = %f"
    % (r, area, 2 * r, 2 * PI * r)
)
print("PI = %s\tr = %s\tarea = %s" % (type(PI), type(r), type(area)), end="\n\n")

# # Input and output.
inp = input("Input a value : ")
inpVal = eval(inp)
print(
    "Your input is %s, and type of your input is %s.\nDigit : %f"
    % (inp, type(inpVal), inpVal)
)
