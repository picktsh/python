import  math

def Paixu(A5):
        A99 = 0
        B99 = 1
        C99 = 2
        D99 = 3
        E99 = 4
        for X in range(math.ceil(len(A5) / 5)):
            # print(str(A) + '' + str(B) + '' + str(C) + '' + str(D) + '' + str(E))
            if X == (math.ceil(len(A5) / 5)) - 1:
                Yushu = len(A5) % 5
                # print(Yushu)
                if Yushu == 1:
                    print(' ' + A5[A99])
                elif Yushu == 2:
                    print(' '+str(A99)+','+ A5[A99] + '     ' +str(B99)+','+ A5[B99])
                elif Yushu == 3:
                    print(' ' +str(A99)+','+ A5[A99] + '     ' +str(B99)+','+ A5[B99] + '     ' +str(C99)+','+ A5[C99])
                elif Yushu == 4:
                    print(' ' +str(A99)+','+ A5[A99] + '     ' +str(B99)+','+ A5[B99] + '     ' +str(C99)+','+ A5[C99] + '     ' +str(D99)+','+ A5[D99])
                else:
                    print(' ' +str(A99)+','+ A5[A99] + '     ' +str(B99)+','+ A5[B99] + '     ' +str(C99)+','+ A5[C99] + '     ' +str(D99)+','+ A5[D99] + '     ' +str(E99)+','+ A5[E99])
            else:
                print(' ' +str(A99)+','+ A5[A99] + '     ' +str(B99)+','+ A5[B99] + '     ' +str(C99)+','+ A5[C99] + '     ' +str(D99)+','+ A5[D99] + '     ' +str(E99)+','+ A5[E99])
            # print('X = '+str(X))
            A99 += 5
            B99 += 5
            C99 += 5
            D99 += 5
            E99 += 5

A5 = ['well', 'believe', 'fact', 'reason', 'heart', 'easy', 'worker', 'sport', 'artist', 'rock', 'perform', 'task', 'basic', 'Christian', 'tool', 'cool', 'salt', 'bridge', 'guide', 'celebrate', 'physician', 'immediate', 'practical', 'concert', 'burst', 'twist', 'dilemma', 'merchant', 'fever', 'zero', 'contrary', 'institute', 'Arctic', 'sorrow', 'amusement', 'walnut', 'punctuate', 'vice', 'Antarctic', 'moustache', 'offence']
ListA = ['GMAT', 'NGEE', 'NCEE', 'CET4', 'CET6', 'TEM', 'TOEFL', 'GRE', 'IELTS', 'NONE']
ListC = ['GMAT', '考研', '高考', '四级', '六级', '英专', '托福', 'GRE', '雅思', '任意']
Paixu(ListA)