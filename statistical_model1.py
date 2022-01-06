class statistical_model1():
   
   
    def __init__(self, data):  
        
        self.data = data  #av type list
        
        if len(self.data)==0:
            raise Exception("Your array is empty.")
        if type(self.data) != list:
            raise Exception("Your data  must be of type 'list'! ")
                  
        
    def max(self):   
        max_v=self.data[0]       
        for obs in self.data:
            if obs > max_v:
                max_v=obs
        return max_v
    
    def min(self):
        min_v=self.data[0]
        for obs in self.data:
            if obs < min_v:
                min_v=obs
        return min_v
    
    
    
    def range(self):
        return self.max()-self.min()
        
    def mode(self):
        """
        fre_dic{obsrvation: frequency, ....}
        return an integer, the most frequent observation
        """
        freq_dic={} 
        
        for obs in self.data:
            if obs in freq_dic:
                freq_dic[obs] +=1
            else:
                 freq_dic[obs] =1
               
        keys = list(freq_dic.keys())
        vals = list(freq_dic.values()) 
                 
        pos=vals.index(max(vals))  #index of the most freq. val
        
        return keys[pos] 
    
    
    def median(self):
        """
        #if case the length og data is even number, we take the average of the two middle values
        """
        sorted_data= sorted(self.data)
        
        if (len(sorted_data)%2)==1: #check if n is odd nr.
            return sorted_data[int(len(sorted_data)/2)]
            
        else:
            
            return( sorted_data[int(len(sorted_data)/2 )-1 ] + sorted_data[int(len(sorted_data)/2)]  ) / 2
              
            
    def mean(self): 
        count=0
        for obs in self.data:
            count+=obs
            
        return count/len(self.data)        
              
        
    def variance(self):
        mn=self.mean()
        
        sub_from_mean=[i-mn for i in self.data]
        
        squred_vals=[i*i for i in sub_from_mean]   #squre the values
       
        count=0
        for  value in squred_vals:
            count+=value 
        print(count)   
        return count/(len(squred_vals)-1)
    
    def standard_diviation(self):
        return (self.variance())** 0.5   #The square root
        
    def quartiles(self):
        sorted_data= sorted(self.data)
       
        obj1=statistics_model1(sorted_data[0:int(len(sorted_data)/2)]) #  a new data set, from pos.0-median to find Q1
        obj2=statistics_model1(sorted_data[int(len(sorted_data)/2)+1:]) #  a new data set, from pos.median to -1  to find Q1
        
        #find quertiles
        Q1=obj1.median() 
        Q2=self.median()
        Q3=obj2.median()

        #find inter-quertile
        interQ= Q3-Q1
        return Q1,Q2,Q3, interQ
    
    def z_scores(self):        
        return [(obs-self.mean())/self.standard_diviation() for obs in self.data]

    
    def detect_outliers(self):
        Q1, Q3, interQ= self.quartiles()[0], self.quartiles()[2], self.quartiles()[3]
        """parms:
        dataset: type list 
        Q1 and Q3 stands for quertile 1, quertile 3. type float
        interQ stands for interquertile.
        return: 
        list of outliers if any exits, otherwise it return empty array
        """    
        outliers=[]
        for obs in self.data:
            if obs< Q1-(interQ*1.5) or obs>Q3+(interQ*1.5):
                outliers.append(obs)
        return outliers
    
    
    #coefficient of variance, measure the scale of the data (usually for comparison)
    def coefficient_of_variance(self): 
        return self.standard_diviation()/self.mean()
