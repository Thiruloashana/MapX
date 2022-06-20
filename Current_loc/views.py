from django.shortcuts import render
import string
import folium
import serial
import time

mport = "/dev/ttyAMA0"            #for Raspberry Pi pins

def parseGPS(data):
    if data[0:6] == "$GPGGA":     #a kind of nmea msg format
        s = data.split(",")
        if s[7] == '0' or s[7]=='00':
            print ("no satellite data available")
            return
        time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
        lat = decode(s[2])
        lon = decode(s[4])
        return  lat,lon


def decode(coord):
    l = list(coord)
    for i in range(0,len(l)-1):
            if l[i] == "." :
                    break
    base = l[0:i-2]
    degi = l[i-2:i]
    degd = l[i+1:]
    baseint = int("".join(base))
    degiint = int("".join(degi))
    degdint = float("".join(degd))
    degdint = degdint / (10**len(degd))
    degs = degiint + degdint
    full = float(baseint) + (degs/60)
    return full

def live(request):
	ser = serial.Serial(mport,9600,timeout = 2) #braudrate(9600)-Rate at which info is  shared to the communication channel
						    #timeout-gets data from port every 2s



	flag=1
	while flag:
		try:
        		dat=ser.readline().decode()
        		mylat,mylon = parseGPS(dat)
        		flag=0
		except:
			print("error")

	m=folium.Map(location=[19,-12],zoom_start=2)
	folium.Marker([mylat,mylon]).add_to(m)
	m=m._repr_html_()
	context={
		'm':m,
	}
	return render(request,'live.html',context)

