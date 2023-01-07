def bisection_zero(f_x, a_0, b_0): 
    """
-------------------------------------------------------
Finds one zero of the polynomial by using the bisection method.
Use: zero_f = bisection_zero(f_x,a_0,b_0)
-------------------------------------------------------
Parameters:   
f_x - a polynomial function (list)
a_0 - a test point with f(a_0) < 0 (float)
b_0 - a test point with f(b_0) > 0 (float)
Returns:
zero_f - a zero of the polynomial f(zero_f) = 0 (float)
-------------------------------------------------------
"""
    f_a = (compute_value(f_x, a_0))
    f_b = (compute_value(f_x, b_0))

    #We want f_a to be larger than f_b. This if statement swaps the values to meet this condition
    if f_a < f_b:
        f_a, f_b, a_0, b_0 = f_b, f_a, b_0, a_0

    m = (a_0 + b_0)/2
    f_m = compute_value(f_x, m)
    if f_a*f_b > 0:
        return "The function may not have a root on this interval, because the endpoints of the interval are the same polarity"
    elif f_a == 0:
        return "The root is: " + str(a_0)
    elif f_b == 0:
        return "The root is: " + str(b_0)
    elif f_m == 0:
        return "the root is: " + str(m)
    else:
        while f_a > 0 and f_b < 0 and abs(f_m) > 1e-11:
            if f_m > 0:
                a_0 = m
            elif f_m < 0:
                b_0 = m
            m = (a_0+ b_0)/2
            f_m = compute_value(f_x, m)
        return "The root is approximately: " + str(m)


def compute_value(f_x, x):
    """
    -------------------------------------------------------
    Computes the value of a polynomial f with respect to x
    Use: f_val = compute_value(f_x, x)
    -------------------------------------------------------
    Parameters:
    f_x - a polynomial function (list)
    x - an x value (float)
    Returns:
    f_val - y value of the function with respect to x (float)
    -------------------------------------------------------
    """
    #note: let x be the value you are inputting into the function
    n = len(f_x)-1 #this is the degree of the polynomial
    f_val = f_x[0]*x**(n) #initialize
    for i in range(1,n+1): #watch indices
        f_val += f_x[i]*(x**(n-i)) #sum each remaining term
    return f_val

# Test cases:
def main():
    print(bisection_zero([1, -7, 10], 1, 4))
    print(bisection_zero([2,-13,22,-8], -1, 1.5))
    print(bisection_zero([8,0,0,-1], -1, 3))
    print(bisection_zero([2, 0, 2], -12, 5))
    print(bisection_zero([1, 0, -1], -1, 1))

if __name__ == "__main__":
    main()