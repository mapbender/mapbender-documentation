.RECIPEPREFIX = >
SPHINXOPTS    = --keep-going -Q
SPHINXPROJ    = mapbender-documentation
SPHINXBUILD   = sphinx-build
BUILDDIR      = _build
SOURCEDIR     = .

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
