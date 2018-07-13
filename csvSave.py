import csv as csv
    

"""
vars:

Functionality: saves csv file, writes statistics to it. Potentially just add this function
to the processor class.
"""
def save(rxnID, file, mean, variance, folderwoID):
    
    with open(folderwoID+'/summary_%s.csv' % (rxnID),'a+') as csvfile:
        
        swriter = csv.writer(csvfile)

        swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])
