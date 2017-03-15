import csv
import os

def parseFile(csvInput):
        with open(csvInput) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')

                placemark = '<Placemark>\n<name>' + csvInput + '</name>\n<LineString>\n<altitudeMode>absolute</altitudeMode>\n<coordinates>'

                next(reader)
                for row in reader:
                        placemark += row[3].split(',')[1] + ',' + row[3].split(',')[0] + ',' + '{:.2f}'.format(int(row[4]) * 0.3048) + '\n'

                placemark += '</coordinates>\n</LineString>\n</Placemark>'
                return placemark

def createKML(name, csvDirectory):
        kmlFilename = name + '.kml'
        kmlText = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n<name>' + kmlFilename +'</name>'
        
        for file in os.listdir(csvDirectory):
                if file.endswith('.csv'):
                        print(file)
                        kmlText += parseFile(csvDirectory + file)

        kmlText += '</Document>\n</kml>'
        kmlFile = open(kmlFilename, 'w')
        kmlFile.truncate()
        kmlFile.write(kmlText)
        kmlFile.close()

createKML('test','../flightdata/')
