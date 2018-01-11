SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = output
SRCDIR        = .
LATEXDIR      = build/latex
SINGLEHTMLDIR = build/singlehtml
LINKCHECKDIR  = build/linkcheck

html:
	$(SPHINXBUILD) $(SPHINXOPTS) $(SRCDIR) $(BUILDDIR)

latex:
	$(SPHINXBUILD) -b latex $(SRCDIR) $(LATEXDIR)

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(SRCDIR) $(SINGLEHTMLDIR)

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(SRCDIR) $(LINKCHECKDIR)


clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(BUILDDIR)/.doctrees
	rm $(BUILDDIR)/.buildinfo
