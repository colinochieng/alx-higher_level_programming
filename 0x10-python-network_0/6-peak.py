#!/usr/bin/python3
"""Module for function that finds a peak in a list of unsorted integers"""


def find_peak(arr):
    """function to find a peak"""
    if len(arr) == 0:
        return None
    else:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > arr[mid + 1] and arr[mid - 1] < arr[mid]:
                return arr[mid]
            elif arr[mid] == arr[mid + 1] and arr[mid - 1] == arr[mid]:
                return arr[mid]
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
