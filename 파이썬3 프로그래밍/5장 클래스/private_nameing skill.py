class CounterManager:
    __insCount = 0

    def __init__(self):
        CounterManager.__insCount += 1

    def staticPrintCount():
        print("Instance Count: %d" %CounterManager.__insCount)

    SPrintCount = staticmethod(staticPrintCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()

CounterManager.staticPrintCount() #문제없이 작동

print(CounterManager.insCount) #직접 접근을 하려고 하면 에러 

