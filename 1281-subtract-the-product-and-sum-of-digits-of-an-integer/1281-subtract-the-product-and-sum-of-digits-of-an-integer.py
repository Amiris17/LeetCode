class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        


        product_list=[]
        sum_list=[]
        
        product_=1 # NEEDS TO BE 1
        my_sum=0 
        result=0
        
        
        my_str=str(n)
        
        
        for i in my_str:
            product_list.append(i)
            sum_list.append(i)
        
        #now we have them stored in list lets multiply them after we convert them to integers to avoid type conversion errors
        product_list2=[int(items) for items in product_list]
        print(product_list2)      
        
        sum_list2=[int(items) for items in sum_list]

        
        for j in sum_list2:
            my_sum+=j
            print(my_sum)
            
        for k in product_list2:
            product_= product_*k
            print(product_)
    
    
        return product_-my_sum