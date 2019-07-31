def make_string(str1, num):
    return str1*num

def sum_string(str2,num):
    if (type(num)==int) or (type(num)==float) or (type(num)==complex) :
        a = str(num)
        result = str2+a
        return result

        
    else:
        a = str(num)
        result = str2+a
        return result

        
#print(str(3.14))    
#print(type(int)==type(int))
print(make_string('abc',3))
print(sum_string('abc',3.14))
print(sum_string('abc',3j))

