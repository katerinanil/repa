import sys

def interpeter(st):
	lst = []
	for ch in st:
		if ch == 'h': print('hello')
		elif ch == ' ': pass
		elif ch == 's':
			print(sum(lst))
			lst = []
		else: lst.append(int(ch))

def comp(st):
	res = ''
	for s in st.split():
		res += s + ' '
	return res

def load(path):
	f = open(path)
	code = f.read()
	virt = comp(code)
	interpeter(virt)
	f.close()

if __name__ == '__main__':
	load(sys.argv[1])