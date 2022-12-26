CXX = g++
CXXFLAGS = -std=c++14 -Wall -MMD -Werror=vla
EXEC = a4q1
OBJECTS = expression.o binaryexpression.o loneinteger.o unaryexpression.o variable.o
DEPENDS = ${OBJECTS:.o=.d}

${EXEC}: ${OBJECTS}
	${CXX} ${CXXFLAGS} ${OBJECTS} -o ${EXEC}

-include ${DEPENDS}

.PHONY: clean

clean:
	rm ${OBJECTS} ${EXEC} ${DEPENDS}
