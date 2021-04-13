# coding : utf-8
import click
import zipfile


@click.command()
@click.option("-b", defalult=1, help="1:暴力破解，2：字典破解")
@click.option("-d", help="如果需要，传入文件路径")
@click.option("-f", help="传入被加密的文件路径")
def zip(b, d, f):
    if b == 2:
        dictionary(dic=d, zfile=f)
    elif b == 1:
        bruteforce(zipfile=f)
    else:
        return


def dictionary(dic, zfile):
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileNotFoundError:
        print("你输入的文件不存在")
        return


password = ""
with open(dic, "r") as f:
    data = f.readlines()

    for item in data:
        password = item.strip()
    try:
        myzip.extractall(pwd=password.encode())
        print("woo")
        return
    except Exception as e:
        print("尝试密码错误：", password)
print("字典没有密码")
