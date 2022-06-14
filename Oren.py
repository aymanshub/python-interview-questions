# x=[[1,2,3,4,5,6,7,8,9,10],[...],....N]
# z=[2,4,1,9,3]

def reflector(x, z):
    result = []
    for test in x:

        for item in z:
            if test.include(item):
                continue
            else:
                result.append("False")
                flag = False
                break

        if flag:
            result.append("True")

    return result


result = ['True', 'True', 'False']
