# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 13:05
# @Author  : GuYi
# @Function    :


'''
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
class Solution {
public:
    int firstBadVersion(int n) {
        int lo = 1;
        int hi = n;

        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return hi;
    }
};

'''
def isBadVersion():
    return None
# 测试用例
# FFFFF
# TFFFF
# TTFFF
# TTTFF
# TTTTF
def first_bad_version(self,n):
    left = 1
    right = n
    while left < right:
        # 主要mid取值
        mid = right - (right-left)/2
        # 如果中间位是错位版本 说明 目标值在左区间
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left