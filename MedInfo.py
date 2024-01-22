from bs4 import BeautifulSoup
import requests

class MedInfo:
    def __init__(self):
        self.__link = "https://www.drugs.com/"  # drugs.com websit : https://www.drugs.com/ + {Component name}.html
        self.__componentName = ""               # this will hold the Component name
        self.__info = {}                        # this will hold all the information about the component
    
    def __fetchMedInfo(self, component_name:str, subCatagory="") -> None:          # Private utility method for fetching info about the Component from the Website 
        self.__componentName = component_name.lower()
        page = requests.get(url="{}/{}{}.html".format(self.__link, subCatagory, self.__componentName.replace(" ", "-"))) # info from drugs.com by using GET request
        '''if(page.status_code != 200 and subCatagory == ""):
            self.__fetchMedInfo(component_name, subCatagory="mtm/")     # for using a page with subcatagory /mtm/
        el'''
        if(page.status_code != 200):    # for checking the validity of the request
            print("|| ERROR || : Request error: ", page.status_code, "\n")
            return
        soup = BeautifulSoup(page.content, 'lxml')             # creating soup by fetching info using BeautifulSoup from that pebpage content 
        main_content = soup.find(id="content")                 # getting main content from fetched data using id attribute
        cont_box = main_content.find('div', class_="contentBox")    # getting the div using id where all information is writter
        # for getting basic information about the component
        self.__info['Name'] = cont_box.h1.text     # name of the Component
        self.__info['Detailed_names'] = cont_box.find('p').text        # detailed names of the component
        # for getting advanced information about the component
        allContents = cont_box.find('h1')           # getting reference of the first H1 tag
        curr = ""           # a variable to store current dictionary key for info Dictionary to store data
        for ele in allContents.next_elements:       # iterating through next elements from the reference
            if(ele.string != None):                 # for avoiding unnecessary spaces and elements
                if(ele.name == "h2"):               # for getting the heading from h2 tags 
                    self.__info[ele.string]=""      # making the heading as the dictionary keys
                    curr = ele.string               # using curr to hold the current dictionary key
                if(ele.name == "p"):                # for retrieving information from paragraphs
                    self.__info[curr]=self.__info.get(curr, "")+"\n"+ele.string      # holding paragraphs as the value in the current dictionary key
    
    def __removeKeys(self) -> None:     # private method for remove unnecessary keys from info dictionary
        # list of all the required info keys
        self.__infoList = ['Name', 'Detailed_names', 'What is {} ?'.format(self.__info['Name'].lower()), 'Warnings', 'Before taking this medicine', 'How should I use {} ?'.format(self.__info['Name'].lower()), 'What happens if I miss a dose?', 'What happens if I overdose?', 'What should I avoid?', '{} side effects'.format(self.__info['Name'].lower()), 'What other drugs will affect {} ?'.format(self.__info['Name'].lower())]
        blackList = []      # for storing the not-required keys
        for k in self.__info.keys():
            if(k not in self.__infoList): blackList.append(k)   
        
        for k in blackList: self.__info.pop(k)      # removing black-listed keys from the info dictionary
        
    def getInfoList(self) -> list:      # public method for getting the Info-list for the component after fetching the data
        if(self.__componentName == ""):
            print("|| ERROR || : You need to fetch the data first to get Info\n")
        else: return self.__infoList

    def getAllInfo(self, component_name) -> dict:   # public method for getting all the information as a Dictionary
        self.__fetchMedInfo(component_name)
        self.__removeKeys()
        return self.__info

    def getInfo(self, component_name, info_name="") -> str:     # public method for getting specific information about the component
        self.__fetchMedInfo(component_name)
        self.__removeKeys()
        if(info_name not in self.__infoList):                   # checking info name if that key exist or not
            print("|| ERROR || : Give proper info_name\n")
        else: return self.__info[info_name]

if __name__=="__main__":
    m = MedInfo()
    infos = m.getAllInfo("mg")
    for k in infos.keys():
        print(k, " : \n", infos[k])
        print("-"*100)

'''
Examples for demo:

Hydroxychloroquine
Paracetamol
Dextrose
Zometa 
Nizoral

'''
