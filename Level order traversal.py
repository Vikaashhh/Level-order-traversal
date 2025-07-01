class Solution:
    def levelOrder(self, root):
        # Agar root hi nahi hai toh return karo empty list
        if not root:
            return []

        result = []        # Final answer list jisme levels store karenge
        queue = [root]     # Queue use karenge level by level traversal ke liye (BFS)

        # Jab tak queue mein nodes hain, hum process karte rahenge
        while queue:
            level_size = len(queue)  # Current level mein kitne nodes hain
            current_level = []       # Is level ke nodes ka data yaha store karenge

            # Har level ke saare nodes ko process karenge
            for _ in range(level_size):
                node = queue.pop(0)         # Queue se node nikalo
                current_level.append(node.data)  # Node ka data current level mein add karo

                # Agar left child hai toh usse queue mein daalo
                if node.left:
                    queue.append(node.left)

                # Agar right child hai toh usse bhi queue mein daalo
                if node.right:
                    queue.append(node.right)

            # Current level ka data result mein daal do
            result.append(current_level)

        # Final result return karo jisme har level ka data ek sublist mein hoga
        return result
