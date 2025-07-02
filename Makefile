ifndef FACE
$(error FACE is not set. Usage: make FACE=your_watch_face)
endif

SRC_DIR = src
LIB_DIR = $(SRC_DIR)/lib
WATCHFACE_DIR = $(SRC_DIR)/watchfaces
VENDOR_LIB_DIR = $(SRC_DIR)/vendor_lib
MPY_CROSS = $(SRC_DIR)/tools/mpy-cross

OUT_DIR = out
OUT_LIB_DIR = $(OUT_DIR)/lib

PY_FILES = $(wildcard $(LIB_DIR)/*.py)

.PHONY: all clean

all: clean setup copy_code compile_libs copy_vendor

clean:
	rm -rf $(OUT_DIR)

setup:
	mkdir -p "$(OUT_DIR)"
	mkdir -p "$(OUT_LIB_DIR)"

copy_code:
		@if [ ! -f "$(WATCHFACE_DIR)/$(FACE).py" ]; then \
			echo "Error: Watchface '$(FACE)' not found in $(WATCHFACE_DIR)/"; \
			exit 1; \
		fi
		cp "$(WATCHFACE_DIR)/$(FACE).py" "$(OUT_DIR)/code.py"

compile_libs:
	@for f in $(PY_FILES); do \
		fn=$$(basename $$f .py); \
		"$(MPY_CROSS)" "$$f" -o "$(OUT_LIB_DIR)/$$fn.mpy"; \
	done

copy_vendor:
	cp -r "$(VENDOR_LIB_DIR)"/* "$(OUT_LIB_DIR)/"

