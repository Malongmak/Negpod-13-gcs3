def roman_to_int(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
            result += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
        else:
            result += roman_dict[s[i]]
    return result
print(roman_to_int('III'))
print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))
print(roman_to_int('XCIX'))
print(roman_to_int('MMDCCCL'))
