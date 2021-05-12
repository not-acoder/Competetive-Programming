temp = []
temp2 = []
result=[]
def merge_the_tools(string, k):
    #a = int(len(string) / k)
    for i in range(0,int(len(string)),k):
        b = string[i:i+k]
        temp.append(b)
        b = None



    print(temp)
    for x in range(int(len(temp))):
        z="".join(dict.fromkeys(temp[x]))
        result.append(z)



    for q in result:
        print(q)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)