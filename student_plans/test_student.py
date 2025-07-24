
from smume.student_plan import StudentPlan
import smume.report

# Create a student plan for the 2024–25 catalog, starting in Fall 2024
plan = StudentPlan("2024-25", start_year=2024, start_term="Fall")

grouped = plan.courses_by_term()

# Mark some courses as completed
plan.mark_completed("MTH 171")
plan.mark_completed("MTH 172")
plan.mark_completed("PHY 171")
plan.mark_completed("PHY 171L")
plan.mark_completed("PHY 172")
plan.mark_completed("COR 100")
plan.mark_completed("COR 110")
plan.mark_completed("COR 120")

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

# Generate a text-based report of the plan
report = smume.report.Report(plan)
print(report.generate_text())

# Add a note to the student plan
plan.add_note("This is a test note for the student plan.", date="2024-10-01")

# Generate an HTML report
print(report.generate_html())

# Save the report to a file
report.save("student_plan_report.html")

# Generate a combined HTML document with the report and flowchart
from smume.me_plan_document import MEPlanDocument
document = MEPlanDocument(plan)
combined_path = document.save_combined_document()
print(f"Combined document saved to: {combined_path}")

# Export the combined document to PDF
pdf_path = document.export_combined_document_pdf()
print(f"PDF document saved to: {pdf_path}")