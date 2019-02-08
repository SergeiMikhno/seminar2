try:
    x = 1 / 0
except ArithmeticError:             
    print ("division by 0")
try:
    import a1 as a
except ImportError:
    print ("failed to import a module or its attribute")
try:
    print ("2"+2)
except Exception:
    print ("Cannot be concatenated")
    


