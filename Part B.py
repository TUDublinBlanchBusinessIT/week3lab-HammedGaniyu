#Hammed Ganiyu
#17/02/2025
#Part B 

from divisors import divisors
def isperfectNumber(n):
    if sum (divisors(n)) == n:
        return True
        return False

print(isperfectNumber(496))
if isperfectNumber(496):
    print("It is a perfect Number")

