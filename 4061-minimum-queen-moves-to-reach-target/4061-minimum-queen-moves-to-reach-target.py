class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:

        if target == source: 
            return 0                                

        (sr, sc), (tr, tc) = source, target
        rDiff, cDiff = abs(sr - tr), abs(sc - tc)

       
        if (rDiff == 0 or cDiff == 0 or rDiff == cDiff):                 
            return 1

        return 2                            