class Solution:
    def validIPAddress(self, IP: str) -> str:
        hexs = {chr(ord('0') + i) for i in range(0, 10)} | {chr(ord('a') + i) for i in range(0, 6)} \
               | {chr(ord('A') + i) for i in range(0, 6)}
        v4_part = IP.split('.')
        if len(v4_part) == 4 and all(
                part.isdigit() and 0 <= int(part) <= 255 and (part == '0' or part[0] != '0') for part in v4_part):
            return 'IPv4'
        v6_part = IP.split(':')
        if len(v6_part) == 8 and all(1 <= len(part) <= 4 and all(c in hexs for c in part) for part in v6_part):
            return 'IPv6'
        return 'Neither'
