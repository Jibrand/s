# python
print("1) Variables & Data Types")
x = 10
y = 3.14
name = "Ali"
flag = True
print("x:", x, "type:", type(x))
print("y:", y, "type:", type(y))
print("name:", name, "type:", type(name))
print("flag:", flag, "type:", type(flag))

print("\n2) Basic Operators")
a, b = 15, 4
 

print("\n3) If-Else Statements")
num = 7
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

print("\n4) For Loop")
for i in range(5):
    print("i:", i)

print("Loop through list")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("\n5) While Loop")
count = 0
while count < 3:
    print("count:", count)
    count += 1

print("\n6) Lists")
numbers = [10, 20, 30, 40]
print("List:", numbers)
print("Access 2nd element:", numbers[1])
numbers.append(50)
print("After append:", numbers)
numbers.remove(20)
print("After remove:", numbers)
print("Slice:", numbers[1:4])
print("Reverse:", numbers[::-1])
print("Length:", len(numbers))

print("\n7) Dictionaries")
student = {"name":"Ali","age":20,"grade":"A"}
print("Dictionary:", student)
print("Access name:", student["name"])
student["age"] = 21
print("Updated age:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

print("\n8) Tuples")
t = (1, 2, 3, 4)
print("Tuple:", t)
print("Access element:", t[2])
print("Length:", len(t))

print("\n9) Sets")
s = {1, 2, 3, 3, 4}
print("Set:", s)
s.add(5)
print("After add:", s)
s.remove(2)
print("After remove:", s)

print("\n10) List Comprehension")
squares = [x**2 for x in range(6)]
print("Squares:", squares)
even_numbers = [x for x in range(10) if x%2==0]
print("Even numbers:", even_numbers)

print("\n11) Dictionary Comprehension")
dict_squares = {x:x**2 for x in range(5)}
print(dict_squares)

print("\n12) Functions")
def greet(name):
    return "Hello " + name
print(greet("Ali"))

print("\n13) Lambda Functions")
square = lambda x: x**2
print("Square of 5:", square(5))

print("\n14) Range Examples")
print("range(5):", list(range(5)))
print("range(2,10):", list(range(2,10)))
print("range(0,10,2):", list(range(0,10,2)))

print("\n17) Type Checking")
print(type(a))
print(isinstance(a,list))

print("\n19) Strings")
s = "Python"
print(s[0], s[-1])
print(s[0:4])
print("Length:", len(s))
print("Upper:", s.upper(), "Lower:", s.lower())
print("Split:", s.split("t"))

print("\n20) Concatenation")
a = [1,2]
b = [3,4]
print("Concatenate lists:", a+b)
print("Repeat list:", a*2)

# pvtble
import pandas as pd

data = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT", "IT"],
    "Team": ["A", "B", "A", "B", "A", "A", "B"],
    "Employee": ["Ali", "Sara", "John", "Jane", "Usman", "Zara", "Ahmed"],
    "Salary": [50000, 60000, 45000, 47000, 70000, 72000, 68000],
    "Experience": [2, 3, 5, 4, 6, 7, 5]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)


print("1) Basic pivot table: average salary by Department")
pivot1 = df.pivot_table(index="Department", values="Salary")
print(pivot1)

print("\n2) Pivot with multiple aggregation functions")
pivot2 = df.pivot_table(index="Department", values="Salary", aggfunc=["mean","max","min"])
print(pivot2)

print("\n3) Pivot with multiple columns (Department vs Team)")
pivot3 = df.pivot_table(index="Department", columns="Team", values="Salary", aggfunc="mean")
print(pivot3)

print("\n4) Pivot with multiple values")
pivot4 = df.pivot_table(index="Department", values=["Salary","Experience"], aggfunc="sum")
print(pivot4)

print("\n5) Pivot with fill_value for missing data")
pivot5 = df.pivot_table(index="Department", columns="Team", values="Salary", aggfunc="mean", fill_value=0)
print(pivot5)

print("\n6) Pivot table with margins (total row/column)")
pivot6 = df.pivot_table(index="Department", columns="Team", values="Salary", aggfunc="mean", margins=True, fill_value=0)
print(pivot6)

print("\n7) Pivot using multiple indices")
pivot7 = df.pivot_table(index=["Department","Team"], values="Salary", aggfunc="sum")
print(pivot7)

print("\n8) Pivot with multiple aggregation functions and multiple values")
pivot8 = df.pivot_table(index="Department", values=["Salary","Experience"], aggfunc={"Salary":"mean","Experience":"sum"})
print(pivot8)

print("\n9) Reset index after pivot")
pivot9 = df.pivot_table(index="Department", values="Salary").reset_index()
print(pivot9)

print("\n10) Pivot table with custom lambda function")
pivot10 = df.pivot_table(index="Department", values="Salary", aggfunc=lambda x: x.max()-x.min())
print(pivot10)

# ilo loc
import pandas as pd
 
data = {
    "Employee": ["Ali", "Sara", "John", "Jane", "Usman"],
    "Department": ["Sales", "HR", "IT", "HR", "IT"],
    "Salary": [50000, 60000, 45000, 47000, 70000],
    "Experience": [2, 3, 5, 4, 6]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)


print("1) Select row by label (index) using loc")
print(df.loc[0])

print("\n2) Select multiple rows using loc")
print(df.loc[[0, 2, 4]])

print("\n3) Select rows and columns by label")
print(df.loc[0, "Employee"])
print(df.loc[0, ["Employee", "Salary"]])
print(df.loc[[0, 2], ["Employee", "Salary"]])

print("\n4) Conditional selection using loc")
print(df.loc[df["Salary"] > 50000])
print(df.loc[df["Department"] == "IT", ["Employee", "Salary"]])

print("\n5) Set value using loc")
df.loc[0, "Salary"] = 52000
print(df)

print("ILOC = selection by integer position")

print("\n6) Select row by integer position")
print(df.iloc[0])
print(df.iloc[[0, 2]])

print("\n7) Select rows and columns by integer position")
print(df.iloc[0, 1])  
print(df.iloc[0:3, 0:2]) 

print("\n8) Negative indexing with iloc")
print(df.iloc[-1])  
print(df.iloc[-3:, -2:])   

print("9) Slice rows using loc and iloc")
print(df.loc[1:3, "Employee":"Salary"])  
print(df.iloc[1:3, 0:3])  

print("\n10) Boolean conditions with loc")
print(df.loc[(df["Salary"] > 45000) & (df["Experience"] > 3), ["Employee", "Salary"]])

print("\n11) Add new column using loc")
df.loc[:, "Bonus"] = df["Salary"] * 0.1
print(df)

print("\n12) iloc for single column")
print(df.iloc[:, 2])  
print(df.iloc[:, [0, 2]])  

print("\n13) iloc with step")
print(df.iloc[::2, 0:2])   

print("\n14) loc with multiple conditions and assignment")
df.loc[(df["Department"]=="IT") & (df["Salary"]>65000), "Bonus"] = 8000
print(df)
 
import pandas as pd

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None)


data = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT", "IT"],
    "Employee": ["Ali", "Sara", "John", "Jane", "Usman", "Zara", "Ahmed"],
    "Salary": [50000, 60000, 45000, 47000, 70000, 72000, 68000],
    "Experience": [2, 3, 5, 4, 6, 7, 5]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)


print("1) Basic groupby: group by single column")
grouped = df.groupby("Department")
print(grouped)  
print("List of groups:", grouped.groups)


print("2) Aggregate single column with mean")
mean_salary = grouped["Salary"].mean()
print(mean_salary)

print("\n3) Aggregate multiple columns with different functions")
agg_func = grouped.agg({"Salary": "mean", "Experience": "sum"})
print(agg_func)

print("\n4) Using multiple aggregation functions")
multi_agg = grouped["Salary"].agg(["mean", "sum", "max", "min"])
print(multi_agg)


print("5) Iterate through groups")
for name, group in grouped:
    print("Group:", name)
    print(group)


print("6) Filter groups (example: avg salary > 60000)")
filtered = grouped.filter(lambda x: x["Salary"].mean() > 60000)
print(filtered)


print("7) Transform example (add mean salary column)")
df["Mean_Salary"] = grouped["Salary"].transform("mean")
print(df)


print("8) Group by multiple columns")
data2 = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT", "IT"],
    "Team": ["A", "B", "A", "B", "A", "A", "B"],
    "Employee": ["Ali", "Sara", "John", "Jane", "Usman", "Zara", "Ahmed"],
    "Salary": [50000, 60000, 45000, 47000, 70000, 72000, 68000]
}
df2 = pd.DataFrame(data2)
grouped_multi = df2.groupby(["Department", "Team"])
print(grouped_multi["Salary"].mean())


print("9) Size of each group")
size = grouped.size()
print(size)

print("\n10) Count of non-null entries per group")
count = grouped.count()
print(count)


print("11) Apply custom function to each group")
def range_salary(x):
    return x["Salary"].max() - x["Salary"].min()
salary_range = grouped.apply(range_salary)
print(salary_range)


print("12) Reset index after groupby")
mean_salary_reset = grouped["Salary"].mean().reset_index()
print(mean_salary_reset)


print("13) Sort groups by aggregate value")
sorted_salary = grouped["Salary"].mean().sort_values(ascending=False)
print(sorted_salary)


print("14) Group by with as_index=False")
group_mean = df.groupby("Department", as_index=False)["Salary"].mean()
print(group_mean)


print("15) Group by with multiple aggregation using dict")
agg_dict = grouped.agg({"Salary": ["mean", "max"], "Experience": ["sum", "min"]})
print(agg_dict)


print("16) Access specific group")
sales_group = grouped.get_group("Sales")
print(sales_group)


print("17) Example: add new column based on group operation")
df["Salary_Rank"] = grouped["Salary"].rank(ascending=False)
print(df)



# REGEX?
import re

print("1) Extract all numbers from text")
text = "My 2 phones cost 15000 and 23000 rupees"
numbers = re.findall(r"\d+", text)
print(numbers, "- all numbers")

print("\n2) Extract 2-digit numbers")
text = "Ali is 23, Sara is 19, Ahmed is 7"
two_digit = re.findall(r"\b\d{2}\b", text)
print(two_digit, "- exactly 2 digits")

print("\n3) Extract 4-digit years")
text = "The years are 2021, 1999, 300 and 98765"
years = re.findall(r"\b\d{4}\b", text)
print(years, "- 4-digit numbers only")

print("\n4) Extract words starting with capital letters")
text = "Ahmed and Bilal went to Karachi to meet Dr. Ali"
capital_words = re.findall(r"\b[A-Z]\w+", text)
print(capital_words, "- words starting with capital letters")

print("\n5) Extract words ending with ing")
text = "They are running, eating, and playing outside"
ing_words = re.findall(r"\b\w+ing\b", text)
print(ing_words, "- words ending with ing")

print("\n6) Extract hashtags")
text = "Feeling #great today, enjoying the #sunnyDay"
hashtags = re.findall(r"#\w+", text)
print(hashtags, "- hashtags")

print("\n7) Extract emails")
text = "Contact ali@mail.com, sara123@gmail.com"
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
print(emails, "- email addresses")

print("\n8) Extract phone numbers (11 digits)")
text = "Call 03001234567 or 03345556677 or office 12345"
phones = re.findall(r"\b\d{11}\b", text)
print(phones, "- 11-digit phone numbers")

print("\n9) Extract simple URLs")
text = "Visit google.com or youtube.com for info"
urls = re.findall(r"[a-zA-Z0-9]+\.[a-zA-Z]+", text)
print(urls, "- simple URLs")

print("\n10) Extract decimal numbers")
text = "Pi is approx 3.1415 and e is 2.718"
decimals = re.findall(r"\d+\.\d+", text)
print(decimals, "- decimal numbers")

print("\n11) Replace digits with X")
text = "My ID is 12345 and phone is 03001234567"
masked = re.sub(r"\d", "X", text)
print(masked, "- all digits replaced")

print("\n12) Extract content from HTML divs")
html = "<div>Hello</div><div>World</div>"
div_content = re.findall(r"<div>(.*?)</div>", html)
print(div_content, "- content inside div tags")

print("\n13) Extract words of exactly 4 letters")
text = "The lion runs fast in the wild"
four_letters = re.findall(r"\b\w{4}\b", text)
print(four_letters, "- 4-letter words")

print("\n14) Extract dates DD-MM-YYYY")
text = "Today is 21-11-2025 and yesterday was 20-11-2025"
dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
print(dates, "- dates in DD-MM-YYYY format")

print("\n15) Extract lines starting with a digit")
text = "1. First\nSecond line\n3. Third line"
lines = re.findall(r"^\d.*", text, re.MULTILINE)
print(lines, "- lines starting with a digit")

print("\n16) Extract vowels")
text = "Hello World"
vowels = re.findall(r"[aeiouAEIOU]", text)
print(vowels, "- vowels only")

print("\n17) Extract text inside quotes")
text = 'He said "Hello" and she said "Hi"'
quotes = re.findall(r'"(.*?)"', text)
print(quotes, "- text inside double quotes")

print("\n18) Extract IP addresses")
text = "My IP is 192.168.1.1 and server 10.0.0.5"
ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", text)
print(ips, "- IP addresses")

print("\n19) Extract variable names (letters+numbers+_)")
text = "var1 = 10, my_var = 20, x = 5"
variables = re.findall(r"\b\w+\b", text)
print(variables, "- variable-like words")

print("\n20) Extract duplicate words")
text = "hello hello world world test"
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)
print(duplicates, "- repeated words")
