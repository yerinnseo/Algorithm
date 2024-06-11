n, k = map(int, input().split())
N = 1
K = 1
NK = 1 

for i in range(0, n-1):
    N *= n - i
    
for i in range(0, k-1):
    K *= k - i

for i in range(0, n-k-1):
    NK *= n - k - i
    
print(int(N/(NK*K)))