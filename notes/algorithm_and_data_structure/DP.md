# Dynamic Programming (DP)

## 重叠子问题

### 子问题

#d 子问题定义
A problem whose solution contributes to the solution of a larger problem.

#d 子问题的表示
虽然原问题和子问题可以使用自然语言来描述，但我们会发现数学化、符号化的方式来表述他们会更加简洁和准确。问题或子问题一般都可以看做是一个关于状态s1,...,sk的函数F(s1, ..., sk), 或者是数组dp[s1]...[sk]。

#d 问题与状态的关系
在讨论某个问题的子问题是什么的时候，其实已经隐含了一个前提，那就是我们已经想好我们要定义的状态是什么了。有了状态，才能够描述问题与子问题。

#e 斐波那契数列 子问题定义
For example, the problem of computing the Fibonacci sequence exhibits overlapping subproblems. The problem of computing the nth Fibonacci number F(n), can be broken down into the subproblems of computing F(n − 1) and F(n − 2), and then adding the two. 

#e 数字三角形 子问题定义
在给定的深度为n的树中，“使得从叶节点(深度=n-1)到根节点(深度=0)数字和最大的路径”，可以被分解为“使得从叶节点(深度=n-1)到节点`node[1,0]`(深度=1)数字和最大的路径”和“使得从叶节点(深度=n-1)到节点`node[1,1]`(深度=1)数字和最大的路径”两个子问题中更大的那条路径，再连上根节点。

#e 凑零钱 子问题定义
原问题：给定amount=11，面值为c1=1,c2=2,c3=5时，最少硬币的方案的硬币数为F(11)。子问题，F(11)可以被分解为，在使用1枚硬币后，凑余下的钱时需要的硬币数，也即，选择使用c1=1时，要看F(10)，在选择使用c2=2时，要看F(9)，在选择使用c3=5时，要看F(6)，所以F(11)的求解中就包含了F(10), F(9)和F(6)三个子问题。


### 什么叫重叠

#d 重叠子问题的定义
a problem is said to have overlapping subproblems if the problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems

#e 第n-1个斐波那契数 重叠子问题的定义
In Fibonacci sequence problem, F(n) can be broken down into the subproblems of computing F(n − 1) and F(n − 2). The subproblem of computing F(n − 1) can itself be broken down into a subproblem that involves computing F(n − 2). Therefore, the computation of F(n − 2) is reused.

#e 数字三角形的重叠子问题 重叠子问题的定义
我们可以将子问题定义为T(1, 0)，表示：使得从叶节点(深度=n-1)到节点`node[1,0]`(深度=1)数字和最大的路径。那么，要得到T(1, 0)，就需要知道T(2, 0)和T(2, 1)；要得到T(1, 1)就需要知道T(2, 1)和T(2, 2)。于是我们看到，T(2, 1)这个子问题重复出现了。

#e 凑零钱 重叠子问题的定义
F(11)可以分解F(10), F(9)和F(6)，而F(8)可以分解为F(7), F(6)和F(3)。这里F(6)就是一个重复出现了的子问题。

#d 判断子问题重叠
1. 一种最简单粗暴的方式就是画图，把递归树画出来（节点denotes子问题），看看有没有重复的节点。
1. 另一种是通过递归框架代码，直接分析，看看从某个状态到另一个状态是否有多条路径，例如看从状态(i, j)->(i-1, j-1)是否有多条路径，若有，那么说明子问题肯定有重叠.

### 与分治法的关联

#d 子问题是否重叠
分治法中也提到子问题，The main and major difference between these two methods relates to the superimposition of subproblems in dynamic programming. A subproblem can be used to solve a number of different subproblems. In the “divide and conquer” approach, subproblems are entirely independent and can be solved separately. Moreover, recursion is used, unlike in dynamic programming where a combination of small subproblems is used to obtain increasingly larger subproblems.

#d 总结
To sum up, it can be said that the “divide and conquer” method works by following a top-down approach whereas dynamic programming follows a bottom-up approach.
![dp vs divide and conquer](/images/dp_divide_and_conquer.png)


## 状态和状态转移方程

#d 状态的定义
状态原本不是问题中必然存在的要素，而是我们为了更好更有效地解决问题时，人为定义出来的概念。由于最优解的问题往往牵涉到做选择，即做什么样的选择是更优的。所以，状态也就往往和选择密切相关。状态可以被定义为：状态是为了更好解决问题，人为定义出来的、在做某个选择的时候，所对应的那时候的情形。

#e 斐波那契数列中的状态 状态的定义
状态为n

#e 数字三角形中的状态 状态的定义
状态为节点位置(i, j)，其中i为节点所在深度，j为从左往右数的顺位。

#e 凑零钱 状态的定义
状态为金额amount

#d 状态的表示
状态通常对应问题中的一个或者多个变量。

#d 选择
选择是导致「状态」产生变化的行为。

#d 状态转移方程


#d 暴力解与状态转移
它是解决问题的核心。状态转移方程其实通常直接代表着暴力解法。千万不要看不起暴力解，动态规划问题最困难的就是写出这个暴力解，即状态转移方程。只要写出暴力解，优化方法无非是用备忘录或者 DP table，再无奥妙可言。

#e 斐波那契额数列状态转移方程 状态转移方程
F(n) = F(n - 1) + F(n - 2)

## 最优子结构

#d 什么是最优
最优指的是题目要求我们求得某个问题或者子问题的最大值、最小值之类的。

#e Fibonacci不具备 什么是最优
The example of the Fibonacci sequence is not strictly a dynamic programming because it does not involve finding the optimal value

#d 最优子结构的定义
算法导论：如果一个问题的最优解包含其子问题的最优解，我们就称此问题具有最优子结构
如果用"白"一点的话说。定义一个问题 Ｑ，求目标解 Ａ。如果我们找出的目标解 A 的同时， Q 的子问题的目标解同时也被找到，那么称问题 Ｑ 具有最优子结构。
判断某个子问题的最优解是否被包含在一个更大问题的最优解中时，要从最优路径的角度来理解和反推。

#e 全校最高成绩 最优子结构的定义
假设你们学校有 10 个班，你已经计算出了每个班的最高考试成绩。如果要计算全校最高的成绩，不用重新遍历全校学生的分数进行比较，而是只要在这 10 个最高成绩中取最大的就是全校的最高成绩。这个问题就符合最优子结构。每个班的最优成绩就是子问题，从子问题的最优结果可以推出更大规模问题的最优结果。反过来也同样成立：更大规模问题的最优结果一定包含了其某个子问题的最优结果。用这个例子来说就是：全校最高分，一定包含在某个班之中，而这个全校最高分也一定是这个班里的最高分。

#e 和最大的路径 最优子结构的定义
下面是一个地图，我们要找一条从左下角（起点）到右上角（终点）、只向右和向上走的路径。

<img src="https://picx.zhimg.com/50/v2-4cc436c57c1505b1bbe8fa536db7bede_720w.jpg?source=1940ef5c" data-caption="" data-size="normal" data-rawwidth="88" data-rawheight="77" class="content_image" width="88"/>

如果要让路径经过的数字总和最大，那么最优路径是下面这条：

<img src="https://pica.zhimg.com/50/v2-12aa22f2e3b094ba1fb6f6a148be165d_720w.jpg?source=1940ef5c" data-caption="" data-size="normal" data-rawwidth="88" data-rawheight="77" class="content_image" width="88"/>

作者：王赟 Maigo
链接：https://www.zhihu.com/question/52165201/answer/288025858

可以验证，对于最优路径上的任意一点，最优路径从起点到该点的部分，也正是从起点到该点的所有路径中数字总和最大的那一条。这就叫「满足最优子结构」。

#e 绝对值和最小的路径 最优子结构的定义

现在换一个「最优」的标准，要求路径经过的数字总和的绝对值最小。那么最优路径是下面这条：

<img src="https://picx.zhimg.com/50/v2-e25d6e4d7cd17287c5f1f3708a872e5a_720w.jpg?source=1940ef5c" data-caption="" data-size="normal" data-rawwidth="88" data-rawheight="77" class="content_image" width="88"/>

但是，对于最优路径上 -4 这个点，最优路径从起点到该点的部分，却不是从起点到该点的所有路径中，数字总和的绝对值最小的那一条，因为下面这条路径上数字总和的绝对值更小：

<img src="https://picx.zhimg.com/50/v2-478bca87eccd0d812ecea954339e851d_720w.jpg?source=1940ef5c" data-caption="" data-size="normal" data-rawwidth="88" data-rawheight="77" class="content_image" width="88"/>

这就叫「不满足最优子结构」。

作者：王赟 Maigo
链接：https://www.zhihu.com/question/52165201/answer/288025858


#d 子问题独立
要符合「最优子结构」，子问题间必须互相独立。

#e 考试最大分数差 子问题独立
假设你们学校有 10 个班，你已知每个班的最大分数差（最高分和最低分的差值），求全校学生中的最大分数差。肯定不能通过已知的这 10 个班的最大分数差推到出来。因为这 10 个班的最大分数差不一定就包含全校学生的最大分数差，比如全校的最大分数差可能是 3 班的最高分和 6 班的最低分之差。该问题就不符合最优子结构，因为你没办通过每个班的最优值推出全校的最优值，没办法通过子问题的最优值推出规模更大的问题的最优值。全校的最大分数差可能出现在两个班之间，显然子问题不独立，所以这个问题本身不符合最优子结构。


#d 不具备最优子结构
不满足最优子结构往往不是因为子结构的原因，而是因为“最优”导致“最优子结构”不满足。

#e 绝对值和模值 不具备最优子结构
绝对值，模值这种的目标函数就不具有最优子结构。


#d 最优子结构与DP关系
“最优子结构”是某些问题的一种特定性质，并不是动态规划问题专有的，能求最值的问题大部分都具有这个性质。也就是说，很多问题其实都具有最优子结构，只是其中大部分不具有重叠子问题，所以我们不把它们归为动态规划系列问题而已。但反过来，最优子结构性质作为动态规划问题的必要条件，一定是让你求最值的。

#e 二叉树的最大值 最优子结构与DP关系
以 root 为根的树的最大值，可以通过两边子树（子问题）的最大值推导出来，这个问题也符合最优子结构，但这不是动态规划问题。

## 总结

#d 三者的关系
状态转移方程、重叠子问题和最优子结构是DP的核心要素。但是这三者之间并不是完全独立无关的，而是相互交织在一起。因此，在面对一个新问题的时候，往往需要我们能够仔细地分辨和分析出他们分别是什么。

#d 可递归性
这种与决策有一定关系、寻找最优解的题目，通常其核心点在于找到状态转移方程，而状态转移方程一般可以被递归的方式来实现，也就是说这类可以被DP解决的问题，也一定可以被递归解决，只不过效率上可能存在很大差异（看是否有重复计算）。
通过cache住已经算过的结果，可以显著提升性能（通常被称为带备忘录的递归）。

#d 有序性
如果一个问题完全没有预定的顺序，不是很方便使用DP，因为没有办法按照一定的递推顺序去计算状态和重用状态。
遍历的顺序如何确定，要把握两点：
1. 遍历的过程中，所需的状态必须是已经计算出来的
1. 遍历结束后，存储结果的那个位置必须已经被计算出来

#d 无后向性
有序性的另一种表述是无后向性。

## 解题套路

#d 判断是否用DP
如果你碰到了求最值、求可行性或者是求方案总数的问题的话，那么这个问题就八九不离十了，你基本可以确定它就需要使用动态规划来解。

#d 找最优子结构
找最优子结构的过程，其实就是证明状态转移方程正确性的过程，方程符合最优子结构就可以写暴力解了，写出暴力解就可以看出有没有重叠子问题了，有则优化，无则 OK。

