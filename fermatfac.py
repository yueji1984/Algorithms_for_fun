# Fermat’s Factorization Method, 
# Named after Pierre de Fermat 
# A factorization method for odd numbers n based on the representation of an odd integer as the difference of two squares	 
# n = a^2 - b^2 = (a + b) (a - b)	and if neither of the two factors (a + b) and (a – b) equals to 1, then this is a proper factorization of n.

# The Fermat factorization of odd numbers follows the following steps:
# 1)	Find the smallest integer t >= sqrt(n) 
# 2)	Consider the sequence of numbers t^2 - n, (t+1)^2 - n, ..., ((n+1)/2)^2 - n, 
#     stopping when a square p = (t + k)^2 - n is found.
# 3)	Let q = t + k, then we have n = (q - p)(q + p) which is a factorization of n.
