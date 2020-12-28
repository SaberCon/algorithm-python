class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        block_comment = False
        for line in source:
            if not block_comment:
                ans.append('')
            i = 0
            while i < len(line):
                if block_comment:
                    if i < len(line) - 1 and line[i] + line[i + 1] == '*/':
                        block_comment = False
                        i += 2
                    else:
                        i += 1
                    continue
                if i < len(line) - 1 and line[i] + line[i + 1] == '//':
                    break
                if i < len(line) - 1 and line[i] + line[i + 1] == '/*':
                    block_comment = True
                    i += 2
                else:
                    ans[-1] += line[i]
                    i += 1
        return [line for line in ans if line]
