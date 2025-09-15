# Carpeta para auxiliares
$aux_dir = 'build';

# Carpeta para PDF final
$out_dir = '.';

$pdf_mode = 1;            # pdflatex (1), xelatex (5), lualatex (4)
$interaction = 'nonstopmode';

# Forzar rutas de BibTeX/biber al aux_dir
$bibtex_use = 2;   # hace que latexmk llame bibtex en build/

# Redefinir dónde escribir el synctex
$ENV{'TEXMFOUTPUT'} = 'build';
