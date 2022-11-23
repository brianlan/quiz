# 572. Longest Common Subsequence

## 0. 题目原描述

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

## 1. 具体->抽象转化模型 - 题目，数学的、符号的、形式化的描述
input: p of length n, q of length m
def: s1 <= p[i_1]p[i_2]...p[i_x], where i_1 ~ range(0, n), i_1 < i_2 < ... < i_x
def: s2 <= p[j_1]p[j_2]...p[j_y], where j_1 ~ range(0, m), j_1 < j_2 < ... < j_y
def: longest common sequence - s1 == s2 where i_x == i_y and no longer i_x and i_y exists.

## 2. 特性提取模型 - 问题有哪些关键特点、特性（不是那种平凡的，而是稍微有点insight的、可能成为突破口的那些）
1. p and q are strings
1. p and q can be iterated
1. subsequences can be non-consecutive
1. p has 1 + c{n, 1} + c{n, 2} + ... + c{n, n-1} subsequences while q has 1 + c{m, 1} + c{m, 2} + ... + c{m, m-1} subsequences.
1. for a given subsequence, adding a new one from the rest substring (either place) would get a new subsequence.

## 3. BF解法模型 - 一种BF的思路
for i in range(len(p)):
    


## 4. 性能分析模型 - BF中哪个环节拖累了性能（并判断是否可优化），其他还有哪些地方是可优化的
O(n^3)
完全没有利用之前已经判断过的子串p'和q'的最长公共子序列是什么、长度为多少

## 5. 方法库匹配模型 - 已知的某种方法（或其类似物，或变化情况），有实现思路且可实现一种新方法
