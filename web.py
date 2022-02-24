import uasyncio as asyncio
from nanoweb import Nanoweb
import network,gc
import ure,ujson

ap = network.WLAN(network.AP_IF)
ap.active(True) 
ap.config(essid='mpy',authmode=network.AUTH_OPEN) 


naw = Nanoweb()


ha=["wifi","password","api","api2","ot"]
def c_html(ea):
    html_b="""
    <html>
        <head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1"><title>设置你的micropython</title></head>
        <body>
            <h1>你的配置更改位</h1>
            <ul>
    """
    html_e="""
                
            </ul>
        </body>
    </html>
    """
    c=""
    for i in ea:
        b="<li><h2><b>%s</b>:%s</h2></li>" % (i,ea[i])
        c=c+b
    return html_b+c+html_e
    
    
    
def s_html(ha):
    html_b="""
    <html>
        <head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1"><title>设置你的micropython</title></head>
        <body>
            <h1>设置你的micropython</h1>
            <form>
    """
    html_e="""
                <button>提交</button>
            </form>
        </body>
    </html>
    """
    c=""
    for i in ha:
        b="%s <input type='text' name='%s'> <br>" % (i,i)
        c=c+b
    return html_b+c+html_e
        
def urem(xt,c):
    p=str(xt)+"=(.+?)&"
    m=ure.search(p,c)
    rex={"status":False,"bak":False}
    if m:
        rex['bak']=m.group(1)
        rex['status']=True
    return rex
    
    

@naw.route("/")
def ping(request):
    qu=request.url
    await request.write("HTTP/1.1 200 OK\r\n\r\n")
    html=s_html(ha)
    await request.write(html)

@naw.route("/?*")
def ping(request):
    conf={}
    for i in ha:
        c=urem(i,request.url+"&")
        if c['status']:
            conf[i]=c["bak"]
    html=c_html(conf)
    f=open("config.ini",'w')
    f.write(ujson.dumps(conf))
    f.close()
    await request.write("HTTP/1.1 200 OK\r\n\r\n")
    await request.write(html)



loop = asyncio.get_event_loop()
loop.create_task(naw.run())
#loop.run_forever()

