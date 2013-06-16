# CSC_TYPES and DT_TYPES lists definitions
#
# [0]   self-explanatory label
# [1]   short label
# [2]   either list of subsystems or number of chambers

CSC_TYPES = [
	['ME+','p',[
		["ME+4",'4',[
			["ME+4/ALL",'ALL', 36],
			["ME+4/2",'2', 36],
			["ME+4/1",'1', 18]]
		],
		["ME+3",'3',[
			["ME+3/ALL",'ALL', 36],
			["ME+3/2",'2', 36],
			["ME+3/1",'1', 18]]
		],
		["ME+2",'2',[
			["ME+2/ALL",'ALL', 36],
			["ME+2/2",'2', 36],
			["ME+2/1",'1', 18]]
		],
		["ME+1",'1',[
			["ME+1/ALL",'ALL', 36],
			["ME+1/3",'3', 36],
			["ME+1/2",'2', 36],
			["ME+1/1",'1', 36],#["ME+1/4",'4', 36]
			]
		]],
		1
	],
	['ME-','m',[
		["ME-1",'1',[
			#["ME-1/4",'4', 36],
			["ME-1/1",'1', 36],
			["ME-1/2",'2', 36],
			["ME-1/3",'3', 36],
			["ME-1/ALL",'ALL', 36]]
		],
		["ME-2",'2',[
			["ME-2/1",'1', 18],
			["ME-2/2",'2', 36],
			["ME-2/ALL",'ALL', 36]]
		],
		["ME-3",'3',[
			["ME-3/1",'1', 18],
			["ME-3/2",'2', 36],
			["ME-3/ALL",'ALL', 36]]
		],
		["ME-4",'4',[
			["ME-4/1",'1', 18],
			["ME-4/2",'2', 36],
			["ME-4/ALL",'ALL', 36]]
		]],
		2
	]
];

DT_TYPES = [
	['MB+2','2',[
		["MB+2/1",'1', 12],
		["MB+2/2",'2', 12],
		["MB+2/3",'3', 12],
		["MB+2/4",'4', 14]]
	],
	['MB+1','1',[
		["MB+1/1",'1', 12],
		["MB+1/2",'2', 12],
		["MB+1/3",'3', 12],
		["MB+1/4",'4', 14]]
	],
	['MB-0','0',[
		["MB-0/1",'1', 12],
		["MB-0/2",'2', 12],
		["MB-0/3",'3', 12],
		["MB-0/4",'4', 14]]
	],
	['MB-1','-1',[
		["MB-1/1",'1', 12],
		["MB-1/2",'2', 12],
		["MB-1/3",'3', 12],
		["MB-1/4",'4', 14]]
	],
	['MB-2','-2',[
		["MB-2/1",'1', 12],
		["MB-2/2",'2', 12],
		["MB-2/3",'3', 12],
		["MB-2/4",'4', 14]]
	],
	['MB-ALL','ALL',[
		["MB-ALL/1",'1', 12],
		["MB-ALL/2",'2', 12],
		["MB-ALL/3",'3', 12],
		["MB-ALL/4",'4', 14]]
	]
];
