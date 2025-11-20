# Given the lengths of semi-major axis A and semi-minor axis B of an ellipse, calculate the Area
#  of the Ellipse.
#  Area of ellipse having semi-major axis length a and semi-minor axis length b is given by π * a * b.
def ellipse(A, B):
    return 3.14 * A * B
print(ellipse(5, 3))  