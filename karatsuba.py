import math

class karatsuba:

	def _init__(self):
		print "Karatsuba online!"

	def multiply(self, x, y):
		sx = str(x)
		sy = str(y)
		#print "Multiplying %s and %s" % (sx, sy)
		nx = len(sx)
		ny = len(sy)
		if nx==1 or ny==1:
			r = int(x)*int(y)
			#print "returning " + str(r)
			return r
		n = nx
		if nx>ny:
			sy = sy.rjust(nx, '0')
			n = nx
		elif ny>nx:
			sx = sx.rjust(ny, '0')
			n = ny
		#print sy
		#print sx
		m = n % 2
		offset = 0
		even = n
		if m!=0:
			n+=1
			#print "N is now " + str(n)
			offset = 1
		floor = int(math.floor(n/2))-offset
		ceil = int(math.ceil(n/2))-offset
		a = sx[0:floor]
		b = sx[ceil:n]
		c = sy[0:floor]
		d = sy[ceil:n]
		r = ((10**n)*self.multiply(a,c)) + ((10**(n/2))*(self.multiply(a,d) + self.multiply(b,c))) + self.multiply(b,d)
		#print "returning" + str(r)
		return r


k = karatsuba();
print k.multiply(4,5)
print k.multiply(47,5)
print k.multiply(4,5087)
print k.multiply(773920,583922303)
print k.multiply(6538945,3409127)
