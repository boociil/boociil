def reverse_num(num):
    num = str(num)
    num = list(num)
    j = len(num) -1 
    for i in range(len(num)//2):
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        j -= 1

    num = "".join(num)
    num = int(num)
    return num

def beautiful_day(min,max,k):
    ans = 0
    min = int(min)
    max = int(max)
    k = int(k)
    for i in range(min,max+1):
        rev = reverse_num(i)
        i = int(i)
        if (abs(i-rev) % k == 0):
            ans += 1
    
    return ans

if __name__ == '__main__':
    a,b,c = input().split()
    result = beautiful_day(a,b,c)
    print(result)