##
## @file		makefile
## @brief		PICSP makefile.
## @author		Sayan Adhikari <sayan.adhikari@fys.uio.no>
##

CXX		= g++

#ARG =
                        

EXEC	= picsp

CXXFLAGS = -std=c++11 -Wall
CFLAGS	=  -Ilib/iniparser/src   # Flags for compiling

LFLAGS	=  -Llib/iniparser -liniparser # Flags for linking

SDIR	= src
ODIR	= src/obj
#HDIR	= src
LDIR	= lib
OUTDIR  = output


all: version $(EXEC)

OBJ = main.o

$(EXEC): $(OBJ)
	@echo "PICSP is being compiled"
	@$(CXX) $(CXXFLAGS) -o  $(EXEC) $(OBJ) $(CFLAGS) $(LFLAGS)
	@mv $(OBJ) $(ODIR)/$(OBJ)
	@cp main.cpp $(SDIR)/main.cpp
	@echo "PICSP is built"

$(OBJ): main.cpp
	@$(CXX) $(CXXFLAGS) -c main.cpp $(CFLAGS) $(LFLAGS)

.phony: version
version:
	@echo "Embedding git version"
	@echo "#define VERSION \"$(shell git describe --abbrev=4 --dirty --always --tags)\"" > $(SDIR)/version.h

clean:
	@echo "Cleaning compilation files (run \"make veryclean\" to clean more)"
	@rm -f *~ $(ODIR)/*.o $(SDIR)/*.o
	@rm -f $(OUTDIR)/* *.dat


