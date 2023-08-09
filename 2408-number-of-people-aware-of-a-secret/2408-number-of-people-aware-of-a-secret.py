def mod_add(a: int, b: int) -> int:
	MOD = 1000000007
	return ((a % MOD) + (b % MOD)) % MOD 


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [0] * forget
        people[0] = 1
        
        for _ in range(1, n):
            for idx in range(forget - 1, 0, -1):
                people[idx] = people[idx - 1] 
            
            new = 0
            for idx in range(forget):
                if idx >= delay:
                    new = mod_add(new, people[idx])
                    
            people[0] = new
            
        total = 0
        for p in people:
            total = mod_add(total, p)
            
        return total      