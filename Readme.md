#Python Convert Excel to other formats

Excel to is a small snippet, how to convert an excel file, no matter if google spreadsheet or microsoft excel, in other formats for further processing.

##Installation

I've done this with python 3.7. Should work with older 3.x versions. If you have python 2.x, maybe you get an idea from this code and implement an adaptive solution.

###Modules needed
-pip for installing modules
-pandas

`pip install pandas`

##Starting

With pandas, it's very easy to transform the given data to a csv file or a json


###Commands
`python convert_to_csv.py`
`python convert_to_json.py`

Inside the json converter, we have two functions of pandas data frame saving. By column or by row.