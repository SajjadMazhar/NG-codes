n10=int(input("No. of 10 rupee note = "))
n20=int(input("No. of 20 rupee note = "))
n50=int(input("No. of 50 rupee note = "))
n100=int(input("No. of 100 rupee note = "))
n200=int(input("No. of 200 rupee note = "))
n500=int(input("No. of 500 rupee note = "))
n2000=int(input("No. of 2000 rupee note = "))
t10=10*n10
t20=20*n20
t50=50*n50
t100=100*n100
t200=200*n200
t500=500*n500
t2000=2000*n2000
ex=int(input("Extra change(if any) = "))
total=t10+t20+t50+t100+t200+t500+t2000+ex
print(f"\n Total amount = ₹{total} ")