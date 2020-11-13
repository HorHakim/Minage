#include:utf-8
"""
Author : Horairy Hakim
Email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""
import hashlib
import time
import matplotlib.pyplot as plt
from tqdm import *

dictBloc = {
	"version"    : "1",
	"prevBlock"  : "0000000000000b954f72baaf2fc64bc2e2f01d692d4de72986ea808f6e99813f",
	"merkleroot" : "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
	"time"       : "1305200806",
	"bits"		 : "1a6a93b3",
	"mounce"     : "0"
}

def loadBloc(dictBloc):
	bloc = ""
	for value in dictBloc.values():
		bloc += value
	return bloc


def SHA256(bloc):
	blocDigest = hashlib.sha256(bloc.encode('utf-8')).hexdigest()
	return blocDigest

def incrementMounce(dictBloc):
	dictBloc["mounce"] = int(dictBloc["mounce"])
	dictBloc["mounce"] +=1
	dictBloc["mounce"] = str(dictBloc["mounce"])
	return dictBloc

def minage(dictBloc, difficulty, verbose=False):
	tempsDebut = time.time()
	bloc = loadBloc(dictBloc)
	blocDigest = SHA256(bloc)

	while blocDigest[:difficulty] != "0" * difficulty:
		dictBloc = incrementMounce(dictBloc)
		bloc = loadBloc(dictBloc)
		blocDigest = SHA256(bloc)

	tempsFin = time.time()
	if verbose:
		print("la valeur de mounce : {0}".format(dictBloc["mounce"]))
		print("le hash digest du bloc est :{0}".format(blocDigest))
		print("Temps total :{0}".format(tempsFin - tempsDebut))
	
	return tempsFin - tempsDebut



def testPerfMinageOnGenerateBlocs(numberOfBlocs, difficulty):
	dictBlocExample = {
	"version"    : "1",
	"prevBlock"  : "0000000000000b954f72baaf2fc64bc2e2f01d692d4de72986ea808f6e99813f",
	"merkleroot" : "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
	"time"       : "1305200806",
	"bits"		 : "1a6a93b3",
	"mounce"     : "0"
	}
	blocs = []
	temps = []
	for k in tqdm(range(numberOfBlocs)):
		tmpBloc = dictBlocExample
		tmpBloc["prevBlock"] = SHA256(str(k))
		temps.append(minage(tmpBloc, difficulty))

	return temps

def tempsMoyen(times):
	somme = 0
	for time in times:
		somme += time
	return somme / len(times)

################################################################################################################################
################################################################################################################################
numberOfBlocs = 50
difficulties = range(1,5)
TimesDifficulty = []


"""Afficher les graphes pour 50 blocs"""
for difficulty in difficulties:
	print("Calcul de la valeur de mounce des {0} blocs de test avec comme difficulté : {1}".format(numberOfBlocs, difficulty))
	times = testPerfMinageOnGenerateBlocs(numberOfBlocs, difficulty)
	print("\n")
	TimesDifficulty.append(times)
	plt.plot(times, "ro")
	plt.title('Temps moyen nécessaire pour miner des blocs de difficulté {0} : {1}'.format(difficulty, round(tempsMoyen(times), 6)))
	plt.xlabel('blocs')
	plt.ylabel('temps')
	plt.show()
