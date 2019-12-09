PROJECT=Algorithmes_genetiques
AUTHOR=Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki Diakité
PYTHONPATH=./src
export PYTHONPATH
SPHINXBUILD=python3 -m sphinx
CONFIGPATH=.
SOURCEDOC=sourcedoc
DOC=doc

.PHONY: clean doc archive author

clean:
	rm -f *~ */*~
	rm -rf __pycache__ src/__pycache__ src/problem*/__pycache__ 
	rm -rf $(DOC)
	rm -f $(PROJECT).zip

doc: author
	$(SPHINXBUILD) -c $(CONFIGPATH) -b html $(SOURCEDOC) $(DOC)

archive: clean
	zip -r $(PROJECT).zip . -x \*.md \.git\*


author:
	sed -i -e 's/^project =.*/project = "$(PROJECT)"/g' conf.py
	sed -i -e 's/^copyright =.*/copyright = "2019, $(AUTHOR), Univ. Lille"/g' conf.py
	sed -i -e 's/^author =.*/author = "$(AUTHOR)"/g' conf.py
