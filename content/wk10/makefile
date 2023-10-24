WORK := /data/share/omics_sandbox/vim/$(USER)

hello:
	echo Welcome to an introduction to vim, the powerful editor

mk_sandbox: $(WORK)
	cp -f *.md $(WORK)
	cp -f *.txt $(WORK)
	#cp -f sandbox.sh ../..
	find $(WORK) -type f

$(WORK):
	mkdir -p $(WORK)
