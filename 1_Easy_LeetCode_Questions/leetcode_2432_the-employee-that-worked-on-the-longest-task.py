class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_value = logs[0][1]
        index_of_max_value = logs[0][0]

        hard_workers = [index_of_max_value]

        for i in range(1, len(logs)):
            # print(f"Max value: {max_value}")
            # print(f"Value: {logs[i][1] - logs[i-1][1]}")
            if logs[i][1] - logs[i-1][1] > max_value:
                max_value = logs[i][1] - logs[i-1][1]
                index_of_max_value = logs[i][0]
                hard_workers = [index_of_max_value]
            elif logs[i][1] - logs[i-1][1] == max_value:
                hard_workers.append(logs[i][0])

            # print(hard_workers)

        return min(hard_workers)


solution = Solution()
print(solution.hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))   # 1
print(solution.hardestWorker(26, [[1,1],[3,7],[2,12],[7,17]]))  # 3
print(solution.hardestWorker(10, [[0,10],[1,20]]))              # 0
print(solution.hardestWorker(70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))   # 12