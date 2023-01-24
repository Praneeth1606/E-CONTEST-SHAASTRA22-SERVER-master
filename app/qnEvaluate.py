import filecmp
import os
import re
import multiprocessing
from app.compiler import interpret

noTC = {'1': 1, '2': 5, '3': 5, '4': 5, '5': 16, '6': 5, '7': 5}


def score(code, qn_no, pno):
    count = 0
    inputPath = './app/evaluation/input/qn' + qn_no
    #inputPath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/input/qn' + qn_no
    for filename in os.listdir(inputPath):
        if 'tc' in filename:
            fno = re.sub('[^0-9]+', '', filename)
            outputfilePath = './app/evaluation/output' + pno + '.txt'
            #outputfilePath = 'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/output' + pno + '.txt'
            
            count += 1
            inpfilePath = inputPath + '/' + filename
            Q = multiprocessing.Queue()
            prc = multiprocessing.Process(target=interpret, args=(code, inpfilePath, outputfilePath, Q))
            prc.daemon = True
            prc.start()

            prc.join(5)

            if prc.is_alive():
                prc.terminate()
                prc.join(1)
                #mfile.close()
#                 os.remove(outputfilePath)
                return 'TIME LIMIT EXCEEDED'
            else:
                Message = Q.get()
                if Message == 'ANSWER WRITTEN':
                    with open('./app/evaluation/expected_output/qn'+qn_no+'/output-'+str(fno)+'.txt') as tgtfile :
                    #with open('C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn' + qn_no + '/output-' + str(fno) + '.txt') as tgtfile:
                        if filecmp.cmp(outputfilePath,'./app/evaluation/expected_output/qn'+qn_no+'/output-'+str(fno)+'.txt') :
                        #if filecmp.cmp(outputfilePath,'C:/Users/Admin/PycharmProjects/E-CONTEST-SHAASTRA20-SERVER-MASTER/app/evaluation/expected_output/qn' + qn_no + '/output-' + str(fno) + '.txt'):
                            pass
                        else:
                            tgtfile.close()
                            #mfile.close()
#                             os.remove(outputfilePath)
                            return 'WRONG ANSWER'
                else:
                    #mfile.close()
#                     os.remove(outputfilePath)
                    return Message

#     os.remove(outputfilePath)
    return 'CORRECT ANSWER'
