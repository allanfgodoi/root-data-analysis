'''
THIS CODE MAKES A GRAPH WITH A LINEAR FIT.

REQUIRES CERN ROOT INSTALLED IN YOUR PC.

PLEASE LOOK TO README (SOON) FOR MORE INFO.
'''

from __future__ import print_function
from ROOT import *
from array import array

datafile = "data-tgraph-pol01.txt" # DATA FILE NAME AND FORMAT
title = "" # CANVAS TITLE
x_title = "" # X AXIS CANVAS TITLE
y_title = "" # Y AXIS CANVAS TITLE
filename = "tgraph_pol01.pdf" # FILE NAME AND FORMAT FOR THE CANVAS PRINT

data = []

with open(datafile, "r") as f:
    for item in f:
        data.append(item.strip())

n = len(data)

x, y = array("d"), array("d")

for i in range(n):
    x.append(i)

for j in data:
    y.append(float(j))

gr = TGraph(n, x, y)

gr.SetTitle(title)

gr.GetXaxis().SetTitle(x_title)
gr.GetYaxis().SetTitle(y_title)

gr.SetMarkerStyle(20)
gr.SetMarkerColor(kBlack)
gr.SetMarkerSize(1.3)

fit = TF1("fit", "pol1")

c1 = TCanvas()
gr.Draw("AP")
gr.Fit("fit")

c1.Print(filename)