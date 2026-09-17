def shut_down(s:str)->str:
    return ("yes" , "no")

if s == "yes":
    return "Shutting down"
elif s == "no":
    return "Shutdown aborted"
else: 
    return "Sorry"
