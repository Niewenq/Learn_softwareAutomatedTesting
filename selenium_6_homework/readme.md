## po免登录说明
### 作业是通过login_cookie.json文件保存登录后的cookies的，并且已经把expiry字段删除了。想要免登录时，只需要读取login_cookie.json文件中的cookies内容即可。
1. 刚开始没有login_cookie.json文件，那么会直接使用用户名和密码登录，并在控制台输出相关的信息，登录后会将登录后的cookies信息保存到login_cookie.json文件中；
2. 下一次登录时首先会判断login_cookie.json文件是否存在，如果存在那么读取并尝试登录，登录成功则退出函数，否则会尝试用户名和密码登录，并更新cookies信息。
### 测试流程：
1. 首先运行main.py文件，因为刚开始运行没有login_cookie.json文件，会直接使用用户名和密码登录，在控制台打印如下信息，并保存cookies信息。<br>正在尝试使用用户名和密码登陆......<br>通过用户名和密码登陆成功!
2. 再次运行main.py文件，则会使用login_cookie.json文件中cookies信息实现免登录功能，如果登录成功，那么控制台打印如下信息：<br>正在尝试使用cookies登陆......<br>通过cookies登陆成功!
3. 当我们修改cookies信息，使得cookies失效时，比如删除名字为：beegosessionID的cookie，那么再次运行main.py文件，那么会先尝试使用cookies登录，cookies登录失败则使用用户名和密码登录，并更新cookies信息。<br>正在尝试使用cookies登陆......<br>通过cookies登陆失败!<br>正在尝试使用用户名和密码登陆......<br>通过用户名和密码登陆成功!