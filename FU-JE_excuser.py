import requests
from lib import data

documentation_URL = "https://excuser.herokuapp.com"

def status():

    for number in range(1,50):
       
        request = requests.get(f"https://excuser.herokuapp.com/v1/excuse/id/{number}").status_code
        #self.assertEqual(request, 200)
        
        if request == 200:
            print("pass", request)
        else:
            print("faild numbers: ", request)

    #return test_status()

def index(x,y,z):
    asw_category = []
    for i in range(x,y,z):
        url_numb = f"https://excuser.herokuapp.com/v1/excuse/id/{i}"
        url_numb = requests.get(url_numb).json()
        asw_category.append(url_numb)
    return asw_category
                

def data_kategorije(kategorija):
                
    return index(*data[kategorija]) # =======>>>>> spread or expand: keys[kateforija][0],keys[kateforija][1],keys[kateforija][2], 


def finaly_test(categoty):
    response = data_kategorije(categoty)
    lenght_response = len(response)    
    expected_result = ["id", "excuse", "category"]
    lenght_expected_result = len(expected_result)
    for i in range(lenght_expected_result):
        for y in range(lenght_response):
            if expected_result[i] in response[y]:
                print("passed")
            else:
                print("faild", response[y])
################################################################    POZIVANJE FU-IJA       #######################################################
def all_function():
    for i in data.keys():
        test = finaly_test(i)
        print(test)
        
TEST = all_function()
print(TEST)