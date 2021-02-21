# Generic Makefile for CS-1101
#
#	Deepraj Pandey
# 14 January, 2021

INTERACTIVE = $(shell [ -t 0 ] && echo 1)

EXE = addition
SRCS = $(EXE).c
LIBS = -lm

CC = clang
CFLAGS = -fsanitize=signed-integer-overflow -fsanitize=undefined -O0 -Qunused-arguments -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow

$(EXE): $(SRCS)
	@echo "🚧 Building..."
	$(CC) $(CFLAGS) $(LIBS) $^ -o $@

run: $(EXE)
	./$(EXE)

debug: CFLAGS += -ggdb3
debug: $(EXE)

.PHONY: clean
clean:
	@echo "🧹 Clearing directories..."
	rm -f $(EXE) *.o

##################
### Autograder ###
##################
ENV = grader
PY = $(ENV)/bin/python3
ACTIVATE = source $(ENV)/bin/activate

init_grader: autograder.py
	sudo apt-get -y install gcc libpq-dev clang
	sudo apt-get -y install python-dev  python-pip
	sudo apt-get -y install python3-dev python3-pip python3-venv python3-wheel --allow-downgrades --allow-remove-essential --allow-change-held-packages --assume-yes --fix-broken
	sudo -H pip3 install setuptools wheel
	python3 -m venv $(ENV)
	$(PY) -m pip install wheel
	@echo "🛠 Setting up autograder..."
	make $(ENV)

$(ENV): $(ENV)/autogen

$(ENV)/autogen: requirements.txt
	python3 -m venv $(ENV)
	$(PY) -m pip install -Ur requirements.txt
	touch $(ENV)/autogen

grade: $(ENV)
	@echo "📚 Grading..."
	$(PY) autograder.py
