# -*- coding: UTF-8 -*-
import re

#findall :找到所有符合的
# text = 'aaa$12,ad$44'
# ret = re.findall('\$\d+', text)
# print(ret)#['$12', '$44']

#sub 根据规则替换字符串
# text = 'helll wolrd, asd ,, Hoqp'
# ret = re.sub(",| ", '\n', text)
# print(ret)
# #如果用replace则需要俩次
# replace = text.replace(' ', '\n')
# replace = replace.replace(',', '\n')
# print(replace)

# html = """
# <div class="job-detail">
#     <p>1. 3年以上相关开发经验 ，全日制统招本科以上学历</p>
#     <p>2. 精通一门或多门开发语言(Python,C,Java等)，其中至少有一门有3年以上使用经验</p>
#     <p>3. 熟练使用ES/mysql/mongodb/redis等数据库；</p>
#     <p>4. 熟练使用django、tornado等web框架，具备独立开发 Python/Java 后端开发经验；</p>
#     <p>5. 熟悉 Linux / Unix 操作系统&nbsp;</p>
#     <p>6. 熟悉 TCP/IP，http等网络协议</p>
#     <p>福利：</p>
#     <p>1、入职购买六险一金（一档医疗+公司全额购买商业险）+开门红+全额年终奖（1年13薪，一般会比一个月高）</p>
#     <p>2、入职满一年有2次调薪调级机会</p>
#     <p>3、项目稳定、团队稳定性高，团队氛围非常好（汇合员工占招行总员工比例接近50%）；</p>
#     <p>4、有机会转为招商银行内部员工；</p>
#     <p>5、团队每月有自己的活动经费，法定节假日放假安排；</p>
#     <p>6、办公环境优良，加班有加班费（全额工资为计算基数，加班不超过晚上10点，平日加班为时薪1.5倍，周末加班为日薪2倍，周末加班也可优先选择调休，管理人性化）。</p>
# </div>
# """
#
# result = re.sub('<.+?>', '', html)
# print(result)

#split:根据规则分割字符
# text = 'hello world yead,sdf'
# result = re.split(' |,', text)
# print(result)

#compile : 编译表达式
# text = 'apple price is 34.56'
# result = re.compile('''
# \d+ #整数
# .?  #小数点
# \d* #小数
# ''',re.VERBOSE)  #注意注释
#
# r = re.search(result, text)
# print(r.group())