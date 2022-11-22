from LeetCode.common import create_binary_tree


def assert_tree_node(actual, expected):
    if expected is None:
        assert actual is None
    else:
        assert actual.val == expected


def test_create_binary_tree_1():
    tree = create_binary_tree([1])
    assert_tree_node(tree, 1)
    assert_tree_node(tree.left, None)
    assert_tree_node(tree.right, None)


def test_create_binary_tree_2():
    tree = create_binary_tree([1, 2, 3])
    assert_tree_node(tree, 1)
    assert_tree_node(tree.left, 2)
    assert_tree_node(tree.right, 3)
    assert_tree_node(tree.left.left, None)
    assert_tree_node(tree.left.right, None)
    assert_tree_node(tree.right.left, None)
    assert_tree_node(tree.right.right, None)


def test_create_binary_tree_3():
    tree = create_binary_tree([1, None, 2, 3])
    assert_tree_node(tree, 1)
    assert_tree_node(tree.left, None)
    assert_tree_node(tree.right, 2)
    assert_tree_node(tree.right.left, 3)
    assert_tree_node(tree.right.right, None)
    assert_tree_node(tree.right.left.left, None)
    assert_tree_node(tree.right.left.right, None)


def test_create_binary_tree_4():
    """
             5
            / \\
           4   7
          /   /
         3   2
        /   /
       -1  9
    """
    tree = create_binary_tree([5, 4, 7, 3, None, 2, None, -1, None, 9])
    assert_tree_node(tree, 5)
    assert_tree_node(tree.left, 4)
    assert_tree_node(tree.right, 7)

    assert_tree_node(tree.left.left, 3)
    assert_tree_node(tree.left.right, None)
    assert_tree_node(tree.left.left.left, -1)
    assert_tree_node(tree.left.left.right, None)
    assert_tree_node(tree.left.left.left.left, None)
    assert_tree_node(tree.left.left.left.right, None)

    assert_tree_node(tree.right.left, 2)
    assert_tree_node(tree.right.right, None)
    assert_tree_node(tree.right.left.left, 9)
    assert_tree_node(tree.right.left.right, None)
    assert_tree_node(tree.right.left.left.left, None)
    assert_tree_node(tree.right.left.left.right, None)


def test_create_binary_tree_5():
    """
                     1
                  /    \\
                2        3
              /   \\    /
             4.    5   6
              \\  / \\   \\
               7  8  9     10
                  \\
                   11
                  / \\
                 12  13

    """
    tree = create_binary_tree([1, 2, 3, 4, 5, 6, None, None, 7,8,9,None,10,None,None,None,11,None,None,None,None,12,13])
    assert_tree_node(tree, 1)

    assert_tree_node(tree.left, 2)
    assert_tree_node(tree.right, 3)

    assert_tree_node(tree.left.left, 4)
    assert_tree_node(tree.left.right, 5)
    assert_tree_node(tree.right.left, 6)
    assert_tree_node(tree.right.right, None)

    assert_tree_node(tree.left.left.left, None)
    assert_tree_node(tree.left.left.right, 7)
    assert_tree_node(tree.left.right.left, 8)
    assert_tree_node(tree.left.right.right, 9)
    assert_tree_node(tree.right.left.left, None)
    assert_tree_node(tree.right.left.right, 10)

    assert_tree_node(tree.left.left.right.left, None)
    assert_tree_node(tree.left.left.right.right, None)
    assert_tree_node(tree.left.right.left.left, None)
    assert_tree_node(tree.left.right.left.right, 11)
    assert_tree_node(tree.left.right.right.left, None)
    assert_tree_node(tree.left.right.right.right, None)
    assert_tree_node(tree.right.left.right.left, None)
    assert_tree_node(tree.right.left.right.right, None)

    assert_tree_node(tree.left.right.left.right.left, 12)
    assert_tree_node(tree.left.right.left.right.right, 13)

    assert_tree_node(tree.left.right.left.right.left.left, None)
    assert_tree_node(tree.left.right.left.right.left.right, None)
    assert_tree_node(tree.left.right.left.right.right.left, None)
    assert_tree_node(tree.left.right.left.right.right.right, None)