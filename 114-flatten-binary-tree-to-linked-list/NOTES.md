https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)/335509
​
1. find the right most
2. remove left node
3. update prev pointer to current node
3. go back to previous layer then update the right node to prev pointer