def code_clean(x):
    code = str(x)
    
    if len(code) == 11:
        return code[:5]
    else:
        return code[:6]        
    
def code_comm(x):
    code = str(x)
    
    if len(code) == 5:
        return code[:1]
    else:
        return code[:2]        