import flet as ft
from flet import colors
from decimal import Decimal

# Classificando os operadores:
botoes = [
    {'operador': 'AC', "fonte": colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', "fonte": colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', "fonte": colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', "fonte": colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '8', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '9', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '*', "fonte": colors.BLACK, 'fundo': colors.ORANGE},
    {'operador': '4', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '5', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '6', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '-', "fonte": colors.BLACK, 'fundo': colors.ORANGE},
    {'operador': '1', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '2', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '3', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '+', "fonte": colors.BLACK, 'fundo': colors.ORANGE},
    {'operador': '0', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '.', "fonte": colors.BLACK, 'fundo': colors.WHITE24},
    {'operador': '=', "fonte": colors.BLACK, 'fundo': colors.ORANGE},
    
]

# Criando a página inicial da Calculadora:
def main(page: ft.Page):
    page.bgcolor = '#000' #Cor do fundo da janela
    page.window_resizable = False
    page.window_width =300 #Altura da página
    page.window_height =380 #Largura da página
    page.title = 'Calculadora' #Nome da Janela
    page.window_always_on_top =True
    
    result = ft.Text(value= '0', color = colors.WHITE, size=20 )

# Criando a função para calcular os valores digitados    
    def calculate(operador, value_at): 
        try:   
            value = eval(value_at)
            
            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return 'Error'
        
        digtis = min(abs(Decimal(value).as_tuple().exponent), 5)   
        return format(value, f'.{digtis}f')

# Função para concatenar os valores:    
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value
        
        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '.'):
                value_at = value_at[:-1]
                
            value = value_at + value
            
            if value[-1] in ('=','%','±'):
                value = calculate(operador=value[-1], value_at=value_at)
        
        result.value = value
        result.update()

# Configurando o Display da Calculadora:    
    display = ft.Row(
        width=250,
        controls=[result],
        alignment = 'end',
    )
    
# Criando os butões da Calculadora:
    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment= ft.alignment.center,
        on_click=select
    ) for btn in botoes]
           
    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )
    
    page.add(display, keyboard) 

  
ft.app(target = main)