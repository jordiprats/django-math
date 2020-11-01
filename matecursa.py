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
def restes(file, pages, min, max):
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
                    operacio = str(primer_numero)+' - '+str(segon_numero)+' ='
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
def sumes(file, pages, min, max, min_segona_unitat, max_segona_unitat):
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
                    operacio = str(primer_numero)+' + '+str(segon_numero)+' ='
                pdf.cell(w=0,h=0, txt=operacio, ln=0 )
                anterior_operacio = operacio
        if pagina%4 == 0:
            max += 1
    pdf.output(file,'F')

curses.add_command(sumes)
curses.add_command(restes)

if __name__ == '__main__':
    curses()
    