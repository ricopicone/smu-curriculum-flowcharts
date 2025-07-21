

from smume.student_plan import StudentPlan
from smume.report import generate_html
from smume.graph_builder import build_graph
import os

class MEPlanDocument:
    def __init__(self, student_plan: StudentPlan, output_dir="output", filename="ME-Plan-Document"):
        self.plan = student_plan
        self.output_dir = output_dir
        self.filename = filename
        self.report_html = ""
        self.graph_path = ""

        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self):
        """Generate HTML report from the student plan."""
        self.report_html = generate_html(self.plan)

    def generate_graph(self):
        """Generate SVG graph from the student plan."""
        output_path = os.path.join(self.output_dir, self.filename)
        self.graph_path = build_graph(self.plan, output_path)

    def save_combined_document(self):
        """Combine HTML report and embedded SVG graph into a single HTML file."""
        if not self.report_html:
            self.generate_report()
        if not self.graph_path:
            self.generate_graph()

        svg_content = ""
        with open(self.graph_path, "r") as f:
            svg_content = f.read()

        combined_html = f"""
        <html>
        <head><meta charset="utf-8"><title>Student Plan</title></head>
        <body>
            <h1>Student Plan Report + Flowchart</h1>
            {self.report_html}
            <div>{svg_content}</div>
        </body>
        </html>
        """

        combined_path = os.path.join(self.output_dir, f"{self.filename}.html")
        with open(combined_path, "w") as f:
            f.write(combined_html)
        return combined_path