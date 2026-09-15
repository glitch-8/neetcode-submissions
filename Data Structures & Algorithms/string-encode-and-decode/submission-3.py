class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = str(len(s))
            encoded += f'{length}#{s}'
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_list = list()
        idx = 0
        start = 0
        while idx<len(s):
            if s[idx] == "#":
                length = int(f"{s[start:idx]}")
                decoded_list.append(s[idx+1:idx+1+int(length)])
                start = idx + length + 1
                idx += length + 1
            else:
                idx += 1
        
        return decoded_list

