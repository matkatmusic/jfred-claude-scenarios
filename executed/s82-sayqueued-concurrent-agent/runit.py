from base import inc

result = inc(41)
double = inc(inc(41))
print(result)
print(double)

with open("out.txt", "w") as f:
    f.write(str(result))
