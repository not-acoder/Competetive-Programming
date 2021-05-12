
# Complete the repeatedString function below.
def repeatedString(s, n):
    l=len(s)
    if(l<= n) :
        if(n%l == 0 ) :
            return int(s.count('a')*n/l)
        else:
            return int(s.count('a')*((n - (n% l )) / l)+ s [: n %l].count('a'))
    else:
        return int(s[:n].count('a'))



s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
n = 736778906400
result = repeatedString(s, n)

print(result)
