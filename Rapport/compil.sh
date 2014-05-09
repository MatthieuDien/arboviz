# compilation des fichiers Python

python testTikz.py 500 true
python testTikz.py 500 false
python testTikz.py 10000 true
python testTikz.py 10000 false
python testAsymptote.py 500 true
python testAsymptote.py 500 false
python testAsymptote.py 10000 true
python testAsymptote.py 10000 false
#python3 testNetworkx.py 500 20 true
#python3 testNetworkx.py 500 20 false
#python3 testNetworkx.py 10000 20 true
#python3 testNetworkx.py 10000 20 false

# compilation du fichier LaTeX et génération en pdf

pdflatex PSTL_rapport.tex
bibtex PSTL_rapport
asy PSTL_rapport-1.asy
asy PSTL_rapport-2.asy
asy PSTL_rapport-3.asy
asy PSTL_rapport-4.asy
pdflatex PSTL_rapport.tex
pdflatex PSTL_rapport.tex

# nettoyage
rm *.aux *.log *.out *.toc PSTL_rapport-* *.pre test*.tex *.blg *.bbl *~