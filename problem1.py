steps = list(map(int, input("Enter the steps taken each day separated by spaces: ").split()))

highest = max(steps)
lowest = min(steps)

avg = sum(steps) / len(steps)

sort = sorted(steps, reverse=True)

print(f"Highest Steps: {highest}")
print(f"Lowest Steps: {lowest}")
print(f"Average Daily Steps: {avg:.2f}")
print(f"Sorted Steps in Descending Order: {sort}")