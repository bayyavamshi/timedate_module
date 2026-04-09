try:
    print(2/0)
except:
    try:
        print(int('1'))
    except:
        print("valueerror")
    try:
        print(90/0)
    except Exception as r:
        print(r)
else:
    try:
        print(int('vamshi'))
    except Exception as v:
        print(v)
finally:
    print("completed")
