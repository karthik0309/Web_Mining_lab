def calculate_PageRank(outlinks):
	d = 0.9	
	size = len(outlinks[0])
	page_ranks = [round(1/size, 2) for i in range(size)]	
	out_degrees = []
	for i in range(size):
		sums = 0
		for j in range(size):
			sums += outlinks[j][i]
		out_degrees.append(sums)
		
	
	print('Initial page ranks:')
	print(page_ranks)
	
	for _ in range(2):
		dup = page_ranks[:]
		for i in range(size):
			temp = 0
			for j in range(size):
				if outlinks[i][j] == 1:
					temp += dup[j] / out_degrees[j]
			temp *= d
			temp += (1-d)
			page_ranks[i] = round(temp, 2)
		
	return page_ranks
			
outlinks=[[0,1,0,0,1],
		  [0,0,0,0,1],
		  [1,0,0,1,1],
		  [0,1,0,0,0],
		  [1,0,0,1,0]]


page_ranks = calculate_PageRank(outlinks)	
print()
print('The converged page rank is:')
print(page_ranks)
print()
sums = 0
for i in page_ranks:
	sums += i
print('The sum of page ranks is: ', round(sums, 2))