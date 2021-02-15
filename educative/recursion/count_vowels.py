

def countVowels(string): # function that returns the count of vowels
    return countVowelsHelper(0, string)

def countVowelsHelper(count, string):
    if len(string) == 1:
        if string.lower() in "aeiou":
            return count + 1
        else:
            return count
    return countVowelsHelper(count,string[1:])


# Driver code
string = "Educative"
print(countVowels(string))