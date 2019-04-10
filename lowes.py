import requests
import csv
from bs4 import BeautifulSoup
import xlrd
from selenium import webdriver

class scrapper :
	def lowesScrapper(urlpath):
		productName = []
		#page = requests.get('https://www.lowes.com/pd/Kraus-Arcus-Chrome-1-Handle-Single-Hole-WaterSense-Bathroom-Faucet/50317367')
		page = requests.get(urlpath)

		soup = BeautifulSoup(page.text, 'html.parser')

		#print(soup)
		
		for pd in soup.find_all(True,{"class":["h3", "ellipsis-two-line"]}):
			productName.append(pd.text.strip())
		#print(productName)
		scrapper.writeDataToCSV(productName, 'DataSet.csv')
		scrapper.screenShot(urlpath,productName[0])

	def writeDataToCSV(productList, fileName):
		with open(fileName, 'a') as Datafile:
			writer = csv.writer(Datafile)
			writer.writerow(productList)
		Datafile.close()
			
	def screenShot(urlpath, S_shotName):
		DRIVER = 'chromedriver.exe'
		driver = webdriver.Chrome(DRIVER)
		driver.get(urlpath)
		screenShot = driver.save_screenshot('screenshot/{}.png'.format(S_shotName))
		driver.quit()


	def readExcelFileURL():
		loc = ("URL List.xlsx")
		wb = xlrd.open_workbook(loc)
		sheet = wb.sheet_by_index(0)
		sheet.cell_value(0, 0)
		
		for i in range(sheet.nrows):
			print (sheet.cell_value(i, 0))
			scrapper.lowesScrapper(sheet.cell_value(i, 0))

	
if __name__ == '__main__':
	scrapper.readExcelFileURL()