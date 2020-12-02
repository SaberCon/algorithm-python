class Solution:
    def isValid(self, code: str) -> bool:
        if not code or code[0] != '<':
            return False
        i = 1
        tags = ['<']
        cdata = False
        while i < len(code):
            if not tags:
                return False
            curr = code[i]
            for group in ('</', '<![CDATA[', ']]>'):
                if i < len(code) - len(group) + 1 and code[i: i + len(group)] == group:
                    curr = group
                    i += len(group) - 1
                    break
            i += 1
            if cdata:
                if curr == ']]>':
                    cdata = False
                continue
            if tags[-1][-1] == '>':
                if curr == '<' or curr == '</':
                    tags.append(curr)
                if curr == '<![CDATA[':
                    cdata = True
            else:
                if curr.isupper():
                    if len(tags[-1]) >= 11 or (not tags[-1].startswith('</') and len(tags[-1]) >= 10):
                        return False
                    tags[-1] += curr
                elif curr == '>':
                    if len(tags[-1]) <= 1:
                        return False
                    if tags[-1].startswith('</'):
                        if tags.pop()[2:] != tags.pop()[1:-1]:
                            return False
                    else:
                        tags[-1] += '>'
                else:
                    return False
        return not tags
