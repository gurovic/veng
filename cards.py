import sys
import random
 


wordict = {'���������� �������':'O(n ** 2)', 
           '���������� ���������':'O(n ** 2)',
           '���������� ���������':'O(n ** 2)',
           '���������� ��������':'O(n * log2(n))', 
           '���������� ���������':'O(n + k)',
           '������� ����������':'O(n * log2(n))',
           '������ ����������':'O(n ** 3)'}

hdict = {'a':'O(n ** 2)', 'b':'O(n * log2(n))', 'c':'O(n + k)', 'd':'O(n ** 3)'}

wrong = 0
right = 0
keys = list(wordict.keys())
while True:
    tmpkey = random.choice(keys)
    print("{0}: {1}".format(len(keys), tmpkey))
    value = wordict[tmpkey]
    ans = input('''Time: 
    a) O(n ** 2)
    b) O(n * log2(n))
    c) O(n + k)
    d) O(n ** 3)
    ''')
    if ans == 'exit':
        sys.exit()
    elif hdict[ans] in value.split(", "):
        print("True.".format(value))
        keys.remove(tmpkey)
        right += 1
    else:
        wrong += 1
        print("Wrong! {0}\n".format(value))
    if len(keys) < 1:
        if wrong == 0:
            print('Perfect!=)')
        elif wrong <= 2:
            print('Good!;)')
        elif wrong <= 4:
            print('Satisfactorily!:(')
        else:
            print('Bad!=(')
        print("Right - {0}. Wrong - {1}".format(right, wrong))
        sys.exit()