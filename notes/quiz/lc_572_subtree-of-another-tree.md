# 572. Subtree of Another Tree

## 1. 具体->抽象转化模型
### 输入：原题目的描述
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


### 输出：数学的、符号的、形式化的描述
树A是树B的子树 <=> 在B上存在一个节点x，该节点的val等于A的root的val，并且x的左子树和A的左子树完全相同，且x的右子树与A的右子树也完全相同.

## 2. 特性提取模型
### 输入：题目的数学形式化描述 （模型1的输出）

### 输出：问题有哪些关键特点、特性（不是那种平凡的，而是稍微有点insight的、可能成为突破口的那些）
【平凡】二叉树可以被递归遍历
比较两棵二叉树是否相等，可以递归遍历来比较，比较次数等于较小的那棵二叉树的节点数
二叉树的结构不是线性的，而是层次的
二叉树可以被前序、中序、后序输出成序列，但是序列不能再转回二叉树

## 3. BF解法模型
### 输入：题目的数学形式化描述 + 问题特性 （模型1+2的输出）

### 输出：一种BF的思路
遍历`tree`的每一个节点，并将其当做根节点的子树来跟`subRoot`进行比较（遍历）

## 4. 性能分析模型
### 输入：题目的数学形式化描述 + 问题特性 + BF思路 （模型1+2+3的输出）

### 输出：BF中哪个环节拖累了性能（并判断是否可优化），其他还有哪些地方是可优化的
BF的时间复杂度为O(n+m)，n为`tree`大小，m为`subRoot`大小
内层遍历存在重复比较

## 5. 方法库匹配模型
### 输入：题目的数学形式化描述 + 问题特性 + BF思路 + 性能分析结果（模型1+2+3+4的输出）

### 输出：已知的某种方法（或其类似物，或变化情况），有实现思路且可实现一种新方法
直接优化：将内层遍历所需的计算（O(m)）替换为O(1)的方法 => 计算树哈希
问题转换：将树按照DFS的先序遍历输出成字符串，问题就被转换为字符串匹配问题 => 字符串匹配（KMP, Sunday, BM, RK, etc.）
