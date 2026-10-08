#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]

        return result


# Call the function
solution = Solution()

print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
        


# In[ ]:




