class Solution():
  def isHappy(self, n: int) -> bool:
    
    n = str(n)
    
    previous_loop_total = "temp string"
    loop_checking_list = []
        
    while True:
      prev_total = previous_loop_total
      temp_total = 0
      
      #Iterating and adding up the squares of the numbers in the variable n
      for i in n:
        temp_total += int(i) * int(i)
       
        
      #For case if number is stuck at/reaches 1
      if temp_total == 1:
        return True
      #If nothing else then let n be the new total of the squared numbers from the previous variable n
      else:
        previous_loop_total = temp_total
        n = str(temp_total)
     
                    
      #If the while loop keeps looping around the same 'temp_total' endlessly without ever reaching 1, 
      #but does not go to 1      
      if temp_total in loop_checking_list:
        return False
      else:
        loop_checking_list.append(temp_total)
        
 
number = 1111111
solution = Solution()
print(solution.isHappy(number))