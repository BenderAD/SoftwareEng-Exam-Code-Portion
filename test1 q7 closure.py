# Closure Example for Question 7 of Programming Languages Test 1
# Alex Bender

def begin(a):
    def multiplyBySeven():
        
            print (a * 7)

    return multiplyBySeven

varSum1 = begin(12)
varSum1()

varSum2 = begin(70)
varSum2()
