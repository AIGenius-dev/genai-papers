class BytePairEncoding:
    def __init__(self,input_string):
        self.input=input_string
        self.tokens=list(input_string)
        
    def get_pair_frequency(self):
        pairs={}
        for i in range(len(self.tokens)-1):
            pair=(self.tokens[i],self.tokens[i+1])
            pairs[pair]=pairs.get(pair,0)+1
        return pairs
        
    def merge_tokens(self,pair):
        new_tokens=[]
        i=0
        while i < len(self.tokens):
            if i<len(self.tokens)-1 and (self.tokens[i],self.tokens[i+1])==pair:
                new_tokens.append(self.tokens[i]+self.tokens[i+1])
                i=i+2
            else:
                new_tokens.append(self.tokens[i])
                i=i+1
        return new_tokens
        
    def train(self):
        pairs={}
        for i in range(10):
            pairs=self.get_pair_frequency()
            print(f"Iteration {i+1}:")
            if not pairs:
                print("No more pairs to merge!")
                break
            print(f"Pairs: {pairs}")
            max_frequency_pair=max(pairs,key=pairs.get)
            print(f"Max frequency pair: {max_frequency_pair}")
            self.tokens=self.merge_tokens(max_frequency_pair)
            print(f"Tokens after merging: {self.tokens}\n")
        return self.tokens
bytepairencoding=BytePairEncoding(f"Ishwari is a developer. Ishwari writes her code herself. Ishwari love to intelligently do her work by herself.")
print(bytepairencoding.train())    