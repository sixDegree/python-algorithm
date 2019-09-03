from timeit import Timer

def test_gen1():
   l = [i for i in range(1000)]

def test_gen2():
   l = list(range(1000))

def test_concat1():
   l = []
   for i in range(1000):
      l = l + [i]

def test_concat2():
   l = []
   for i in range(1000):
      l+=[i]

def test_append():
   l = []
   for i in range(1000):
      l.append(i)

def test_extend():
   l = []
   for i in range(1000):
      l.extend([i])


if __name__=='__main__':

    # class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
    # timeit.Timer.timeit(number=1000000)

    t1=Timer("test_gen1()","from __main__ import test_gen1")
    r1=t1.timeit(number=1000)
    t2=Timer("test_gen2()","from __main__ import test_gen2")
    r2=t2.timeit(number=1000)

    print("test_gen1 : [i for i in range(...)]   => cost: %.5fs" % r1)
    print("test_gen2 : list([range(...)])        => cost: %.5fs" % r2)
    print("`[i for i in range(...)]` - `list([range(...)])` = %.5f" % (r1-r2))

    print("***"*10)

    t1=Timer("test_concat1()","from __main__ import test_concat1")
    r1=t1.timeit(number=1000)
    
    t2=Timer("test_concat2()","from __main__ import test_concat2")
    r2=t2.timeit(number=1000)

    print("test_concat1 : l=l+[i] => cost: %.5fs" % r1)
    print("test_concat2 : l+=[i]  => cost: %.5fs" % r2)
    print("`l=l+[i]` - `l+=[i]` = %.5f" % (r1-r2))

    print("***"*10)

    t1=Timer("test_append()", "from __main__ import test_append")
    r1=t1.timeit(number=1000)

    t2=Timer("test_extend()","from __main__ import test_extend")
    r2=t2.timeit(number=1000)

    print("test_append : l.append(i)   => cost: %.5fs" % r1)
    print("test_extend : l.extend([i]) => cost: %.5fs" % r2)
    print("`l.append(i)` - `l.extend([i])` = %.5f" % (r1-r2))

    print("***"*10)

    x = list(range(2000000))
    t_pop_head=Timer("x.pop(0)","from __main__ import x")
    r1=t_pop_head.timeit(number=1000)
    
    t_pop_tail=Timer("x.pop()","from __main__ import x")
    r2=t_pop_tail.timeit(number=1000)
    
    print("pop head : pop(0)    => cost: %.5fs" % r1)
    print("pop tail : pop()     => cost: %.5fs" % r2)
    print("`pop(0)` - `pop()` = %.5f" % (r1-r2))

    print("***"*10)


# Run Result:
#
# test_gen1 : [i for i in range(...)]   => cost: 0.04163s
# test_gen2 : list([range(...)])        => cost: 0.01663s
# `[i for i in range(...)]` - `list([range(...)])` = 0.02500
# ******************************
# test_concat1 : l=l+[i] => cost: 1.22195s
# test_concat2 : l+=[i]  => cost: 0.08704s
# `l=l+[i]` - `l+=[i]` = 1.13491
# ******************************
# test_append : l.append(i)   => cost: 0.07949s
# test_extend : l.extend([i]) => cost: 0.11865s
# `l.append(i)` - `l.extend([i])` = -0.03916
# ******************************
# pop head : pop(0)    => cost: 1.70021s
# pop tail : pop()     => cost: 0.00009s
# `pop(0)` - `pop()` = 1.70012
