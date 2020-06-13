
class Parent:  # define parent class
    'Parent Class'
    parentAttr = 100  
    def __init__(self):   
        print ("Calling parent constructor") 
    
    def parentMethod(self):  
        print ("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr*4

    def getAttr(self):
        print ("parent Attribute: ", Parent.parentAttr)

class Child(Parent):  # define child class
    'child Class'
    def __init__(self):  
        print ("Calling child constructor") 

    def childMethod(self):  
        print ("Calling child method")

            
c = Parent()        # instance of parent
c = Child()         #instance of child
c.childMethod()     # child callas its method
c.parentMethod()    # Call parent´s method
c.setAttr(200)      # again Call parent´s method
c.getAttr()         # again Call parent´s method

