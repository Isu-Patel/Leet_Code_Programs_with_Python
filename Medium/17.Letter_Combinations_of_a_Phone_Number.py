class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, current_combination):
            nonlocal result
            if index == len(digits):
                result.append(current_combination)
                return
            
            digit = digits[index]
            letters = mapping[digit]
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result
