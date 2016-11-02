#a/r forward hedge


AR = 200000.0
ForwardRate = 1.10

ForwardHedge = AR * ForwardRate

print "test", ForwardHedge


#use code above to check accuracy of code below
#-------------------------------------------------------------------------------
#use code below in CLI

AR = float(input("What are your Account Receivables?"))
ForwardRate = input("What is the forward Rate?")

ForwardHedge = AR * ForwardRate

print "Your Forward Hedge for Account Receivables is", ForwardHedge
