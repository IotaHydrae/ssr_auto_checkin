import random
import os
# 中文测试
def do(times):
    sum = 0
    for i in range(times):
        for i in range(30):
            v = random.randint(1,99)
            sum+=v
        with open('total.txt', 'a+') as f:
            f.write('%d\n' % sum)
            sum=0
            f.close()

if __name__ == '__main__':
    do(1000)
    file = open('total.txt', 'r')
    total = file.readlines()
    sum = 0
    for i in total:
        v = int(i)
        sum+=v
    print(sum/len(total))
    sum = 0
    file.close()
    os.remove('total.txt')