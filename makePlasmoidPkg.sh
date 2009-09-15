#!/bin/bash
zip   -r ../plasma_pyweather.plasmoid . -x ".git/*" -x ".project" -x ".settings/*" -x ".pydevproject"  -x "*/*.pyc" -x ".gitignore" -x "makePlasmoidPkg.sh"
