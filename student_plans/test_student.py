from smume.student_plan import StudentPlan

# Create a student plan for the 2024–25 catalog, starting in Fall 2024
plan = StudentPlan("2024-25", start_year=2024, start_term="Fall")

grouped = plan.courses_by_term()

# Mark some courses as completed
plan.mark_completed("MTH 171")
plan.mark_completed("MTH 172")
plan.mark_completed("PHY 171")
plan.mark_completed("PHY 171L")
plan.mark_completed("PHY 172")

# Move a course to a specific term
plan.set_course_term("GE 204", 2026, "Spring") # This violates a prerequisite as we'll see

# Substitute a course
plan.substitute_course(old_name="COR 310", new_name="COR 320") # This is a valid substitution

# Switch writing intensive courses
plan.switch_writing_intensive(old_name="COR 250W", new_name="COR 210W") # This is a valid switch

# Check prerequisites, corequisites, and coprerequisites (dependency check)
dependency_issues = plan.print_dependency_issues()

# Check for category requirements
plan.print_category_requirement_issues()

# Generate a visual representation of the plan
from smume.graph_builder import build_graph
build_graph(plan, output_path="test_student", format="svg")