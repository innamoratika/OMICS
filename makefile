
vim_sandbox: $(WORK)
	cd content/wk10; make -f makefile mk_sandbox


sep := '--------------------------------------------------'
g:
	@echo ''
	@echo $(sep)
	@echo 1. GIT STATUS
	git status -uno
	@echo ''
	@echo $(sep)
	@echo 2. BACKUP URL ON GitHub
	git remote -v
	@echo ''
	@echo $(sep)
	@echo 3. LOCAL git branch
	git branch


