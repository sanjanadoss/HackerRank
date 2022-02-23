#failed in one of the test cases for runtime error 

if "PM" in s:
        x = s.split(":")
        n1 = x[0]
        n1 = int(n1)
        if n1<12:
            n1 = n1 + 12
            n1 = str(n1)
        n2 = x[1]
        n3 = x[2].split("PM")
        n4 = n3[0]
        final1 = n1+":"+n2+":"+n4
        return final1
if "AM" in s:
    x = s.split(":")
    n1 = x[0]
    if n1=="12":
        n1 = "00"
    n2 = x[1]
    n3 = x[2].split("AM")
    n4 = n3[0]
    final2 = n1+":"+n2+":"+n4
    return final2