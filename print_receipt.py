from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    ["Date", "Name", "Subscription", "Price ($)"],
    ["5/6/2023", "Receipt", "Lifetime", "1,000"],
    ["5/6/2023", "Receipt+", "Lifetime", "1,000"],
    ["Subtotal", "", "", "120"],
    ["Discount", "", "", "20"],
    ["Total", "", "", "100"],
]

pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1
title = Paragraph( "Testing" , title_style )
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)
table = Table( DATA , style = style )
pdf.build([ title , table ])
