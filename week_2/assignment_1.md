# 🧪 Python Assignment: Student Report Card (If/Else Only)

This beginner-friendly assignment helps you practice using:

- 🎯 Arithmetic operations
- ✅ Logical conditions
- 🧠 `if` and `else` statements (**no `elif`**)

---

## 📝 Task Description

Create a Python program that: 

1. Takes input marks for **Math**, **English**, and **Science**
2. Calculates:
    - **Total marks**
    - **Percentage**
3. Decides the **Grade** based on percentage
4. Checks if the student **Passed or Failed** (must pass all subjects)
5. Prints a **Formatted Report Card**

---

## 📚 Rules & Grading

- Each subject is out of **100**
- A student must score at least **40 marks in each subject to pass**
- Use only `if` and `else` (**no `elif`**)

### 🎓 Grade Table

| Percentage      | Grade |
|----------------|-------|
| 90 or above    | A     |
| 80 - 89        | B     |
| 70 - 79        | C     |
| 60 - 69        | D     |
| Below 60       | F     |

---

## 🔤 Sample Code

```python
# Ask for marks from the user
math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))

# Calculate total and percentage
total = math + english + science
percentage = (total / 300) * 100

# Decide the grade using if-else only (no elif)
if percentage >= 90:
    grade = "A"
else:
    if percentage >= 80:
        grade = "B"
    else:
        if percentage >= 70:
            grade = "C"
        else:
            if percentage >= 60:
                grade = "D"
            else:
                grade = "F"

# Check if the student passed all subjects
if math >= 40 and english >= 40 and science >= 40:
    result = "You passed!"
else:
    result = "You failed."

# Print the report card
print("\n--- Report Card ---")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)
```

---

## 📥 Sample Input
```
Enter Math marks: 65
Enter English marks: 70
Enter Science marks: 80
```

## 📤 Sample Output
```
--- Report Card ---
Total Marks: 215
Percentage: 71.66666666666667
Grade: C
Result: You passed!
```

---

## 📌 Submission Instructions

- ✅ Complete this task in **Google Colab**
- ✅ Download it as **PDF**
- ✅ Submit the **Colab link** or **.py file**

---

## 💡 Bonus Tips

- Try changing marks and see how the grade changes.
- Understand how if-else nesting works.
- Focus on the logic – not just copying!
- Convert this in Google Colab file