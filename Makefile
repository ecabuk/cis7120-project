GRAMMAR=Ismo
CLASSPATH=CLASSPATH="/usr/local/Cellar/antlr/4.7.1_1/antlr-4.7.1-complete.jar:."

build:
	antlr -Dlanguage=Python3 -o parser -no-listener -visitor $(GRAMMAR).g4

clean:
	rm -rf parser

run:
	python3 main.py input

debug:
	antlr $(GRAMMAR).g4
	$(CLASSPATH) javac $(GRAMMAR)*.java
	grun $(GRAMMAR) prgm input -gui && rm -f $(GRAMMAR)*.{class,java,interp,tokens}