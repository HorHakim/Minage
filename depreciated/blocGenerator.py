#include:utf-8
"""
Author : Horairy Hakim
Email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""
import hashlib
import pickle

def SHA256(bloc):
	blocDigest = hashlib.sha256(bloc.encode('utf-8')).hexdigest()
	return blocDigest

def generateBlocs(numberOfBlocs):
	dictBlocExample = {
	"version"    : "1",
	"prevBlock"  : "0000000000000b954f72baaf2fc64bc2e2f01d692d4de72986ea808f6e99813f",
	"merkleroot" : "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
	"time"       : "1305200806",
	"bits"		 : "1a6a93b3",
	"mounce"     : "0"
	}
	blocs = []
	for k in range(numberOfBlocs):
		tmpBloc = dictBlocExample
		tmpBloc["prevBlock"] = SHA256(str(k))
		blocs.append(tmpBloc)

	return blocs

def saveGeneratedBlocs(blocs, pathTransactionsBlocs="./transactionsBlocs"):


	with open(pathTransactionsBlocs, 'wb') as bFile:
		myPickler = pickle.Pickler(bFile)
		myPickler.dump(blocs)

	return None

def loadGeneratedBlocs(pathTransactionsBlocs="./transactionsBlocs"):

	with open(pathTransactionsBlocs, 'rb') as bFile:
		myDepickler = pickle.Unpickler(bFile)
		blocs = myDepickler.load()

	return blocs

blocs = generateBlocs(100)
for bloc in blocs:
	print(bloc)
saveGeneratedBlocs(blocs)
# print(loadGeneratedBlocs())