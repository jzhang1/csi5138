import os
from myImage import *
from dataFeeder import *
from random import shuffle

#returns the datGenerators for the model
def getDataGenerators(imgDim,batch,numClasses,numOfChannels,shuffleInBatch,DataSetPath):
	#iterate over dataset and get all the paths and labels
	airplaneNum = 0
	dogNum = 1
	frogNum = 2
	personNum =3
	truckNum = 4
	
	myImagesPlane = []
	myImagesDog = []
	myImagesFrog = []
	myImagesPerson = []
	myImagesTruck = []

	for subdir, dirs, files in os.walk("../DataSet"):
		for file in files:
			#print os.path.join(subdir, file)
			filepath = subdir + os.sep + file

			if filepath.endswith(".png"):
				if "airplane" in str(filepath):
					myImagesPlane.append(MyImage(filepath,airplaneNum))
				if "dog" in str(filepath):
					myImagesDog.append(MyImage(filepath,dogNum))
				if "frog" in str(filepath):
					myImagesFrog.append(MyImage(filepath,frogNum))
				if "person" in str(filepath):
					myImagesPerson.append(MyImage(filepath,personNum))
				if "truck" in str(filepath):
					myImagesTruck.append(MyImage(filepath,truckNum))



	partition ={"train" : [],"test":[]}

	partition["train"] = [myImagesPlane[i].path for i in range(int(len(myImagesPlane)*0.8))]+[myImagesDog[i].path for i in range(int(len(myImagesDog)*0.8))]+[myImagesFrog[i].path for i in range(int(len(myImagesFrog)*0.8))]+[myImagesPerson[i].path for i in range(int(len(myImagesPerson)*0.8))]+[myImagesTruck[i].path for i in range(int(len(myImagesTruck)*0.8))]

	trainLabels = {myImagesPlane[i].path:myImagesPlane[i].classNum for i in range(int(len(myImagesPlane)*0.8))}
	trDogLabels = {myImagesDog[i].path:myImagesDog[i].classNum for i in range(int(len(myImagesDog)*0.8))}
	trFrogLabels = {myImagesFrog[i].path:myImagesFrog[i].classNum for i in range(int(len(myImagesFrog)*0.8))}
	trPersonLabels = {myImagesPerson[i].path:myImagesPerson[i].classNum for i in range(int(len(myImagesPerson)*0.8))}
	trTruckLabels = {myImagesTruck[i].path:myImagesTruck[i].classNum for i in range(int(len(myImagesTruck)*0.8))}

	trainLabels = {**trainLabels,**trDogLabels}
	trainLabels = {**trainLabels,**trFrogLabels}
	trainLabels = {**trainLabels,**trPersonLabels}
	trainLabels = {**trainLabels,**trTruckLabels}

   

	partition["test"] = [myImagesPlane[i].path for i in range(int(len(myImagesPlane)*0.8),len(myImagesPlane))]+[myImagesDog[i].path for i in range(int(len(myImagesDog)*0.8),len(myImagesDog))]+[myImagesFrog[i].path for i in range(int(len(myImagesFrog)*0.8),len(myImagesFrog))]+[myImagesPerson[i].path for i in range(int(len(myImagesPerson)*0.8),len(myImagesPerson))]+[myImagesTruck[i].path for i in range(int(len(myImagesTruck)*0.8),len(myImagesTruck))]
	testLabels = {myImagesPlane[i].path:myImagesPlane[i].classNum for i in range(int(len(myImagesPlane)*0.8),len(myImagesPlane))}
	testDogLabels = {myImagesDog[i].path:myImagesDog[i].classNum for i in range(int(len(myImagesDog)*0.8),len(myImagesDog))}
	testFrogLabels = {myImagesFrog[i].path:myImagesFrog[i].classNum for i in range(int(len(myImagesFrog)*0.8),len(myImagesFrog))}
	testPersonLabels = {myImagesPerson[i].path:myImagesPerson[i].classNum for i in range(int(len(myImagesPerson)*0.8),len(myImagesPerson))}
	testTruckLabels = {myImagesTruck[i].path:myImagesTruck[i].classNum for i in range(int(len(myImagesTruck)*0.8),len(myImagesTruck))}
	testLabels = {**testLabels,**testDogLabels}
	testLabels = {**testLabels,**testFrogLabels}
	testLabels = {**testLabels,**testPersonLabels}
	testLabels = {**testLabels,**testTruckLabels}
	shuffle(partition["test"])
	shuffle(partition["train"])
    
	params = {'dim': (imgDim[0],imgDim[1]),
				'batch_size': batch,
				'n_classes': numClasses,
				'n_channels': numOfChannels,
				'shuffle': shuffleInBatch}



	training_generator = DataGenerator(partition['train'], trainLabels, **params)         
	test_generator = DataGenerator(partition['test'], testLabels, **params)	
	return training_generator,test_generator