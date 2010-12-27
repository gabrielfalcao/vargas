all: test

filename=vargas-`python -c 'import vargas;print vargas.version'`.tar.gz

export PACKAGE_DEPENDENCIES:= nose sure

check_dependencies:
	@echo "Checking for dependencies to run tests ..."
	@for dependency in `echo $$PACKAGE_DEPENDENCIES`; do \
		python -c "import $$dependency" 2>/dev/null || (echo "You must install $$dependency in order to run package's tests" && exit 3) ; \
		done

test: check_dependencies clean
	@echo "Running tests ..."
	@nosetests -s --verbosity=2 --with-coverage --cover-erase --cover-package=vargas

clean:
	@printf "Cleaning up files that are already in .gitignore... "
	@for pattern in `cat .gitignore`; do rm -rf $$pattern; done
	@echo "OK!"

release: test
	@printf "Exporting to $(filename)... "
	@tar czf $(filename) vargas setup.py README.md COPYING
	@echo "DONE!"
