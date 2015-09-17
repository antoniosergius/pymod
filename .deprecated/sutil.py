import re

def midtxt(text, width):
    text = str(text)
    blanks = width-len(text)
    right=blanks//2
    left=right+blanks%2
    return left*' '+text+right*' '

def printASCII():
    printRangeASCII(32, 255)

def printRangeASCII(start, end):
    ordList=[]
    chrList=[]
    for i in range(start, end+1):
        ordList.append(midtxt(i,4))
        chrList.append(midtxt(chr(i),4))
    textUp='chr:'
    textDown='ord:'
    fullTxt=''
    for i in range(0,len(ordList)):
        if i!=0 and i%16==0:
            fullTxt+='\n'+textUp+'\n'+textDown+'\n'
            textUp='chr:'
            textDown='ord:'
        textUp+=chrList[i]
        textDown+=ordList[i]
    fullTxt+='\n'+textUp+'\n'+textDown+'\n'
    print(fullTxt)    

def cutStrSides(s):
    return s[1:len(s)-1]
        
def oneTriangleInt(n):
    for i in range(n, 0, -1):
        x = 0
        for j in range(0,i):
            x = x*10+1
        print(x)

def oneTriangleStr(n):
    for i in range(n, 0, -1):
        print('1'*i)

def adder(expr):
    oper = expr.index("+")
    pref = int(expr[0:oper])
    suf = int(expr[oper+1:len(expr)])
    return pref+suf

def substringCount(sub, string):
    if isinstance(sub, str) and isinstance(string, str):
        if len(sub)==0:
            return 0
        i = 0
        repeated = 0;
        while i < len(string):
            if string[i:i+len(sub)]==sub:
                repeated += 1
            i += 1
        return repeated
    else:
        return -1

#def timeAfter(stime, toAdd):
	#if type(stime)!=str and type(toAdd)!=int:
		#raise TypeError("Invalid types.")
	#time=stime.partition(":")	
	#if stime.find(":")==-1 or stime.count(":")>1 or time[1]!=':':
		#raise ValueError("Invalid time format.")
	#hour=time[0]
	#minute=time[2]
	#if len(hour)!=2 or len(minute)!=2:
		#raise ValueError("Invalid time format.")
	#hour=int(hour)
	#minute=int(minute)+toAdd
	#if minute>60:
		#hour += minute//60
		#minute = minute%60
	#if hour>=24:
		#if hour==24:
			#hour=0
		#else:
			#hour %= 24
	#return "%02d:%02d" % (hour,minute)
	
def addMinutes(stime, toAdd):
	if type(stime)!=str and type(minute)!=int:
		raise TypeError("Invalid types.")
	regex=re.compile("\d{0,1}\d:\d\d")
	match=regex.match(stime)
	if not match:
		raise ValueError("Invalid time format.")
	time=stime.partition(":")	
	hour=int(time[0])
	minute=int(time[2])+toAdd
	if minute>60:
		hour += minute//60
		print(hour)
		minute = minute%60
		print(minute)
	if hour>=24:
		if hour==24:
			hour=0
		else:
			hour = hour%24
	return "%02d:%02d" % (hour,minute)


