class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        TIME: 6:13.40

        logic:
        - iterate through list backwards
        - if digit < 9: increment and return, we're done
        - if digit == 9: set to 0 and set carry == 1
        - if last digit was 9 and loop is done: add 1 to front
        """
        carry = False
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            carry = True
        
        if carry:
            digits.insert(0, 1)
        
        return digits

        """
        test cases:
        - base case [1,2,3]
        - carry case [9,9,9]
        - middle carry ends [1,0,9,9,9]
        - [1,9,9,9], [1,0,0,0]
        - no leading zeros, so don't need to test
        """