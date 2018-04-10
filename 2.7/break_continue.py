# simple break
abc =5
while True:
    test = int(raw_input("input:"))
    if test == abc:
        print "nice"
        break
    else:
        print "cuowu"
        test = int(raw_input("input:"))

# simple continue


for i in range(10):
    if i%2 !=0:
        print i
        continue
        i+=2
    print i