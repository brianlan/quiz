# Dynamic Programming (DP)

## 重叠子问题

### 子问题

#d 子问题定义
A problem whose solution contributes to the solution of a larger problem.

#d 子问题的表示
原问题和子问题可以使用自然语言来描述，不一定非要用数学化、符号化的语言来描述。然而，我们会发现，使用后一种方式来描述问题和子问题会显得更加的简洁和准确，同时也让我们离解题的下一个步骤更近。其实，使用后一种方式来对问题和子问题进行描述，就是我们所说的“定义状态”。

#e 斐波那契数列 子问题定义
For example, the problem of computing the Fibonacci sequence exhibits overlapping subproblems. The problem of computing the nth Fibonacci number F(n), can be broken down into the subproblems of computing F(n − 1) and F(n − 2), and then adding the two

#e 数字三角形 子问题定义
在给定的深度为n的树中，“使得从叶节点(深度=n-1)到根节点(深度=0)数字和最大的路径”，可以被分解为“使得从叶节点(深度=n-1)到节点`node[1,0]`(深度=1)数字和最大的路径”和“使得从叶节点(深度=n-1)到节点`node[1,1]`(深度=1)数字和最大的路径”两个子问题中更大的那条路径，再连上根节点


### 什么叫重叠

#d 重叠子问题的定义
a problem is said to have overlapping subproblems if the problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems

#e 第n-1个斐波那契数 重叠子问题的定义
In Fibonacci sequence problem, F(n) can be broken down into the subproblems of computing F(n − 1) and F(n − 2). The subproblem of computing F(n − 1) can itself be broken down into a subproblem that involves computing F(n − 2). Therefore, the computation of F(n − 2) is reused.

#e 数字三角形的重叠子问题 重叠子问题的定义
我们可以将子问题定义为T(1, 0)，表示：使得从叶节点(深度=n-1)到节点`node[1,0]`(深度=1)数字和最大的路径。那么，要得到T(1, 0)，就需要知道T(2, 0)和T(2, 1)；要得到T(1, 1)就需要知道T(2, 1)和T(2, 2)。于是我们看到，T(2, 1)这个子问题重复出现了。

### 与分治法的关联

#d 子问题是否重叠
分治法中也提到子问题，The main and major difference between these two methods relates to the superimposition of subproblems in dynamic programming. A subproblem can be used to solve a number of different subproblems. In the “divide and conquer” approach, subproblems are entirely independent and can be solved separately. Moreover, recursion is used, unlike in dynamic programming where a combination of small subproblems is used to obtain increasingly larger subproblems.

#d 总结
To sum up, it can be said that the “divide and conquer” method works by following a top-down approach whereas dynamic programming follows a bottom-up approach.
![dp vs divide and conquer](/images/dp_divide_and_conquer.png)


## 状态和状态转移方程

#d 状态的定义
状态是对问题的一种数学化、符号化的定义，通常是对要解决的问题或者子问题的一种抽象表述。

#e 斐波那契数列中的状态 状态的定义
通常用F(n)，或者是dp[n]来表示第n个Fibonacci数，即该问题的状态.

#e 数字三角形中的状态 状态的定义
以第i层第j个数字为根节点的子树的使得数字和最大的路径: T(i, j)

#d 状态转移方程
它是解决问题的核心。状态转移方程其实通常直接代表着暴力解法。千万不要看不起暴力解，动态规划问题最困难的就是写出这个暴力解，即状态转移方程。只要写出暴力解，优化方法无非是用备忘录或者 DP table，再无奥妙可言。

#e 斐波那契额数列状态转移方程 状态转移方程

## 最优子结构

#d 最优子结构的定义

#d 什么是最优

#e Fibonacci不具备 什么是最优
The example of the Fibonacci sequence is not strictly a dynamic programming because it does not involve finding the optimal value

#d 什么是子结构

#d 什么是最优子结构
~~ 通常一个可以用动态规划来解决的问题都有被称作为“最优子结构”的特性。~~

#e XXX 什么是最优子结构

#d 最优解包含性

#e YYY 最优解包含性

## 总结

#d 三者的关系
状态转移方程、重叠子问题和最优子结构是DP的核心要素。但是这三者之间并不是完全独立无关的，而是相互交织在一起。因此，在面对一个新问题的时候，往往需要我们能够仔细地分辨和分析出他们分别是什么。

#d 可递归性
这种特性一定可以被递归的定义出来，也就是说一个题目可以被DP解决，那也一定可以被递归解决，只不过效率上可能存在很大差异（看是否有重复计算）。
通过cache住已经算过的结果，可以显著提升性能（通常被称为带备忘录的递归）。
