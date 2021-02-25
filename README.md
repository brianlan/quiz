# 做题指导方针

## 思考清楚

- 构造一个例子，用笔在纸上**可视化**一下，或者用excel可视化.  需要构建**至少一个正例和一个反例**，这样才能思考全面.
- 理解清楚题目，仔细思考突问题破口。
- **代码一般都不会长**，所以说如果发现某种解题方案需要写大量代码，首先反思是不是当前的思路不对，是否有更好的思路。

## 看清楚输入数据范围

有的题目中会给出输入数据范围的hint，有时候这些数据的范围会给我们一些算法设计的灵感，或者是帮助我们排除掉一些肯定不能用的方案。

## 边界情况

根据题目的描述，思考输入数据的边界情况和特殊情况。往往一套算法实现下来大问题没有，但就是这些边界情况没有考虑到。

## 做好自测

一定要测！总有你想不到的犯低级错误的地方!

* 题目中给的输入一定要测
* 如果输入的形式不复杂且容易造出满足要求的输入，一定要随机生成2-3组数据进行测试，然后OJ上也跑一次看看是否和正确答案一致
* 构造边界条件进行测试

## 通过暴力解法来试探更优解法

对于没有做过的题型，有时候很难一下子想出最优解法。不要紧，可以先想想看暴力解法怎么解，这至少有三个好处
1. 可以知道这个方法的时间/空间复杂度的上限，帮助后续思考更优解法时做排除法（更优解法如果复杂度跟暴力解法相同，那么这种优化就没有意义）
1. 帮助我们更深的理解题意，那么就有可能在这个过程中想到一些优化的点。
1. 写出来提交一把试试看，万一就直接通过了呢。就算没通过，如果拿到一个超时的结果，那么也可以帮助我们知道至少计算的结果是正确的。

# 题目类型总结

## DP

* 字符串匹配
  * Leetcode: 1143, 72, 10, 583, 1035, 712
  * 通常需要`dp[i][j]`来记录字符串`a[:i]`和`b[:j]`之间的计算过程
* 股票
* Game DP
* 背包问题

# 对Leetcode算法题的看法

* 在Leetcode中重要的是思想，而代码只不过是辅助用来实现思想的工具而已。要写真正好的程序，需要考虑的东西很多，远远不是Leetcode做得好就代表了编程编得好。
* 想要做到Leetcode大神，至少需要3方面基本能力：
  1. 数学思维 - 很多题目（特别是难题）背后隐藏的是纯数学上的东西，也就是说解题的关键在于找到那个数学结论（可以是凭灵感和聪颖看出来的，也可以是现成的数学定理/结论，也可以是自己证明出来的）。培养这方面的能力，首先需要自己心理上不抗拒数学。其次，需要让自己惯于使用数学语言和数学符号。最后，就是多看例题从而熟练掌握常见定理和结论，以及多看证明题，学会一些常用的数学证明方法。
  1. 问题建模和转换思维 - 很多题目会用一些故事来包装其背后的实质问题，或者是对一些经典问题的变化。我们平时刷题练习做的再多，总有新的披着各种皮囊的题目出来。这就需要我们能够对表面问题进行转换，变成我们已知的某个问题，或者对问题进行建模变为我们已知可解的问题。培养这方面的能力，需要在做题过程中对不同的题型进行归纳总结，然后将不同表象的题和实质题型进行关联，并通过做大量的题目来练习这种转换能力。
  1. 计算机数据结构和算法 - 最终到了实现层面，还是离不开数据结构和算法。因此对各种数据结构的适用范围和特性，以及各类算法所解决的问题也需要熟知。培养这方面的能力，首先需要系统化地学习数据结构和算法的基础知识，然后通过大量的练习来强化这些知识的记忆和运用。

  