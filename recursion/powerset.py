class Powerset:
    def __init__(self): 
        self.powerset = []
    
    def _recurse(self, arr, index, subset):
        if index == len(arr):
            self.powerset.append(subset)
        else:
            self._recurse(arr, index + 1, subset) # Do not include the current element
            self._recurse(arr, index + 1, subset+[arr[index]]) # Include the current element

    def main(self, arr):
        self._recurse(arr, 0, [])
        return self.powerset

if __name__  == "__main__":
    ps = Powerset()
    arr = [1,2,3,4,5,6,7]
    res = ps.main(arr)
    assert len(res) == 2 ** len(arr) 
    print(res)
