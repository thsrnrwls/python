class CounterManager:
    insCount = 0
    
    def __init__(self):
        CounterManager.insCount += 1

    def staticPrintCount():
        print("Instance Count : ", CounterManager.insCount)
        
    SPrintCount = staticmethod(staticPrintCount)

    def classPrintCount(cls):
        print("Instance Count: ", cls.insCount)
        
    CPrintCount = classmethod(classPrintCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()

b.SPrintCount()

b.CPrintCount()
