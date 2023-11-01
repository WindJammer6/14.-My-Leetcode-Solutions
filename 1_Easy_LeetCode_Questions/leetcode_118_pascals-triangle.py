#An important characteristic of the Pascal's Triangle I realised is that it is symmetrical! Hence, all the
#rows of numbers are symmetrical as well.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        #To consider the case if the numRows input is 0
        if numRows == 0:
            return []
        #To consider the case if the numRows input is 1
        if numRows == 1:
            return [[1]]
        


        else:
            pascal_triangle = [[1], [1,1]]

            #Iterating through each numbered row to print out the rows of the Pascal's triangle
            for i in range(2, numRows):
                print(i)

                #This if else statement is used to split the scenarios when that numbered row contains an even 
                #or odd number of numbers
                #If that numbered row contains an even number of numbers in that row:
                if i % 2 == 0:
                    row_of_numbers = [1]
                    center_index_point = i/2    #the center point is not exactly 'i/2', but the center index 
                                                #point is in between elements at the index given and the -1 
                                                #of the index given in the numbered row. Even numbered rows
                                                #do not have a center index element, but the center index point
                                                #is shared by 2 same elements at the left and right of the 
                                                #center index point
                    
                    #Using the two pointers paradigm to add every 2 elements together until the second pointer
                    #reaches the center index point and does the last reiteration with the right middle element 
                    #to the center index point
                    first_pointer = 0
                    second_pointer = 1

                    #Adding every 2 numbers and appending to the 'row_of_numbers' Array

                    #Using the previous numbered row's numbers in the Pascal's Triangle when referring with 
                    #the two pointers, 'first_pointer' and 'second_pointer' by using 
                    #'pascal_triangle[i-1][first_pointer]' and 'pascal_triangle[i-1][second_pointer]'
                    while second_pointer <= center_index_point:
                        row_of_numbers.append(pascal_triangle[i-1][first_pointer] + pascal_triangle[i-1][second_pointer])
                        first_pointer += 1
                        second_pointer += 1


                    #Leverging on the symmetrical nature of the Pascal's Traingle and hence its rows, we will 
                    #duplicate the Array, but in reverse for the remaining numbers in the numbered row/Array

                    #Used '[:-1]' for the even numbers if statement unlike the odd number else statment to 
                    #exclude the center index number being duplicated symmetrically in the row since after an 
                    #evem number row, the next row (which is the numbered row you are creating in this 
                    #iteration of the for loop) will be an odd number row with only 1 number taking the middle 
                    #of the row/array (while for even number rows/Array there is 2 numbers sharing the middle 
                    #being the same)
                    for i in reversed(row_of_numbers[:-1]):
                        print("index", i)
                        row_of_numbers.append(i)

                    pascal_triangle.append(row_of_numbers)



                #If that numbered row contains an odd number of numbers in that row:
                else:
                    row_of_numbers = [1]
                    center_index_point = i//2   #this is the center element's index of the numbered row and it 
                                                #refers directly to the sole middle element in an odd number row

                    #Using the two pointers paradigm to add every 2 elements together until the second pointer
                    #reaches the center index point and does the last reiteration with the right middle element 
                    #to the center index point
                    first_pointer = 0
                    second_pointer = 1

                    #Adding every 2 numbers and appending to the 'row_of_numbers' array

                    #Using the previous numbered row's numbers in the Pascal's Triangle when referring with 
                    #the two pointers, 'first_pointer' and 'second_pointer' by using 
                    #'pascal_triangle[i-1][first_pointer]' and 'pascal_triangle[i-1][second_pointer]'
                    while second_pointer <= center_index_point:
                        row_of_numbers.append(pascal_triangle[i-1][first_pointer] + pascal_triangle[i-1][second_pointer])
                        first_pointer += 1
                        second_pointer += 1


                    #Leverging on the symmetrical nature of the Pascal's Traingle and hence its rows, we will 
                    #duplicate the array, but in reverse for the remaining numbers in the row/array

                    #Dont have the '[:-1]' for the odd numbers else statement unlike for the even numbers if 
                    #statement to include the center number being duplicated symmetrically in the row since 
                    #after an odd number row, the next row in an even number row with the 2 numbers sharing 
                    #the middle being the same
                    for i in reversed(row_of_numbers):
                        row_of_numbers.append(i)

                    pascal_triangle.append(row_of_numbers)


        return pascal_triangle

        
number_of_rows = 7

solution = Solution()

print(solution.generate(number_of_rows))