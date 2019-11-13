from selenium import webdriver # 从selenium导入webdriver
import pandas as pd

f = pd.read_csv('grade.csv',encoding='gbk',header=0) #header=None 表示没有列标题，=0表示把第一行的值当成列标题

ps_data=list()
qm_data=list()
sy_data=list()

for i in range(f.shape[0]):
	ps_data.append(f.loc[i,'平时'])
	qm_data.append(f.loc[i, '期末'])
	sy_data.append(f.loc[i, '实验'])

ps=list()
qm=list()
sy=list()
for i in range(2,42):
	ps.append('DataGrid1:_ctl'+str(i)+':ps')
	qm.append('DataGrid1:_ctl'+str(i)+':qm')
	sy.append('DataGrid1:_ctl'+str(i)+':sy' )


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://jsyd.suda.edu.cn/')
name = driver.find_element_by_name("TextBox1")
name.send_keys("13N139") #登陆用户名
pw = driver.find_element_by_name("TextBox2")
pw.send_keys("")#登陆密码
yzm=driver.find_element_by_name("TextBox3")
a=input()
yzm.send_keys(a)
login_button=driver.find_element_by_name('Button1')
login_button.click()

path=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/a/span")
path.click()

driver.get('http://jsyd.suda.edu.cn/js_cjmm.aspx?xkkh=(2018-2019-2)-COMS1013-13N139-1&zgh=13N139&gnmkdm=N12211')

name = driver.find_element_by_name("TextBox1")
name.send_keys("")#课程密码
login_button=driver.find_element_by_name('Button1')
login_button.click()
t=driver.switch_to_alert()
t.accept()



for i in range(40):
	
	print(str(ps_data[i]),str(ps_data[i]),str(sy_data[i]))
	gridps=driver.find_element_by_name(ps[i])
	gridps.send_keys(str(ps_data[i]))
	gridqm = driver.find_element_by_name(qm[i])
	gridqm.send_keys(str(qm_data[i]))
	gridsy = driver.find_element_by_name(sy[i])
	gridsy.send_keys(str(sy_data[i]))
