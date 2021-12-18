class Decorators():
    def divby0(func):
        def inside(a,b): 
            if a==0 or b==0: print("Cannot divide by 0...");return
            else: return func()
        return inside