#coding=utf-8
#!/usr/bin/python
import socket,time,threading,re,sys,optparse

"""
关于main函数flag传参
一,扫描指定端口频段传参格式:
1-500，
表示扫描从1到500的端口
二,扫描默认端口列表传参格式:
输入m或不填
表示扫描默认端口列表
三,扫描全端口格式：
输入a
表示扫描全端口
"""

#扫描函数
def scan(ip,port):
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result=s.connect_ex((ip,port))
		if result == 0:
			print ip+":"+str(port)+" 端口开放\n"
		s.close()
	except:
		print '端口扫描异常'

#主函数
def main(ip,flag):
	#扫描指定端口频段
	if '-' in flag:  
		print "开始扫描指定端口段:\n" 
		l =  re.findall(r"\d+\.?\d*",flag)
		start = l[0]
		end = l[1]
		doActionB(start,end)
		
	#全端口扫描
	elif flag == 'a': 
		print "全端口扫描:\n" 
		portList = getAllPortList()
		for i in portList:
			start = i[0]
			end = i[1]
			doActionB(start,end)
			
	#扫描默认端口
	else:
		print "开始扫描默认端口：\n" 
		portList = ['21','22','23','25','80','888','8080','3128','8081','9080','1080','443','110','7001','9080','9090','3389','8081','1521','1158','2100','1433','1080','3306']
		doActionA(portList)
def doActionA(portList):
		threads = []
		for x in portList:
			threads.append(threading.Thread(target=scan,args=(ip,int(x),)))
		try:
			for t in threads:  
				t.start()
		except:
			print '不能开启新的线程'

		try:
			for t in threads:
				t.join()
		except:
			print '线程出错~'

def doActionB(start,end):
	threads = []
	for x in xrange(int(start),int(end)):  
				threads.append(threading.Thread(target=scan,args=(ip,int(x),)))
	try:
		for t in threads:
			t.start()
	except:
		print '不能开启新的线程'

	try:
		for t in threads:
					t.join()
	except:
		print '线程出错~'


#获取全端口数组
def getAllPortList():
	l = [[0, 500], [500, 1000], [1000, 1500], [1500, 2000], [2000, 2500], [2500, 3000], [3000, 3500], [3500, 4000], [4000, 4500], [4500, 5000], [5000, 5500], [5500, 6000], [6000, 6500], [6500, 7000], [7000, 7500], [7500, 8000], [8000, 8500], [8500, 9000], [9000, 9500], [9500, 10000], [10000, 10500], [10500, 11000], [11000, 11500], [11500, 12000], [12000, 12500], [12500, 13000], [13000, 13500], [13500, 14000], [14000, 14500], [14500, 15000], [15000, 15500], [15500, 16000], [16000, 16500], [16500, 17000], [17000, 17500], [17500, 18000], [18000, 18500], [18500, 19000], [19000, 19500], [19500, 20000], [20000, 20500], [20500, 21000], [21000, 21500], [21500, 22000], [22000, 22500], [22500, 23000], [23000, 23500], [23500, 24000], [24000, 24500], [24500, 25000], [25000, 25500], [25500, 26000], [26000, 26500], [26500, 27000], [27000, 27500], [27500, 28000], [28000, 28500], [28500, 29000], [29000, 29500], [29500, 30000], [30000, 30500], [30500, 31000], [31000, 31500], [31500, 32000], [32000, 32500], [32500, 33000], [33000, 33500], [33500, 34000], [34000, 34500], [34500, 35000], [35000, 35500], [35500, 36000], [36000, 36500], [36500, 37000], [37000, 37500], [37500, 38000], [38000, 38500], [38500, 39000], [39000, 39500], [39500, 40000], [40000, 40500], [40500, 41000], [41000, 41500], [41500, 42000], [42000, 42500], [42500, 43000], [43000, 43500], [43500, 44000], [44000, 44500], [44500, 45000], [45000, 45500], [45500, 46000], [46000, 46500], [46500, 47000], [47000, 47500], [47500, 48000], [48000, 48500], [48500, 49000], [49000, 49500], [49500, 50000], [50000, 50500], [50500, 51000], [51000, 51500], [51500, 52000], [52000, 52500], [52500, 53000], [53000, 53500], [53500, 54000], [54000, 54500], [54500, 55000], [55000, 55500], [55500, 56000], [56000, 56500], [56500, 57000], [57000, 57500], [57500, 58000], [58000, 58500], [58500, 59000], [59000, 59500], [59500, 60000], [60000, 60500], [60500, 61000], [61000, 61500], [61500, 62000], [62000, 62500], [62500, 63000], [63000, 63500], [63500, 64000], [64000, 64500], [64500, 65000], [65000, 65500], [65500, 65534]]
	return l



if __name__=='__main__':
	parse = optparse.OptionParser("Usage: %prog [options] target")
	parse.add_option("-i","--ip",dest="ip",type="string",help="target ip")
	parse.add_option("-w","--way",dest="way",default = 'm',type="string",help="Port scanning mode selection, m is the default port, a is the full port detection, x-y is the designated port detection (x,y is the port value) 	")
	(opt,args)=parse.parse_args()
	#IP = gethostbyname(Host)
	if opt.ip == None:
		print'help: python portscan.py -h'
		print'Usage: python portscan.py -i [IP] -w [opt]'
		print'eg: python portscan.py -i 149.129.122.123 -w m'
		sys.exit(0)
	#ip = sys.argv[1]
	#ip = str(sys.argv[1])
	ip = opt.ip
	way = opt.way
	print "目标主机:%s"%ip
	start_time=time.time()
	main(ip,way)
	print '扫描结束：'+str(time.time()-start_time)
