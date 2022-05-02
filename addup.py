from xml.dom.expatbuilder import FilterVisibilityController


def addup(n):
    a = 0
    for i in range(1, n+1):
        a = a + i
    return a

print(addup(10))    
        