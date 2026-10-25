class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = {}
        for string in strs:
            strkey = "".join(sorted(string))
            if strkey not in output.keys():
                output.update({strkey:[string]})
            else:
                output[strkey].append(string)
        return list(output.values())