
from collections import defaultdict
from typing import Dict, List, Iterable, Tuple

def build_roster(registrations: Iterable[Tuple[str, str]]) -> Dict[str, List[str]]:
    """
    Given a list (or any iterable) of (student_id, course_id) pairs, build a course roster.

    Returns:
        A dictionary where:
          - each key is a course id (string)
          - each value is a sorted list of unique student ids (strings)
            enrolled in that course

    Rules:
        - Duplicate registrations for the same (student_id, course_id) pair
          should appear only once in the output.
        - Treat course IDs and student IDs as case-sensitive.
    """
    roster_sets: Dict[str, set] = defaultdict(set)

    for student_id, course_id in registrations:
        roster_sets[course_id].add(student_id)

    roster: Dict[str, List[str]] = {
        course_id: sorted(students)
        for course_id, students in roster_sets.items()
    }
    return roster

if __name__ == "__main__":
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
