class Solution:
    def intToRoman(self, num: int) -> str:
        roman_to_integer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
        'M': 1000, 'IV':4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        integer_to_roman = {value: key for key, value in roman_to_integer.items()}
        res = ''
        # ПЕРВЫЙ вариант
        # power = 1
        # while num != 0:
        #     last_fig = num % (10 ** power)
        #     num -= last_fig
        #     power += 1
        #     churn = ''
        #     if last_fig not in integer_to_roman:
        #         choice = {key:value for key, value in integer_to_roman.items() if key < last_fig and len(str(key)) == len(str(last_fig))
        #                   and len(value) == 1}
        #         while last_fig != 0:
        #             n = max(choice.keys())
        #             churn += choice[n]
        #             last_fig -= n
        #             if last_fig < n:
        #                 del choice[n]
        #         res = churn + res
        #     else:
        #         res = integer_to_roman[last_fig] + res
        # return res

        #  ВТОРОЙ способ
        power = len(str(num)) - 1
        while num != 0:
            fig = num // (10 ** power)
            #print(fig)
            fig_full = fig * (10 ** power)
            num -= fig_full
            if fig_full in integer_to_roman:
                res += integer_to_roman[fig_full]
            else:
                choice = {key: value for key, value in integer_to_roman.items() if
                          key < fig_full and len(str(key)) == len(str(fig_full))}
                print('choice', choice)
                while fig_full != 0:
                    max_part = max(choice.keys())
                    if max_part <= fig_full:
                        res += choice[max_part]
                        fig_full -= max_part
                    if fig_full < max_part:
                        del choice[max_part]
            power -= 1
        return res




ex =Solution()
#print(ex.intToRoman(3))
print(ex.intToRoman(58))
print(ex.intToRoman(1994))
print(ex.intToRoman(21))