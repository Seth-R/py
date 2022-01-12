"kata: RGB To Hex Conversion"
"The rgb function is incomplete. Complete it so that passing in RGB decimal values "
"will result in a hexadecimal representation being returned. Valid decimal values for "
"RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value."

"Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here."
"The following are examples of expected output values:"
# rgb"(255, 255, 255)  returns FFFFFF
# rgb"(255, 255, 300)  returns FFFFFF
# rgb"(0,0,0)  returns 000000
# rgb"(148, 0, 211)  returns 9400D3

def rgb(r, g, b):

    rgb = []

    if int(r) > 255:
        r = 255
    if int(r)<0:
        r=0

    if int(g) >255:
        g=255
    if int(g)<0:
        g=0

    if int(b) > 255:
        b=255
    if int(b)<0:
        b=0
    
    r = format(r, "X")
    g = format(g, "X")
    b = format(b, "X")
    rgb = [r.zfill(2), g.zfill(2), b.zfill(2)]
    return "".join(rgb)

print(rgb(r = -20, g = 257, b = 125))