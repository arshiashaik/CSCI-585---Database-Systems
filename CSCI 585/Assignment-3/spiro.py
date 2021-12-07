import math
import numpy as numpy
import simplekml

kml = simplekml.Kml()

R,r,a = 8,1,4;
x0,y0,pie = (R + r - a),0,(math.pi);
nReverse = 16;
for t in numpy.arange(0.0, pie*nReverse, 0.1):
	x = (R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t);
	y = (R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t);
	ttpoint1 = -118.28533453255395;
	ttpoint2 = 34.020253880814293;
	kml.newpoint(coords=[((ttpoint1+0.0005*x),(ttpoint2+0.0005*y))])

kml.save("spiro.kml")

