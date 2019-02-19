temp = [{8: '✔️ success'}, {5: '✖️ fail'}, {5: '✖️ fail'}, {3: '✖️ fail'}]
temp2 = [8,5,5,3]
a = b = ''
index = 0
for item in temp:
	a = temp2[index]
	b = temp[index]
	index += 1

print(a)
print(b)
print(temp[0][8])