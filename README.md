[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Uq6lo4ay)
# hw02 – Course Enrollment Roster (Dictionaries + Sets)

## Story

A university wants to see **who is in each course**.

They collect many registration records. Each record has a **student id** and a
**course id**. A student can register for many courses. Sometimes, a student
may appear more than once in the same course (for example, system errors).

You will build a function that takes a list of `(student_id, course_id)` pairs
and returns a **roster**: each course id maps to a **sorted list of unique
student ids** in that course.

---

## Technical Description

Write a function:

```python
def build_roster(registrations):
    ...
```
- `registrations`: a list of `(student_id, course_id)` pairs (two strings).

- Return value: a dictionary where:

    - Keys are course ids (strings).

    - Values are sorted lists of unique student ids (strings) enrolled in that course.

Example:

```
registrations = [
    ("s1", "CS101"),
    ("s2", "CS101"),
    ("s1", "MATH200"),
    ("s1", "CS101"),  # duplicate registration
]

build_roster(registrations)
# -> {
#    "CS101": ["s1", "s2"],
#    "MATH200": ["s1"]
# }
```

### Constraints

- `len(registrations)` can be from `0` to `100_000`.

- Student ids and course ids are non-empty strings.

- A student may appear multiple times in the same course; treat as one enrollment.
- 
### Expected Complexity

- Building the internal structure: about O(n) time, where n is the number of registration pairs.

- Sorting the student lists: O(m log m) per course, where m is the number of distinct students in that course.

- Total time: about O(n log n) in the worst case.

- Space: O(n) for storing student-course information.
---

## 8 Steps of Coding – Scaffold (hw02)
Use the 8 Steps. Write your thinking as comments or notes.

1. Read & Understand the problem

    - What question is the university asking? Write it as one short sentence.

1. Re-phrase the problem

    - Use the words input, output, and duplicate.

    - For example: “Input: a list of …; Output: a dictionary that … and removes duplicates.”

1. Identify input, output, variables

    - Input: what type? what does each element mean?

    - Output: what type? what does each value mean?

    - Variables: how will you store students for a course? one structure per course? one structure for all?

1. Break down the problem

- How will you group registrations by course?

- How will you handle duplicates?

- When will you sort the student ids?

1. Pseudocode the solution

    - Write a short step-by-step plan for:

        - Creating the groups.

        - Removing duplicates.

        - Sorting the lists.
    
#### 6–8. Write code, Debug, Optimize

- Step 6: translate your pseudocode into Python in main.py.

- Step 7: run tests and add your own extra tests.

- Step 8: explain why your solution matches the expected complexity.
___

## Hints (not full solutions)
1. You can use a dictionary from course_id to a set of student ids to avoid duplicates, then convert to sorted list at the end.

1. Make sure you always return lists in the final dictionary, not sets.

1. Think about what happens if registrations is empty.
___

## How to Run Tests
```
python -m pytest -q
```
---
## FAQ
Q1: Do I read from input() or work with registrations?
Use the registrations argument only. Do not use input() for this homework.

Q2: Do I need to preserve the order of registrations in the input?
No. The output for each course must be a sorted list of student ids.

Q3: What if the same (student_id, course_id) pair appears many times?
Treat it as one enrollment. The student id should appear only once in the list
for that course.

Q4: What Big-O complexity do you expect?
We expect about O(n log n) time total. The grouping is O(n), sorting is O(n log n)
in the worst case.

Q5: How do I read long pytest error messages?
Look near the bottom for the lines that start with E. They show what the
test expected and what your function returned.

Q6: Will you grade code style?
Yes. We will check that your code is readable: good names, simple loops, and
clear logic.

Q7: Can I use defaultdict or setdefault?
Yes, they are part of the standard library and are allowed. You can also use
basic dictionary patterns without them.