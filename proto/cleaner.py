total = 1410000

a = ["2,193",826,"9,643","1,338","151,199","9,801","65,787","1,742","6,491",
"284,171","41,380","4,120","2,189","21,516","7,293","2,838","3,229","3,044",
"8,361","1,290","32,244","247,681","17,706","8,083","1,234","6,463",484,
"1,213","10,800","8,591","116,136","3,407","97,773","21,077","1,798","12,990","2,262","8,640","39,489",
"4,503","12,546",375,"4,628","64,105","14,868",605,"21,206","14,812","1,189","4,378",262]


for i in range(len(a)):
	if type(a[i]) != int:
		a[i] = a[i].replace(",", "")

a = [int(i) for i in a]

a = [(total - i) for i in a]