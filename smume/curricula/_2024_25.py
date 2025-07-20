from smume.curriculum import Curriculum
from smume.generic_plan import GenericPlan

curriculum = Curriculum("ME 2024–25")
    
# have to add this course because it's a prereq
curriculum.course('COR 120', 4, category="C", full_name="Critical Reading and Writing")

# math and science
curriculum.course('MTH 171', 4, category="MS", full_name="Calculus I")
curriculum.course('PHY 171', 4, category="MS", full_name="Physics I").add_coprereq('MTH 171')
curriculum.course('PHY 171L', 1, category="MS", full_name="Physics I Laboratory").add_coreq('PHY 171')
curriculum.course('MTH 172', 4, category="MS", full_name="Calculus II").add_prereq('MTH 171')
curriculum.course('PHY 172', 4, category="MS", full_name="Physics II").add_coprereq('MTH 172').add_prereq('PHY 171')
curriculum.course('PHY 172L', 1, category="MS", full_name="Physics II Laboratory").add_coreq('PHY 172')
curriculum.course('CHM 145', 3, category="MS", full_name="Chemistry for Engineers", note="Chemistry for Engineers. Or CHM 141 (more credits).")
curriculum.course('MTH 353', 3, category="MS", full_name="Linear Algebra").add_prereq('MTH 172')

# GE
curriculum.course('GE 104', 3, category="GE", full_name="Engineering Computing").add_prereq('MTH 171').add_prereq('PHY 171')
curriculum.course('GE 204', 3, category="GE", full_name="Statics").add_prereq('MTH 171').add_prereq('PHY 171')
curriculum.course('GE 205', 3, category="GE", full_name="Dynamics").add_prereq('GE 204')
curriculum.course('GE 206', 3, category="GE", full_name="Mechanics of Materials").add_prereq('GE 204')
curriculum.course('GE 207', 1, category="GE", full_name="Mechanics of Materials Laboratory").add_coprereq('GE 206')

# ME
curriculum.course('ME 100', 1, category="ME", full_name="Mechanical Engineering Seminar")
curriculum.course('ME 201', 2, category="ME", full_name="Technical Communication").add_prereq('COR 120')
curriculum.course('ME 300', 3, category="ME", full_name="Manufacturing").add_prereq('GE 206')
curriculum.course('ME 300L', 1, category="ME", full_name="Manufacturing Laboratory").add_coprereq('ME 300')
curriculum.course('ME 303', 3, category="ME", full_name="Materials Science").add_prereq('GE 206').add_prereq('CHM 145')
curriculum.course('ME 316', 2, category="ME", full_name="Numerical Methods").add_coprereq('ME 345')
curriculum.course('ME 340', 3, category="ME", full_name="Thermodynamics I").add_prereq('CHM 145').add_prereq('PHY 172').add_coprereq('MTH 172')
curriculum.course('ME 345', 3, category="ME", full_name="Mechatronics").add_prereq('MTH 172').add_prereq('PHY 172')
curriculum.course('ME 302', 3, category="ME", full_name="Machine Design").add_prereq('GE 206')
curriculum.course('ME 308', 3, category="ME", full_name="Fluid Mechanics I").add_prereq('GE 205').add_prereq('GE 206').add_prereq('MTH 172')
curriculum.course('ME 309', 2, category="ME", full_name="Fluid Mechanics Laboratory").add_coreq('ME 308')
curriculum.course('ME 350', 3, category="ME", full_name="Parametric Solid Modeling")
curriculum.course('ME 370', 3, category="ME", full_name="System Dynamics and Control").add_prereq('ME 345').add_prereq('GE 205').add_coprereq('MTH 353')
curriculum.course('ME 430', 3, category="ME", full_name="Heat Transfer").add_prereq('ME 340').add_prereq('ME 308').add_coreq('ME 430L')
curriculum.course('ME 430L', 2, category="ME", full_name="Heat Transfer Laboratory")
curriculum.course('ME 498', 3, category="ME", full_name="Senior Design I").add_prereq('ME 302').add_prereq('ME 370').add_coprereq('ME 430')
curriculum.course('ME 499', 3, category="ME", full_name="Senior Design II").add_prereq('ME 498')
curriculum.course('ME El. 1', 3, category="ME", full_name="Mechanical Engineering Elective 1")
curriculum.course('ME El. 2', 3, category="ME", full_name="Mechanical Engineering Elective 2")
curriculum.course('ME El. 3', 3, category="ME", full_name="Mechanical Engineering Elective 3")

generic_plan = GenericPlan(curriculum)
generic_plan.apply_term_mapping({
    "1F": ["COR 120", "MTH 171", "PHY 171", "PHY 171L", "ME 100"],
    "1S": ["MTH 172", "PHY 172", "PHY 172L", "GE 104", "ME 201"],
    "2F": ["GE 204", "CHM 145", "MTH 353"],
    "2S": ["GE 205", "GE 206", "GE 207", "ME 350"],
    "3F": ["ME 300", "ME 300L", "ME 303", "ME 316", "ME 345", "ME 340"],
    "3S": ["ME 302", "ME 308", "ME 309", "ME 370"],
    "4F": ["ME 430", "ME 430L", "ME 498", "ME El. 1"],
    "4S": ["ME 499", "ME El. 2", "ME El. 3"],
})