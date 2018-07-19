
import time
import cv2
import numpy as np
import CameraOps as co
import csv as csv
import os
import datetime
from matplotlib import pyplot as plt


"""
variables: 
    reaction_id - identifier for reaction 
    interv - time between pictures being taken
    t- total time of the experiment
    dir_file - the path of the destination of the picture files
    n - camera ID

functionality: processsor is the class that contains all of the functions to execute the gather or images
and the detection of images and the 

"""
class ImageCapture:
	def __init__(self, time, interv,rxn_id, dir_file):
		
		self.reaction_id=rxn_id
	
		self.interv=interv

		self.t  = time
		
		self.dir_file = dir_file

		self.rxn_foldername = os.path.join(self.dir_file, str(self.reaction_id))
	'''
	notes: Processor Class
	var 
	functionality
	'''


	def run(self):
		#creates directory
		if not os.path.exists(self.rxn_foldername):
		
			os.makedirs(self.rxn_foldername)

		for i in range(int(self.t/self.interv)):
			#runs a single image process
			tempM,tempV=self.iteration()
			#time intervals between trials
			time.sleep(self.interv) 
	

	"""
	notes

	var

	functionality

	"""        
			
	def getTime(self):
		#gets time
		currentDT = datetime.datetime.now()
		#formats
		time=currentDT.strftime('%Y%m%d%H%M%s')
		
		return time
		
	"""
	notes

	var

	functionality

	"""
	def iteration(self):
		
		#add camera number as a user input

		#change to 1 for functionality of the webcam 
		#OPTIM: change here for more user options, will have to make this a user inputted variable
		initial_img = co.snap(0)

		name= self.getTime()

		cv2.imwrite("frame%s.jpg" % name, initial_img)
		
		img = cv2.imread("frame%s.jpg" % name)

		#img = img[:,:,::-1] # Change BGR to RGB format - Tim
		print('***img',img[:2,:2,:])

		center, radius = co.detect(co, img)

		# Adjust radius - Hannah
		#print('***radius:', radius)
		radius = radius - int(0.1*radius)

		# Draw circle into image
		circle=cv2.circle(img,center,radius,(0,255,0),2)
		circle = circle[:,:,::-1] #Change BGR to RGB format - Tim
		np.save(self.rxn_foldername+"/%s.npy" % (name),circle)

		img = img[:,:,::-1] #Change BGR to RGB format - Tim

		mask=np.zeros((int(img.shape[0]),int(img.shape[1]),3))
	
		left=radius
		right=radius
		top=radius
		bottom=radius

		for i in range(int(radius)):
			delta=int(np.sqrt(int(radius)**2-int(i)**2))
			
			left=delta
			right=delta
			up=i
			down=i
			#this is used to detect boundaries and ensure that there is no boudary jumping
			if mask.shape[0]<center[0]+right:
				
				right=-center[0]+mask.shape[0]-1

			if 0>center[0]-left:
				
				left=center[0]
			
			if mask.shape[1]<center[1]+down:
				
				down=-center[1]+mask.shape[1]-1
			
			if 0>center[1]-up:
				
				up=center[1]
			
			#pythagorean
			delta=int(np.sqrt(int(radius)**2-int(i)**2))
			
			x=np.arange(int(center[0])-left,int(center[0])+right)

			mask[x,(center[1]-up),:] = np.nan

			mask[x,(center[1]+down),:] = np.nan
		
		# # Applies mask
		# img_masked = img * mask

		mask = np.array(mask)
		img_nonzero = []

		# Goes through image and appends pixels that are in circle
		for row in range(mask.shape[0]):
			for col in range(mask.shape[1]):
				if not np.isnan(mask[row, col]).all():
					img_nonzero.append(img[row, col])

		img_nonzero = np.array(img_nonzero)

		print('***shape of image:', img.shape)
		print('***shape of img_nonzero:', img_nonzero.shape)

		# # Goes through image and appends pixels that are in circle...TESTING
		# img_nonzero = []
		# for i in range(img.shape[0]):
		#     for j in range(img.shape[1]):
		#         if not all(img_masked[i,j]==[0,0,0]):
		#             img_nonzero.append(img_masked[i,j])
		# img_nonzero = np.array(img_nonzero)

		print('****************')
		print('img_nonzero', img_nonzero)

		mean=[np.mean(img_nonzero[:,0]), np.mean(img_nonzero[:,1]), np.mean(img_nonzero[:,2])]
		
		var=[np.std(img_nonzero[:,0]), np.std(img_nonzero[:,1]), np.std(i_nonzero[:,2])]
		
		# file to save the output of the program
		self.save(self.reaction_id,name,mean,var,self.rxn_foldername)

		return mean, var
>>>>>>> db0fbf9bdf4234490aa9ffd97e8381b46f4a0f9d
    
    def __init__(self, time, interv,rxn_id, dir_file,n):
        self.reaction_id=rxn_id

        self.interv=interv

        self.t  = time

        self.dir_file = dir_file

        self.rxn_foldername = os.path.join(self.dir_file, str(self.reaction_id))

        self.n=n

    """


    var 
        tempM-temporary mean, returned for testing
        tempV-variance, used for testing

    functionality: creates a directory if it does not currently exist for output images. 
    Runs the snapshot/detection method at regular intervals for the desired number of 
    iterations. 

    """
    def run(self):
        
        #creates directory
        if not os.path.exists(self.rxn_foldername):
        
            os.makedirs(self.rxn_foldername)

        for i in range(int(self.t/self.interv)):
            #runs a single image process
            tempM,tempV=self.iteration()
            #time intervals between trials
            time.sleep(self.interv) 


    """
    var
        currentDT-turns a time object that is not in the desired format
        time - time in desired srtting format for use in 

    functionality: returns time for image naming purposes
    """        

                
    def getTime(self):
        #gets time
        currentDT = datetime.datetime.now()
        #formats
        time=currentDT.strftime('%Y%m%d%H%M%s')
        
        return time
    
    """
    var
        initial_img - the raw image, with colr, from the webcam
        name - retrieves time for unique naming
        center - center of beaker  
        radius - radius of beaker 
        mask - creates a mask that detects circle boundaries while not overstepping image boundaries

    functionality

    """
    def iteration(self):
        
        initial_img = co.snap(self.n)

        name= self.getTime()
        #write raw image to a file
        cv2.imwrite("frame%s.jpg" % name, initial_img) 
        #reads back that image in the correct format
        img = cv2.imread("frame%s.jpg" % name)

        #img = img[:,:,::-1] # Change BGR to RGB format - Tim - Testing
        #print('***img',img[:2,:2,:])
        
        #detects the beaker location and size, adjusts size
        center, radius = co.detect(co, img)
        radius = radius - int(0.1*radius)

        # Draw circle into image
        circle=cv2.circle(img,center,radius,(0,255,0),2)
        circle = circle[:,:,::-1] #Change BGR to RGB format - Tim
        np.save(self.rxn_foldername+"/%s.npy" % (name),circle)

        img = img[:,:,::-1] #Change BGR to RGB format - Tim

        mask=np.zeros((int(img.shape[0]),int(img.shape[1]),3))

        #the extreme bounds of the circle
        left=radius
        right=radius
        top=radius
        bottom=radius

        #this is used to detect boundaries and ensure that there is no out of bounds exceptions
        #this creates a mask to not include values outside of the circle 

        for i in range(int(radius)):
            #left/right dimensions of the circle scan
            delta=int(np.sqrt(int(radius)**2-int(i)**2))
            
        
            left=delta
            right=delta
            up=i
            down=i

            if mask.shape[0]<center[0]+right:
                
            #     right=-center[0]+mask.shape[0]-1

            # if 0>center[0]-left:
                
            #     left=center[0]
            
            # if mask.shape[1]<center[1]+down:
                
            #     down=-center[1]+mask.shape[1]-1
            
            # if 0>center[1]-up:
                
            #     up=center[1]
            
            #pythagorean
            #delta=int(np.sqrt(int(radius)**2-int(i)**2))
            
            x=np.arange(int(center[0])-left,int(center[0])+right)

            #mask[x,(center[1]-up),:] = np.nan
            #mask[i,x,:] = np.nan
            mask[i,x,:] = [1,1,1]

            #mask[x,(center[1]+down),:] = np.nan
        
        # # Applies mask
        # img_masked = img * mask

        mask = np.array(mask)
        img_nonzero = []

        plt.figure(1)
        plt.imshow(mask)

        plt.figure(2)
        plt.imshow(img)
        plt.show()


        # Goes through image and appends pixels that are in circle
        for row in range(mask.shape[0]):
            
            for col in range(mask.shape[1]):
                #detects where in the mask nan values ar present sorts it
                if not np.isnan(mask[row, col]).all():
                    img_nonzero.append(img[row, col])

        img_nonzero = np.array(img_nonzero)
        #checks that image size is preserved 
        print('***shape of image:', img.shape)
        print('***shape of img_nonzero:', img_nonzero.shape)

        # # Goes through image and appends pixels that are in circle...TESTING
        # img_nonzero = []
        # for i in range(img.shape[0]):
        #     for j in range(img.shape[1]):
        #         if not all(img_masked[i,j]==[0,0,0]):
        #             img_nonzero.append(img_masked[i,j])
        # img_nonzero = np.array(img_nonzero)

        print('****************')
        print('img_nonzero', img_nonzero)
        #gathers statistics for data group from the masked image, saves to csv for controller group
        mean=[np.mean(img_nonzero[:,0]), np.mean(img_nonzero[:,1]), np.mean(img_nonzero[:,2])]

        var=[np.std(img_nonzero[:,0]), np.std(img_nonzero[:,1]), np.std(img_nonzero[:,2])]

        
        # file to save the output of the program
        #4eb037332cb384cfdb6704f1578ced29f4247a49
        self.save(self.reaction_id,name,mean,var,self.rxn_foldername)

        return mean, var

    
    def save(self,rxnID, file, mean, variance, folderwoID):
    '''
    Input: 
        rxnID 
        file
        mean 
        variance 
        folderwoID 
                        
    Functionality: saves csv file, writes statistics to it. 
    '''

        with open(folderwoID+'/summary_%s.csv' % (rxnID),'a+') as csvfile:
            
            swriter = csv.writer(csvfile)

            swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])