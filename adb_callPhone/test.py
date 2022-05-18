import subprocess

order = 'adb shell ls /sdcard/Music'  # 获取连接设备
try:
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    print("aaa:", pi.stdout.read())
    print(pi.communicate())
except:
    print("aa")  # 打印结果
# print(pi.stdout)
