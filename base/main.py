from base.municipality_Artemisa import *
from base.municipality_Camaguey import *
from base.municipality_CiegodeAvila import *
from base.municipality_Cienfuegos import *
from base.municipality_Granma import *
from base.municipality_Guantanamo import *
from base.municipality_Holguin import *
from base.municipality_IsladelaJuventud import *
from base.municipality_LaHabana import *
from base.municipality_LasTunas import *
from base.municipality_Matanzas import *
from base.municipality_Mayabeque import *
from base.municipality_PinardelRio import *
from base.municipality_SanctiSpiritus import *
from base.municipality_SantiagodeCuba import *
from base.municipality_VillaClara import *



class Provinces_Municipaly ():
	def __init__ (self):
		self.__provinces = {

			"Isla de la Juventud**" : municipality_IsladelaJuventud ,
			"Pinar del Rio" : municipality_PinardelRio ,
			"Artemisa" : municipality_Artemisa  ,
			"La Habana" : municipality_LaHabana ,
			"Mayabeque" : municipality_Mayabeque ,
			"Matanzas" : municipality_Matanzas ,
			"Cienfuegos" : municipality_Cienfuegos  ,
			"Villa Clara" : municipality_VillaClara ,
			"Sancti Spíritus" : municipality_SanctiSpiritus ,
			"Ciego de Ávila" : municipality_CiegodeAvila  ,
			"Camagüey" : municipality_Camaguey  ,
			"Las Tunas" : municipality_LasTunas ,
			"Granma" : municipality_Granma  ,
			"Holguín" : municipality_Holguin ,
			"Santiago de Cuba" : municipality_SantiagodeCuba ,
			"Guantánamo" : municipality_Guantanamo 

		}
		self.__provinces_West = {
			"Isla de la Juventud" : municipality_IsladelaJuventud ,
			"Pinar del Rio" : municipality_PinardelRio ,
			"Artemisa" : municipality_Artemisa  ,
			"La Habana" : municipality_LaHabana ,
			"Mayabeque" : municipality_Mayabeque ,
			"Matanzas" : municipality_Matanzas ,
		}
		self.__provinces_Center = {
			"Cienfuegos" : municipality_Cienfuegos  ,
			"Villa Clara" : municipality_VillaClara ,
			"Sancti Spíritus" : municipality_SanctiSpiritus ,
			"Ciego de Ávila" : municipality_CiegodeAvila  ,
		}
		self.__provinces_East = {
			"Camagüey" : municipality_Camaguey ,
			"Las Tunas" : municipality_LasTunas ,
			"Granma" : municipality_Granma ,
			"Holguín" : municipality_Holguin ,
			"Santiago de Cuba" : municipality_SantiagodeCuba ,
			"Guantánamo" : municipality_Guantanamo ,
		}

	@ property
	def provinces (self):
		return list(self.__provinces)

	@ property
	def municipality (self):
		return	  self.__provinces["Isla de la Juventud"]	\
				+ self.__provinces["Pinar del Rio"] 		\
		 		+ self.__provinces["Artemisa"] 				\
				+ self.__provinces["La Habana"]	 			\
				+ self.__provinces["Mayabeque"] 			\
				+ self.__provinces["Matanzas"] 				\
				+ self.__provinces["Cienfuegos"]	 		\
				+ self.__provinces["Villa Clara"] 			\
				+ self.__provinces["Sancti Spíritus"]	 	\
				+ self.__provinces["Ciego de Ávila"]	 	\
				+ self.__provinces["Las Tunas"] 			\
				+ self.__provinces["Camagüey"] 				\
				+ self.__provinces["Granma"]				\
				+ self.__provinces["Holguín"]				\
				+ self.__provinces["Santiago de Cuba"] 		\
				+ self.__provinces["Guantánamo"]			





#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#							 SETERS PER PROVINCES 
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------



	@ property
	def IsladelaJuventud  (self):
		return self.__provinces["Isla de la Juventud**"]
	




	@ property
	def PinardelRio (self):
		return self.__provinces["Pinar del Rio"]
	
	@ property
	def Artemisa (self):
		return self.__provinces["Artemisa"]
	
	@ property
	def LaHabana (self):
		return self.__provinces["La Habana"]
	

	@ property
	def Mayabeque (self):
		return self.__provinces["Mayabeque"]
	
	@ property
	def Matanzas (self):
		return self.__provinces["Matanzas"]








	@ property
	def Cienfuegos (self):
		return self.__provinces["Cienfuegos"]
	

	@ property
	def VillaClara (self):
		return self.__provinces["Villa Clara"]
	

	@ property
	def SanctiSpiritus (self):
		return self.__provinces["Sancti Spíritus"]
	

	@ property
	def CiegodeAvila (self):
		return self.__provinces["Ciego de Ávila"]
	






	@ property
	def Camaguey (self):
		return self.__provinces["Camagüey"]
	
	@ property
	def LasTunas (self):
		return self.__provinces["Las Tunas"]
	
	@ property
	def Granma (self):
		return self.__provinces["Granma"]
	
	@ property
	def Holguin (self):
		return self.__provinces["Holguín"]
	
	@ property
	def SantiagodeCuba (self):
		return self.__provinces["Santiago de Cuba"]
	
	@ property
	def Guantanamo (self):
		return self.__provinces["Guantánamo"]
	


