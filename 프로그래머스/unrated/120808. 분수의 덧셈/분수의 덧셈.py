import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    n = numer1*denom2 + numer2*denom1
    d = denom1*denom2
    g = math.gcd(n,d)
    return [n//g, d//g]