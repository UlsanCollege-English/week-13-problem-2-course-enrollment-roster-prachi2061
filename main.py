from collections import defaultdict
from typing import Dict, List, Iterable, Tuple

def build_roster(registrations: Iterable[Tuple[str, str]]) -> Dict[str, List[str]]:
    """
    Build a course roster from (student_id, course_id) pairs.
    Each course maps to a sorted list of unique student IDs.
    """
    roster_sets: Dict[str, set] = defaultdict(set)
    for student_id, course_id in registrations:
        roster_sets[course_id].add(student_id)

    return {course_id: sorted(students) for course_id, students in roster_sets.items()}

if __name__ == "__main__":
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
