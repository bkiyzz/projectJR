from registmeds import registermeds
from registpac import registerpac
import PySimpleGUI as sg

menu = ['menu',['LightGreen10', 'LightBrown8', 'Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']]

def crear_ventanaMain(tema):
    sg.theme(tema),
    sg.set_options(font='Calibry 15', button_element_size=(6,2)) #ancho,alto

    #tamano_boton=(8,2)

    
    layout=[
        [sg.Button('Registrar Medico', key='-REGMED-')],

        [sg.Button('Registrar Paciente', key='-REGPAC-')]

    ]
    return sg.Window('Hospital JR',layout=layout)

def crear_ventanameds(tema):

    sg.theme(tema),
    sg.set_options(font='Calibry 15', button_element_size=(6,2)) #ancho,alto

    #tamano_boton=(8,2)

    
    layout=[
        [sg.Text('Registro Medico')],

        [sg.Text('ID '), sg.InputText(key='-ID-')],

        [sg.Text('Nombre '), sg.InputText(key='-NOMBRE-')],

        [sg.Text('Altura(cm) '), sg.InputText(key='-ALTURA-')],
        
        [sg.Text('Peso(kg) '), sg.InputText(key='-PESO-')],

        [sg.Text('Edad '), sg.InputText(key='-EDAD-')],

        [sg.Text('Tipo de sangre '), sg.InputText(key='-SANGRE-')],

        [sg.Button('Guardar', key='-SAVEBUTTON-'), sg.Button('Eliminar', key='-DELETEBUTTON-')],

    ]
    return sg.Window('Hospital JR',layout=layout)

def crear_ventanapacs(tema):
    sg.theme(tema),
    sg.set_options(font='Calibry 15', button_element_size=(6,2)) #ancho,alto

    #tamano_boton=(8,2)

    
    layout=[
        [sg.Text('Registro Paciente')],

        [sg.Text('ID '), sg.InputText(key='-ID-')],

        [sg.Text('Nombre '), sg.InputText(key='-NOMBRE-')],

        [sg.Text('Altura(cm) '), sg.InputText(key='-ALTURA-')],
        
        [sg.Text('Peso(kg) '), sg.InputText(key='-PESO-')],

        [sg.Text('Edad '), sg.InputText(key='-EDAD-')],

        [sg.Text('Tipo de sangre '), sg.Combo(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-','O+' , 'O-'], key='-SANGRE-')],

        [sg.Text('Enfermedad '), sg.Combo(['No', 'Diabates', 'Hipertensión', 'Cáncer de prostata', 'Cáncer de mama', 'Cáncer de colon', 'Alzheimer/demencia', 'Artritis', 'Asma', 'Fibrosis quística', 'Epilepsia', 'VIH', 'Parkinson'],default_value='No',key='-ENFERMEDAD-')],

        [sg.Button('Guardar', key='-SAVEBUTTON-'), sg.Button('Eliminar', key='-DELETEBUTTON-')],

    ]
    return sg.Window('Hospital JR',layout=layout)

window = crear_ventanapacs('DarkGrey14')
ejecutandose = True

while ejecutandose:
    event,valores = window.read()

    if event == sg.WIN_CLOSED:
        ejecutandose = False