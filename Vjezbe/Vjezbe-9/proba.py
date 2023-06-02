import two_body_system as tbs

b1=tbs.Body("sunce","y",1.989*10**30,0,0)
b2=tbs.Body("zemlja","b",5.9742*10**24,1.486*10**11,29783)
ss=tbs.System(b1,b2)
ss.simulate(0.001)