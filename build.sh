#!/bin/bash

rm paul_maynard.zip

zip -r paul_maynard.zip blob.py blob_finder.py bead_tracker.py avogadro.py

pandoc -o Paul_Maynard_Report.pdf Paul_Maynard_Report.md

zip -r paul_maynard.zip Paul_Maynard_Report.pdf

xdg-open Paul_Maynard_Report.pdf

if [[ -a Mena_Mossa_Report.pdf ]]; then
    zip -r paul_maynard.zip Mena_Mossa_Report.pdf
fi

if [[ -a XingYi_Chen_Report.pdf ]]; then
    zip -r paul_maynard.zip XingYi_Chen_Report.pdf
fi