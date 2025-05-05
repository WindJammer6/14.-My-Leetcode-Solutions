class Solution:
    def minDominoRotations(self, tops, bottoms):
        counter_dict = {}
        counter_dict_for_each_element_in_tops = {}
        counter_dict_for_each_element_in_bottoms = {}
        
        for i in range(len(tops)):
            if tops[i] == bottoms[i]:
                if (tops[i] in counter_dict):
                    counter_dict[tops[i]] += 1
                else:
                    counter_dict[tops[i]] = 1

            else:
                if (tops[i] in counter_dict):
                    counter_dict[tops[i]] += 1
                else:
                    counter_dict[tops[i]] = 1

                if (bottoms[i] in counter_dict):
                    counter_dict[bottoms[i]] += 1
                else:
                    counter_dict[bottoms[i]] = 1

            
            # Handle the counter dict for each element in tops and bottoms
            if (tops[i] in counter_dict_for_each_element_in_tops):
                counter_dict_for_each_element_in_tops[tops[i]] += 1
            else:
                counter_dict_for_each_element_in_tops[tops[i]] = 1

            if (bottoms[i] in counter_dict_for_each_element_in_bottoms):
                counter_dict_for_each_element_in_bottoms[bottoms[i]] += 1
            else:
                counter_dict_for_each_element_in_bottoms[bottoms[i]] = 1


        print(counter_dict)
        print(f"Tops: {counter_dict_for_each_element_in_tops}")
        print(f"Bottoms: {counter_dict_for_each_element_in_bottoms}")



        # Get elements that can fill all the tops and bottoms
        elements_that_can_fill = []

        for key, value in counter_dict.items():
            if value == len(tops):
                elements_that_can_fill.append(key)

        print(elements_that_can_fill)

        if elements_that_can_fill == []:
            return -1


        # For each element that can fill all the tops and bottoms, see which one requires the least 
        # rotations

        # To handle if the element don't exist in either tops or bottoms
        #--code--

        min_rotations = 10000000000000000
        for element in elements_that_can_fill:
            if (len(tops) - counter_dict_for_each_element_in_tops[element] < len(tops) - counter_dict_for_each_element_in_bottoms[element]):
                if len(tops) - counter_dict_for_each_element_in_tops[element] < min_rotations:
                    min_rotations = len(tops) - counter_dict_for_each_element_in_tops[element]

            else: 
                if len(tops) - counter_dict_for_each_element_in_bottoms[element] < min_rotations:
                    min_rotations = len(tops) - counter_dict_for_each_element_in_bottoms[element]


        return min_rotations
        

solution = Solution()
print(solution.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(solution.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
