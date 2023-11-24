import PySimpleGUI as sg

# Définition du thème de l'interface utilisateur
sg.theme('LightBlue2')

# Définition de la disposition des éléments de l'interface utilisateur
layout = [
    [sg.Text('Entrez une valeur :')],
    [sg.InputText(key='input')],
    [sg.Radio('Oui', "RADIO1", default=True, key='oui'), sg.Radio('Non', "RADIO1", key='non')],
    [sg.Button('Afficher'), sg.Button('Annuler')]
]

# Création de la fenêtre avec une icône personnalisée
window = sg.Window('Prompt convivial', layout, icon='C:/Users/xi1le/OneDrive/Bureau/NuancePDF_0001.ico')

# Boucle principale de l'application
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Annuler':
        break

    if event == 'Afficher':
        valeur = values['input']
        bouton_clic = 'Oui' if values['oui'] else 'Non'
        if valeur:
            sg.popup_ok("Vous avez entré : " + valeur + "\nBouton cliqué : " + bouton_clic)
        else:
            sg.popup_error("Veuillez entrer une valeur.")

# Fermeture de la fenêtre
window.close()
