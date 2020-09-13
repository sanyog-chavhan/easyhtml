from html5print import HTMLBeautifier
flag=0
idcnt=0
csscode=""
code="<html>\n<head>\n<meta http-equiv='Content-Type' content='text/html; charset=utf-8'/> \n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<link rel='stylesheet' src='index.css'>\n<title>\napoorv\n</title>\n</head>\n<body style='text-align:center;margin:0'>\n<div style='overflow-x:hidden'>\n"

endcode="</div></body></html>"

comm={"add","end"}

href={"a","link"}

types={"input"}

src={"img","video","audio","script","style"}

wrappers={"div","span","form","h1","h2","h3","h4","h5",
"h6","p","strong","code","marquee","i","b","small","s","sub","sup","kbd"}
def addHref(a):
	global code,idcnt,csscode
	code=code+"<"+a[1]+" href='"+a[2]+"' id='"+a[1]+str(idcnt)+"'>"
	csscode=csscode+"#"+a[1]+str(idcnt)+"{}\n"
	idcnt=idcnt+1
def endHref(a):
	global code
	code=code+"</"+a[1]+">"	
	
def addSrc(srctype,srcContent):
	global code,idcnt,csscode
	code=code+"<"+srctype+" src='"+srcContent+"' height='200px' controls id='"+srctype+str(idcnt)+"'><br>\n</"+srctype+" >\n<br>\n"
	csscode=csscode+"#"+srctype+str(idcnt)+"{}\n"
	idcnt=idcnt+1
def addWrappers(wraptype):
	global code,idcnt,csscode
	code=code+"<"+wraptype+" id='"+wraptype+str(idcnt)+"'>\n"
	csscode=csscode+"#"+wraptype+str(idcnt)+"{}\n"
	idcnt=idcnt+1
def endWrappers(wraptype):
	global code
	code=code+"</"+wraptype+">\n"		
def addComponent(comp,comptype,compvalue):
	global code,idcnt,csscode
	s="<"+comp+" type='"+comptype+"' value='"+compvalue+"' id='"+comptype+str(idcnt)+"'/><br>"
	code=code+s
	csscode=csscode+"#"+comptype+str(idcnt)+"{}\n"
	idcnt=idcnt+1
while(flag==0):
	a=input()
	if(a=="###"):
		flag==1
		break
	else:
		a=a.split(" ");
		if(a[0].lower() in comm):
			if(a[1].lower() in types):
				gg=""
				for i in range(3,len(a)):
					gg=gg+" "+a[i]
				gg=gg.strip()
				eval(a[0]+"Component")(a[1],a[2],gg)
			elif(a[1] in wrappers):
				eval(a[0]+"Wrappers")(a[1])
			elif(a[1] in src):
				eval(a[0]+"Src")(a[1],a[2])
			elif(a[1] in href):
				print(a[0]+"Href"+a[1])
				eval(a[0]+"Href")(a)
			
				
		elif(a[0].lower() in wrappers):
			eval("addWrappers")(a[0])
		else:
			gg=""
			for i in range(0,len(a)):
				gg=gg+" "+a[i]
			gg=gg.strip()
			code=code+gg+"<br>\n"
			
	
code=code+endcode

code=HTMLBeautifier.beautify(code, 4)
f=open("index.html","w")
f.write(code)
g=open("index.css","w")
g.write(csscode)
