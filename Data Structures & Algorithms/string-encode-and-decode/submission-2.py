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
    """

    def encode(self, strs: List[str]) -> str:
        result = []

        if len(strs) == 0:
            return "null"

        for s in strs:
            word = '.'.join([str(ord(c)) for c in s])
            result.append(word)
        encoded = '|'.join([r for r in result])
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "null":
            return []

        res = []
        words = s.split('|')
        for word in words:
            if word == "":
                res.append("")
                continue
            ascii_nums = word.split('.')
            out = ''
            for num in ascii_nums:
                out += chr(int(num))
            res.append(out)
        return res
