class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        rez = 0
        for i in J:
            rez += S.count(i)
        return rez
