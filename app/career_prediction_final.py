
from app.final_new_updated_model import prediction
from app.api import API
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import pymongo


def growthRate(str,api:API):
    
    res = []
    
    res.append('Here are some top suggestions📈 for a career matching your skillset...👇')

    client = pymongo.MongoClient(
    "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
    mydb = client["pragati"]
    mycol = mydb["growth_rate"]
    print(str)
    filcol = mycol.find()

    if "\n" in str:
        pskills = list(str.split("\n"))
    elif "," in str:
        pskills = list(str.split(","))
    elif len(str.split()) == 1:
        pskills = str.split()
    else:
        api.send_text("Please separate your skills with a comma or mention it one below the other.")
        return "SKILLS ERROR"
    print(pskills)
    li = prediction(pskills)
    if li == False:
        api.send_text("""I'm sorry I could not find anything""")
        return "NOT FOUND"
    res.append(li)
    df = pd.DataFrame({'Careers': li})

    percentage = []

    for i in range(len(df)):
        for z in mycol.find():
            if  df.Careers[i].strip() == z['job_name'].strip():
                pct = z['job_growth']
                print(f"{z['job_name'].strip()} : {z['job_growth']}")
                percentage.append(pct)

    print(percentage)

    for i in range(0, len(percentage)):
        percentage[i] = int(percentage[i])
    percentage.sort()
    # print(percentage)
    df['Percentage'] = percentage

    # depict illustration~
    plt.figure(figsize=(8, 8))
    colors_list = ['Red', 'Orange', 'Blue', 'Purple', 'Yellow']
    graph = plt.bar(li, df['Percentage'], color=colors_list)
    plt.title('The Growth Rate of the top career paths recommended for you')
    #
    i = 0
    for p in graph:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        i += 1
    plt.savefig('app/images/plotting.png')
    # plt.show()
    img_path = 'app/images/plotting.png'
    res.append(img_path)

    return res
    # return image

# api = API("dhfajksdfjkasldfa",919538533738)

# result = growthRate("html css angularjs",api)
# print(result)

