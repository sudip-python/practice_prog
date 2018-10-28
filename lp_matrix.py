mat1 = [[1,2,9],
        [5,3,8],
        [4,6,7]]

class LongPath(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
    
    def isSafe(self, i, j, visited):
        if i >= self.columns or i < 0 or j >= self.rows or j < 0:
            return False
        if visited[i][j] == True:
            return False
        return True

    def longestPathUtils(self, visited, i, j, my_list):
        four_pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited[i][j] = True
        cur_num = self.matrix[i][j]
        for pos in four_pos:
            cur_i = i + pos[0]
            cur_j = j + pos[1]
            if self.isSafe(cur_i, cur_j, visited):
                if self.matrix[cur_i][cur_j] == cur_num + 1 or self.matrix[cur_i][cur_j] == cur_num - 1:
                    my_list.append(self.matrix[cur_i][cur_j])
                    self.longestPathUtils(visited, cur_i, cur_j, my_list)

    def longestPath(self):
        final_list = []
        for i in range(self.rows):
            for j in range(self.columns):
                visited = [[0,0,0],[0,0,0],[0,0,0]]
                my_list = [self.matrix[i][j]]
                self.longestPathUtils(visited, i, j, my_list)
                if len(final_list) < len(my_list):
                    final_list = my_list
        print final_list

lP = LongPath(mat1)
lP.longestPath()
