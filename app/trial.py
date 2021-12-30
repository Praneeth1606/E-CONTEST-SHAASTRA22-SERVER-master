import os, filecmp, multiprocessing, re
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

def interpret(program,inputPath,outputPath) :
	global MAX_CELLS, MAX_VAL, MIN_VAL, MAX_SIZE
	global lineno, ptr, data, brackets, inp_buff, out_buff, inp_ind

	strlen = len(program)
	if (strlen > MAX_SIZE) :
		print("MEMORY LIMIT EXCEEDED")
		return


	#with open('programs.txt', 'w') as f:
		#f.write(program)

	with open(outputPath, 'w') as f:
		f.write('')

	os.system(f'asciidots programs.txt < {inputPath} >> {outputPath}')

	with open(outputPath, 'r') as f:
		out_buff = f.read()
		if out_buff[:55] == "failed to import curses; running in compatibility mode\n":
			out_buff = out_buff[55:]

	if out_buff=='':
		print("SYNTAX ERROR: No output obtained")
		return

	with open(outputPath,'w') as f :
		f.write(out_buff)

	print("ANSWER WRITTEN")
	return


count = 0
qn_no = '2'
pno = '1'
code = 'Pls work'
inputPath = './app/evaluation/input/qn' + qn_no
inputPath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/input/qn' + qn_no
'''
for filename in os.listdir(inputPath):
	if 'tc' in filename:
		fno = re.sub('[^0-9]+', '', filename)
		outputfilePath = './app/evaluation/output' + pno + '.txt'
		outputfilePath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/output' + pno + '.txt'
		with open(outputfilePath, 'w+') as mfile:
			count += 1
			inpfilePath = inputPath + '/' + filename
			#Q = multiprocessing.Queue()
			#prc = multiprocessing.Process(target=interpret, args=(code, inpfilePath, outputfilePath, Q))
			#prc.daemon = True
			#prc.start()

			#prc.join(5)

			''''''if prc.is_alive():
				prc.terminate()
				prc.join(1)
				mfile.close()
				os.remove(outputfilePath)
				print('TIME LIMIT EXCEEDED')
			''''''

			interpret(code, inpfilePath, outputfilePath)

			#Message = Q.get()
			Message = 'ANSWER WRITTEN'
			if Message == 'ANSWER WRITTEN':
				# with open('./app/evaluation/expected_output/qn'+qn_no+'/output-'+str(fno)+'.txt') as tgtfile :
				with open('C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn' + qn_no + '/output-' + str(fno) + '.txt') as tgtfile:
				# if filecmp.cmp(outputfilePath,'./app/evaluation/expected_output/qn'+qn_no+'/output-'+str(fno)+'.txt') :
					if filecmp.cmp(outputfilePath,'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn' + qn_no + '/output-' + str(fno) + '.txt'):
						pass
					else:
						tgtfile.close()
						mfile.close()
						#os.remove(outputfilePath)
						print('WRONG ANSWER')
			else:
				mfile.close()
				#os.remove(outputfilePath)
				print(Message)
#os.remove(outputfilePath)
print('CORRECT ANSWER')
'''

for filename in os.listdir(inputPath):
	if 'tc' in filename:
		fno = re.sub('[^0-9]+', '', filename)
		outputfilePath = './app/evaluation/output' + pno + '.txt'
		outputfilePath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/output' + pno + '.txt'

		# with open(outputfilePath, 'w+') as mfile:
		count += 1
		inpfilePath = inputPath + '/' + filename
		'''
		Q = multiprocessing.Queue()
		prc = multiprocessing.Process(target=interpret, args=(code, inpfilePath, outputfilePath, Q))
		prc.daemon = True
		prc.start()

		prc.join(5)
		
		if prc.is_alive():
			prc.terminate()
			prc.join(1)
			# mfile.close()
			os.remove(outputfilePath)
			return 'TIME LIMIT EXCEEDED'
		else:
		'''
		interpret(code, inpfilePath, outputfilePath)
		#Message = Q.get()
		Message = 'ANSWER WRITTEN'
		if Message == 'ANSWER WRITTEN':
			# with open('./app/evaluation/expected_output/qn'+qn_no+'/output-'+str(fno)+'.txt') as tgtfile :
			with open('C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn' + qn_no + '/output-' + str(fno) + '.txt') as tgtfile:
				# if filecmp.cmp(outputfilePath,'./app/evaluation/expected_output/qn'+qn_no+'/output-'+str(fno)+'.txt') :
				if filecmp.cmp(outputfilePath,'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn' + qn_no + '/output-' + str(fno) + '.txt'):
					pass
				else:
					tgtfile.close()
					# mfile.close()
					os.remove(outputfilePath)
					print('WRONG ANSWER')
		else:
			# mfile.close()
			os.remove(outputfilePath)
			print(Message)

os.remove(outputfilePath)
print('CORRECT ANSWER')

'''
inputPath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/input/qn2/tc1.txt'
#outputPath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/trial_.txt'
pno='1'
outputPath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/output' + pno + '.txt'
program = "Pls work"
interpret(program, inputPath, outputPath)
if filecmp.cmp(outputPath,'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn2/output-1.txt'):
	print("Matching")
os.remove(outputPath)
'''