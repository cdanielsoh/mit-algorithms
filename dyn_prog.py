
def fib_recurse(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_recurse(n-1) + fib_recurse(n-2)
        
def fib_dynprog(n):
    fib_list = [1,1]
    if n <= 2:
        return fib_list[n]
    else:
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list.pop()

def srtbot_bowling(v):
    # Subprobs: B(i)=max_score_possible
    # Original: B(0)
    # Relate: B(i) = max(B(i+1), B(i+1) + v[i], B(i+2) + v[i]*v[i+1])
    # Topological order: decreasing i -> for i=n,n-1,...,0
    # Base: B(n) = 0
    # Time: O(n)
    memo = {}
    v.append(0)
    def B(i):
        if i >= len(v)-1: return 0
        if i not in memo:
            memo[i] = max(B(i+1), v[i] + B(i+1), v[i]*v[i+1] + B(i+2))
        print(memo)
        return memo[i]
    return B(0)

def bottomup_bowling(v):
    B = {}
    B[len(v)] = 0
    B[len(v)+1] = 0
    v.append(0)
    for i in reversed(range(len(v)-1)):
        B[i] = max(B[i+1], v[i] + B[i+1], v[i]*v[i+1] + B[i+2])
    print(B)
    return B[0]
    
def blackjack(c):
    B = {}
    B[len(c) - 4]

cards = [10,1,6,3,5,7,8,9,2,4]
pins = [-3,1,1,9,9,2,-5,5]
print(srtbot_bowling(pins))
print(bottomup_bowling(pins))