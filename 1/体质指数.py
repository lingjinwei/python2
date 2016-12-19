#体质指数判断
H = input('请输入您的身高(单位：m)：')
W = input('请输入您的体重（单位：kg）：')
h = float(H)
w = float(W)
bmi = w / (h * h)
print('您的BMI指数为：%.2f'%bmi)
if bmi < 18.5:
    print('您的身体些许的廋了呢，要多吃点哦')
elif bmi < 25:
    print('您的身体是正常的指标哦，请继续保持')
elif bmi < 28:
    print('您的身体有点胖了哦，现在减肥还来得及哦')
elif bmi < 32:
    print('您的身体比较肥胖了哦，该减肥啦')
elif bmi >= 32:
    print('您的身体太胖了哦，放弃吧 安安心心做一个胖子也是不错的')
else:
    print('别折腾我辛辛苦苦写的代码好嘛')
    
