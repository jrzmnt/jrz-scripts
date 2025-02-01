"""
Module for implementing and manipulating a Binary Search Tree (BST) with type hints.

Classes:
    TreeNode: Represents a node in the BST, containing a key and references to left and right child nodes.
    BinarySearchTree: Represents the BST itself, with methods for insertion, deletion, searching, and traversal.

Methods of the TreeNode class:
    __init__(self, key: int) -> None: Initializes a TreeNode with a given key.
    __str__(self) -> str: Returns a string representation of the node's key.

Methods of the BinarySearchTree class:
    __init__(self) -> None: Initializes an empty BST.
    _insert(self, node: Optional[TreeNode], key: int) -> TreeNode: Helper method to recursively insert a key into the BST.
    insert(self, key: int) -> None: Inserts a key into the BST.
    _search(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]: Helper method to recursively search for a key in the BST.
    search(self, key: int) -> Optional[TreeNode]: Searches for a key in the BST.
    _delete(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]: Helper method to recursively delete a key from the BST.
    delete(self, key: int) -> None: Deletes a key from the BST.
    _min_value(self, node: TreeNode) -> int: Helper method to find the smallest key in a subtree.
    _inorder_traversal(self, node: Optional[TreeNode], result: List[int]) -> None: Helper method to perform an inorder traversal of the BST.
    inorder_traversal(self) -> List[int]: Performs an inorder traversal of the BST and returns the keys in ascending order.

Usage Example:
    bst = BinarySearchTree()
    nodes = [50, 30, 20, 40, 70, 60, 80]
    for node in nodes:
        bst.insert(node)
    print('Search for 80:', bst.search(80))
    print("Inorder traversal:", bst.inorder_traversal())
    bst.delete(40)
    print("Search for 40:", bst.search(40))
"""

from typing import Optional, List


class TreeNode:
    """
    Represents a node in a binary search tree.

    Attributes:
        key: The value stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """

    def __init__(self, key: int) -> None:
        """
        Initializes a TreeNode with a given key.

        Args:
            key: The value to be stored in the node.
        """
        self.key: int = key
        self.left: Optional["TreeNode"] = None  # Left child node
        self.right: Optional["TreeNode"] = None  # Right child node

    def __str__(self) -> str:
        """
        Returns the string representation of the node's key.

        Returns:
            A string representation of the key.
        """
        return str(self.key)


class BinarySearchTree:
    """
    Represents a binary search tree (BST).

    Attributes:
        root: The root node of the BST.
    """

    def __init__(self) -> None:
        """
        Initializes an empty binary search tree.
        """
        self.root: Optional[TreeNode] = None  # Root node of the BST

    def _insert(self, node: Optional[TreeNode], key: int) -> TreeNode:
        """
        Helper method to recursively insert a key into the BST.

        Args:
            node: The current node being processed.
            key: The value to be inserted.

        Returns:
            The node with the key inserted.
        """
        if node is None:
            return TreeNode(key)  # Create a new node if the current node is None

        # Recursively insert into the left or right subtree
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key: int) -> None:
        """
        Inserts a key into the BST.

        Args:
            key: The value to be inserted.
        """
        self.root = self._insert(self.root, key)

    def _search(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Helper method to recursively search for a key in the BST.

        Args:
            node: The current node being processed.
            key: The value to search for.

        Returns:
            The node containing the key, or None if the key is not found.
        """
        if node is None or node.key == key:
            return node  # Return the node if found or None if not found

        # Recursively search in the left or right subtree
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key: int) -> Optional[TreeNode]:
        """
        Searches for a key in the BST.

        Args:
            key: The value to search for.

        Returns:
            The node containing the key, or None if the key is not found.
        """
        return self._search(self.root, key)

    def _delete(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Helper method to recursively delete a key from the BST.

        Args:
            node: The current node being processed.
            key: The value to be deleted.

        Returns:
            The node with the key deleted.
        """
        if node is None:
            return node  # Return None if the node is not found

        # Recursively delete from the left or right subtree
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.key = self._min_value(node.right)
            # Delete the inorder successor
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key: int) -> None:
        """
        Deletes a key from the BST.

        Args:
            key: The value to be deleted.
        """
        self.root = self._delete(self.root, key)

    def _min_value(self, node: TreeNode) -> int:
        """
        Helper method to find the smallest key in a subtree.

        Args:
            node: The root node of the subtree.

        Returns:
            The smallest key in the subtree.
        """
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node: Optional[TreeNode], result: List[int]) -> None:
        """
        Helper method to perform an inorder traversal of the BST.

        Args:
            node: The current node being processed.
            result: A list to store the traversal result.
        """
        if node:
            self._inorder_traversal(node.left, result)  # Traverse the left subtree
            result.append(node.key)  # Visit the current node
            self._inorder_traversal(node.right, result)  # Traverse the right subtree

    def inorder_traversal(self) -> List[int]:
        """
        Performs an inorder traversal of the BST.

        Returns:
            A list of keys in ascending order.
        """
        result: List[int] = []
        self._inorder_traversal(self.root, result)
        return result


def main() -> None:
    """
    Demonstrates the usage of the BinarySearchTree class.
    """
    # Initialize a Binary Search Tree
    bst = BinarySearchTree()

    # List of nodes to insert into the BST
    nodes = [50, 30, 20, 40, 70, 60, 80]

    # Insert nodes into the BST
    for node in nodes:
        bst.insert(node)

    # Search for a key in the BST
    print("Search for 80:", bst.search(80))

    # Perform an inorder traversal of the BST
    print("Inorder traversal:", bst.inorder_traversal())

    # Delete a key from the BST
    bst.delete(40)

    # Search for the deleted key
    print("Search for 40:", bst.search(40))


if __name__ == "__main__":
    main()
