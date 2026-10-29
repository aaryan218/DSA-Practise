class Solution:

    def lemonadeChange(self, bills):

        fives = 0
        tens = 0

        for b in bills:

            if b == 5:

                fives += 1

            elif b == 10:

                if fives >= 1:

                    fives -= 1
                    tens += 1

                else:

                    return False

            else:

                if fives >= 1 and tens >= 1:

                    fives -= 1
                    tens -= 1

                elif fives >= 3:

                    fives -= 3

                else:

                    return False

        return True