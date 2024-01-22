import json

class WritingIdentifier:
    def getTextFromImg(self, path="") -> str:
        with open(path, 'r+') as f:
            data = json.load(f)
        return data['description'].replace("\n", " ").lower()

if __name__ == "__main__":
    wi = WritingIdentifier()
    jsonPath = 'response.json'.replace("\\", "/")
    print(wi.getTextFromImg(jsonPath))


    
'''
Examples:

1.) [The json response from Google Vision API]:
"Dolomol-5\nOverdose of may be\nus to liver\nMy LioNo.: 78/U1/2018\nMade in India by\nPRCMBF-001\nProchem Pharmaceuticals PM d.\n140-141, Makkanpur, Bhagwanpur,\nRoorkee, Dist. Haridwar (UK-247 661\nMarketed by\nMICRO LABS\nMICRO LABU LIMITED\nPlot No. 37. (CA), 147, 151, 279-281,\nGround, Mezzanine, 1st & 2nd Floor\nKIAD.B., Jigani Bommasandra Link Road,\nBangalore-562 106. India,\nTM Trade Mad of Micro Labs Limited\nDolomol-500 डोलोमोल-५००\nडोलोमोल-५००\nParacetamol\nTablets IP 500 mg\nDolomol-500\nDolomol-500\nSIGTHIC-400\nB.NO, BAR-20708 JUN.2020 EXP MAY 2023\nDolomol-500\nडोलोमोल-५००\nAnalgesic & Antipyretio\nEach uncoated tablet.cooteins:\nParacetamol IP....\nExcipients\nStore in a dry & dark place,\na temperature not exceeding 30°C\nDosage: As directed by the physician.\nKeep out of reach of children.\nOverdose of may be\ninjurious to liver.\nMfg. Lic. No.: 78/UA/2016\nMade in India by:\nPRCMBFa-001\nProchem Pharmaceuticals Pvt. Ltd.\n140-141, Makkanpur, Bhagwanpur\nRoorkee, Oist, Haridwan (UK) 247 663\nMarketed by\nMICRO LABS\nMONO LAUS LIMITED\nPlot No. 37, (CA), 147-151, 279 281,\nGround, Mezzanine, 1st & 2nd Floor,\nKIA.D.B. Jigani Bommasandra Link Road,\nBangalore-562 106. India,\nTM Trade Mark of Micro Cabs Limited\nPolomol-500 डोलोमोल-100\n500 mg\nडोलोमोल-५००\nParacetamol\n00c\n"

____
2.) "Paracetamol is It works with Hydroxychloroquine against fever. B.NO, BAR-20708 JUN.2020 EXP MAY 2023"
'''