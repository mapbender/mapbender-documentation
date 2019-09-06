.RECIPEPREFIX = >
SPHINXOPTS    = --keep-going -Q -v
SPHINXPROJ    = mapbender-documentation
SPHINXBUILD   = sphinx-build
SPHINXINTL    = sphinx-intl
BUILDDIR      = _build
SOURCEDIR     = .
DOWNLOAD_DIR  = downloads

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

intl:
	@$(SPHINXINTL) update -l de,en
	@$(SPHINXINTL) build
	make SPHINXOPTS="-Dlanguage=de" html

epub_dowload:
	@$(SPHINXBUILD) -b epub "$(SOURCEDIR)"/de "$(DOWNLOAD_DIR)"/epub/de
	@$(SPHINXBUILD) -b epub "$(SOURCEDIR)"/en "$(DOWNLOAD_DIR)"/epub/en
	cp "$(DOWNLOAD_DIR)"/epub/de/Mapbender_DE.epub "$(DOWNLOAD_DIR)"/Mapbender_de.epub
	cp "$(DOWNLOAD_DIR)"/epub/en/Mapbender_EN.epub "$(DOWNLOAD_DIR)"/Mapbender_en.epub

singlehtml_download:
	@$(SPHINXBUILD) -b singlehtml "$(SOURCEDIR)"/de "$(DOWNLOAD_DIR)"/singlehtml/de $(SPHINXOPTS)
	@$(SPHINXBUILD) -b singlehtml "$(SOURCEDIR)"/en "$(DOWNLOAD_DIR)"/singlehtml/en $(SPHINXOPTS)

html_download:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)"/de "$(DOWNLOAD_DIR)"/html/de $(SPHINXOPTS)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)"/en "$(DOWNLOAD_DIR)"/html/en $(SPHINXOPTS)

html_all_download:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(DOWNLOAD_DIR)"/html $(SPHINXOPTS)

latexpdf_download:
	make latexpdf
	cp "$(BUILDDIR)"/latex/Mapbender_de.pdf "$(DOWNLOAD_DIR)"
	cp "$(BUILDDIR)"/latex/Mapbender_en.pdf "$(DOWNLOAD_DIR)"

zip_download:
	zip -r "$(DOWNLOAD_DIR)"/Mapbender_de.zip "$(DOWNLOAD_DIR)"/html/de
	zip -r "$(DOWNLOAD_DIR)"/Mapbender_en.zip "$(DOWNLOAD_DIR)"/html/en

downloads: html_download singlehtml_download latexpdf_download zip_download epub_dowload

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
