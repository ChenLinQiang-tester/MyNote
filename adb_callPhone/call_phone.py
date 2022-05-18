# 操作前先在设置里打开power键可以结束通话按钮，否则会导致代码报错
import time
import os
import xlrd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
if not os.path.exists(path):
    os.mkdir(path)


def test_call(number_list):
    # number_list.pop(0)
    n = 0
    for i in number_list:
        if type(i) is float:
            i = str(int(i))
        elif type(i) is str:
            i = "".join(i.split())
        else:
            break
        print(i)
        # 拨打电话
        call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:{}'.format(i))
        time.sleep(6)
        # 截图
        ScreenShot = os.popen('adb shell /system/bin/screencap -p /sdcard/phoneScreen/'+str(n)+"_"+i+'.png')
        # 挂断电话
        # Hangup = os.popen('adb shell input keyevent 26')
        Hangup = os.popen('adb shell input keyevent KEYCODE_ENDCALL ')
        time.sleep(5)
        n += 1
    SaveScreenShot = os.popen('adb pull /sdcard/phoneScreen/ ' + path)


# 执行代码：
file_name = input("输入Excel表名or测试：")
if file_name == "测试":
    phone = input("输入手机号码：")
    test_call([phone])
else:
    book = xlrd.open_workbook(file_name)
    sh = book.sheet_by_index(0)
    col_0 = sh.col_values(colx=0)
    test_call(col_0)
print("执行结束！")

# test_call(["13030206549\t"])

SaveScreenShot = os.popen('adb pull /sdcard/phoneScreen/ ' + path)

