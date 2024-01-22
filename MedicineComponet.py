import requests

class MedCompTracker:
    def __init__(self):
        self.__link = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" #url to RxNorm drug web api
    
    def __getAllInfoJson(self, med_name:str) -> dict:
        url = self.__link+med_name
        response = requests.get(url)        # getting response of the request from the api source
        if(response.status_code!=200):
            print("|| ERROR || : Can't fetch data from api")
        else:
            self.__med_json = response.json()       # getting the response as JSON 
            return self.__med_json      

    def getComponentsList(self, s:str) -> list:     # public method for searching the key components related to medicine from a string of words
        self.__componentList = []       # list that will hold all the components
        c = 1
        bucket = set()     # to check for checking is something is already identified or not
        compCount = 0
        for word in s.split(" "):     # iterating through the space-splitted string
            word = word.strip()
            med_js = self.__getAllInfoJson(word)    # getting info json
            blackList = ["as", "sugar", "calcium", "corn", "mg", "liver"]                  # names of some words that are not related to medicine components
            if(len(med_js['drugGroup'])>1 and word not in blackList): 
                if(word in bucket):
                    print(c, " : words searched, the word is : ", word, "---> (Already Selected : {})".format(compCount))
                else:
                    compCount+=1
                    self.__componentList.append(word)       # if info json ['drugGroup'] key value length > 1, then it is a medicine component 
                    bucket.add(word)
                    print(c, " : words searched, the word is : ", word, "---> (Selected : {})".format(compCount))
            else: print(c, " : words searched, the word is : ", word)
            c+=1
            
        return self.__componentList # returning the component list

if __name__=="__main__": #main
    md = MedCompTracker()
    asking = "Paracetamol Paracetamol Paracetamol Hydroxychloroquine Paracetamol Paracetamol is an analgesic (pain reliever) and anti-pyretic (fever reducer). It works by blocking the release of certain chemical messengers that cause pain and fever.".replace("\n", " ")
    print("\nComponents : ", md.getComponentsList(asking))

'''
Examples for demo:

Statement1 : Hydroxychloroquine is used to prevent or treat malaria caused by mosquito bites. The United States Center for Disease Control provides updated guidelines and travel recommendations for the prevention and treatment of malaria in different parts of the world.

Statement2 : Paracetamol is an analgesic (pain reliever) and anti-pyretic (fever reducer). It works by blocking the release of certain chemical messengers that cause pain and fever.

Statement3 : Dextrose is the name of a simple sugar that is made from corn and is chemically identical to glucose, or blood sugar. Zometa (zolcdronic acid) Injection is a bisphosphonate used to treat Paget's disease, high blood levels of calcium caused by cancer (hypercalcemia of malignancy), multiple myeloma (a type of bone marrow cancer), or metastatic bone cancer.

Statement4 : Ketoconazole, sold under the brand name Nizoral among others, is an antifungal medication used to treat a number of fungal infections. Applied to the skin it is used for fungal skin infections such as tinea, cutaneous candidiasis, pityriasis versicolor, dandruff, and seborrheic dermatitis.


'''
