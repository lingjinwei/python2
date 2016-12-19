# _*_ coding: utf-8 _*_
a = input('请输入原本的值：')
b = input('请输入变化的值：')
A = float(a)
B = float(b)
if int(A)>int(B):
    c = (A-B)/A*100
    print('您的数据降低了%.2f%%' %c)
elif int(A)<int(B):
    c = (B-A)/A*100
    print('您的数据增长了%.2f%%' %c)
else:
    print('天呐不要折磨我的代码了')
