from django.shortcuts import render
import tkinter as tk
from selenium import webdriver
import time
from django.templatetags.static import static
def delay(x):
    time.sleep(x)
# Create your views here.
def Prompt1(location,value):
    l = len(value)
    range = value[:l - 1] + "000"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.redfin.com/")
    delay(5)
    driver.find_element("id", "search-box-input").send_keys(f"{location}")
    delay(5)
    driver.find_element('css selector', "#tabContentId0 > div > div > form > div > button").click()
    delay(5)
    driver.find_element('css selector',
                        "#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div").click()
    # Price
    delay(10)
    driver.find_element("css selector","#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div.flex.align-center.inputRangeAfterHistogram > span:nth-child(3) > span > div > input").send_keys(f"{range}")
    delay(3)
    driver.find_element('css selector',
                        "#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(3)
    # SELECT hometype
    driver.find_element('css selector',
                        "#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.default.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign").click()
    delay(2)
    driver.find_element('css selector',
                        "#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div > div > div > div > div:nth-child(1)").click()
    # SELECT HOUSE

    delay(2)
    driver.find_element('xpath',
                        "/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/button[2]/span").click()

    delay(2)
    driver.find_element('css selector',
                        "#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign").click()
    # HOUSE DONE
    delay(5)
    driver.find_element('xpath',
                        "/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[6]").click()
    delay(2)
    driver.find_element('css selector',
                        "#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(20)

def BOT():
    root = tk.Tk()  # use to create new chat nav
    root.geometry('350x450+30+400')
    def getresult(message):
        arr = message.split(" ")
        if arr[0] == "Find":
            textarea.insert("end", "\nBot : Processing.... ")
            Prompt1("Houston", "600k")
            root.destroy()
        elif arr[0] == "Add":
            textarea.insert("end", "Bot : Processing.... ")

        elif arr[0] == "Log":
            textarea.insert("end", "Bot : Processing.... ")

        else:
            textarea.insert("end", "Invalid Input")

    def botReply():
        question = query.get()
        textarea.insert("end", "\nYou : " + question)
        query.delete(0, "end")
        getresult(question)

    root.title("Chat Bot for new prompt")
    root.config(bg="aquamarine")

    # Headear Logo
    # head = tk.PhotoImage(file="head1.png")
    # Insert_head = tk.Label(root, image=head)
    # Insert_head.config(bg='aquamarine')
    # Insert_head.pack()

    # Frame[Conatiner for message]
    Centeral_frame = tk.Frame(root)
    Centeral_frame.pack()
    scrol = tk.Scrollbar(Centeral_frame)
    scrol.pack(side='right')

    # Text area
    textarea = tk.Text(Centeral_frame, font=('time new roman', 10, 'bold'), height=10, yscrollcommand=scrol.set)
    textarea.pack(side='left')
    scrol.config(command=textarea.yview)

    # Enter message
    query = tk.Entry(root, font=('verdana', 10, 'bold'), width=30)
    query.pack(pady=15)

    # Buttom
    btn = tk.Button(root, text='Send !', bd='5', command=botReply)
    btn.pack()
    root.mainloop()
def firstone(request):
    BOT()
    return render(request,'index.html')