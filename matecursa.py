from random import randrange
from fpdf import FPDF

import random
import click

@click.group()
def curses():
  pass

#
# sumes
#

@click.command()
@click.option('--file', default='sumes.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=1, help='min int')
@click.option('--max', default=6, help='max int')
@click.option('--min-segona-unitat', default=0, help='max int segona unitat')
@click.option('--max-segona-unitat', default=0, help='max int segona unitat')
@click.option('--multiplicador', default=1, help='multiplicador')
@click.option('--disable-total-operacions', is_flag=True, default=True, help='Elimina missatge de total de operacions')
def sumes(file, pages, min, max, min_segona_unitat, max_segona_unitat, multiplicador, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    if disable_total_operacions:
      pdf.set_font('helvetica', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min, max)
          if min_segona_unitat:
            min_segon_numero=min_segona_unitat
          else:
            min_segon_numero=min
          if max_segona_unitat:
            max_segon_numero=max_segona_unitat
          else:
            max_segon_numero=max
          segon_numero = randrange(min_segon_numero, max_segon_numero)
          operacio = str(primer_numero*multiplicador)+' + '+str(segon_numero*multiplicador)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

@click.command()
@click.option('--file', default='sumes_hortizontal.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min1', default=100, help='min int')
@click.option('--max1', default=900, help='max int')
@click.option('--min2', default=100, help='min int')
@click.option('--max2', default=300, help='max int')
@click.option('--min3', default=10, help='min int')
@click.option('--max3', default=100, help='max int')
@click.option('--disable-marge-calculs', is_flag=True, default=False, help='deixa marge per calcul')
def sumes_horitzontal(file, pages, min1, max1, min2, max2, min3, max3, disable_marge_calculs):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    # pdf.set_font('helvetica', '', 25.0)
    # pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 18.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 2):
      if disable_marge_calculs:
        range_files = range(0,4)
      else:
        range_files = range(0,11)
      for linea in range_files:
        if disable_marge_calculs:
          pdf.set_xy(10.0 + (columna*100), 32.5+ (linea*22*3))
        else:
          pdf.set_xy(10.0 + (columna*100), 40 + (linea*20))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min1, max1)
          segon_numero = randrange(min2, max2)
          tercer_numero = randrange(min3, max3)
          operacio = str(primer_numero)+' + '+str(segon_numero)+' + '+str(tercer_numero)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
  pdf.output(file,'F')

#
# restes
#

@click.command()
@click.option('--file', default='restes.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min', default=1, help='max int')
@click.option('--max', default=5, help='max int')
@click.option('--multiplicador', default=1, help='multiplicador')
def restes(file, pages, min, max, multiplicador):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 25.0)
    pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min+1, max)
          if min==primer_numero:
            segon_numero = min
          else:
            segon_numero = randrange(min, primer_numero)
          operacio = str(primer_numero*multiplicador)+' - '+str(segon_numero*multiplicador)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

@click.command()
@click.option('--file', default='restes_vertical.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min', default=100, help='max int')
@click.option('--max', default=999, help='max int')
@click.option('--disable-total-operacions', is_flag=True, default=True, help='Elimina missatge de total de operacions')
def restes_vertical(file, pages, min, max, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    if not disable_total_operacions:
      pdf.set_xy(5.0, 276)
      pdf.set_font('helvetica', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 3):
      for linea in range(0,5):
        primer_numero = randrange(int(max/4), max)
        segon_numero = randrange(min, primer_numero)
        pdf.set_xy(30.0 + (columna*65), 47.5+ (((linea*2)-0.4)*25))
        pdf.cell(w=0,h=0, txt=str(primer_numero), ln=0 )
        pdf.set_xy(30.0 + ((columna*65)-5), 47.5+ ((linea*2)*25))
        pdf.set_font('helvetica', '', 30.0)
        pdf.cell(w=0,h=0, txt="-", ln=0 )
        pdf.set_font('helvetica', '', 20.0)
        pdf.set_xy(30.0 + (columna*65), 47.5+ ((linea*2)*25))
        pdf.cell(w=0,h=0, txt=str(segon_numero), ln=0 )
        pdf.set_line_width(0.5)
        pdf.line(
              20.0 + (columna*65), 52.5+ ((linea*2)*25), 
              45.0 + (columna*65), 52.5+ ((linea*2)*25)
            )
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

#
# multiplicacions
#

@click.command()
@click.option('--file', default='multiplicacions.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=1, help='min int')
@click.option('--max', default=6, help='max int')
@click.option('--min-segona-unitat', default=0, help='max int segona unitat')
@click.option('--max-segona-unitat', default=0, help='max int segona unitat')
@click.option('--multiplicador', default=1, help='multiplicador')
@click.option('--disable-total-operacions', is_flag=True, default=True, help='Elimina missatge de total de operacions')
def multiplicacions(file, pages, min, max, min_segona_unitat, max_segona_unitat, multiplicador, disable_total_operacions):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(0, pages):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    if not disable_total_operacions:
      pdf.set_xy(5.0, 276)
      pdf.set_font('helvetica', '', 25.0)
      pdf.cell(w=0,h=0, txt='Operacions fetes en 2 minuts .......................', ln=0 )
    pdf.set_font('helvetica', '', 20.0)
    anterior_operacio = ''
    operacio = ''
    for columna in range(0, 4):
      for linea in range(0,14):
        pdf.set_xy(10.0 + (columna*50), 32.5+ (linea*17))
        while anterior_operacio == operacio:
          print('range: '+str(min)+'-'+str(max))
          primer_numero = randrange(min, max)
          if min_segona_unitat:
            min_segon_numero=min_segona_unitat
          else:
            min_segon_numero=min
          if max_segona_unitat:
            max_segon_numero=max_segona_unitat
          else:
            max_segon_numero=max
          segon_numero = randrange(min_segon_numero, max_segon_numero)
          operacio = str(primer_numero*multiplicador)+' x '+str(segon_numero*multiplicador)+' ='
        pdf.cell(w=0,h=0, txt=operacio, ln=0 )
        anterior_operacio = operacio
    if pagina%4 == 0:
      max += 1
  pdf.output(file,'F')

@click.command()
@click.option('--file', default='taules_multiplicar.pdf', help='output file')
@click.option('--min', default=2, help='min int')
@click.option('--max', default=30, help='max int')
def taules_multiplicar(file, min, max):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(min, int((max/2))):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 20.0)
    for columna in range(0, 2):
      for linea in range(1,11):
        pdf.set_xy(10.0 + (columna*100), 40.5+ (linea*17))
        pdf.cell(w=0,h=0, txt=str(linea)+' x '+str(((pagina*2))+columna)+' = ', ln=0 )
  pdf.output(file,'F')

#
# problemes
#

operacions = {

  ## sumes
  "sumes_2": [
    "Tinc {} cosins per part de pare i {} per part de mare. Quants cosins tinc?",
    "En dos incendis diferents es van cremar {} i {} hectàreas respecticament. Quantes s'han cremat en total?"
  ],
  "sumes_3": [
    "Ahir vaig fer {}km, avui n'he fet {}km, demà en faré {}km. Quants kilometres hauré fet en total?",
    "Al Zoo hi ha {} espècies de mamífers, {} espècies d'aus i {} espècies de ràptils. Quantes espècies hi ha?",
  ],

  ## restes
  "restes_primer_gros": [
    "Tenia {} caramels, però n'he regalat {}. Quants me'n queden?",
    "Li he donat {} sardines al gat, però només se'n ha menjat {}. Quantes en queden?",
    "Un guepart pot còrrer a {}km/h, però una zebra va {}km/h més lenta que el guepart. A quina velocitat por còrrer la zebra?",
    "De un total de {} hectàreas, se'n han creamat {}. Quantes no s'han cremat?"
  ],
  "restes_un_sol_numero": [
    "Tenia {} ampolles d'aigua a casa. Han vingut els meus amics i n'he donat una a cadascú. Quants amics han vingut?",
  ],

  ## multiplicacions
  "multiplicacions": [
    "Vull comprar {} tasses i cada una val {}. Quants diners necessito per comprar-les?",
    "Per fer un berenar vull comprar {} croisants per cada persona. Si venen {} amics, quants croisants haig de comprar?",
    "A cada paquet de mocadors n'hi ha {}. Si tinc {} paquets, quants mocadors tinc?",
    "Si faig {} km cada hora i m'hi he estat {} hores. Quants kilometres he fet en total?",
    "La meva tortuga pon {} vegades a l'any. Cada vegada que ho fa en neixen {} tortugues. Al final de l'any, quantes tortugues hauran nascut?",
    "Si hi ha {} bolígrafs en cada paquet. Si tenim {} paquets, quants bolígrafs tenim?",
    "Si cadascú es menja {} pomes per esmorçar, quantes pomes necessitem si a casa som {}",
  ],
  "multiplicacions_un_sol_numero": [
    "Avui anirem a fer una excursió amb raquetes de neu amb {} companys. Quantes raquetes necessitem? (dues per persona)",
    "Quantes persones serem si venen {} parelles",
  ],

  ## divisions
  "divisions_gros_primer": [
    "Tinc {} euros, si cada llibre val {} euros, quants llibres puc comprar?",
  ],
  "divisions_petit_primer": [
    "Vull preparar truites per sopar. Per cada una necesito {} ous, si en tinc {} quantes en podré preparar?"
  ]
}

def problemes_get_pregunta(sumes_min, sumes_max, mul_min, mul_max):
  group = random.choice(list(operacions.keys()))

  pregunta = random.choice(operacions[group])

  if group=="sumes_2":
    return pregunta.format(randrange(sumes_min, sumes_max), randrange(sumes_min, sumes_max))
  elif group=="sumes_3":
    return pregunta.format(randrange(sumes_min, sumes_max), randrange(sumes_min, sumes_max), randrange(sumes_min, sumes_max))
  elif group=="restes_primer_gros":
    resta_gros = randrange(sumes_min+int(sumes_max/4), int(sumes_max/2))
    resta_petit = randrange(sumes_min, resta_gros)
    return pregunta.format(resta_gros, resta_petit)
  elif group=="restes_un_sol_numero":
    return pregunta.format(randrange(sumes_min, sumes_max))
  elif group=="multiplicacions":
    return pregunta.format(randrange(mul_min, mul_max), randrange(mul_min, mul_max))
  elif group=="multiplicacions_un_sol_numero":
    return pregunta.format(randrange(mul_min, mul_max))
  elif group=="divisions_gros_primer":
    factor_1 = randrange(mul_min, mul_max)
    factor_2 = randrange(mul_min, mul_max)
    resultat = factor_1*factor_2

    return pregunta.format(resultat, factor_1)
  elif group=="divisions_petit_primer":
    factor_1 = randrange(mul_min, mul_max)
    factor_2 = randrange(mul_min, mul_max)
    resultat = factor_1*factor_2

    return pregunta.format(factor_1, resultat)
  else:
    return ""


@click.command()
@click.option('--file', default='problemes.pdf', help='output file')
@click.option('--pagines', default=4, help='numero de pàgines')
@click.option('--sumes-min', default=5, help='sumes min int')
@click.option('--sumes-max', default=150, help='sumes max int')
@click.option('--mul-min', default=2, help='multiplicacions min int')
@click.option('--mul-max', default=10, help='multiplicacions max int')
def problemes(file, pagines, sumes_min, sumes_max, mul_min, mul_max):
  pdf = FPDF(orientation='P', unit='mm', format='A4')
  for pagina in range(1, int(pagines+1)):
    pdf.add_page()
    pdf.set_font('helvetica', '', 15.0)
    pdf.set_xy(5.0, 18)
    pdf.cell(w=0,h=0, txt='Nom: ........................................................................... Data: ...................................', ln=0 )
    pdf.set_xy(5.0, 276)
    pdf.set_font('helvetica', '', 12.0)
    for linea in range(0,5):
      pdf.set_xy(10.0, 35.5+ (linea*45))
      pdf.multi_cell(w=0,h=10, txt=str(linea+1)+'. '+problemes_get_pregunta(sumes_min, sumes_max, mul_min, mul_max).encode('latin-1', 'replace').decode('latin-1'))
  pdf.output(file,'F')


#
# main
#

curses.add_command(sumes)
curses.add_command(sumes_horitzontal)

curses.add_command(restes)
curses.add_command(restes_vertical)

curses.add_command(multiplicacions)
curses.add_command(taules_multiplicar)

curses.add_command(problemes)

if __name__ == '__main__':
  curses()
  