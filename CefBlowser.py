try:
    from cefpython3 import cefpython as cef
except Exception as error:
    print("您还未安装CefPython3组件包，无法使用在线翻译！！")
    ceflock = True;
finally:
    pass
import platform
import sys
def translate(URL):
    if ceflock == True:
        print("请安装cefpython3后再使用在线翻译！")
        return 0;
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    if URL == "Baidu":
        cef.CreateBrowserSync(url="http://fanyi.baidu.com",
                              window_title="百度翻译")
    elif URL == "Google":
        cef.CreateBrowserSync(url="http://fanyi.youdao.com",
                              window_title="有道翻译")
    elif URL == "Qihoo":
        cef.CreateBrowserSync(url="http://fanyi.so.com",
                              window_title="360翻译")
    elif URL == "BlowerMode":
        while True:
            Link = input("请输入您想浏览的网站的URL,输入Quit以退出:")
            if Link == "Quit":
                break;
            cef.CreateBrowserSync(url=Link,
                                  window_title="CefPython3浏览器")
    cef.MessageLoop()
    cef.Shutdown()
def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
        ver=platform.python_version(),
        arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"