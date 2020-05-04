import  math
import requests,openpyxl
import sys
sys.setrecursionlimit(100000)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
print('''———————————————————————————————————————————————————
                        目前版本5.0
                        【单词量测试】
    本版本新增功能：
    1：答题即时判断对错
    2：答题错误后即时输出正确答案
    3：错词本有序排列打印
    4：错词本自动以xlsx表格自动保存本地，且有序保存单词和正确的词义
    欢迎申请新功能~待开发功能：好看的窗体控件
    ———————————————————————————————————————————————————''')


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
                print(' '+str(A99+1)+','+A5[A99])
            elif Yushu == 2:
                print(' ' + str(A99 + 1) + ',' + A5[A99] + '     ' + str(B99 + 1) + ',' + A5[B99])
            elif Yushu == 3:
                print(' ' + str(A99 + 1) + ',' + A5[A99] + '     ' + str(B99 + 1) + ',' + A5[B99] + '     ' + str(C99 + 1) + ',' + A5[C99])
            elif Yushu == 4:
                print(' ' + str(A99 + 1) + ',' + A5[A99] + '     ' + str(B99 + 1) + ',' + A5[B99] + '     ' + str(C99 + 1) + ',' + A5[C99] + '     ' + str(D99 + 1) + ',' + A5[D99])
            else:
                print(' ' + str(A99 + 1) + ',' + A5[A99] + '     ' + str(B99 + 1) + ',' + A5[B99] + '     ' + str(C99 + 1) + ',' + A5[C99] + '     ' + str(D99 + 1) + ',' + A5[D99] + '     ' + str(E99 + 1) + ',' +A5[E99])
        else:
            print(' ' + str(A99 + 1) + ',' + A5[A99] + '     ' + str(B99 + 1) + ',' + A5[B99] + '     ' + str(C99 + 1) + ',' + A5[C99] + '     ' + str(D99 + 1) + ',' + A5[D99] + '     ' + str(E99 + 1) + ',' + A5[E99])
        # print('X = '+str(X))
        A99 += 5
        B99 += 5
        C99 += 5
        D99 += 5
        E99 += 5

while True:
    Ex = openpyxl.Workbook()
    sheet = Ex.active
    sheet.title = '错词本'
    sheet['A1'] = '英文单词'
    sheet['B1'] = '词义'
    url = 'https://www.shanbay.com/api/v1/vocabtest/category/?_=1587792409933'
    params = {'_': '1587792409933'}
    res = requests.get(url,headers=headers,params=params)
    res_status = res.status_code
    Number = -1
    ListA = []
    ListC = []
    if int(res_status) == 200:
        res_Json = res.json()
        List = res_Json['data']
        for A in List:
            name = A[1]
            Links_Number = A[0]
            Number = Number + 1
            #print(Number,name)
            ListC.append(name)
            ListA.append(Links_Number)
        print('''请输入你选择的词库编号，按Enter确认''')
        #print(ListC)
        Paixu(ListC)
        '''
        1，GMAT  2，考研  3，高考  4，四级  5，六级
        6，英专  7，托福  8，GRE  9，雅思  10，任意
        '''
        answerA = int(input('请选择出题范围（输入数字序号即可）：'))
        Choice = ListA[answerA-1]
        url1 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=CET6&_=1587792416212'
        params = {
            'category': str(Choice),
            '_': '1587792416212'
        }
        res1 = requests.get(url1,headers=headers,params=params)
        res_status1 = res1.status_code
        ListB_All = []
        List_All_C_Word = []
        ListB = []
        List_Right_Rank = []

        List_Right_Rank_All = []
        rubbish = []
        Bigdefinition = []

        BigRank = []

        Boss = []
        Boss1 = []
        A5 = []
        if int(res_status1) == 200:
            print('请选择你认识的单词（随机50个单词）【认识请按1，不认识直接按Enter】：')
            answerS = input('如果你想直接测试所有单词，请按1，否则请按任意键下一步：')
            if answerS == '1':
                res_JsonA = res1.json()
                List_AB = res_JsonA['data']
                # 列表打印出所有单词
                for B in List_AB:
                    word = B['content']
                    ListB_All.append(word)
                    # 把单词放进ListB_All列表里
                    right_Rank = B['rank']
                    List_Right_Rank_All.append(right_Rank)
                    print(word)
                    List_All_C_Word.append(word)
                    List_Rank = []
                    # 这里的列表会封装四个不同词义的Rank数值
                    definition_List = []
                    # 这里的列表会装4个不同选择的词义，让使用者去选择
                    ListB.append(word)
                    List_Right_Rank.append(right_Rank)
                    # 本单词正确的rank数值
                    definition_choices = B['definition_choices']
                    # 单词里的四个选择
                    for C in definition_choices:
                        definition = C['definition']
                        definition_Rank = C['rank']
                        definition_List.append(definition)
                        List_Rank.append(definition_Rank)
                    Bigdefinition.append(definition_List)
                    BigRank.append(List_Rank)
                    # 让装有4个词义的列表统一放进一个大列表里
            else:
                res_JsonA = res1.json()
                List_AB = res_JsonA['data']
                #列表打印出所有单词
                for B in List_AB:
                    word = B['content']
                    ListB_All.append(word)
                    #把单词放进ListB_All列表里
                    right_Rank = B['rank']
                    List_Right_Rank_All.append(right_Rank)
                    print(word)

                    answerB = input('这个单词认识吗？')
                    #answerB = 1
                    #使用者的认识单词和不认识的单词区分

                    if answerB == '1':
                        List_All_C_Word.append(word)
                        List_Rank = []
                        #这里的列表会封装四个不同词义的Rank数值
                        definition_List = []
                        #这里的列表会装4个不同选择的词义，让使用者去选择
                        ListB.append(word)
                        List_Right_Rank.append(right_Rank)
                        #本单词正确的rank数值
                        definition_choices = B['definition_choices']
                        #单词里的四个选择
                        for C in definition_choices:
                            definition = C['definition']
                            definition_Rank = C['rank']
                            definition_List.append(definition)
                            List_Rank.append(definition_Rank)
                        Bigdefinition.append(definition_List)
                        # 让装有4个词义的列表统一放进一个大列表里
                        BigRank.append(List_Rank)
                        # 让装有4个词义Rank的列表统一放进一个大列表里

                    else:
                        BigRank1 = []
                        List_Right_Rank1 = []
                        Bigdefinition1 = []
                        A6 = []
                        A6.append(word)
                        A5.append(word)
                        # '''
                        MX1 = -1
                        GG1 = []
                        List_Rank1 = []
                        # 这里的列表会封装四个不同词义的Rank数值
                        definition_List1 = []
                        # 这里的列表会装4个不同选择的词义，让使用者去选择
                        List_Right_Rank1.append(right_Rank)
                        # 本单词正确的rank数值
                        List_Rank1 = []
                        definition_choices = B['definition_choices']
                        for C in definition_choices:
                            definition = C['definition']
                            definition_Rank = C['rank']
                            definition_List1.append(definition)
                            List_Rank1.append(definition_Rank)
                        Bigdefinition1.append(definition_List1)
                        # 让装有4个词义的列表统一放进一个大列表里
                        BigRank1.append(List_Rank1)
                        # 让装有4个词义Rank的列表统一放进一个大列表里
                        GN1 = -1
                        for G1 in BigRank1:
                            GN1 += 1
                            GN2 = -1
                            for G2 in G1:
                                GN2 += 1
                                if G2 == List_Right_Rank1[MX1]:
                                    GG1.append(GN2)
                            GU1 = int(GG1[GN1])
                            #print('GU1：'+str(GU1))
                            CiYi1 = Bigdefinition1[GN1][GU1]
                            #print('CiYi1：'+str(CiYi1))
                            sheet.append([A6[MX1], CiYi1])
                            MX1 += 1
                        #'''



            Boss.append([Bigdefinition,BigRank])
            print('接下来是单词测试，请选择正确的词义（请直接输入数字）：')

            MX = -1
            MM = 0
            A4 = []
            GG = []
            for D in Boss:
                #print(D[1])
                #D[0]是词汇大列表，D[1]是词汇对应的rank值大列表
                for E in D[0]:
                    #print(E)
                    NM = 0
                    MM = MM + 1
                    MX = MX + 1
                    print('———分界线———————————————————————————————————————————————————' + '\n' + '————————————      '+'第'+str(MM) + '个单词'+'  '+List_All_C_Word[MX]+ '      ——————————————————' + '\n' + '————————————————————————————————————————————————分界线——————')
                    for E1 in  E:
                    #此For循环是列出小列表里的四个词义，所以只会有四个数值
                        #print(E1)
                        NM = NM + 1
                        print(NM, E1)
                    GN = -1
                    for G in D[1][MX]:
                        GN += 1
                        if G == List_Right_Rank[MX]:
                            GG.append(GN)

                    while True:
                        try:
                            answerC = int(input('请选择：'))-1
                            #answerC = 1#测试专用代码
                            if answerC <= 3:
                                Question_Answer_Rank = D[1][MX][answerC]
                                #这是使用者选择的答案的rank数值
                                List_Right_Rank_U = List_Right_Rank[MX]
                                #这是正确的Rank值
                                if Question_Answer_Rank == List_Right_Rank_U:
                                    A4.append(Question_Answer_Rank)
                                    # 把回答正确的rank放入A4列表里
                                    print('                ======回答正确======')
                                else:
                                    GU = int(GG[MX])
                                    CiYi = E[GU]
                                    A5.append(ListB_All[MX])
                                    sheet.append([ListB_All[MX],CiYi])
                                    print('                ======回答错误======')
                                    print('●●●●●●●正确答案：'+CiYi)
                                    # 把回答错误的单词放入A5列表里
                                break
                            else :
                                print('这里只有四个选择诶，请你再认真选一选，别搞事情嗷~QAQ')
                        except ValueError:
                            print('你是不是输入了什么奇怪的东东[○･｀Д´･ ○]，请输入纯数字！')



    #print(List_Right_Rank)
    str_list = ""
    for a in range(len(List_Right_Rank)):
        if a == len(List_Right_Rank) - 1:
            str_list = str_list + str(List_Right_Rank[a])
        else:
            str_list = str_list + str(List_Right_Rank[a]) + ','
    str_list2 = ""
    for a2 in range(len(A4)):
        if a2 == len(A4) - 1:
            str_list2 = str_list2 + str(A4[a2])
        else:
            str_list2 = str_list2 + str(A4[a2]) + ','
    #str_listA = str_list.encode('utf-8')
    #str_listB = str_list2.encode('utf-8')
    #print(str_list)
    #print(str_list2)
    url5 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
    data = {
        'category': str(Choice),
        'phase':'',
        'right_ranks':str(str_list2),
        'word_ranks':str(str_list),
        }
    #print(data)
    res5 = requests.post(url5, headers=headers, data=data)
    res5_status = res5.status_code
    if int(res5_status) == 200:
        res_Json5 = res5.json()
        #lista = res_Json5['data']
        Score = res_Json5['data']['vocab']
        Comment = res_Json5['data']['comment']
        #print(lista)
        #print(Score,Comment)
        print('============================================'+'\n'+'                                       '+'\n'+'=====      你的词汇量大约是：'+str(Score)+'        ====='+'\n'+'    '+Comment+'           '+'\n'+'============================================')
        #print(len(GG))#测试GG列表有多少个数组
    answerD = input('需要查看错词本吗？(需要的请输入数字1，不需要的话直接回车)')
    if answerD == '1':
        #print(A5)
        Paixu(A5)
        Ex.save('错词本.xlsx')

    answerE = input('请问还想要再重新测试一次吗？(需要的请输入数字1，不需要的话直接回车)')
    if answerE != '1':
        break