class Solution:
    """
    assuming we want the encoded string to be much smaller.
    anything in 256 valid ascii characters means the delimiter is important and can't just be some char

    thoughts:
    encode
        1. convert each char to ascii value
        2. combine them with delimiter
    
    decode
        1. separate at delimiter
        2. convert back from ascii
    
    time to complete: 33:45.00

    pretty bad overall. better solution (from chat gpt): length-prefix encoding.
    should work as generalized algorithm
    """

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(s)}#{s}" for s in strs])

    # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        result = []
        i, j = 0, 0

        while i < len(s):
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1
            
            result.append(s[j: j + length])
            i = j = j + length

        return result





