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

# 题目类型划分

## Pattern: Sliding window
