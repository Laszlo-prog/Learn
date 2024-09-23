powers = [1, 2, 3, 8, 9, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] 
   
mini, maxi = 1, 20
   
for power in powers: 
    if mini == 1 and maxi == 10: 
        mini, maxi = powers[0], powers[0] 
        print(mini, maxi) 
    else: 
        mini = min(mini, power) 
        maxi = max(maxi, power) 
        print(mini, maxi) 
        
