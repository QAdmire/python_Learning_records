#coding=utf-8
import hashlib
def main():
    oldmd5='fcea920f7412b5da7be0cf42b8c93759'  #这里写的是需要破解的MD5
    f = open('superdic.txt','r+')              #这里要把明文的密码字典写上（注意路径问题）
    while True:
        line = f.readline() #read读整个文件， readline读一行 存str readlines按每一行读全部 存list
        print(line)
        if len(line) == 0: #读到最后一行之后没有找到关闭文件
            f.close()
            print('PASSWOWD NOT FOUND')
            break
        print('\r' in line)
        #print line
        passwdmd5=line.strip() #去掉首尾空格和换行符
        print('\r' in line)
        print(passwdmd5)
        h = hashlib.md5()
        h.update(passwdmd5.encode())
        if h.hexdigest() == oldmd5:
            f.close()
            print('PASSWOWD FOUND:\n'+line)
            break
if __name__ == '__main__':
    main()