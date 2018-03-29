welcome_princep="t'ha tocat ser el princep"
welcome_princesa="t'ha tocat ser la princesa"
welcome_rei="t'ha tocat ser el rei"
welcome_pages="t'ha tocat ser el pages"
welcome_drac="t'ha tocat ser el drac"
welcome_bou="t'ha tocat ser el bou"

def welcome(state):
    if state == "princep": return welcome_princep
    elif state == "princesa": return welcome_princesa
    elif state == "rei": return welcome_rei
    elif state == "pages": return welcome_pages
    elif state == "drac": return welcome_drac
    elif state == "bou": return welcome_bou

