WORK := $(HOME)/share/omics_sandbox/wk12/$(USER)

hello:
	echo Welcome to Microbiome Analysis

mk_sandbox: $(WORK)
	cp -f *.md $(WORK)
	cp -f Makefile $(WORK)
	find $(WORK) -type f

$(WORK):
	mkdir -p $(WORK)
