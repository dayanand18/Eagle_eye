from reportlab.lib import colors
from reportlab.lib.pagesizes import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import *
from datetime import datetime as dt
from test import *


def background(c):
    c.setFillColorRGB(1,0,0)
    c.rect(5,5,652,792,fill=1)


c= Canvas("Background",pagesize=letter)
c.setTitle("Background")
# background(c)
PATH_OUT = ""

# mnth = {'mar20':'MARCH2020'}


def create(rent,bill,memb,name,user,user_storage,pending_amount=0):
    p_status = 'Paid'
    if pending_amount > 0:
        p_status = "Pending"
    try:
        elements = []
        styles = getSampleStyleSheet()

        title = str(dt.now().strftime('%B%Y'))
        #doc = SimpleDocTemplate(PATH_OUT + 'Report_File.pdf')
        store_path = os.path.join(os.getcwd(),os.path.join(user_storage,str(title)+'.pdf'))
        #store_path = f'{user_storage}.pdf'
        doc = SimpleDocTemplate(store_path, pagesize = A4, rightMargin = 20, leftMargin = 25, topMargin = 30, bottomMargin = 18,)

        elements.append(Paragraph("Room Expense For The Month "+ str(title), styles['Title']))


        df = view_user(user,title+'.csv')
        if len(df)>0:
            lista = [list(df.keys())]
            for vl in df.values:
                lista.append(vl)

            ts = TableStyle([('ALIGN',(1,1),(0,0),'RIGHT'),
                                   ('TEXTCOLOR',(1,1),(-2,-2),colors.green),
                                   ('VALIGN',(5,5),(2,3),'MIDDLE'),
                                   ('TEXTCOLOR',(0,0),(0,-1),colors.black),
                                   ('ALIGN',(0,-1),(0,0),'CENTER'),
                                   ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                                   ('TEXTCOLOR',(0,-1),(-1,-1),colors.black),
                                   ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                   ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                   ])
            table = Table(lista, style=ts,colWidths=[1.9*inch] * len(lista))

            ration_total=total_file(title+'.csv')
            your_spent = check_user(user,title+'.csv')
            styles = getSampleStyleSheet()
            styleNormal = styles['Normal']
            styleHeading = styles['Heading1']
            styleHeading2 = styles['Heading2']


            #
            # #Configure style and word wrap
            now = dt.now().strftime('%d-%m-%Y')
            s = getSampleStyleSheet()
            s = s["BodyText"]
            s.wordWrap = 'CJK'
            head = 'Roomate Details'
            space='_'*96
            line1 = f"Name:{str(name)} "
            line2 = f'Email:{user}'
            line3 = 'Report Date: ' + str(now)
            line4 = 'Payment Status: '+str(p_status)
            line9 = f'Room rent:{str(rent)}'
            line7 = '_'*96
            line8 = 'Payment Details'
            line10 = f'Power Bill:{str(bill)}'
            line11 = f'Ration Bill:{str(ration_total)}'
            total = float(rent)+float(bill)+float(ration_total)
            line12 = f'Total:{str(total)}'
            line13 = f'Total member   :{str(memb)}'
            each_memb = total / float(memb)
            line14 = f'For Each Person:{str(each_memb)}'
            line15 = '_'*96
            line16 =f'Net Amout:{str(each_memb)}'
            line17 = f'you spent:{str(your_spent)}'

            line18 = f'pending payment:{str(pending_amount)}'
            net = float(each_memb) + float(pending_amount)-float(your_spent)
            line19 = f'Net payble{str(net)}'
            line20 = '_'*96

            # c.setStrokeColorRGB(0,1,0.3) #choose your line color
            # c.line1(2,2,2*inch,2*inch)

            #Send the data and build the file
            elements.append(Paragraph(head, styleNormal))
            elements.append(Paragraph(space, styleNormal))
            elements.append(Spacer(inch, 0.1*inch))
            elements.append(Paragraph(line1, styleNormal))
            elements.append(Paragraph(line2, styleNormal))
            elements.append(Paragraph(line3, styleNormal))
            #elements.append(Spacer(inch, 0.25*inch))
            elements.append(Paragraph(line4, styleNormal))
            # elements.append(Paragraph(line5, styleNormal))
            # elements.append(Paragraph(line6, styleNormal))
            elements.append(Paragraph(line7, styleNormal))
            elements.append(Paragraph(line8,styles['title']))
            elements.append(Paragraph(line9, styleNormal))
            elements.append(Paragraph(line10, styleNormal))
            elements.append(Paragraph(line11, styleNormal))
            elements.append(Paragraph(line12, styleNormal))
            elements.append(Paragraph(line13, styleNormal))
            elements.append(Paragraph(line14, styleNormal))
            elements.append(Paragraph(line15, styleNormal))
            elements.append(Paragraph(line16, styleNormal))
            elements.append(Paragraph(line17, styleNormal))
            elements.append(Paragraph(line18, styleNormal))
            elements.append(Paragraph(line19, styleNormal))
            elements.append(Paragraph(line20, styleNormal))
            elements.append(Spacer(inch, .25 * inch))
            elements.append(Spacer(inch, .25*inch))
            elements.append(table)

            doc.build(elements)
            return store_path
        return False
    except Exception as e:


        return ''


