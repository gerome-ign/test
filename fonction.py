from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt

from .mapping_version import *

def afficheerreur(text, titre="Erreur"):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(Ok)
    msg.setText(text)
    msg.setWindowFlags(WindowStaysOnTopHint)
    msg.exec()

def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)

    msg.setWindowTitle(titre)
    msg.setText(text)
    btnAnnuler = msg.addButton("Annuler", YesRole)
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")
    btnValider = msg.addButton("valider les modifications", AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")
    msg.setWindowFlags(WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True
