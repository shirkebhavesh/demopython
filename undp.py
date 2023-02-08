import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from selenium.webdriver.common.keys import Keys
from Global_variable import *
import time
from deep_translator import GoogleTranslator
import PySimpleGUI as sg
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import warnings
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
import datetime
from AllFunctions import all_function
from selenium.common.exceptions import TimeoutException
import pandas as pd

# Yt33aht0ku80akd1f1y2ioe0jdn2k4i3

sg.theme("DarkGreen6")

layout = [
          [sg.Text("Please Enter Key:", size=(15, 1), pad=(12, 18), font=('Arial', 10, 'bold')),
           sg.InputText(key='-pwd-', size=(27, 1), pad=(12, 18), password_char='*')],
          [sg.Button('Log In', pad=(25, 10), bind_return_key=True,font=('Arial', 10, 'bold')), sg.Button('Cancel', pad=(10, 10),font=('Arial', 10, 'bold'))]]
window = sg.Window("Key Verification", layout, auto_size_text=False, text_justification='r', return_keyboard_events=True,
                   alpha_channel=1)

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    else:
        if event == "Log In":
            key = (values['-pwd-'])
            if key:
                try:
                    key = key[19:20] + key[23:24] + key[27:28] + key[31:32] + '-' +key[11:12] + key[15:16] + '-' + key[3:4] + key[7:8]
                    key = datetime.datetime.strptime(key,'%Y-%m-%d')
                    current = datetime.datetime.today()
                except:
                    sg.popup('please enter valid key !!!!')
                    continue

                if key >= current:
                    window.close()
                    sg.theme('DarkGreen6')
                    sg.SetOptions(font='opensans 11')
                    cal = "\U0001F4C5"

                    _nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')


                    def _surrogatepair(match):
                        char = match.group()
                        assert ord(char) > 0xffff
                        encoded = char.encode('utf-16-le')
                        return (
                                chr(int.from_bytes(encoded[:2], 'little')) +
                                chr(int.from_bytes(encoded[2:], 'little')))


                    def with_surrogates(text):
                        return _nonbmp.sub(_surrogatepair, text)


                    todays = datetime.datetime.now()

                    subtract = datetime.timedelta(days=2)
                    Two_day_back = todays - subtract

                    add = datetime.timedelta(days=365 * 2)
                    two_year_ahead = todays + add

                    txt = (with_surrogates('📅'))
                    # layout1 = [,
                    #                                    ]
                    directory = "D:/DATA ENTRY/app_eop_gb/"
                    layoutprefile = [
                        [sg.Text('Select File:',font=('Arial', 10, 'bold'))],
                        [sg.InputText(directory,font=('Arial', 10, 'bold'),key='-path-'), sg.FolderBrowse()],
                        [sg.Text("Start Date", pad=(10, 10), font=('Arial', 10, 'bold')),
                         sg.In(key='-CAL-', enable_events=True, visible=True, size=(11, 7),
                               default_text=(Two_day_back.strftime('%d-%m-%Y')), font=('Arial', 10, 'bold')),
                         sg.CalendarButton(txt, target='-CAL-', key='_FROMDATE_', format=('%d-%m-%Y'))],
                        [sg.Text("End Date  ", pad=(9, 10), font=('Arial', 10, 'bold')),
                         sg.In(key='-CAL1-', enable_events=True, visible=True, size=(11, 7),
                               default_text=(todays.strftime('%d-%m-%Y')), font=('Arial', 10, 'bold')),
                         sg.CalendarButton(txt, target='-CAL1-', key='_TODATE_', format=('%d-%m-%Y'))],

                        [sg.Text("Choose Notice :", pad=(10, 10), font=('Arial', 10, 'bold')),
                         # sg.Checkbox(['Tender', 'Corrigenda', 'Contract Awards'], size=(12, 5),font=('Arial', 10, 'bold'))],
                         sg.Radio('Tender', 'RADIO1', key='Tender',default=True, font=('Arial', 10, 'bold')),
                         sg.Radio('CA', 'RADIO1', key='CA', font=('Arial', 10, 'bold')),

                        ],
                        [sg.Submit('Submit', pad=(10, 10), font=('Arial', 10, 'bold')),
                         sg.Cancel('Close', pad=(10, 10), font=('Arial', 10, 'bold'))],
                        # [sg.Text("Final Output :", pad=(10, 10), font=('Arial', 10, 'bold')),
                        #  sg.Text(size=(25, 1), key='-PROG-', font=('Arial', 10, 'bold')),
                         [sg.Text(size=(10, 1), key='-ADD SUB-', font=('Arial', 10, 'bold'))],
                        [sg.Text('Download Count :', pad=(10, 10), font=('Arial', 10, 'bold')),
                         sg.Text(key='-Tcount-', size=(10, 1), font=('Arial', 10, 'bold'))]
                         # sg.Text('Dublicate Count :', pad=(10, 10), font=('Arial', 10, 'bold')),
                         # sg.Text(key='-Dcount-', size=(10, 1), font=('Arial', 10, 'bold'))]
                    ]

                    window = sg.Window('UNDP', layoutprefile, resizable=True)

                    while True:

                        event, values = window.read(timeout=1000)
                        window.refresh()

                        if event == 'Close' and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
                            break
                        elif event in (None, sg.WIN_CLOSED):
                            break

                        elif event == 'Submit':
                            # print('Proceed')
                            FilePath = (values['-path-']) + '/'
                            cal_date = values['-CAL-']
                            from_date = cal_date[0:2] + '.' + cal_date[3:5] + '.' + cal_date[6:]
                            print('from_date', from_date)
                            datee = from_date.split('.')[0]
                            month = from_date.split('.')[1]
                            year = from_date.split('.')[2]

                            print('date', datee)
                            print('month', month)

                            cal_date1 = values['-CAL1-']
                            To_date = cal_date1[0:2] + '.' + cal_date1[3:5] + '.' + cal_date1[6:]
                            print('To date', To_date)

                            datee2 = To_date.split('.')[0]
                            month2 = To_date.split('.')[1]
                            year2 = To_date.split('.')[2]

                            print('date', datee2)
                            print('month', month2)

                            # Global = 'Global'
                            Tender = values['Tender']
                            CA = values['CA']
                            # Procurement = values['Procurement']

                            progress = 1
                            z = []

                            if Tender:
                                colums = ['id',
                                          'Org',
                                          'Short_des',
                                          'Des',
                                          'tender_no',
                                          'notice_type',
                                          'deadline',
                                          "est_cost",
                                          'Tender_File_url',
                                          'Country',
                                          'address',
                                          'email',
                                          'doc_start',
                                          'ICB/NCB',
                                          'cpv'
                                          ]

                                df = pd.DataFrame(columns=colums)

                                df.to_csv(FilePath + todays.strftime('%d-%m-%Y') + ' Tender' +'.csv',index=False)

                                Dub_tender = 1
                                Down_tender = 1
                                driver = DriverDetails()

                                driver.get('https://procurement-notices.undp.org/search.cfm')
                                time.sleep(5)
                                driver.find_element_by_xpath('(//input)[1]').clear()
                                driver.find_element_by_xpath('(//input)[1]').send_keys(datee)
                                driver.find_element_by_xpath("(//select)[1]").click()
                                driver.find_element_by_xpath("(//select)[1]/option[@value=" + str(month) + "]").click()
                                driver.find_element_by_xpath("(//select)[2]").click()
                                driver.find_element_by_xpath("(//select)[2]/option[@value=" + str(year) + "]").click()

                                driver.find_element_by_xpath('(//input)[2]').clear()
                                driver.find_element_by_xpath('(//input)[2]').send_keys(datee2)
                                driver.find_element_by_xpath("(//select)[3]").click()
                                driver.find_element_by_xpath("(//select)[3]/option[@value=" + str(month2) + "]").click()
                                driver.find_element_by_xpath("(//select)[4]").click()
                                driver.find_element_by_xpath("(//select)[4]/option[@value=" + str(year2) + "]").click()
                                driver.find_element_by_xpath("//a[text()='SEARCH']").click()

                                for i in range(2, 1000):
                                    # nttxt=driver.find_element_by_xpath("//table[@class='standard cellborder']/tbody/tr["+str(i)+"]/td[7]").text.strip()
                                    # if nttxt=='Expression of interest':
                                    #     notice_type='3(Prequalification)'
                                    #     earnest_money='Expression of interest'
                                    #     Heading_Tenders_details='Expression of interest'
                                    #
                                    # elif nttxt=='Request for EOI':
                                    #     notice_type='3(Prequalification)'
                                    #     earnest_money='Request for EOI'
                                    #     Heading_Tenders_details='Request for EOI'
                                    #
                                    # elif nttxt=='Request for proposal ':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Request for proposal '
                                    #     Heading_Tenders_details='Request for proposal '
                                    #
                                    # elif nttxt=='Request for quotation ':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Request for quotation '
                                    #     Heading_Tenders_details='Request for quotation '
                                    #
                                    # elif nttxt=='Invitation to bid ':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Invitation to bid '
                                    #     Heading_Tenders_details='Invitation to bid '
                                    #
                                    # elif nttxt=='Request for pre-qualification ':
                                    #     notice_type='3(Prequalification)'
                                    #     earnest_money='Request for pre-qualification '
                                    #     Heading_Tenders_details='Request for pre-qualification '
                                    #
                                    # elif nttxt=='Request for information ':
                                    #     notice_type='3(Prequalification)'
                                    #     earnest_money='Request for information '
                                    #     Heading_Tenders_details='Request for information '
                                    #
                                    #
                                    # elif nttxt=='Grant support-call for proposal ':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Grant support-call for proposal '
                                    #     Heading_Tenders_details='Grant support-call for proposal '
                                    #
                                    # elif nttxt=='Pre-bid notice ':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Pre-bid notice '
                                    #     Heading_Tenders_details='Pre-bid notice '
                                    #
                                    # elif nttxt=='Individual consultant':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Individual consultant'
                                    #     Heading_Tenders_details='Individual consultant'
                                    #
                                    # elif nttxt=='Call for Proposal – Quality Based Fixed Budget':
                                    #     notice_type='1(Tender Notice)'
                                    #     earnest_money='Call for Proposal – Quality Based Fixed Budget'
                                    #     Heading_Tenders_details='Call for Proposal – Quality Based Fixed Budget'
                                    #
                                    # else:
                                    #     notice_type=''
                                    #     earnest_money='Type of notice '+nttxt+' Found New Notice Type'
                                    #
                                    #     Heading_Tenders_details=nttxt
                                    # print('earnest_money:',earnest_money)
                                    # print('notice_type:',notice_type)
                                    # Heading_Tenders_details = 'Tenders are invited for'
                                    country = driver.find_element_by_xpath(
                                        "//table[@class='standard cellborder']/tbody/tr[" + str(
                                            i) + "]/td[6]").text

                                    # try:
                                    #     country1 = driver.find_element_by_xpath(
                                    #         "//table[@class='standard cellborder']/tbody/tr[" + str(
                                    #             i) + "]/td[6]").text.capitalize()
                                    #     links = mycursor.execute(
                                    #         "select * from RegionNew where country_name = '%s' " % (
                                    #             country1))
                                    #     #     keep by defalt value from  id >= 0 and to id <= 10000 on runform
                                    #     chek = links.fetchall()
                                    #     full = [x[0] for x in chek]
                                    #     ind_classification = ','.join(full)
                                    #
                                    #     print('ind_classification', ind_classification)
                                    #     country12 = [x[1] for x in chek]
                                    #     country = ','.join(country12).split(',')[0]
                                    #     print(country)
                                    #     if country == 'IN':
                                    #         source = 'Procurement-notices.undp.org(283679)_Criteria'
                                    #     else:
                                    #         source = 'Procurement-notices.undp.org(283679)'
                                    #         pass
                                    #
                                    # except:
                                    #     country = ''
                                    #     source = 'Procurement-notices.undp.org(283679)'

                                    try:
                                        short_desc = driver.find_element_by_xpath(
                                            "//table[@class='standard cellborder']/tbody/tr[" + str(
                                                i) + "]/td[4]/a").text.strip()+ '\n\n'
                                        print('short_desc:', short_desc)
                                    except:
                                        short_desc = ''
                                    tenders = driver.find_element_by_xpath(
                                        "//table[@class='standard cellborder']/tbody/tr[" + str(
                                            i) + "]/td[4]/a").get_attribute('href')
                                    driver.execute_script("window.open('','_blank');")
                                    driver.switch_to.window(driver.window_handles[1])
                                    driver.get(tenders)

                                    try:
                                        email = driver.find_element_by_xpath(
                                            "//td[text()='Contact :']/following-sibling::td/a").text
                                    except:
                                        email = ''
                                    print('email:', email)

                                    try:
                                        tender_notice_no = driver.find_element_by_xpath(
                                            "//td[text()='Reference Number :']/following-sibling::td").text
                                    except:
                                        tender_notice_no = ''
                                    print('tender_notice_no:', tender_notice_no)

                                    try:
                                        det2txt = driver.find_element_by_xpath(
                                            "//td[text()='Published on :']/following-sibling::td").text
                                        Details2 =  det2txt + '\n'
                                    except:
                                        Details2 = ''
                                        det2txt = ''
                                    print('Details2:', Details2)

                                    try:
                                        det3txt = driver.find_element_by_xpath(
                                            "//td[text()='Deadline :']/following-sibling::td").text
                                        Details3 = 'Deadline : ' + det3txt + '\n\n'
                                        doc_lasttxt1 = det3txt.split(' ')[0].strip()
                                        doc_last = datetime.datetime.strptime(doc_lasttxt1, '%d-%b-%y').strftime('%d/%m/%Y')
                                        # To_match = doc_last.split('/')
                                        #
                                        # To_match = To_match[2] + '/' + To_match[1] + '/' + \
                                        #            To_match[
                                        #                0]
                                        # MatchDeadline = datetime.strptime(To_match,
                                        #                                   '%Y/%m/%d').date()
                                        #
                                        # print('MatchDeadline:', MatchDeadline)
                                        print('doc_last:', doc_last)
                                    except:
                                        Details3 = ''
                                        det3txt = ''
                                        doc_last = ''
                                    print('Details3:', Details3)
                                    print('doc_last:', doc_last)
                                    Details1 =  short_desc
                                    print('Details1:', Details1)
                                    tenders_details = Details1 + Details2

                                    tender_doc_file = driver.current_url
                                    print('tender_doc_file:', tender_doc_file)
                                    # try:
                                    #     Download_File = driver.find_element_by_xpath(
                                    #         "//a[text()='this link']").get_attribute('href')
                                    # except:
                                    #     Download_File = ''
                                    # print('Download_File:', Download_File)

                                    try:
                                        html = driver.find_element_by_xpath(
                                            "//td[@class='content']/ancestor::table").get_attribute('innerHTML')
                                    except:
                                        html = ''

                                    # print('text1:',text1)
                                    print('======================================================')

                                    maj_org, short_desc, tenders_details, add1 = all_function.textModForSpeciaChr(
                                        maj_org, short_desc, tenders_details, add1)

                                    final_html = Google_translate + "<br /><br />" + html

                                    soup = BeautifulSoup(final_html, "lxml")

                                    for m in soup.find_all('a'):
                                        m.replaceWithChildren()

                                    try:
                                        soup.find('td', class_='sidebar').decompose()
                                    except:
                                        pass
                                    try:
                                        for l in soup.find_all("img"):
                                            l.decompose()
                                    except:
                                        pass
                                    try:
                                        soup.find('div', class_='tabs').decompose()
                                    except:
                                        pass
                                    #
                                    # # try:
                                    #     for div in soup.find_all("div", {'class': 'divTextoCentrado'}):
                                    #         div.decompose()
                                    #
                                    # except:
                                    #     pass
                                    id = random.randrange(0000000000, 1111111111)
                                    with open(FilePath + str(id) + '.html', "w",
                                              encoding="utf-8") as file:
                                        file.write(str(soup))
                                    df = pd.DataFrame(data={'id': [id],
                                                            "Org": ['United Nations Development Programme (UNDP)'],
                                                            "Short_des": [short_desc],
                                                            "Des": [tenders_details],
                                                            "tender_no": [tender_notice_no],
                                                            "notice_type": ['Tender Notice'],
                                                            "deadline": [doc_last],
                                                            "est_cost": [est_cost],
                                                            "Tender_File_url": [tender_doc_file],
                                                            "Country": [country],
                                                            "address": ['United Nations Development Programme One United Nations Plaza New York, NY 10017 USA'],
                                                            "email": [email],
                                                            "doc_start": [doc_start],
                                                            "ICB/NCB": ['ICB'],
                                                            'cpv': [cpv],
                                                            })
                                    df.to_csv(
                                        FilePath + str(
                                            todays.strftime(
                                                '%d-%m-%Y') + ' Tender') + '.csv',
                                        mode='a', index=False, header=False)
                                    time.sleep(1)
                                    window['-Tcount-'].update(progress)
                                    window.refresh()
                                    progress += 1



                                    parent = driver.window_handles[0]

                                    child1 = driver.window_handles[1]
                                    driver.close()
                                    driver.switch_to.window(parent)

                            elif CA:
                                colums = ['id',
                                          'Org',
                                          'Short_des',
                                          'Des',
                                          'tender_no',
                                          'notice_type',
                                          'deadline',
                                          "est_cost",
                                          'Tender_File_url',
                                          'Country',
                                          'address',
                                          'email',
                                          'doc_start',
                                          'ICB/NCB',
                                          'cpv'
                                          ]

                                df = pd.DataFrame(columns=colums)

                                df.to_csv(FilePath + todays.strftime('%d-%m-%Y') + ' Contract_Award' + '.csv', index=False)

                                Dub_tender = 1
                                Down_tender = 1
                                driver = DriverDetails()
                                driver.get('https://procurement-notices.undp.org/view_awards.cfm')
                                time.sleep(5)
                                driver.find_element_by_xpath('(//input)[1]').clear()
                                driver.find_element_by_xpath('(//input)[1]').send_keys(datee)
                                driver.find_element_by_xpath("(//select)[1]").click()
                                driver.find_element_by_xpath("(//select)[1]/option[@value=" + str(month) + "]").click()
                                driver.find_element_by_xpath("(//select)[2]").click()
                                driver.find_element_by_xpath("(//select)[2]/option[@value=" + str(year) + "]").click()

                                driver.find_element_by_xpath('(//input)[2]').clear()
                                driver.find_element_by_xpath('(//input)[2]').send_keys(datee2)
                                driver.find_element_by_xpath("(//select)[3]").click()
                                driver.find_element_by_xpath("(//select)[3]/option[@value=" + str(month2) + "]").click()
                                driver.find_element_by_xpath("(//select)[4]").click()
                                driver.find_element_by_xpath("(//select)[4]/option[@value=" + str(year2) + "]").click()
                                driver.find_element_by_xpath("//a[text()='SEARCH']").click()
                                try:
                                    for i in range(1, 1000):
                                        short_desc1 = driver.find_element_by_xpath(
                                            "//table[@class='standard cellborder'][" + str(
                                                i) + "]//strong[text()='Title :']/parent::th").text.strip().capitalize()
                                        short_desc = short_desc1.replace('Title :', '')

                                        Details1 =  short_desc + '\n'
                                        try:
                                            add2txt1 = driver.find_element_by_xpath(
                                                "//table[@class='standard cellborder'][" + str(
                                                    i) + "]//td[text()='UNDP Office :']/following-sibling::td").text
                                            add1 = add2txt1

                                        except:
                                            add2txt1 = ''
                                            add1 = ''
                                        print('add2:', add2)

                                        country = driver.find_element_by_xpath(
                                            "//table[@class='standard cellborder'][" + str(
                                                i) + "]//td[text()='Country of Contractor :']/following-sibling::td").text

                                        # try:
                                        #     country1 = driver.find_element_by_xpath(
                                        #         "//table[@class='standard cellborder'][" + str(
                                        #             i) + "]//td[text()='Country of Contractor :']/following-sibling::td").text
                                        #     links = mycursor.execute(
                                        #         "select * from RegionNew where country_name = '%s' " % (
                                        #             country1))
                                        #     #     keep by defalt value from  id >= 0 and to id <= 10000 on runform
                                        #     chek = links.fetchall()
                                        #     full = [x[0] for x in chek]
                                        #     ind_classification = ','.join(full)
                                        #
                                        #     print('ind_classification', ind_classification)
                                        #     country12 = [x[1] for x in chek]
                                        #     country = ','.join(country12).split(',')[0]
                                        #     print(country)
                                        #     if country == 'IN':
                                        #         source = 'Procurement-notices.undp.org(283679)_Criteria'
                                        #     else:
                                        #         source = 'Procurement-notices.undp.org(283679)_CA'
                                        #         pass
                                        #
                                        # except:
                                        #     country = ''
                                        #     source = 'Procurement-notices.undp.org(283679)_CA'
                                        print('country:', country)

                                        print('Details1:', Details1)
                                        try:
                                            Details2 = driver.find_element_by_xpath(
                                                "//table[@class='standard cellborder'][" + str(
                                                    i) + "]//td[text()='Description of Contract :']/p").text.strip().capitalize()
                                        except:
                                            Details2 = ''
                                        print('Details2:', Details2)

                                        tenders_details = Details1+Details2

                                        try:
                                            maj_org = driver.find_element_by_xpath(
                                                "//table[@class='standard cellborder'][" + str(
                                                    i) + "]//td[text()='Name of Contractor :']/following-sibling::td").text
                                        except:
                                            maj_org = ''
                                        print('maj_org:', maj_org)

                                        try:
                                            tender_notice_no = driver.find_element_by_xpath(
                                                "//table[@class='standard cellborder'][" + str(
                                                    i) + "]//td[text()='Contract Reference Number :']/following-sibling::td").text
                                        except:
                                            tender_notice_no = ''
                                        print('tender_notice_no:', tender_notice_no)

                                        try:
                                            det3txt1 = driver.find_element_by_xpath(
                                                "//table[@class='standard cellborder'][" + str(
                                                    i) + "]//td[text()='Date of Contract Signature :']/following-sibling::td").text.strip()
                                            Details3 = 'Date of Contract Signature : ' + det3txt1
                                            doc_lasttxt1 = datetime.datetime.strptime(det3txt1, '%d-%b-%y').strftime(
                                                '%d/%m/%Y')
                                            from dateutil.relativedelta import relativedelta

                                            doc_last4 = datetime.datetime.strptime(doc_lasttxt1,
                                                                                   '%d/%m/%Y').date() + relativedelta(
                                                months=2)
                                            # print('doc_last4',doc_last4)
                                            doc_last5 = str(doc_last4)
                                            doc_last6 = doc_last5.replace('-', '/').split('/')
                                            doc_last = doc_last6[2] + '/' + doc_last6[1] + '/' + doc_last6[
                                                0]
                                            print('doc_last: ', doc_last)

                                            # to_match1 = doc_last5.split('-')
                                            #
                                            # to_match = to_match1[0] + '/' + to_match1[1] + '/' + to_match1[
                                            #     2]
                                            # MatchDeadline = datetime.datetime.strptime(to_match,
                                            #                                            '%Y/%m/%d').date()
                                            # print('MatchDeadline', MatchDeadline)
                                        except:
                                            det3txt1 = ''
                                            Details3 = ''
                                            doc_lasttxt1 = ''
                                        # print('Details3:', Details3)
                                        print('doc_last:', doc_lasttxt1)
                                        try:
                                            est_costtxt = driver.find_element_by_xpath(
                                                "//table[@class='standard cellborder'][" + str(
                                                    i) + "]//td[text()='Contract Amount in US :']/following-sibling::td").text.strip()
                                            est_cost = est_costtxt.strip()
                                        except:
                                            est_costtxt = ''
                                            est_cost = ''
                                        print('est_cost:', est_cost)

                                        print(
                                            '===================================================================================')
                                        maj_org, short_desc, tenders_details, add1 = all_function.textModForSpeciaChr(
                                            maj_org, short_desc, tenders_details, add1)
                                        try:
                                            k = driver.find_elements_by_xpath(
                                                "(//table[@class='standard cellborder'])[" + str(i) + "]/tbody/tr")
                                            html = ''
                                            for e in k:
                                                html1 = ''
                                                html1 = e.get_attribute('innerHTML') + '<br>'

                                                print('html1:', html1)
                                                html = html + html1

                                        except:
                                            html = ''

                                        final_html = Google_translate + "<br /><br />" + html

                                        soup = BeautifulSoup(final_html, 'html.parser')
                                        try:
                                            for tag in soup("img"):
                                                tag.decompose()

                                            # sp.decompose()
                                            print('inside')

                                            for m in soup.find_all('a'):
                                                m.replaceWithChildren()
                                        #
                                        except Exception as e:
                                            print(e)



                                        final_html = Google_translate + "<br /><br />" + html

                                        soup = BeautifulSoup(final_html, "lxml")

                                        id = random.randrange(0000000000, 1111111111)
                                        with open(FilePath + str(id) + '.html', "w",
                                                  encoding="utf-8") as file:
                                            file.write(str(soup))
                                        df = pd.DataFrame(data={'id': [id],
                                                                "Org": [maj_org],
                                                                "Short_des": [short_desc],
                                                                "Des": [tenders_details],
                                                                "tender_no": [tender_notice_no],
                                                                "notice_type": ['Contract Awards'],
                                                                "deadline": [doc_last],
                                                                "est_cost": [est_cost],
                                                                "Tender_File_url": [tender_doc_file],
                                                                "Country": [country],
                                                                "address": [add1],
                                                                "email": [email],
                                                                "doc_start": [doc_start],
                                                                "ICB/NCB": ['ICB'],
                                                                'cpv': [cpv],
                                                                })
                                        df.to_csv(
                                            FilePath + str(
                                                todays.strftime(
                                                    '%d-%m-%Y') + ' Contract_Award') + '.csv',
                                            mode='a', index=False, header=False)
                                        time.sleep(1)
                                        window['-Tcount-'].update(progress)
                                        window.refresh()
                                        progress += 1






                                except Exception as e:
                                    print(e)
                                    pass
                                except TimeoutException as e:
                                    print(e)


                            else:
                                sg.popup('please select any one notice')
                                continue
                            window['-ADD SUB-'].update('** All Done **')
                    window.close()
                else:
                    sg.popup('Key has been expired')
            else :
                sg.popup ('Please Enter Key')
window.close()
