class ExpDateCheck:
    def __init__(self):
        self.__date = ""

    def __getDateFromString(self, s:str) -> None:
        catchPhrase = "exp"
        text = s.lower().split(catchPhrase)[1].strip().upper()
        date = ""
        i=0
        while(not text[i].isdigit()):
            date+=text[i]
            i+=1
        while(text[i].isdigit()):
            date+=text[i]
            i+=1
        self.__date = date
            
    
    def getExpDate(self, s:str) -> str:
        self.__getDateFromString(s)
        return self.__date

if __name__ == "__main__":
    e = ExpDateCheck()
    print(e.getExpDate("B.NO, BAR-20708 JUN.2020 EXP MAY 2023 a foojfjoj jojrjforv jjgojorjgrogj"))
