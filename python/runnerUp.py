if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

sorted_arr = sorted(arr, reverse = True)
max_score = sorted_arr[0]
runner_up_score = sorted_arr[-1]
for score in sorted_arr:
    if score < max_score and score > runner_up_score:
        runner_up_score = score
print(runner_up_score)