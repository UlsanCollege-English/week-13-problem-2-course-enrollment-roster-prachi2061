
# main.py
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
        - Treat course IDs and student IDs as case-sensitive, e.g. "CS101" != "cs101".
    """
    roster_sets: Dict[str, set] = defaultdict(set)

    for student_id, course_id in registrations:
        # Assumes inputs are valid strings as per tests; otherwise could add type checks
        roster_sets[course_id].add(student_id)

    # Convert sets to sorted lists for deterministic output
    roster: Dict[str, List[str]] = {
        course_id: sorted(students)
        for course_id, students in roster_sets.items()
    }
    return roster


if __name__ == "__main__":
    # Optional manual test
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),  # duplicate registration; should not duplicate in output
    ]
    print(build_roster(sample))
    # Expected: {'CS101': ['s1', 's2'], 'MATH200': ['s1']}
