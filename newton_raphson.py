# f(x) = x^4−3x^3+2

# From calculation, it is expected that the local minimum occurs at x=9/4

def df1(x):
    return 12 * x**2 - 18 * x
    
def df(x):
    return 4 * x**3 - 9 * x**2

# newton method

cur_x = 6 # The algorithm starts at x=6
# if setting cur_x = 1, algorithm will converge to another solution: 0
precision = 0.00001
previous_step_size = 1
n = 0

while previous_step_size > precision:
    prev_x = cur_x
    cur_x += - 1.0 * df(prev_x)/df1(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    n += 1
    print((cur_x,n,previous_step_size))
