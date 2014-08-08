TEMPORARY_DIR=_obuild
ARBOVIZ_BIN_DIR_TMP=$(TEMPORARY_DIR)/arboviz
ARBOVIZ_BIN_TMP=$(ARBOVIZ_BIN_DIR_TMP)/arboviz.asm $(ARBOVIZ_BIN_DIR_TMP)/arboviz.byte
ARBOVIZ_BIN_DIR=bin

all : main

main :
	ocp-build -init
	ocp-build build arboviz
	mkdir -p bin
	cp $(ARBOVIZ_BIN_TMP) $(ARBOVIZ_BIN_DIR)

clean :
	ocp-build clean
	rm bin/arboviz.*
