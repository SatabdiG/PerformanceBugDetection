#This contains datastructues necessary for code

class Stack(object):

    def __init__(self):
        self.items=[]

    def push(self,items):
        self.items.append(items)

    def pop(self):
        if(len(self.items)>0):
          return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def count(self):
        count=len(self.items)
        return count

