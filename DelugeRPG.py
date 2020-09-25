from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import random as r



Path = "/Users/niteesh/chromedriver"
driver = webdriver.Chrome(Path)
nt = input("Whats your USERNAME?")
np = input("Whats your PASSWORD")
driver.maximize_window()

driver.get("https://www.delugerpg.com/login")


login = driver.find_element_by_name("username")
login.send_keys(nt)
login = driver.find_element_by_name("password")
login.send_keys(np)
login.send_keys(Keys.RETURN)
time.sleep(4)
maps = ["https://www.delugerpg.com/map/overworld1","https://www.delugerpg.com/map/overworld2","https://www.delugerpg.com/map/overworld3",
"https://www.delugerpg.com/map/overworld4","https://www.delugerpg.com/map/overworld5","https://www.delugerpg.com/map/overworld6",
"https://www.delugerpg.com/map/overworld7","https://www.delugerpg.com/map/overworld8","https://www.delugerpg.com/map/overworld9",
"https://www.delugerpg.com/map/overworld10","https://www.delugerpg.com/map/overworld11","https://www.delugerpg.com/map/overworld12",
"https://www.delugerpg.com/map/overworld13","https://www.delugerpg.com/map/overworld14","https://www.delugerpg.com/map/overworld15",
"https://www.delugerpg.com/map/overworld16","https://www.delugerpg.com/map/overworld17","https://www.delugerpg.com/map/overworld18",
"https://www.delugerpg.com/map/overworld19","https://www.delugerpg.com/map/overworld20","https://www.delugerpg.com/map/overworld21",
"https://www.delugerpg.com/map/overworld22","https://www.delugerpg.com/map/overworld23","https://www.delugerpg.com/map/overworld24",
"https://www.delugerpg.com/map/overworld25","https://www.delugerpg.com/map/unownruins1","https://www.delugerpg.com/map/unownruins2",
"https://www.delugerpg.com/map/pkmnmansion1","https://www.delugerpg.com/map/pkmnmansion2","https://www.delugerpg.com/map/pkmnmansion3",
"https://www.delugerpg.com/map/pkmnmansion4","https://www.delugerpg.com/map/snowcave1","https://www.delugerpg.com/map/snowcave3",
"https://www.delugerpg.com/map/snowcave2","https://www.delugerpg.com/map/snowcave4","https://www.delugerpg.com/map/rockcave1",
"https://www.delugerpg.com/map/rockcave4","https://www.delugerpg.com/map/rockcave3","https://www.delugerpg.com/map/rockcave2",
"https://www.delugerpg.com/map/powerplant1","https://www.delugerpg.com/map/powerplant2","https://www.delugerpg.com/map/powerplant3",
"https://www.delugerpg.com/map/pkmntower1","https://www.delugerpg.com/map/pkmntower2","https://www.delugerpg.com/map/pkmntower3",
"https://www.delugerpg.com/map/volcano1","https://www.delugerpg.com/map/volcano3","https://www.delugerpg.com/map/volcano4",
"https://www.delugerpg.com/map/volcano2",]

mapselect = r.choice(maps)

driver.get(mapselect)

def pokemonCatching():
    # time.sleep(3)
    directions = ["move_north-west","move_north","move_north-east","move_south-west","move_south-east","move_west",
    "move_east","move_south"]
    i = 0
    while i == 0 :
        
        move = driver.find_element_by_id(r.choice(directions))
        
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID,"pokemonimgwrap"))
            )
            i=0
            found = True
            
            
        except:
            try:
                move.click()
            except:
                move.click()    
            found = False

        if found == True:

            catch = driver.find_element_by_class_name("btn-catch-action")
            catch.click()
            time.sleep(4)
            battle = driver.find_element_by_class_name("btn-battle-action")
            battle.click()
            time.sleep(3)
            ball = driver.find_element_by_id("item-masterball")
            ball.click()
            
            throw = driver.find_element_by_xpath("//*[@id=\"itemwrap\"]/div[1]/form/div[2]/input[2]")
            throw.click()
            time.sleep(3)
            driver.get(mapselect)
            # caught = False
            # while caught == False:
                

                # try:
                #     continu = driver.find_element_by_xpath("//*[@id=\"attack\"]/div/form/div/input[1]")    
                #     continu.click()
                    
                    
                # except:                    
                #     # back = driver.find_element_by_xpath("//*[@id=\"battle\"]/div[1]/a")
                #     # back.click()
                #     driver    
                #     caught = True
                #     break
                    
    
                   
                        # //*[@id="battle"]/div[1]/a

                       
                    
j=0
while j <1000:
    pokemonCatching()      
    j+=1
                       

                    

            
        
        

                
                
        
                
            
   
    
    
    




    


