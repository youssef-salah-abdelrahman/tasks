borrowed_books = ["book a - 7","book b - 5","book c - 10","book a - 3","book f - 6","book c - 4"]

book_data = {}
for entry in borrowed_books:
    title, days = entry.split(" - ")
    days = int(days)

    if title in book_data:
        book_data[title] += days
    else:
        book_data[title] = days

most_borrowed = max(book_data.items(), key=lambda x: x[1])
least_borrowed = min(book_data.items(), key=lambda x: x[1])


total_days = sum(book_data.values())
avg_days = total_days / len(book_data)

unique_titles = set(book_data.keys())

sorted_books = sorted(book_data.items(), key=lambda x: x[1], reverse=True)

print("Most Borrowed Book:", most_borrowed[0], "with", most_borrowed[1], "days")
print("Least Borrowed Book:", least_borrowed[0], "with", least_borrowed[1], "days")
print("Average Borrowing Time:", round(avg_days, 2), "days")
print("Unique Titles:", unique_titles)
print("Books Sorted by Borrowing Duration:")
for title, days in sorted_books:
    print(f"{title}: {days} days")