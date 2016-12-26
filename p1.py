p = [0,1,0,0,0];
world = ['green','red','red','green','green']
measurements = ['red','green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8;
pUndershoot = 0.1;
pOvershoot = 0.1;

def sense(p, Z):
    q = []

    for i in range(len(p)):
	    if world[i] == Z:
	        q.append(p[i]*pHit);
	    else:
	       q.append(p[i]*pMiss);
	prob_sum = sum(q);
    for i in range(len(q)):
	    q[i] = q[i]/prob_sum;
    return q
def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
#
# Move 1000 times
#
limit = 1000;
step = 1;
for i in range(limit):
    p = move(p,step)

#Sense & Move for the measurements & motion
p = [0.2,0.2,0.2,0.2,0.2]
for i in range(len(measurements)):
	p = sense(p,measurements[i]);
	p = move(p,motions[i])
print p

