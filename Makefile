##
## Makefile
## File description:
## 
##

SRC		=	src/bisection.py \
			src/formulas.py  \
			src/helper.py    \
			src/main.py 	\
			src/newton.py 	\
			src/secant.py 	\
			src/105torus	\

all:
	cp $(SRC) ./


tests_run:
	coverage run --source=. -m pytest -vv tests/test.py
	coverage report

clean:
	rm *.py
	rm 105torus

fclean:	clean

re: fclean all

.PHONY: all clean fclean re tests_run

