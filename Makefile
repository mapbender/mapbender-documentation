.RECIPEPREFIX = >
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = output
SRCDIR        = .
LATEXDIR      = build/latex
SINGLEHTMLDIR = build/singlehtml
LINKCHECKDIR  = build/linkcheck
DISTDIR       = build

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
