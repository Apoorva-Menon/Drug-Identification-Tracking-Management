from WritingIdentifier import WritingIdentifier
from MedicineComponet import MedCompTracker
from MedInfo import MedInfo
from ExpDateCheck import ExpDateCheck
from time import sleep
import traceback

class IntegAll:
    def __init__(self):     # Initial messages and creation of related objects
        print("\n/////     || TEAM 15 Project for NEXT NINJAS ||     \\\\\\\\\\")
        print("/////     || Starting A Minimal User Interface for SDITMA     \\\\\\\\\\\n")
        self.__copmCheck = MedCompTracker()     # creating Medicine-Component checker object 

    def run(self):          # this will run the whole Interface after Initialization
        self.__opt=1        # this variable will take care of the options selected
        while(self.__opt!=0):
            try: 
                choice=self.__optList()     # for selecting the option
                if(choice!=0):              # checking if it is exit option or not
                    self.__operate(choice)  # otherwise operate as the option
                else:break
            except Exception:               # handling exception at any step while selecting the options
                    print("\n|| WARNING!! || :: Problem Occured...\n")
                    traceback.print_exc()
                    sleep(2)                # sleeps are given here to make the interface readable
                    print("\nReturning to Information List...")
                    continue
        sleep(1)   
        print("\n/////     Thank you for using \"The Minimal User Interface for SDITMA\".     \\\\\\\\\\")
        sleep(1)

    def __optList(self)->int:  # feature list
        print("\n-------------------------------------------------------------------------------------")
        print("--> Press 0 to Exit this interface")
        print("--> Press 1 to get Text from Image")
        print("--> Press 2 to get Information about the Medicine")
        print("|| Enter your choice of Operation --> ", end="")
        opt=int(input())
        if(opt not in range(3)):
            print("|| Failure || : Wrong Inputs for Operation Selection!!...Try Again->\n")
            self.__optList()
        else: return opt

    def __operate(self, opt): # Operate according to the choice->"opt"
        if(opt==1): self.__getTextFromImg()
        elif(opt==2): self.__getMedicineInfo()
        else: print("|| Failure || : Wrong Inputs for Information checking!!\n")

    def __getTextFromImg(self) -> str:          # for getting text from medicine strip and return it as string
        responsePath = input("Enter the json response path here --> ")
        #....Implement
        self.__WIdentifier = WritingIdentifier()
        self.__medStripInfo = self.__WIdentifier.getTextFromImg(responsePath)
        return self.__medStripInfo

    def __prepareMed(self, medStripText:str) -> None:         # to prepare the MedInfo object by getting Components from med-strip text
        self.__medComponents = self.__copmCheck.getComponentsList(medStripText)     # getting the medicine related component list 
        print("|| Alert || : Identified {}-component(s) from the Medicine Strip Image\n".format(len(self.__medComponents)))

    def __getMedicineInfo(self) -> str:         # for getting information about the medicine component from the med-strip string
        self.__prepareMed(self.__medStripInfo)     # it will take the self.__medStripInfo as input parameter
        self.__infoDict = {x:None for x in self.__medComponents}     # it will crate dictioanry with components as key and info as value
        for k in self.__infoDict.keys():
            self.__medInfo = MedInfo()              # creating Medicine-Info fetching object
            self.__infoDict[k] = self.__medInfo.getAllInfo(k)       # structure like {component name:{info dictionary}}
        # start choosing for information either component or exp date
        # Choosing option for getting option list for medicine info
        opt=1
        while(opt!=0):
            sleep(1)
            try: 
                opt=self.__allOptList()
                if(opt!=0):
                    self.__allOperate(opt)
                else:break
            except Exception:
                    print("\n|| WARNING!! || :: Problem Occured...\n")
                    traceback.print_exc()
                    sleep(2)
                    print("\nReturning to Operations List...")
                    continue
            sleep(1)
        
    def __allOptList(self) -> int:
        print("\n|| Showing list for Operations regarding Medicine: (Enter 0 to exit this choice)")
        print("|--> 1.) See information about the identified medicine components")
        print("|--> 2.) See expiry date of the medicine")
        print("\n|| Enter the serial no. of the Operation you want to do : ", end="")
        opt=int(input())
        if(opt not in range(3)):
            print("|| Failure || : Wrong Inputs for Operation Selection!!...Try Again->\n")
            self.__allOptList()
        else: return opt

    def __allOperate(self, opt) -> None:
        if(opt == 1): self.__componentInfo()
        elif(opt == 2): self.__expDateFromString()
        else: return

        
    def __expDateFromString(self) -> None:
        e = ExpDateCheck()
        self.__expDate = e.getExpDate(self.__medStripInfo)
        print(" || Expiry Date : {}".format(self.__expDate))

    def __componentInfo(self) -> None:
        # Choosing option for getting option list for medicine info
        opt="not empty"
        while(opt!=""):
            sleep(1)
            try: 
                choice=self.__medOptList()
                if(choice!=""):
                    self.__medOperate(choice)
                else:break
            except Exception:
                    print("\n|| WARNING!! || :: Problem Occured...\n")
                    traceback.print_exc()
                    sleep(2)
                    print("\nReturning to Operations List...")
                    continue
            sleep(1)

    def __medOptList(self) -> str:      # for getting list of the medicine components that are identified from the text
        print("\n|| Showing list for Medicine Components: (Enter 0 to exit this choice)")
        for i in range(len(self.__medComponents)):  print("|--> "+str(i+1)+" - "+self.__medComponents[i])
        print("\n|| Enter the serial no. of the Component for which you want to get the Information: ", end="")
        n=int(input())
        if(n>0 and n<=len(self.__medComponents)): return self.__medComponents[n-1]
        else: return ""

    def __medOperate(self, opt) -> None:    # for getting the information about the chosen medicine component
        curr = self.__infoDict[opt]     # getting the component of choice
        print("\n|| Showing list for Medicine Component's Information:")
        tempList = list(curr.keys())
        for i in range(len(tempList)):  print("|--> "+str(i+1)+" - "+tempList[i])
        print("\n|| Enter the serial no. of the Information you want to get: ", end="")
        n=int(input())
        if(n>0 and n<len(tempList)): 
            print("|| {}  :\n  {}".format(tempList[n-1], curr[tempList[n-1]]))
        
if __name__ == "__main__":
    ui = IntegAll()
    ui.run()
