class TMMissing: pass
class TMRange:
    def __init__(self,start,end=TMMissing(),step=1):
        if (type(end) is TMMissing)==True:
            end=start
            start=1
        if isinstance(start,int)==False:
            raise TypeError(f"Value of start should be of type {type(33)}, found {type(start)}")
        if isinstance(end,int)==False:
            raise TypeError(f"Value of end should be of type {type(33)}, found {type(end)}")
        if isinstance(step,int)==False:
            raise TypeError(f"Value of step should be of type {type(33)}, found {type(step)}")
        if step==0: raise ValueError(f"start is {start},end is {end} and step is {step} this leads to infinite range")
        if start<end and step<0: raise ValueError(f"starts is {start}, end is {end} and step is {step},this leads to infinite range")
        if start>end and step>0: raise ValueError(f"starts is {start}, end is {end} and step is {step},this leads to infinite range")
        self.start=start
        self.end=end
        self.step=step
    def __str__(self):
        return f"TMRange({self.start},{self.end})"
    def __iter__(self):    
        iterator=TMRangeIterator(self)
        return iterator
class TMRangeIterator:
    def __init__(self,obj):
        self.start=obj.start
        self.end=obj.end
        self.step=obj.step
        self.current=self.start
    def __next__(self): 
        if self.step>0:
            if self.current>self.end: raise StopIteration
        else:
            if self.current>self.end: raise StopIteration
        data=self.current
        self.current+=self.step
        return data
    def __str__(self):
        return f"TMRangeIterator({self.start},{self.end})"        