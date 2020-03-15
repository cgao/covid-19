import requests
import lxml.html as lh
import pandas as pd

def covidTable( ):
    url = "https://www.worldometers.info/coronavirus/#countries"
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')   
    table = []
    for tr_element in tr_elements[0:]:
        row = []
        for i in idx:
            if isinstance(t, lh.HtmlElement):
                row.append( tr_element[i].text_content().strip() )
        table.append(row)
    df = pd.DataFrame( table[1:], columns = table[0] ).set_index('Country,Other')
    return df
