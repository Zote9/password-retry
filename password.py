password = 'a123456'
n = 3
while n > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break
	else:
		n -= 1
		print('還有%s次機會' % n)