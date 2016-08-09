SPHINXOPTS  =
SPHINXBUILD = sphinx-build
PAPER       =
BUILDDIR    = output
SRCDIR      = .
LATEXDIR    = build/latex

html:
	$(SPHINXBUILD) $(SRCDIR) $(BUILDDIR)

latex:
	$(SPHINXBUILD) -b latex $(SRCDIR) $(LATEXDIR)

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(BUILDDIR)/.doctrees
	rm $(BUILDDIR)/.buildinfo
