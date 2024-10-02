def bubble_sort(nums):
    N = len(nums)  # 리스트의 길이를 구한다
    # i는 실제로 정렬된 값의 위치를 나타낸다.
    for i in range(N - 1, 0, -1):
        for j in range(i):  # 리스트 맨 처음부터 i번째까지 반복
            # 인접한 두수를 비교
            # 두 요소를 비교 후 필요하다면 swap해준다
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

                # nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [42, 32, 24, 68, 15]
bubble_sort(nums)
print(nums)



res = list(range(4, 0, -1))
rse2 = list(range(4))
print(res)
print(rse2)
