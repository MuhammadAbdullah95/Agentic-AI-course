"""Solutions for 'Python Lists & Tuples Assignment'.

Each problem is implemented in a separate function. Running this script
prints the outputs in the formats requested by the assignment so students
can compare results.
"""

import math
from statistics import mean


def problem_1():
    """Student Grade Manager"""
    grades = [78, 85, 92, 67, 88, 94, 73]
    print("Original grades:", grades)

    # Add a new grade
    grades.append(90)
    print("After adding new grade:", grades)

    # Remove the lowest grade
    lowest = min(grades)
    grades.remove(lowest)
    print("After removing lowest grade:", grades)

    # Calculate average
    avg = mean(grades)
    print("Average grade: {:.2f}".format(avg))

    # Count how many grades > 85
    above_85 = sum(1 for g in grades if g > 85)
    print("Grades above 85:", above_85)

    # Honor roll check
    honor_status = "Qualified" if avg >= 87 else "Not Qualified"
    print("Honor Roll Status:", honor_status)


def problem_2():
    """Movie Ratings Analyzer"""
    ratings = [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 6.2, 8.1, 7.8]
    print("First 3 ratings:", ratings[:3])
    print("Last 4 ratings:", ratings[-4:])
    print("Every 2nd rating from index 1:", ratings[1::2])

    highest = max(ratings)
    highest_index = ratings.index(highest)
    half = "First Half" if highest_index < len(ratings) / 2 else "Second Half"
    print(f"Highest rating {highest} is in the: {half}")

    mid = len(ratings) // 2
    first_half_avg = mean(ratings[:mid])
    second_half_avg = mean(ratings[mid:])
    diff = round(first_half_avg - second_half_avg, 2)
    print("First half average: {:.2f}, Second half average: {:.2f}".format(first_half_avg, second_half_avg))
    print("Difference: {:.2f}".format(abs(diff)))

    overall_avg = mean(ratings)
    status = "Highly Rated" if overall_avg > 8.0 else "Not Highly Rated"
    print(f"Collection Status: {status} (Overall average: {overall_avg:.2f})")


def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


def problem_3():
    """3D Coordinate Calculator"""
    point1 = (3, 4, 5)
    point2 = (6, 8, 10)
    origin = (0, 0, 0)

    print("Point 1:", point1)
    print("Point 2:", point2)

    d_points = distance(point1, point2)
    print("Distance between points: {:.2f}".format(d_points))

    d1_origin = distance(point1, origin)
    d2_origin = distance(point2, origin)
    print("Distance from Point 1 to origin: {:.2f}".format(d1_origin))
    print("Distance from Point 2 to origin: {:.2f}".format(d2_origin))

    closer = "Point 1 is closer to origin" if d1_origin < d2_origin else "Point 2 is closer to origin"
    print(closer)

    midpoint = tuple((a + b) / 2 for a, b in zip(point1, point2))
    print("Midpoint:", midpoint)

    has_gt5 = any(coord > 5 for coord in midpoint)
    print("Midpoint has coordinates > 5:", has_gt5)

    # Demonstrate tuple immutability
    print("Attempting to modify tuple...", end=" ")
    try:
        point1[0] = 10  # will raise TypeError
    except TypeError:
        print("Error: Tuples are immutable!")


def problem_4():
    """Sales Performance Tracker"""
    sales_data = [('Jan', 15000), ('Feb', 18000), ('Mar', 12000), ('Apr', 22000), ('May', 19000)]
    print("Sales Data:", sales_data)

    # Find highest and lowest
    highest = max(sales_data, key=lambda x: x[1])
    lowest = min(sales_data, key=lambda x: x[1])
    print(f"Highest Sales: {highest[0]} with ${highest[1]}")
    print(f"Lowest Sales: {lowest[0]} with ${lowest[1]}")

    # Totals and averages
    total = sum(amount for _, amount in sales_data)
    avg = total // len(sales_data)
    print(f"Total Sales: ${total}")
    print(f"Average Monthly Sales: ${avg}")

    # Months above average
    months_above = sum(1 for _, amt in sales_data if amt > avg)
    print("Months above average:", months_above)

    # Compare May vs Jan
    may = sales_data[-1][1]
    jan = sales_data[0][1]
    if may > jan:
        print(f"May vs Jan: May performed better (${may} > ${jan})")
    else:
        print(f"May vs Jan: Jan performed better or equal (${jan} >= ${may})")

    # Quarter averages: Q1 = Jan-Mar, Q2 = Apr-May
    q1 = mean([amt for _, amt in sales_data[:3]])
    q2 = mean([amt for _, amt in sales_data[3:]])
    print(f"Q1 Average: ${int(q1)}, Q2 Average: ${int(q2)}")
    if q2 > q1:
        print("Q2 performed better than Q1")
    else:
        print("Q1 performed better or equal to Q2")

    # Performance rating
    if any(amt > 20000 for _, amt in sales_data):
        perf = "Excellent"
    elif avg > 16000:
        perf = "Good"
    else:
        perf = "Needs Improvement"
    print("Performance Rating:", perf)


def main():
    print("--- Problem 1 ---")
    problem_1()
    print("\n--- Problem 2 ---")
    problem_2()
    print("\n--- Problem 3 ---")
    problem_3()
    print("\n--- Problem 4 ---")
    problem_4()


if __name__ == "__main__":
    main()
