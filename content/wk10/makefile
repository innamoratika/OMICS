WORK := /data/share/omics_sandbox/vim/$(USER)

mk_sandbox: $(WORK)
	cp -f assign*.md $(WORK)
	cp -f *.txt $(WORK)
	cp -f sandbox.sh ../..
	find $(WORK) -type f

$(WORK):
	mkdir -p $(WORK)
