from pdb import set_trace

class Permute:
    def __init__(self): 
        pass

    def _recurse(self, arr, i=0):
        if isinstance(arr, str):
            arr = list(arr)
        if i == len(arr)-1:
            print("".join(arr))
        else:
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                self._recurse(arr, i+1)
                arr[i], arr[j] = arr[j], arr[i]
                

    def generate_permutations(self, arr):
        """ Generate all permutations

        Parameters
        ----------
        arr: list or str
            An array like datastructure or a string
        
        Returns
        -------
        list:
            A list of all possible permutations
        """

        if len(arr) == 1:
            return [arr]

        result = []
        for i, cur in enumerate(arr):
            rem = arr[:i]+arr[i+1:]
            for sub_str in self.generate_permutations(rem):
                result.append(cur+sub_str)
        return result

if __name__ == "__main__":
    p = Permute()
    p._recurse('abcd')
        
