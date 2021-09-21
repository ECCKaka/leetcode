#
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def spiralOrder(self , matrix):
        # write code here
        if len(matrix)==0:
            return []
        elif len(matrix)==1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            ans = []
            for i in matrix:
                ans.append(i[0])
            return ans
            
        ans = []
        visited = []
        for i in range(len(matrix)):
            visited.append([])
            for j in range(len(matrix[i])):
                visited[i].append(False)

        current_row = 0
        current_col = 0
        min_row = 0
        min_col = 0
        max_row = len(matrix)
        max_col = len(matrix[0])
        game = True
        while min_row <= max_row:
            while current_col<max_col and visited[current_row][current_col] == False:
                visited[current_row][current_col] = True
                ans.append(matrix[current_row][current_col])
                current_col+=1
            current_col-=1
            current_row+=1
            min_row+=1

            while current_row<max_row and visited[current_row][current_col] == False:
                visited[current_row][current_col] = True
                ans.append(matrix[current_row][current_col])
                current_row+=1
            current_row-=1

            current_col-=1
            max_col-=1

            while current_col>=min_col and visited[current_row][current_col] == False:
                visited[current_row][current_col] = True
                ans.append(matrix[current_row][current_col])
                current_col-=1
            current_col+=1
            min_col += 1
            current_row-=1
            while current_row>=min_row and visited[current_row][current_col] == False:
                visited[current_row][current_col] = True
                ans.append(matrix[current_row][current_col])
                current_row-=1
            max_row -= 1
            current_row += 1
            current_col += 1

        return ans