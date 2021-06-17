from random import randrange
from fpdf import FPDF

import click

@click.group()
def curses():
  pass

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
@click.option('--file', default='sumes.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=1, help='min int')
@click.option('--max', default=6, help='max int')
@click.option('--min-segona-unitat', default=0, help='max int segona unitat')
@click.option('--max-segona-unitat', default=0, help='max int segona unitat')
@click.option('--multiplicador', default=1, help='multiplicador')
def sumes(file, pages, min, max, min_segona_unitat, max_segona_unitat, multiplicador):
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
@click.option('--file', default='multiplicacions.pdf', help='output file')
@click.option('--pages', default=30, help='number of pages')
@click.option('--min', default=1, help='min int')
@click.option('--max', default=6, help='max int')
@click.option('--min-segona-unitat', default=0, help='max int segona unitat')
@click.option('--max-segona-unitat', default=0, help='max int segona unitat')
@click.option('--multiplicador', default=1, help='multiplicador')
def multiplicacions(file, pages, min, max, min_segona_unitat, max_segona_unitat, multiplicador):
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
@click.option('--file', default='sumes_hortizontal.pdf', help='output file')
@click.option('--pages', default=10, help='number of pages')
@click.option('--min1', default=100, help='min int')
@click.option('--max1', default=900, help='max int')
@click.option('--min2', default=100, help='min int')
@click.option('--max2', default=300, help='max int')
@click.option('--min3', default=10, help='min int')
@click.option('--max3', default=100, help='max int')
def sumes_horitzontal(file, pages, min1, max1, min2, max2, min3, max3):
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
            for linea in range(0,4):
                pdf.set_xy(10.0 + (columna*100), 32.5+ (linea*22*3))
                while anterior_operacio == operacio:
                    print('range: '+str(min)+'-'+str(max))
                    primer_numero = randrange(min1, max1)
                    segon_numero = randrange(min2, max2)
                    tercer_numero = randrange(min3, max3)
                    operacio = str(primer_numero)+' + '+str(segon_numero)+' + '+str(tercer_numero)+' ='
                pdf.cell(w=0,h=0, txt=operacio, ln=0 )
                anterior_operacio = operacio
    pdf.output(file,'F')

curses.add_command(sumes)
curses.add_command(sumes_horitzontal)
curses.add_command(restes)
curses.add_command(multiplicacions)

if __name__ == '__main__':
    curses()
    