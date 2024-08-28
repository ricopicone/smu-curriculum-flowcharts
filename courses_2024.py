# have to add this course because it's a prereq
new_course('COR 120',4,'1F',False)

# math and science
new_course('MTH 171',4,'1F',False)
new_course('PHY 171',4,'1F',False) \
	.add_coprereq('MTH 171')
new_course('PHY 171L',1,'1F',False) \
	.add_coreq('PHY 171')
new_course('MTH 172',4,'1S',False) \
	.add_prereq('MTH 171')
new_course('PHY 172',4,'1S',False) \
	.add_coprereq('MTH 172')
new_course('PHY 172L',1,'1S',False) \
	.add_coreq('PHY 172')
new_course('CHM 145',3,'2F',False)
new_course('MTH 353',3,'2S',False) \
	.add_prereq('MTH 172')

# GE
new_course('GE 104',3,'1S',False) \
	.add_prereq('MTH 171') \
	.add_prereq('PHY 171')
new_course('GE 204',3,'2F',False) \
	.add_prereq('MTH 171') \
	.add_prereq('PHY 171')
new_course('GE 205',3,'2S',False) \
	.add_prereq('GE 204')
new_course('GE 206',3,'2S',False) \
	.add_prereq('GE 204')
new_course('GE 207',1,'2S',False) \
	.add_coprereq('GE 206')
# new_course('GE 359',3,'4S')

# ME
new_course('ME 100',1,'1F',False)
new_course('ME 201',2,'1S',False) \
	.add_prereq('COR 120')
new_course('ME 300',3,'3F',False) \
	.add_prereq('GE 206')
new_course('ME 300L',1,'3F',False) \
	.add_coprereq('ME 300')
new_course('ME 303',3,'3F',False) \
	.add_prereq('GE 206') \
	.add_prereq('CHM 145')
new_course('ME 316',2,'3F',False) \
	.add_coprereq('ME 345')
new_course('ME 340',3,'3F',False) \
	.add_prereq('CHM 145') \
	.add_prereq('PHY 172') \
	.add_coprereq('MTH 172')
new_course('ME 345',3,'3F',False) \
	.add_prereq('MTH 172') \
	.add_prereq('PHY 172')
new_course('ME 302',3,'3S',False) \
	.add_prereq('GE 206')
new_course('ME 308',3,'3S',False) \
	.add_prereq('GE 205') \
	.add_prereq('GE 206') \
	.add_prereq('MTH 172')
new_course('ME 309',2,'3S',False) \
	.add_coreq('ME 308')
new_course('ME 350',3,'3S',False)
new_course('ME 370',3,'3S',False) \
	.add_prereq('ME 345') \
	.add_prereq('GE 205') \
	.add_coprereq('MTH 353')
new_course('ME 430',3,'4F',False) \
	.add_prereq('ME 340') \
	.add_prereq('ME 308') \
	.add_coreq('ME 430L')
new_course('ME 430L',2,'4F',False)
new_course('ME 498',3,'4F',False) \
	.add_prereq('ME 302') \
	.add_prereq('ME 370') \
	.add_coprereq('ME 430')
new_course('ME 499',3,'4S',False) \
	.add_prereq('ME 498')
new_course('ME El. 1',3,'4F',False)
new_course('ME El. 2',3,'4S',False)
new_course('ME El. 3',3,'4S',False)