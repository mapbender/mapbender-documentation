.RECIPEPREFIX = >
SPHINXOPTS    = -j4
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = output
SRCDIR        = .
LATEXDIR      = build/latex
SINGLEHTMLDIR = build/singlehtml
LINKCHECKDIR  = build/linkcheck
DISTDIR       = build

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  dist  		to make a .tgz file"

clean:
	> rm -rf $(BUILDDIR)/*
	> rm -rf $(BUILDDIR)/.doctrees
	> rm $(BUILDDIR)/.buildinfo

distclean:
	> rm -rf $(DISTDIR)/*

allclean:
	> rm -rf $(BUILDDIR)/*
	> rm -rf $(BUILDDIR)/.doctrees
	> rm $(BUILDDIR)/.buildinfo
	> rm -rf $(DISTDIR)/*

html:
	> $(SPHINXBUILD) $(SPHINXOPTS) $(SRCDIR) $(BUILDDIR)

latex:
	> $(SPHINXBUILD) -b latex $(SRCDIR) $(LATEXDIR)

singlehtml:
	> $(SPHINXBUILD) -b singlehtml $(SRCDIR) $(SINGLEHTMLDIR)

linkcheck:
	> $(SPHINXBUILD) -b linkcheck $(SRCDIR) $(LINKCHECKDIR)

dist:
	> tar -czvf $(DISTDIR)/mapbender-documentation.tgz $(BUILDDIR)

latexpdf:
	> $(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(SRCDIR) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	> $(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."
q
