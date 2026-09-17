def shut_down(s):
    return ("yes" , "no")

if shut_down(s) == "yes":
    return"Shutting down"
elif s == "no":
    return"Shutdown aborted"
else: 
    return"Sorry"
