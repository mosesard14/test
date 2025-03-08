def runner_up(a, b, c, d, e):
    if a < b :
        p1 = a
        p2=b
    else:
        p1=b
        p2=a
    if c<p1 :
        p2 = p1
        p1=c
    elif c<p2:
        p2=c
    if d<p1 :
        p2 = p1
        p1=d
    elif d<p2:
        p2=d

    if e<p1 :
        p2 = p1
        p1=e
    elif e<p2:
        p2=e

    return p2

    
# print(runner_up(9.76, 9.9, 10.0, 9.62, 9.78))
# print(runner_up(1,2,3,4,5))
# print(runner_up(1,3,2,4,5))
# print(runner_up(6,7,8,9,10))
print(runner_up(9.51, 9.49, 9.99, 9.72, 9.70))