from fpdf import FPDF

surname_name = input(("Введите Фамилию и Имя:"))
cod = input(("Введите код подготовки:"))
 
def creat_sert(surname_name, cod):
    #создание документа
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_font(family='georgia', style="", fname="Fonts/Georgia.ttf") 
    #задний фон
    pdf.set_page_background('Images/certificate1.png')
    pdf.add_page()
    #Текст
    pdf.set_margin(0)
    pdf.set_font("georgia", "", 40)
    pdf.ln(27)
    pdf.set_margin(5)
    pdf.cell(280, 133, surname_name, align="C")
    pdf.set_margin(0)
    pdf.set_font("georgia", "", 17)
    pdf.ln(85)
    pdf.multi_cell(297, 20, "успешно выполнивший соответствующие требования к обучению и сертификации\n настоящим признается сертифицированным по MikroTik", 
                   align="C", max_line_height=8)
    pdf.set_font("Helvetica", "", 33)
    pdf.ln(1)
    pdf.cell(290, 7, cod, align="C")
    pdf.set_font("Helvetica", "", 16)
    pdf.ln(34)
    pdf.set_margin(25)
    pdf.cell(236, 8, "#TR0417", align="R")
    pdf.set_margin(0)
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_margin(25)
    pdf.cell(236,8, "09-11-2018", align="R")
    pdf.set_margin(0)
    pdf.set_font("georgia", "", 10)
    pdf.ln(8)
    pdf.multi_cell(297, 10, "Действителен в течение трех лет c момента выдачи. Подтвердите подлинность этого документа на https://www.mikrotic.com/certificates/ \n Выдан MikroTikls SIA, Пернавас 46, Рига, Латвия",
                    align="C", max_line_height=6)
    #Сохранение
    pdf.output("sertificate.pdf")

creat_sert(surname_name, cod)


