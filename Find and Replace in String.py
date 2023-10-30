class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        
        sorted_replacements = sorted(zip(index, sources, targets), key=lambda x: x[0], reverse=True)
    
        for idx, source, target in sorted_replacements:
            if S[idx:idx + len(source)] == source:
                S = S[:idx] + target + S[idx + len(source):]

        return S