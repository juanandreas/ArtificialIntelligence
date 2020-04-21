# Given a list of integers, print out a graph containing pluses
# each column i corresponds to list[i]+1. 

# i.e [5]
# prints out a column of 5+1 pluses:
# +
# +
# +
# +
# +
# +

#[5,4,2,1,2,3,2,1,0,1,2,4] 

# +           
# ++         +
# ++   +     +
# +++ +++   ++
# ++++++++ +++
# ++++++++++++


def solve(nums):
    seen = float("-inf")
    height = 0
    while(1):
        peak = max(nums)
        height = max(height, peak)
        for i, num in enumerate(nums):
            if num == peak or num == seen:
                print("+", end="")
                nums[i] = seen
            elif num > seen:
                print(" ", end="")
        print("")

        height -= 1
        if height == -1:
            break


if __name__ == '__main__':
    nums = [5,4,2,1,2,3,2,1,0,1,2,4]
    solve(nums)