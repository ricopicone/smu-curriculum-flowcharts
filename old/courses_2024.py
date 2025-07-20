from curriculum import Curriculum

curriculum = Curriculum("ME 2024")

# have to add this course because it's a prereq
curriculum.course('COR 120', 4, category="C")

# math and science
curriculum.course('MTH 171', 4, category="MS")
curriculum.course('PHY 171', 4, category="MS").add_coprereq('MTH 171')
curriculum.course('PHY 171L', 1, category="MS").add_coreq('PHY 171')
curriculum.course('MTH 172', 4, category="MS").add_prereq('MTH 171')
curriculum.course('PHY 172', 4, category="MS").add_coprereq('MTH 172').add_prereq('PHY 171')
curriculum.course('PHY 172L', 1, category="MS").add_coreq('PHY 172')
curriculum.course('CHM 145', 3, category="MS")
curriculum.course('MTH 353', 3, category="MS").add_prereq('MTH 172')

# GE
curriculum.course('GE 104', 3, category="GE").add_prereq('MTH 171').add_prereq('PHY 171')
curriculum.course('GE 204', 3, category="GE").add_prereq('MTH 171').add_prereq('PHY 171')
curriculum.course('GE 205', 3, category="GE").add_prereq('GE 204')
curriculum.course('GE 206', 3, category="GE").add_prereq('GE 204')
curriculum.course('GE 207', 1, category="GE").add_coprereq('GE 206')
# curriculum.course('GE 359', 3, category="GE")

# ME
curriculum.course('ME 100', 1, category="ME")
curriculum.course('ME 201', 2, category="ME").add_prereq('COR 120')
curriculum.course('ME 300', 3, category="ME").add_prereq('GE 206')
curriculum.course('ME 300L', 1, category="ME").add_coprereq('ME 300')
curriculum.course('ME 303', 3, category="ME").add_prereq('GE 206').add_prereq('CHM 145')
curriculum.course('ME 316', 2, category="ME").add_coprereq('ME 345')
curriculum.course('ME 340', 3, category="ME").add_prereq('CHM 145').add_prereq('PHY 172').add_coprereq('MTH 172')
curriculum.course('ME 345', 3, category="ME").add_prereq('MTH 172').add_prereq('PHY 172')
curriculum.course('ME 302', 3, category="ME").add_prereq('GE 206')
curriculum.course('ME 308', 3, category="ME").add_prereq('GE 205').add_prereq('GE 206').add_prereq('MTH 172')
curriculum.course('ME 309', 2, category="ME").add_coreq('ME 308')
curriculum.course('ME 350', 3, category="ME")
curriculum.course('ME 370', 3, category="ME").add_prereq('ME 345').add_prereq('GE 205').add_coprereq('MTH 353')
curriculum.course('ME 430', 3, category="ME").add_prereq('ME 340').add_prereq('ME 308').add_coreq('ME 430L')
curriculum.course('ME 430L', 2, category="ME")
curriculum.course('ME 498', 3, category="ME").add_prereq('ME 302').add_prereq('ME 370').add_coprereq('ME 430')
curriculum.course('ME 499', 3, category="ME").add_prereq('ME 498')
curriculum.course('ME El. 1', 3, category="ME")
curriculum.course('ME El. 2', 3, category="ME")
curriculum.course('ME El. 3', 3, category="ME")