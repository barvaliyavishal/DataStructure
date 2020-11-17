'''String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). '''


def stringCompression(str1):
    char = ""
    s1 = ""
    counter = 0
    for i in range(len(str1)):
        if i == len(str1)-1:
            if char == str1[i]:
                counter += 1
                s1 = s1 + char + str(counter)
            else:
                s1 = s1 + str1[i] + "1"
        elif char == "":
            char=str1[i]
            counter = 1
        elif str1[i] == char:
            counter += 1
        elif str1[i] != char:
            s1 = s1 + char + str(counter)
            counter = 1
            char = str1[i]
    if len(s1) < len(str1):
        return s1
    return str1

print(stringCompression("aabbcbcccdyyyyy"))