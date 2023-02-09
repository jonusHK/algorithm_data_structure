n = int(input())
k = int(input())
censors = list(map(int, input().split()))

censors.sort()
diff = [censors[i+1] - censors[i] for i in range(n - 1)]
diff.sort(reverse=True)

print(sum(diff[k-1:]))
