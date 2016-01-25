SPHINXOPTS  =
SPHINXBUILD = sphinx-build
PAPER       =
BUILDDIR    = output
SRCDIR      = .

build:
	$(SPHINXBUILD) $(SRCDIR) $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(BUILDDIR)/.doctrees
	rm $(BUILDDIR)/.buildinfo
