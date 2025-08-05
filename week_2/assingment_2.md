# Python Lists & Tuples Assignment

**Instructions:** Solve all 4 problems below. Write clear, well-commented Python code for each problem. Test your solutions with the given data and provide the output.

---

## Problem 1: Student Grade Manager (25 points)
**Topic:** Basic List Operations & Conditional Logic

Create a program that manages student grades:

**Given data:** `grades = [78, 85, 92, 67, 88, 94, 73]`

**Requirements:**
- Add a new grade of 90 to the end of the list
- Remove the lowest grade from the list
- Calculate and print the average of the remaining grades
- Count how many grades are above 85
- Check if the average qualifies for "Honor Roll" (average ≥ 87)
- Print appropriate success/failure messages

**Expected Output Format:**
```
Original grades: [78, 85, 92, 67, 88, 94, 73]
After adding new grade: [78, 85, 92, 67, 88, 94, 73, 90]
After removing lowest grade: [78, 85, 92, 88, 94, 73, 90]
Average grade: 85.71
Grades above 85: 4
Honor Roll Status: Not Qualified
```

---

## Problem 2: Movie Ratings Analyzer (25 points)
**Topic:** List Slicing & Mathematical Operations

Analyze movie ratings data using slicing operations:

**Given data:** `ratings = [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 6.2, 8.1, 7.8]`

**Requirements:**
- Extract and print the first 3 ratings
- Extract and print the last 4 ratings
- Extract every 2nd rating starting from index 1 (ratings[1::2])
- Find the highest rating and check if it's in the first half or second half of the list
- Calculate the difference between the average of first half and second half
- Determine if the movie collection is "Highly Rated" (overall average > 8.0)

**Expected Output Format:**
```
First 3 ratings: [8.5, 7.2, 9.1]
Last 4 ratings: [9.3, 6.2, 8.1, 7.8]
Every 2nd rating from index 1: [7.2, 6.8, 7.5, 6.2, 7.8]
Highest rating 9.3 is in the: Second Half
First half average: 8.12, Second half average: 7.78
Difference: 0.34
Collection Status: Highly Rated (Overall average: 7.95)
```

---

## Problem 3: 3D Coordinate Calculator (25 points)
**Topic:** Tuples, Mathematical Calculations & Comparisons

Work with 3D coordinates stored as tuples:

**Given data:** 
- `point1 = (3, 4, 5)`
- `point2 = (6, 8, 10)`  
- `origin = (0, 0, 0)`

**Requirements:**
- Calculate the distance between point1 and point2 using: √[(x2-x1)² + (y2-y1)² + (z2-z1)²]
- Calculate distance from each point to origin
- Determine which point is closer to origin
- Create a tuple representing the midpoint between point1 and point2
- Check if the midpoint has any coordinate greater than 5
- Attempt to modify point1's x-coordinate to demonstrate tuple immutability (handle the error)

**Expected Output Format:**
```
Point 1: (3, 4, 5)
Point 2: (6, 8, 10)
Distance between points: 7.07
Distance from Point 1 to origin: 7.07
Distance from Point 2 to origin: 14.14
Point 1 is closer to origin
Midpoint: (4.5, 6.0, 7.5)
Midpoint has coordinates > 5: True
Attempting to modify tuple... Error: Tuples are immutable!
```

---

## Problem 4: Sales Performance Tracker (25 points)
**Topic:** Lists of Tuples, Data Analysis & Complex Conditions

Analyze sales performance data:

**Given data:** `sales_data = [('Jan', 15000), ('Feb', 18000), ('Mar', 12000), ('Apr', 22000), ('May', 19000)]`

**Requirements:**
- Find the month with highest sales and lowest sales
- Calculate total sales for all months
- Calculate average monthly sales
- Count how many months had sales above the average
- Check if sales in the last month (May) were higher than the first month (Jan)
- Determine quarterly performance: Q1 (Jan-Mar) vs Q2 (Apr-May) average
- Apply bonus criteria: "Excellent" if any month > $20,000, "Good" if average > $16,000, otherwise "Needs Improvement"

**Expected Output Format:**
```
Sales Data: [('Jan', 15000), ('Feb', 18000), ('Mar', 12000), ('Apr', 22000), ('May', 19000)]
Highest Sales: Apr with $22000
Lowest Sales: Mar with $12000
Total Sales: $86000
Average Monthly Sales: $17200
Months above average: 3
May vs Jan: May performed better ($19000 > $15000)
Q1 Average: $15000, Q2 Average: $20500
Q2 performed better than Q1
Performance Rating: Excellent
```

---

## Submission Guidelines:

1. **File Format:** Submit as a single Python file (.py) with all 4 solutions or Share Google Colab's notebook file link
2. **Code Structure:** Clearly separate each problem with comments
3. **Testing:** Include the exact output for each problem using the given data
4. **Comments:** Add brief comments explaining your logic
5. **Variable Names:** Use descriptive variable names

**Grading Criteria:**
- Correct implementation (60%)
- Code readability and comments (20%)
- Proper output formatting (10%)
- Handling edge cases (10%)

**Due Date:** 05-08-2025
**Total Points:** 100
