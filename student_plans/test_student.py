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


# Generate a visual representation of the plan
from smume.graph_builder import build_graph
build_graph(plan, output_path="test_student", format="svg")