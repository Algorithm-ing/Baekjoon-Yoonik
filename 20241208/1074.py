N,r,c=map(int, input().split())
x=0
def z(current_length,r,c):
    global x
    if current_length<=1:return
    next_length = current_length//2
    if r<next_length and c>=next_length: x+=next_length**2
    if r>=next_length and c<next_length: x+=2*next_length**2
    if r>=next_length and c>=next_length: x+=3*next_length**2
    z(next_length,r%next_length,c%next_length)
z(2**N,r,c)
print(x)