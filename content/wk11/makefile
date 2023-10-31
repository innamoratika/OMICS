SANDBOX := ~/share/omics_sandbox
WORK := $(SANDBOX)/goea/$(USER)

hello:
	echo Welcome to Gene Ontology Enrichment Analysis (GOEA)

goea:
	find_enrichment.py study.txt population.txt association.txt --pval=0.05 --method=fdr_bh --pval_field=fdr_bh --outfile=results_id2gos.xlsx

obo: go-basic.obo

go-basic.obo:
	wget http://current.geneontology.org/ontology/go-basic.obo

mk_sandbox: $(WORK)
	cp -f *.md $(WORK)
	cp -f *.txt $(WORK)
	cp -f makefile $(WORK)
	cp -f sandbox.sh ../..
	find $(WORK) -type f

chmod:
	chmod 777 $(SANDBOX)

$(WORK):
	mkdir -p $(WORK)

clean:
	rm -f go-basic.obo
