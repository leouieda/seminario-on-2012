BIN=~/src/tesseroids/bin
AREA=-30/30/25/85
GRID=100/100
HEIGHT=250000
ORDER=2/2/2

.PHONY: all plot

all: tessggt.txt tessggt-o2.txt

plot: tessggt.txt tessggt-o2.txt plot.py
	python plot.py tessggt.txt
	python plot.py tessggt-o2.txt

tessggt.txt: tess.txt
	$(BIN)/tessgrd -r$(AREA) -b$(GRID) -z$(HEIGHT) | \
	$(BIN)/tessgxx $< | $(BIN)/tessgxy $< | $(BIN)/tessgxz $< | \
	$(BIN)/tessgyy $< | $(BIN)/tessgyz $< | \
	$(BIN)/tessgzz $< -v -ltessgzz.log > $@

tessggt-o2.txt: tess.txt
	$(BIN)/tessgrd -r$(AREA) -b$(GRID) -z$(HEIGHT) | \
	$(BIN)/tessgxx $< -o$(ORDER) -a | $(BIN)/tessgxy $< -o$(ORDER) -a | \
	$(BIN)/tessgxz $< -o$(ORDER) -a | $(BIN)/tessgyy $< -o$(ORDER) -a | \
	$(BIN)/tessgyz $< -o$(ORDER) -a | \
	$(BIN)/tessgzz $< -o$(ORDER) -v -ltessgzz-o2.log -a > $@

clean:
	rm -rf tessggt.txt tessggt-o2.txt *.log
