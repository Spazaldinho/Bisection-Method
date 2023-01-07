# Bisection-Method

A polynomial function takes the form f(x) = c_nx^n+c_{n-1}x^{n-1}+...+c^1x + c_0 where each c_i is some real number. Finding the zeros of a function is an important concept in calculus. In high school, you may have learned methods of factoring to find the zeros of quadratic and cubic functions. However, there are more algorithms to determine the zeros numerically. 

The degree of a polynomial function is the largest n where c_nx^n is present in the function, and c_n is not zero. For example 3x^3- 7x^2+ x-11 is degree 3 and 4x^7-9 is degree 7.

In python we can store a polynomial function as a list, where each element of the list is a coefficient of the polynomial, making sure to include any zero coefficients when necessary. The degree of the polynomial function is the length of the list. For example 

f(x) = c_nx^n+c_{n-1}x^{n-1}+...+c_1x + c_0 is stored as [c_n, c_{n-1}, ..., c_1, c_0], similarly 3x^3- 7x^2+ x-11 is stored as [3, -7, 1, -11] and 

4x^7-9 is stored as  [4, 0, 0, 0, 0, 0, 0, -9]




The Bisection Method - Algorithm
We must first find, a polynomial function f(x), and two points a_0, b_0 such that f(a_0) > 0 and f(b_0) < 0. That is, one value is negative and one value is positive. It must be true that the function f(x) takes on a value of zero somewhere in between the two values a_0, b_0, since polynomial functions are continuous (the notion of continuous functions is beyond the scope of this course).

Input: polynomial function f(x)  and two points  a_i, b_i.

Find the midpoint between  ai, bi, call it mi

Calculate f(m_i). This value will be either negative f(m_i) < 0   or positive f(m_i) > 0

To find a_{i+1}, b{i+1} use m_i and either a_i or b_i so that f(a_{i+1}) < 0 and f(b_{i+1}) > 0. That is, we find two new points, one of which must be the midpoint, so that the two new values are on either side of 0, with one being positive and the other being negative

Stop when f(m_i) = 0

This algorithm will find precisely one zero, and requires that we begin out calculations with a positive and negative value. Furthermore, ai, bi may themselves be any sign (positive or negative), we are checking that the polynomial function takes on positive or negative values with these inputs.

Note: we use the term “polynomial function” to discuss the f(x) in the question, and we will use the term “python function” when referencing any function in the code.

The Requirements
Implement the bisection algorithm for finding zeros of polynomial functions as a python function.

You must take the polynomial function, and two values as input

You must return ONE zero of the polynomial function. [Note: you do NOT need to find all zeros]

You may hardcode functions and test points, but they must enter the python function as parameters

Test your code appropriately, and include the output in your testing.txt file.




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

Computing the value of the function is not a learning outcome for this course. You are welcome to implement this any way that you choose. If you are having trouble, you may use the following code snippet to compute your functions from the list:

#note: let x be the value you are inputting into the function

n = len(f_x)-1 #this is the degree of the polynomial

f_val = f_x[0]*x**(n) #initialize

for i in range(1,n+1): #watch indices

f_val += f_x[i]*(x**(n-i)) #sum each remaining term
