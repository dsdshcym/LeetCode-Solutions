# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        def dfs(node):
            if not node:
                return node
            new_node = UndirectedGraphNode(node.label)
            visited[node] = new_node
            for neighbor in node.neighbors:
                if neighbor in visited:
                    new_node.neighbors.append(visited[neighbor])
                else:
                    new_node.neighbors.append(dfs(neighbor))
            return new_node

        visited = {}
        return dfs(node)

t = Solution()
node = UndirectedGraphNode(0)
node.neighbors = [0, 0]

new_node = t.cloneGraph(node)
assert(new_node.neighbors == [0, 0])
assert(new_node.label == 0)
print("tests passed")
