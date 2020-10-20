# A binary tree class.
# source (mod): https://www.python.org/dev/peps/pep-0255/
class Tree:

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self, level=0, indent="    "):
        s = level*indent + str(self.label)
        if self.left:
            s = s + "\n" + self.left.__repr__(level+1, indent)
        if self.right:
            s = s + "\n" + self.right.__repr__(level+1, indent)
        return s

    def __iter__(self):
        return inorder(self)

# Create a Tree from a list.
def tree(list):
    n = len(list)
    if n == 0:
        return []
    i = n // 2
    return Tree(list[i], tree(list[:i]), tree(list[i+1:]))



# A non-recursive generator.
def inorder(node):
    stack = []
    while node:
        while node.left:
            stack.append(node)
            node = node.left
        yield node.label
        while not node.right:
            try:
                node = stack.pop()
            except IndexError:
                return
            yield node.label
        node = node.right

# Exercise the non-recursive generator.
t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for x in t:
    print(x, end="")
