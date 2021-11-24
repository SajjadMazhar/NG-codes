import pyramid_def as pyr
m=int(input())
pyr.pyramid(m)

for j in range(1,1+m):
	print(end=" ")
	print((1+m-j)*"* ")
	print(j*" ",end="")