from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def reset(self, e):
        self._model.reset()
        self._view._txtOutT.value = self._model.T
        self._view._lv.controls.clear()
        self._view._txtIn.disabled = False
        self._view._btnPlay.disabled = False
        self._view._lv.controls.append(ft.Text("Indovina a quale numero sto pensando!"))
        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txtIn.value
        self._view._txtIn.value = ""
        self._view._txtOutT.value = self._model.T -1
        if tentativoStr == "":
            self._view._lv.controls.append(ft.Text("Attenzione! Inserisci un valore numerico da testare", color = "red"))
            self._view.update()
            return
        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Attenzione! Il valore inserito non è un intero", color="red"))
            self._view.update()
            return

        res  = self._model.play(tentativoInt)
        if res == 0: # ho vinto
            self._view._lv.controls.append(ft.Text(f"Fantastico! Hai vinto, il segreto era {tentativoInt}", color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == 2: # ho finito tutte le vite
            self._view._lv.controls.append(ft.Text(f"Mi dispiace, hai finito le vite, il segreto era {self._model.segreto}", color="red"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == -1: # il mio segreto è più piccolo
            self._view._lv.controls.append(ft.Text(f"Il segreto è più piccolo di {tentativoInt}"))
            self._view.update()
            return
        else:
            self._view._lv.controls.append(ft.Text(f"Il segreto è più grande di {tentativoInt}"))
            self._view.update()
            return

    def getNMax(self):
        return self._model.NMax

    def getTMax(self):
        return self._model.TMax



