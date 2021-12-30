import os
MAX_SIZE = 5e6
MAX_CELLS  = 65536
MAX_VAL = 255
MIN_VAL = 0

lineno = 1
ptr = 0
data = [0] * MAX_CELLS
brackets = []

inp_buff = ''
out_buff = ''
inp_ind = 0

def interpret(program,inputPath,outputPath,Q) :
	global MAX_CELLS, MAX_VAL, MIN_VAL, MAX_SIZE
	global lineno, ptr, data, brackets, inp_buff, out_buff, inp_ind

	#with open(programfilePath, 'r') as f:
	#	program = f.read()

	strlen = len(program)
	if (strlen > MAX_SIZE) :
		Q.put("MEMORY LIMIT EXCEEDED")
		return

	with open('programs.txt', 'wb') as f:
		f.write(bytes(program,'utf-8'))

	with open(outputPath, 'w') as f:
		f.write('')

	os.system(f'asciidots programs.txt < {inputPath} >> {outputPath}')

	with open(outputPath, 'r') as f:
		out_buff = f.read()
		if out_buff[:55] == "failed to import curses; running in compatibility mode\n":
			out_buff = out_buff[55:]

	if out_buff=='':
		Q.put("SYNTAX ERROR: No output obtained")
		return

	with open(outputPath,'w') as f :
		f.write(out_buff)

	Q.put("ANSWER WRITTEN")
	return
