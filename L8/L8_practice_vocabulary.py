import requests,csv
from header import headers
headers = headers.headers

#   封装方法：请求题库，值返回数组，题库名
def bank_res():
    params = {'_': '1565248082002'}
    res_bank = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/',
                            headers=headers,
                            params=params)
    bank_json = res_bank.json()
    bank_names = bank_json['data']
    return bank_names
bank_names = bank_res()
print(bank_names)
#   选题,并取值
def choice():
    print('欢迎来到单词测验，下面为题库类型：')
    for i in range(len(bank_names)):
        print(' %d：%s'%(i,bank_names[i][1]))
    choice_num = int(input('请选择你要测试的题库（选择题库对应的数字）：'))
    usr_choice = bank_names[choice_num][0]
    return usr_choice

#   50词获取
category = choice()
class words_50:
    def __init__(self,category):
        self.url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
        self.c = category
        self.params = {'category': self.c,
                '_': '1565250506195'}
        res_words_50 = requests.get(url=self.url,headers=headers,params=self.params)
        self.words_json = res_words_50.json()
        self.words_data = self.words_json['data']
        self.words_list = []    #   创建词列表
        self.right_list = []    #   创建正确答案列表
        self.question_list = [] #   创建题目列表（嵌套列表)
        for word in self.words_data:
            word_content = word['content']
            pk = word['pk']
            choices = word['definition_choices']
            #   完成词列表
            self.words_list.append(word_content)
            questions = []
            for choice in choices:
                question = choice['definition']
                #   单个词的问题列表添加
                questions.append(question)
                if pk == choice['pk']:
                    right_choice = choice['definition']
                    self.right_list.append(right_choice)   #
            #   总问题列表添加
            self.question_list.append(questions)
#   识别单词
words = words_50(category)
class usr_selection:
    def __init__(self):
        self.words_list = words.words_list  #   单词列表
        self.usr_recognize = []             #   认识不认识列表
        self.usr_count = []                 #   掌握与否列表
        print('请输入y/n来选择您认识的单词：')
        #   认识不认识
        word_count = 0
        for i in self.words_list:
            word_count += 1
            usr_choice = input('第'+str(word_count)+'题'+i+'\ny/n:\n')
            if usr_choice != 'y':
            	usr_choice = 'n'
            self.usr_recognize.append(usr_choice)
        #   掌握没掌握
        print('请选出正确答案，输入对应选项号（0-3）：')
        for k in range(len(self.usr_recognize)):

            if self.usr_recognize[k] == 'y':
                print(str(k), self.words_list[k], '\n')
                question_num = 0
                questions = words.question_list[k]
                for question in questions:
                    print('%d:%s'%(question_num,question))
                    question_num += 1

                usr_select_input = int(input('请选择0-3：\n'))
                usr_select = questions[usr_select_input]
                print(usr_select)

                if usr_select == words.right_list[k]:
                    print('@@恭喜您回答正确\n')
                    self.usr_count.append('已掌握')
                else:
                    print('xx回答错误xx\n')
                    self.usr_count.append('未掌握')
            else:
                self.usr_count.append('---')

main_info = usr_selection()
# print(words.right_list)
# print(len(words.right_list))
# print(main_info.words_list)
# print(main_info.usr_recognize)
# print(main_info.usr_count)

with open('vocabulary_test.csv','w',newline='',encoding='utf-8') as vt:
    writer = csv.writer(vt)
    writer.writerow(['词汇列表','是否认识','是否掌握'])
    for i in range(len(main_info.words_list)):
        writer.writerow([main_info.words_list[i],main_info.usr_recognize[i],main_info.usr_count[i]])

with open('vocabulary_test.csv','r',newline='',encoding='utf-8') as rv:
    reader = csv.reader(rv)
    for i in reader:
        print(i)