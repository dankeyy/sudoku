
def pretty_print(grid, base = 3, side = 9): 
	expandLine = lambda line: line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]

	line0  = expandLine("╔═══╤═══╦═══╗")
	line1  = expandLine("║ . │ . ║ . ║")
	line2  = expandLine("╟───┼───╫───╢")
	line3  = expandLine("╠═══╪═══╬═══╣")
	line4  = expandLine("╚═══╧═══╩═══╝")
	symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	nums   = [ [""]+[symbol[n] for n in row] for row in grid ]
	print(line0)

	for r in range(1,side+1):
	    print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
	    print([line2,line3,line4][(r%side==0)+(r%base==0)])

if __name__ == "__main__":
    pass