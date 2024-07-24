from abc import ABCMeta, abstractmethod 
from Bubble import *
from Insertion import *
 
class Context():

    "This is the object whose behavior will change" 
    @staticmethod

    def request(strategy):         
        "The request is handled by the class passed in"         
        return strategy() 
 
class IStrategy(metaclass=ABCMeta):

    "A strategy Interface"

    lst1 = [2,10,8,90,0,-1,-90] 
    @staticmethod     
    @abstractmethod     
    def lst():         
        return IStrategy.lst1

class Bubble(IStrategy):

    def lst():
        bubbleSort(IStrategy.lst1)
        return IStrategy.lst1

class Insertion(IStrategy):
    
    def lst():
        insertionSort(IStrategy.lst1)
        return IStrategy.lst1

# The Client 
CONTEXT = Context()   
print('Bubble Sort =',Bubble.lst())
print('Insertion Sort =',Insertion.lst())
print(CONTEXT.request(Bubble.lst())) 
print(CONTEXT.request(Insertion.lst())) 