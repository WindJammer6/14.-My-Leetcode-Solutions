#I was trying to pick a sorting algorithm I have learnt to sort the 'children_greed_list' and
#'cookies_size_list'. Initially I tried using Bubble Sort but it didn't work, and Leetcode keep
#giving the error 'Time Limit Exceeded' when it tries to use a large data set for the 2 Lists
#even though it produced the correct output when I try to run it in VS code 

#However, when I tried using Quick Sort, Leetcode accepted the answer, and didn't give the 'Time 
#Limit Exceeded' error. This goes to show the importance of choosing the right sorting Algorithm.

#Quick Sort Algorithm is in nature faster in terms of Big O Notation of Time Complexity of 
#O(n logn) than Bubble Sort, which has a Big O Notation of Time Complexity of O(n^2) instead 
#which likely is what allowed my program to keep within the time limit of the large data set 
#testcase for this Leetcode question (as compared to if I used Bubble Sort Algorithm instead to
#sort my 'children_greed_list' and 'cookies_size_list' for the large data set testcase)


#Bubble Sort Algorithm (dosen't work for this Leetcode question)
# def bubble_sort(number_list):
#     size = len(number_list)

#     for i in range(size - 1):
#         swapped = False

#         for j in range(size - 1 - i):
#             if number_list[j] > number_list[j+1]:
#                 temp = number_list[j]

#                 number_list[j] = number_list[j+1]
#                 number_list[j+1] = temp
#                 swapped = True

#         if not swapped:
#             break


#Quick Sort Algorithm (works for this Leetcode question)
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        quick_sort(g, 0, len(g)-1)
        quick_sort(s, 0, len(s)-1)
        print(g)
        print(s)

        content_children_counter = 0
        g_index = 0

        for i in s:
            if g_index < len(g):
                if g[g_index] <= i:
                    content_children_counter += 1
                    g_index += 1
            else:
                break

        return content_children_counter
                    

chilldren_greed_list = [1,2]
cookies_size_list = [1,2,3]

solution = Solution()

print(solution.findContentChildren(chilldren_greed_list, cookies_size_list))