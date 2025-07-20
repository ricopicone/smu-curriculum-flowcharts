from smume.curricula._2024_25 import curriculum, generic_plan
from smume.generic_plan import GenericPlan
from smume.graph_builder import build_graph

print(f"Loaded curriculum: {curriculum.name}")
print(f"Total courses: {len(curriculum.courses)}")
print(f"Courses: {list(curriculum.courses)}")

build_graph(generic_plan, output_path="plan_2024_25", format="svg")